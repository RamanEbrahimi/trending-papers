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

Last update: 2026-06-22 11:40 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Why Strong Governance Still Drifts: How Institutions Quietly Lose Alignment](https://doi.org/10.5281/zenodo.18471068) | 2026 | 20 | 89 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 2 | [The Field Protocol: Measuring Translation Coherence in Institutional Systems](https://doi.org/10.5281/zenodo.18657810) | 2026 | 20 | 90 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 3 | [The Sovereign Spine: How Institutions Stay True to Their Intent Over Time](https://doi.org/10.5281/zenodo.18646691) | 2026 | 20 | 93 | Open MIND | Robin Edgard Ulrik Mertens |
| 4 | [The Green Dashboard Trap: Why Institutions Lose Sight of Their Own Intent](https://doi.org/10.5281/zenodo.18641907) | 2026 | 19 | 88 | Open MIND | Robin Edgard Ulrik Mertens |
| 5 | [The Sovereign Spine: A New Theory of Institutional Coherence and Agency](https://doi.org/10.5281/zenodo.18649453) | 2026 | 19 | 88 | Open MIND | Robin Edgard Ulrik Mertens |
| 6 | [AI-Augmented Impact Frames: A Closed-Loop Architecture for Purpose-Aligned Decisions](https://doi.org/10.5281/zenodo.18668799) | 2026 | 19 | 88 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 7 | [How Decision Systems Learn What Matters: Building Purpose-Aligned Governance](https://doi.org/10.5281/zenodo.17964280) | 2026 | 19 | 89 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 8 | [Designing the Meaning Infrastructure: Governing Interpretation in AI-Driven Institutions](https://doi.org/10.5281/zenodo.18494690) | 2026 | 19 | 89 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 9 | [Making Meaning Measurable: How to See Coherence in Decision Systems](https://doi.org/10.5281/zenodo.18486778) | 2026 | 19 | 89 | Open MIND | Robin Edgard Ulrik Mertens |
| 10 | [Decision Velocity and the Compression of Detectability: Translation Half-Life in Institutional Governance](https://doi.org/10.5281/zenodo.18770887) | 2026 | 13 | 80 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 105 | 125873 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 68 | 48461 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 26 | 28903 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 23 | 23345 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 19 | 8892 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 19 | 32987 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 15 | 8975 | Nature Machine Intelligence | Cynthia Rudin |
| 8 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 13 | 7345 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 13 | 81540 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 12 | 16112 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 11 | 2147 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 8 | 582 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Artificial Intelligence and Machine Learning in Clinical Medicine, 2023](https://doi.org/10.1056/nejmra2302038) | 2023 | 6 | 1138 | New England Journal of Medicine | Charlotte Haug, Jeffrey M. Drazen |
| 4 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 6 | 2764 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 5 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 5 | 664 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 6 | [Hyperparameter optimization: Foundations, algorithms, best practices, and open challenges](https://doi.org/10.1002/widm.1484) | 2023 | 5 | 804 | Wiley Interdisciplinary Reviews Data Mining and Knowledge Discovery | Bernd Bischl, Martin Binder, Michel Lang, et al. |
| 7 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13331 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 8 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 4 | 367 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 9 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 4 | 22959 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 3506 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 2 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 9 | 538 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 3 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 9 | 903 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 3170 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 8 | 350 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 6 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1519 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 3305 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2452 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 3559 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 7 | 5058 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 9 | 903 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 3170 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 8 | 350 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1519 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 3305 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2452 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 3559 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 8 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 7 | 5058 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 9 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 718 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 10 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 6 | 1444 |  | Joon Sung Park, Joseph O’Brien, Carrie J. Cai, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Efficient Inference for Edge Large Language Models: A Survey](https://doi.org/10.26599/tst.2025.9010166) | 2025 | 3 | 10 | Tsinghua Science & Technology | Guanyu Cai, Ruiming Tian, Lang Yang, et al. |
| 2 | [Compressing Context to Enhance Inference Efficiency of Large Language Models](https://doi.org/10.18653/v1/2023.emnlp-main.391) | 2023 | 3 | 59 |  | Yucheng Li, Bo Dong, Frank Guérin, et al. |
| 3 | [LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression](https://doi.org/10.18653/v1/2024.acl-long.91) | 2024 | 3 | 69 |  | Huiqiang Jiang, Qianhui Wu, Xufang Luo, et al. |
| 4 | [Qwen2.5 Technical Report](https://doi.org/10.48550/arxiv.2412.15115) | 2024 | 3 | 78 | arXiv (Cornell University) | Qwen, :, Yang An, et al. |
| 5 | [A survey of multilingual large language models](https://doi.org/10.1016/j.patter.2024.101118) | 2025 | 3 | 83 | Patterns | Libo Qin, Qiguang Chen, Yuhang Zhou, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 26 | 182765 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 13 | 40243 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 3 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 13 | 125873 | Machine Learning | Leo Breiman |
| 4 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 12 | 64404 | MIS Quarterly | Fred D. Davis |
| 5 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 12 | 94449 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 6 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 11 | 76408 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 7 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 11 | 105211 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 8 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 10 | 33578 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 9 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 9 | 28903 | The Annals of Statistics | Jerome H. Friedman |
| 10 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 9 | 32041 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 5 | 5058 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 4 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 4 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 4 | 46 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 4 | 1444 |  | Joon Sung Park, Joseph O’Brien, Carrie J. Cai, et al. |
| 7 | [Longitudinal modifiable risk and protective factors of internet gaming disorder: A systematic review and meta-analysis](https://doi.org/10.1556/2006.2023.00017) | 2023 | 3 | 82 | Journal of Behavioral Addictions | Xiaoyu Zhuang, Youmin Zhang, Xinfeng Tang, et al. |
| 8 | [Impact of AI assistance on student agency](https://doi.org/10.1016/j.compedu.2023.104967) | 2023 | 3 | 378 | Computers & Education | Ali Darvishi, Hassan Khosravi, Shazia Sadiq, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 4 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 4 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 4 | 46 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Longitudinal modifiable risk and protective factors of internet gaming disorder: A systematic review and meta-analysis](https://doi.org/10.1556/2006.2023.00017) | 2023 | 3 | 82 | Journal of Behavioral Addictions | Xiaoyu Zhuang, Youmin Zhang, Xinfeng Tang, et al. |
<!-- TRENDING-END -->
