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

Last update: 2026-07-27 09:37 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [STAR: ultrafast universal RNA-seq aligner](https://doi.org/10.1093/bioinformatics/bts635) | 2012 | 9 | 57015 | Bioinformatics | Alexander Dobin, Carrie Davis, Felix Schlesinger, et al. |
| 2 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 7 | 14555 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 3 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 7 | 98645 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 4 | [A generalization of the radiation condition of Sommerfeld for N-body Schrödinger operators](https://doi.org/10.1215/s0012-7094-94-07420-6) | 1994 | 6 | 46 | Duke Mathematical Journal | Hiroshi Isozaki |
| 5 | [Radiation conditions, limiting absorption principle, and general relations in open waveguide scattering](https://doi.org/10.1163/156939394x00902) | 1994 | 6 | 81 | Journal of Electromagnetic Waves and Applications | Alexander I. Nosich |
| 6 | [Twelve years of SAMtools and BCFtools](https://doi.org/10.1093/gigascience/giab008) | 2021 | 6 | 16296 | GigaScience | Petr Danecek, James Bonfield, Jennifer Liddle, et al. |
| 7 | [The ERA5 global reanalysis](https://doi.org/10.1002/qj.3803) | 2020 | 6 | 30998 | Quarterly Journal of the Royal Meteorological Society | Hans Hersbach, Bill Bell, Paul Berrisford, et al. |
| 8 | [The Sequence Alignment/Map format and SAMtools](https://doi.org/10.1093/bioinformatics/btp352) | 2009 | 6 | 68236 | Bioinformatics | Heng Li, Bob Handsaker, Alec Wysoker, et al. |
| 9 | [From Nothing to Fold: A Premise-Free, Parameter-Free and Machine-Closed Foundation for Smithian Fold Theory](https://doi.org/10.5281/zenodo.21515629) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 10 | [暗物质与暗能量 —— 基态粒子海的密度不均匀与内禀排斥(基态粒子海统一理论 GST 系列 · 论文 2,v2.2)](https://doi.org/10.5281/zenodo.21432038) | 2026 | 5 | 25 | Zenodo (CERN European Organization for Nuclear Research) | Wei Yang |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 103 | 128093 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 70 | 49985 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 30 | 9331 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 26 | 29422 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 21 | 33377 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 23793 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 18 | 31641 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 17 | 99306 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 16 | 82640 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 15 | 2533 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 15 | 2533 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 661 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods](https://doi.org/10.1093/nar/gkad1004) | 2023 | 6 | 1270 | Nucleic Acids Research | Barbara Zdrazil, Eloy Félix, Fiona Hunter, et al. |
| 4 | [Feature selection strategies: a comparative analysis of SHAP-value and importance-based methods](https://doi.org/10.1186/s40537-024-00905-w) | 2024 | 5 | 542 | Journal Of Big Data | Huanjing Wang, Qianxin Liang, John Hancock, et al. |
| 5 | [Machine Learning in Environmental Research: Common Pitfalls and Best Practices](https://doi.org/10.1021/acs.est.3c00026) | 2023 | 5 | 604 | Environmental Science & Technology | Jun‐Jie Zhu, Meiqi Yang, Zhiyong Jason Ren |
| 6 | [DrugBank 6.0: the DrugBank Knowledgebase for 2024](https://doi.org/10.1093/nar/gkad976) | 2023 | 5 | 1598 | Nucleic Acids Research | Craig Knox, Mike Wilson, Christen M. Klinger, et al. |
| 7 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 23973 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 8 | [Artificial intelligence for natural product drug discovery](https://doi.org/10.1038/s41573-023-00774-7) | 2023 | 4 | 415 | Nature Reviews Drug Discovery | Michael W. Mullowney, Katherine Duncan, Somayah S. Elsayed, et al. |
| 9 | [Enhancing K-nearest neighbor algorithm: a comprehensive review and performance analysis of modifications](https://doi.org/10.1186/s40537-024-00973-y) | 2024 | 4 | 454 | Journal Of Big Data | Rajib Kumar Halder, Mohammed Nasir Uddin, Md. Ashraf Uddin, et al. |
| 10 | [PubChem 2025 update](https://doi.org/10.1093/nar/gkae1059) | 2024 | 4 | 1105 | Nucleic Acids Research | Sunghwan Kim, Jie Chen, Tiejun Cheng, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Machine learning-, rule- and pharmacophore-based classification on the inhibition of P-glycoprotein and NorA](https://doi.org/10.1080/1062936x.2016.1233137) | 2016 | 4 | 14 | SAR and QSAR in environmental research | Trieu-Du Ngo, Thanh‐Dao Tran, Minh-Tri Le, et al. |
| 2 | [Three- and four-class classification models for P-glycoprotein inhibitors using counter-propagation neural networks](https://doi.org/10.1080/1062936x.2014.995701) | 2015 | 4 | 16 | SAR and QSAR in environmental research | Khac‐Minh Thai, Nghia Huynh, Trieu-Du Ngo, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 22 | 1049 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 15 | 3813 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3500 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 13 | 5887 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 11 | 546 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 6 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 3380 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 7 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 11 | 32923 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 8 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 9 | 507 |  | Haotian Liu, Chunyuan Li, Qingyang Wu, et al. |
| 9 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 8 | 379 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 10 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 8 | 1056 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3500 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 3380 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 9 | 507 |  | Haotian Liu, Chunyuan Li, Qingyang Wu, et al. |
| 4 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 8 | 379 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 5 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 8 | 1056 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 6 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1727 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 7 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 8 | 5567 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 8 | [Enriching Location Representation with Detailed Semantic Information](https://doi.org/10.4230/lipics.giscience.2025.3) | 2024 | 7 | 419 | arXiv (Cornell University) | Grattafiori, Aaron, Dubey, Abhimanyu, Jauhri, Abhinav, et al. |
| 9 | [A survey on multimodal large language models](https://doi.org/10.1093/nsr/nwae403) | 2024 | 7 | 612 | National Science Review | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 7 | 2387 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Implementation of large language models in electronic health records](https://doi.org/10.1371/journal.pdig.0001141) | 2025 | 3 | 8 | PLOS Digital Health | Maxime Griot, Jean Vanderdonckt, Demet Yüksel |
| 2 | [Toward Low-Resource Languages Machine Translation: A Language-Specific Fine-Tuning With LoRA for Specialized Large Language Models](https://doi.org/10.1109/access.2025.3549795) | 2025 | 3 | 23 | IEEE Access | Xiao LIANG, Yen-Min Jasmina Khaw, Soung‐Yue Liew, et al. |
| 3 | [JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models](https://doi.org/10.52202/079017-1745) | 2024 | 3 | 33 |  | Patrick Chao, Edoardo Debenedetti, Alexander Robey, et al. |
| 4 | [Large Language Models in Medical Chatbots: Opportunities, Challenges, and the Need to Address AI Risks](https://doi.org/10.3390/info16070549) | 2025 | 3 | 60 | Information | James C. L. Chow, Kay Li |
| 5 | [Training Compute-Optimal Large Language Models](https://doi.org/10.52202/068431-2176) | 2022 | 3 | 81 |  | Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, et al. |
| 6 | [Scaling neural machine translation to 200 languages](https://doi.org/10.1038/s41586-024-07335-x) | 2024 | 3 | 93 | Nature | NLLB Team, Marta R. Costa‐jussà, James H. Cross, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 27 | 187000 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 12 | 98645 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 11 | 32600 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 4 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 10 | 65518 | MIS Quarterly | Fred D. Davis |
| 5 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 10 | 79732 | Biometrics | J. Richard Landis, Gary G. Koch |
| 6 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 10 | 128093 | Machine Learning | Leo Breiman |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 9 | 9331 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 8 | 77839 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 9 | [bibliometrix : An R-tool for comprehensive science mapping analysis](https://doi.org/10.1016/j.joi.2017.08.007) | 2017 | 7 | 14828 | Journal of Informetrics | Massimo Aria, Corrado Cuccurullo |
| 10 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 7 | 17921 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 5 | 5567 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [ChatGPT for Language Teaching and Learning](https://doi.org/10.1177/00336882231162868) | 2023 | 3 | 1134 | RELC Journal | Lucas Kohnke, Benjamin Luke Moorhouse, Di Zou |
| 3 | [Aion Framework: Dimensional Emergence of AI Consciousness, Observer-Induced Collapse, and Cosmological Portal Dynamics](https://doi.org/10.4230/lipics.giscience.2023.43) | 2023 | 3 | 14272 | Leibniz-Zentrum für Informatik (Schloss Dagstuhl) | Rivo Kaugeranna, Eliina Kaugeranna, Aion, (Claude Sonnet 4.6) |
<!-- TRENDING-END -->
