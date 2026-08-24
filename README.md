# Citation Trend Finder

Find papers that are gaining traction recently, regardless of original publication date. Powered by OpenAlex.

## Usage

- Install deps:
  ```bash
  pip install -r requirements.txt
  ```
- Run weekly (or on demand):
  ```bash
  python trending.py --days 90 --max-citing-works 2000 --top-k 50
  ```
- Search a specific topic:
  ```bash
  python trending.py --topic "graph neural networks" --days 120 --top-k 50
  ```
- Optional: set your contact email for OpenAlex etiquette
  ```bash
  export OPENALEX_MAILTO="you@example.com"
  ```

You can also set defaults in `config.yaml` (see that file for fields).

### Project structure

- **`trending.py`**: Main script. Fetches recently published works from OpenAlex, aggregates which prior works they reference in the last N days, ranks trending papers, and updates `README.md`.
- **`config.yaml`**: Default parameters (days window, per-page, top-k, topic/concept filters, mailto). CLI flags override these.
- **`requirements.txt`**: Python dependencies.
- **`.github/workflows/trending.yml`**: Weekly GitHub Actions workflow that runs the script and commits README updates.
- **`README.md`**: Usage docs and an auto-updated section with the current trending table between markers.

### What’s included

- **Automated weekly refresh**: The workflow runs every Monday 06:00 UTC and commits changes to `README.md`.
- **Topic-specific search**: `--topic "..."` biases the recent citing works to that topic. You can also scope by **`--concept-id`** (OpenAlex concept) for stricter scoping.
- **Robust fetching**: Retries with exponential backoff; polite usage via `OPENALEX_MAILTO`.
- **Ranking logic**:
  - Counts how many times each prior work is referenced by works published in the last N days.
  - Sorts by recent citation count, then recency ratio (recent/total), then total citations.
  - Includes venue, authors, DOI/OpenAlex links.
- **Fallback broadening**: If no references are collected with a restrictive `--work-type`, it retries without a type filter.
- **Dry run**: `--no-readme` prints a compact ranking to stdout; `--debug` adds diagnostics.

### Notes

- **Trending definition**: A paper is trending if many recent works cite it, regardless of when it was originally published.
- **Topic vs concept**:
  - **`--topic`** applies OpenAlex full-text search to recent works and is broad.
  - **`--concept-id`** restricts the pool of recent works to a specific concept taxonomy node.
- **Window size (`--days`)**: Larger windows smooth volatility; smaller windows make the list more reactive.
- **API etiquette**: Set `OPENALEX_MAILTO` (or `--mailto`) to identify your requests.
- **Reproducibility**: The README shows the current window and sampling size used for the table.

---

## Weekly Trending Papers (auto-updated)

Last update: 2026-08-24 06:41 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Operative Capacity Adjunct and Mission Temporal Validity: Rollback Capacity, Resource Residual, and Graceful Degradation in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20583953) | 2026 | 10 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 2 | [Post-Consequence Proof Standing and Durable Reconstructability: Proof Survival, Narrative Resistance, and Reviewable Standing Basis in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20573235) | 2026 | 10 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 3 | [Authority Standing and Commit Standing: Current Execution Authority, Scoped Mandate, Non-Revocation, and Commit-Time Proof in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20561344) | 2026 | 10 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 4 | [Unified Claim Standing Record Layer: Evidence, Isolation, Pressure, Authority, and Commit in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20479042) | 2026 | 10 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 5 | [Pressure-Claim Standing: Measurable Boundary Claims and Residual Transfer in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20417363) | 2026 | 10 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 6 | [Decorative Isolation: Non-Burden-Bearing Separation Claims in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20369228) | 2026 | 10 | 32 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 7 | [Evidence Standing Envelope: Claim Standing Under Interval Evidence in Consequence-Bearing AI Systems](https://doi.org/10.5281/zenodo.20276203) | 2026 | 10 | 34 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 8 | [Deterministic Liability and Insurer Readability in High-Consequence AI Systems](https://doi.org/10.5281/zenodo.19657625) | 2026 | 10 | 36 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 9 | [Deterministic Liability, Pressure Isolation, and Mission Invalidation in High-Consequence and Decision-Bearing Systems](https://doi.org/10.5281/zenodo.19655615) | 2026 | 10 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |
| 10 | [Irreversibility Posture and the Boundary of Governance Automation](https://doi.org/10.5281/zenodo.19636475) | 2026 | 10 | 40 | Zenodo (CERN European Organization for Nuclear Research) | Vadym Partasyuk |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 132 | 130270 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 76 | 51742 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 40 | 29918 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 29 | 9762 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 19 | 2958 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 24252 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 19 | 33742 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 83811 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 16 | 32230 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 15 | 8986 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 19 | 2958 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 13 | 604 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 3 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 8 | 735 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 4 | [Machine Learning in Environmental Research: Common Pitfalls and Best Practices](https://doi.org/10.1021/acs.est.3c00026) | 2023 | 5 | 626 | Environmental Science & Technology | Jun‐Jie Zhu, Meiqi Yang, Zhiyong Jason Ren |
| 5 | [Crop yield prediction in agriculture: A comprehensive review of machine learning and deep learning approaches, with insights for future research and sustainability](https://doi.org/10.1016/j.heliyon.2024.e40836) | 2024 | 4 | 218 | Heliyon | Md Abu Jabed, Masrah Azrifah Azmi Murad |
| 6 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 4 | 778 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 27 | 1604 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 22 | 4138 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 21 | 3625 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 3685 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 15 | 102011 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 6 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 12 | 845 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 7 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 12 | 876 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 8 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 11 | 648 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 1919 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 6175 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 21 | 3625 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 3685 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 12 | 876 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 4 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 11 | 648 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 5 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 1919 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 6 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 10 | 573 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 7 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 10 | 865 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 8 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 9 | 546 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 9 | [A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1) | 2024 | 9 | 1437 | Frontiers of Computer Science | Lei Wang, Chen Ma, Xueyang Feng, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 8 | 2476 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Is the information provided by large language models valid in educating patients about adolescent idiopathic scoliosis? An evaluation of content, clarity, and empathy](https://doi.org/10.1007/s43390-024-00955-3) | 2024 | 4 | 24 | Spine Deformity | Siegmund Lang, Jacopo Antonino Vitale, Fabio Galbusera, et al. |
| 2 | [Performance of a large language model on the reasoning tasks of a physician](https://doi.org/10.1126/science.adz4433) | 2026 | 5 | 31 | Science | Peter G. Brodeur, Thomas A Buckley, Zahir Kanjee, et al. |
| 3 | [LLM-assisted systematic review of large language models in clinical medicine](https://doi.org/10.1038/s41591-026-04229-5) | 2026 | 4 | 42 | Nature Medicine | Sully F. Chen, Anton Alyakin, Andreas Seas, et al. |
| 4 | [Large language models in real-world clinical workflows: a systematic review of applications and implementation](https://doi.org/10.3389/fdgth.2025.1659134) | 2025 | 4 | 60 | Frontiers in Digital Health | Yaara Artsi, Vera Sorin, Benjamin S. Glicksberg, et al. |
| 5 | [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://doi.org/10.52202/075280-3275) | 2023 | 4 | 64 |  | Miles Turpin, Julian Michael, Ethan Perez, et al. |
| 6 | [Large language models for building energy applications: Opportunities and challenges](https://doi.org/10.1007/s12273-025-1235-9) | 2025 | 4 | 92 | Building Simulation | Mingzhe Liu, Liang Zhang, Jianli Chen, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 21 | 190277 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 12 | 130270 | Machine Learning | Leo Breiman |
| 3 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 11 | 102011 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 4 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 9 | 107621 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 5 | [The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality in Organizational Fields](https://doi.org/10.2307/2095101) | 1983 | 8 | 36992 | American Sociological Review | Paul DiMaggio, Walter W. Powell |
| 6 | [How to conduct a bibliometric analysis: An overview and guidelines](https://doi.org/10.1016/j.jbusres.2021.04.070) | 2021 | 7 | 13222 | Journal of Business Research | Naveen Donthu, Satish Kumar, Debmalya Mukherjee, et al. |
| 7 | [lavaan : An R Package for Structural Equation Modeling](https://doi.org/10.18637/jss.v048.i02) | 2012 | 7 | 26198 | Journal of Statistical Software | Yves Rosseel |
| 8 | [Institutions, Institutional Change and Economic Performance](https://doi.org/10.1017/cbo9780511808678) | 1990 | 7 | 31717 | Cambridge University Press eBooks | Douglass C. North |
| 9 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 7 | 33043 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 10 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 7 | 79132 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [PISA 2022 Results (Volume I)](https://doi.org/10.1787/53f23881-en) | 2023 | 3 | 1288 | Programme for international student assessment/Internationale Schulleistungsstudie | OECD |
| 2 | [Explainable Artificial Intelligence (XAI): What we know and what is left to attain Trustworthy Artificial Intelligence](https://doi.org/10.1016/j.inffus.2023.101805) | 2023 | 3 | 1649 | Information Fusion | Sajid Ali, Tamer Abuhmed, Shaker El–Sappagh, et al. |
| 3 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 3 | 2958 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The role of evolutionary game theory in spatial and non-spatial models of the survival of cooperation in cancer: a review](https://doi.org/10.1098/rsif.2022.0346) | 2022 | 2 | 33 | Journal of The Royal Society Interface | Helena Coggan, Karen M. Page |
<!-- TRENDING-END -->
