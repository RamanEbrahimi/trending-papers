#!/usr/bin/env python3
import argparse
import collections
import dataclasses
import datetime as dt
import os
import sys
import textwrap
from typing import Any, Dict, Iterable, List, Optional, Tuple

import requests
import yaml
from dateutil import tz
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

OPENALEX_BASE = "https://api.openalex.org"
README_PATH = "README.md"
MARKER_START = "<!-- TRENDING-START -->"
MARKER_END = "<!-- TRENDING-END -->"
DEFAULT_CONFIG_PATH = "config.yaml"


class OpenAlexError(RuntimeError):
    pass


def _today_utc_date() -> dt.date:
    return dt.datetime.now(tz=tz.UTC).date()


def _to_date_string(date_obj: dt.date) -> str:
    return date_obj.isoformat()


def _chunked(items: List[str], size: int) -> Iterable[List[str]]:
    for i in range(0, len(items), size):
        yield items[i : i + size]


@dataclasses.dataclass
class FetchConfig:
    days: int = 90
    max_citing_works: int = 2000
    per_page: int = 200
    top_k: int = 50
    work_type: Optional[str] = "journal-article"
    topic: str = ""
    concept_id: str = ""
    mailto: str = ""


class OpenAlexClient:
    def __init__(self, mailto: Optional[str] = None, timeout_s: int = 30) -> None:
        self.session = requests.Session()
        self.timeout_s = timeout_s
        self.mailto = mailto or os.getenv("OPENALEX_MAILTO") or ""
        headers = {
            "User-Agent": f"citation-trend-finder (mailto:{self.mailto})" if self.mailto else "citation-trend-finder"
        }
        self.session.headers.update(headers)

    @retry(
        reraise=True,
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=20),
        retry=retry_if_exception_type((requests.RequestException, OpenAlexError)),
    )
    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{OPENALEX_BASE}{path}"
        if self.mailto:
            params = {**params, "mailto": self.mailto}
        resp = self.session.get(url, params=params, timeout=self.timeout_s)
        if resp.status_code == 429:
            # OpenAlex rate limit; surface as retryable error
            raise OpenAlexError(f"Rate limited: {resp.text}")
        if not resp.ok:
            raise OpenAlexError(f"HTTP {resp.status_code}: {resp.text}")
        return resp.json()

    def iterate_recent_works(
        self,
        from_date: dt.date,
        per_page: int,
        limit: int,
        work_type: Optional[str] = None,
        topic: str = "",
        concept_id: str = "",
        select_fields: Optional[List[str]] = None,
    ) -> Iterable[Dict[str, Any]]:
        """
        Iterate over works published since from_date, optionally filtered by type/topic/concept.
        We use this as a proxy for "citing works in the recent window" to count their references.
        """
        filters = [f"from_publication_date:{_to_date_string(from_date)}"]
        if work_type:
            filters.append(f"type:{work_type}")
        if concept_id:
            filters.append(f"concepts.id:{concept_id}")

        params: Dict[str, Any] = {
            "filter": ",".join(filters),
            "per_page": per_page,
            "page": 1,
        }
        if topic:
            params["search"] = topic
        if select_fields:
            params["select"] = ",".join(select_fields)
        else:
            params["select"] = (
                "id,doi,title,authorships,publication_year,primary_location,cited_by_count,referenced_works"
            )

        fetched = 0
        while True:
            data = self._get("/works", params)
            results = data.get("results", [])
            if not results:
                break
            for work in results:
                yield work
                fetched += 1
                if fetched >= limit:
                    return
            meta = data.get("meta", {})
            count = meta.get("count", 0)
            per_page_eff = meta.get("per_page", per_page)
            current_page = params.get("page", 1)
            total_pages = (count + per_page_eff - 1) // per_page_eff if per_page_eff else current_page
            if current_page >= total_pages:
                break
            params["page"] = current_page + 1

    def get_works_by_ids(self, openalex_ids: List[str]) -> List[Dict[str, Any]]:
        """Fetch works details in batches using ids filter. Returns in arbitrary order."""
        # OpenAlex supports ids filter separated by | up to a certain size; we use chunks of 50.
        all_results: List[Dict[str, Any]] = []
        for chunk in _chunked(openalex_ids, 50):
            # ids.openalex expects pipe-separated list of full OpenAlex URLs
            ids_value = "|".join([f"https://openalex.org/{cid.split('/')[-1]}" for cid in chunk])
            params = {
                "filter": f"ids.openalex:{ids_value}",
                "per_page": len(chunk),
                "select": (
                    "id,doi,title,authorships,publication_year,primary_location,cited_by_count"
                ),
            }
            data = self._get("/works", params)
            all_results.extend(data.get("results", []))
        return all_results


@dataclasses.dataclass
class TrendingRecord:
    openalex_id: str
    title: str
    year: Optional[int]
    venue: str
    authors: str
    doi_url: Optional[str]
    openalex_url: str
    total_citations: int
    recent_citations: int
    recency_ratio: float


def format_authors_short(authorships: List[Dict[str, Any]], max_names: int = 3) -> str:
    names = []
    for a in authorships:
        author = a.get("author", {}) or {}
        name = author.get("display_name") or a.get("author_position") or "Unknown"
        names.append(name)
    if not names:
        return "Unknown"
    if len(names) > max_names:
        return ", ".join(names[:max_names]) + ", et al."
    return ", ".join(names)


def build_trending_table(records: List[TrendingRecord], header_note: str) -> str:
    lines = []
    lines.append(header_note)
    lines.append("")
    lines.append("| # | Title | Year | Recent | Total | Venue | Authors |")
    lines.append("|---:|---|---:|---:|---:|---|---|")
    for idx, r in enumerate(records, start=1):
        title_link = r.doi_url or r.openalex_url
        title_md = f"[{r.title}]({title_link})"
        lines.append(
            f"| {idx} | {title_md} | {r.year or ''} | {r.recent_citations} | {r.total_citations} | {r.venue} | {r.authors} |"
        )
    return "\n".join(lines)


def update_readme_table(
    readme_path: str,
    table_markdown: str,
    when_str: str,
) -> None:
    if not os.path.exists(readme_path):
        content = f"# Trending Papers\n\nLast update: {when_str}\n\n{MARKER_START}\n\n{table_markdown}\n\n{MARKER_END}\n"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        existing = f.read()

    if MARKER_START not in existing or MARKER_END not in existing:
        # append markers
        existing = existing.strip() + f"\n\nLast update: {when_str}\n\n{MARKER_START}\n\n{MARKER_END}\n"

    before, _, rest = existing.partition(MARKER_START)
    _, _, after = rest.partition(MARKER_END)

    new_content = (
        before
        + MARKER_START
        + "\n"
        + table_markdown.strip()
        + "\n"
        + MARKER_END
        + after
    )

    # Update 'Last update:' line if present
    lines = new_content.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("Last update:"):
            lines[i] = f"Last update: {when_str}"
            break
    new_content = "\n".join(lines) + ("\n" if not lines[-1].endswith("\n") else "")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def load_config(path: str) -> FetchConfig:
    cfg = FetchConfig()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        for field in dataclasses.fields(FetchConfig):
            if field.name in data and data[field.name] is not None:
                setattr(cfg, field.name, data[field.name])
    return cfg


def compute_trending(
    client: OpenAlexClient, cfg: FetchConfig, debug: bool = False
) -> Tuple[List[TrendingRecord], Dict[str, int], Dict[str, Any]]:
    from_date = _today_utc_date() - dt.timedelta(days=cfg.days)

    ref_counts: Dict[str, int] = collections.Counter()
    recent_seen = 0
    recent_with_refs = 0

    def pass_collect(work_type_value: Optional[str]) -> None:
        nonlocal recent_seen, recent_with_refs
        for work in client.iterate_recent_works(
            from_date=from_date,
            per_page=cfg.per_page,
            limit=cfg.max_citing_works,
            work_type=work_type_value,
            topic=cfg.topic,
            concept_id=cfg.concept_id,
        ):
            recent_seen += 1
            refs = work.get("referenced_works") or []
            if refs:
                recent_with_refs += 1
            for rid in refs:
                if isinstance(rid, str) and rid.startswith("http"):
                    rid = rid.split("/")[-1]
                ref_counts[rid] += 1

    # First pass with configured work_type
    pass_collect(cfg.work_type)

    # Fallback: if nothing found and we had a restrictive type, try without type filter
    fallback_used = False
    if not ref_counts and cfg.work_type:
        fallback_used = True
        pass_collect(None)

    debug_info: Dict[str, Any] = {
        "recent_seen": recent_seen,
        "recent_with_refs": recent_with_refs,
        "fallback_used": fallback_used,
    }

    if not ref_counts:
        return [], {}, debug_info

    top_ids = [rid for rid, _ in sorted(ref_counts.items(), key=lambda kv: kv[1], reverse=True)[: cfg.top_k * 2]]

    works = client.get_works_by_ids(top_ids)
    work_by_id = { (w.get("id") or "").split("/")[-1]: w for w in works }

    records: List[TrendingRecord] = []
    for rid, recent in sorted(ref_counts.items(), key=lambda kv: kv[1], reverse=True):
        w = work_by_id.get(rid)
        if not w:
            continue
        title = w.get("title") or "Untitled"
        year = w.get("publication_year")
        pl = w.get("primary_location") or {}
        host = ((pl.get("source") or {}).get("display_name")) or ((pl.get("host_venue") or {}).get("display_name")) or ""
        authors = format_authors_short(w.get("authorships") or [])
        doi = (w.get("doi") or "").lower().replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
        doi_url = f"https://doi.org/{doi}" if doi else None
        openalex_full_id = w.get("id") or ""
        openalex_id = openalex_full_id.split("/")[-1] if openalex_full_id else rid
        openalex_url = f"https://openalex.org/{openalex_id}"
        total = int(w.get("cited_by_count") or 0)
        recency_ratio = (recent / total) if total > 0 else 1.0
        records.append(
            TrendingRecord(
                openalex_id=openalex_id,
                title=title,
                year=year,
                venue=host,
                authors=authors,
                doi_url=doi_url,
                openalex_url=openalex_url,
                total_citations=total,
                recent_citations=int(recent),
                recency_ratio=float(recency_ratio),
            )
        )
        if len(records) >= cfg.top_k * 3:
            break

    records.sort(key=lambda r: (r.recent_citations, r.recency_ratio, r.total_citations), reverse=True)
    records = records[: cfg.top_k]

    return records, dict(ref_counts), debug_info


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Find papers trending by recent citations using OpenAlex and update README.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--config", default=DEFAULT_CONFIG_PATH, help="Path to YAML config")
    p.add_argument("--days", type=int, help="Lookback window for 'recent' citations (days)")
    p.add_argument("--max-citing-works", type=int, help="Max number of recent works to sample")
    p.add_argument("--per-page", type=int, help="Page size for OpenAlex API")
    p.add_argument("--top-k", type=int, help="Number of trending papers to include in README")
    p.add_argument("--work-type", help="Type of works to treat as recent citing works")
    p.add_argument("--topic", help="Keyword/topic string to bias the recent works search")
    p.add_argument("--concept-id", help="OpenAlex concept ID to restrict search space")
    p.add_argument("--mailto", help="Contact email for OpenAlex mailto parameter")
    p.add_argument("--no-readme", action="store_true", help="Do not update README, just print results")
    p.add_argument("--auto-readme", action="store_true", help="Force README update (ignore --no-readme)")
    p.add_argument("--limit-stdout", type=int, default=20, help="When printing only, limit rows shown")
    p.add_argument("--debug", action="store_true", help="Print debug info to stderr")
    return p.parse_args()


def merge_cli_overrides(cfg: FetchConfig, ns: argparse.Namespace) -> FetchConfig:
    merged = dataclasses.replace(cfg)
    for field in dataclasses.fields(FetchConfig):
        cli_value = getattr(ns, field.name.replace("_", "-"), None)
        # argparse converts dashes to underscores; so fetch differently
    # Manual mapping because of underscores vs dashes
    if ns.days is not None:
        merged.days = ns.days
    if ns.max_citing_works is not None:
        merged.max_citing_works = ns.max_citing_works
    if ns.per_page is not None:
        merged.per_page = ns.per_page
    if ns.top_k is not None:
        merged.top_k = ns.top_k
    if ns.work_type is not None:
        merged.work_type = ns.work_type
    if ns.topic is not None:
        merged.topic = ns.topic
    if ns.concept_id is not None:
        merged.concept_id = ns.concept_id
    if ns.mailto is not None:
        merged.mailto = ns.mailto
    return merged


def main() -> None:
    ns = parse_args()
    cfg = load_config(ns.config)
    cfg = merge_cli_overrides(cfg, ns)

    client = OpenAlexClient(mailto=cfg.mailto)
    records, ref_counts, debug_info = compute_trending(client, cfg, debug=ns.debug)

    when = dt.datetime.now(tz=tz.UTC).strftime("%Y-%m-%d %H:%M UTC")
    topic_note = cfg.topic.strip() or (f"concept:{cfg.concept_id}" if cfg.concept_id else "All topics")
    header_note = (
        f"Results for window last {cfg.days} days; topic: {topic_note}. "
        f"Sampled up to {cfg.max_citing_works} recent works."
    )

    if ns.no_readme and not ns.auto_readme:
        # Print a compact table to stdout
        print(header_note)
        print()
        if ns.debug:
            print(
                f"[debug] recent_seen={debug_info['recent_seen']} with_refs={debug_info['recent_with_refs']} fallback={debug_info['fallback_used']}",
                file=sys.stderr,
            )
        print("Rank\tRecent\tTotal\tYear\tTitle")
        for i, r in enumerate(records[: ns.limit_stdout], start=1):
            print(f"{i}\t{r.recent_citations}\t{r.total_citations}\t{r.year or ''}\t{r.title}")
        if len(records) > ns.limit_stdout:
            print(f"... (showing {ns.limit_stdout} of {len(records)})")
        return

    table_md = build_trending_table(records, header_note)
    update_readme_table(README_PATH, table_md, when)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
    except Exception as exc:
        print("Error:", exc, file=sys.stderr)
        sys.exit(1)
