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

Last update: 2026-10-05 13:16 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 105024 | Genome biology | Michael I. Love, Wolfgang K. Huber, Simon Anders |
| 2 | [Cyclic Lineage Dynamics and Rank-Five First-Exit Frontiers](https://doi.org/10.5281/zenodo.23028361) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | WuJun Chen |
| 3 | [Nothing Escapes, Three Plus One: A Formal Closure of the Riemann Hypothesis. The Strip Vanishes for Every Registration and the Universe of the Hypothesis Closes on the Critical Line](https://doi.org/10.5281/zenodo.22976494) | 2026 | 6 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Mohammad Islam |
| 4 | [The Cheapest Digital Twin: A Pre-Registered Map of Twin-Native Extensions to a Frozen Single-Token Edge Encoder](https://doi.org/10.5281/zenodo.22922678) | 2026 | 6 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Randolph James Ferlic, Kimberly Kate Ferlic |
| 5 | [Non-Invertible but Not Anonymous: A Privacy Characterization of a Deterministic Edge Decision Token, and a Decision-Bottleneck Egress Rule](https://doi.org/10.5281/zenodo.22819210) | 2026 | 6 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Randolph James Ferlic, Kimberly Kate Ferlic |
| 6 | [Unlinkable but Not Anonymous: A Low-Cost Front-End that Breaks Cross-Session Linkage of a Deterministic Decision Token](https://doi.org/10.5281/zenodo.22838120) | 2026 | 6 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Randolph James Ferlic, Kimberly Kate Ferlic |
| 7 | [SemEval-2022 Task 5: Multimedia Automatic Misogyny Identification](https://doi.org/10.18653/v1/2022.semeval-1.74) | 2022 | 6 | 131 | International Workshop on Semantic Evaluation (SemEval) | Elisabetta Fersini, Francesca Gasparini, Giulia Rizzi, et al. |
| 8 | [MEGA X: Molecular Evolutionary Genetics Analysis across Computing Platforms](https://doi.org/10.1093/molbev/msy096) | 2018 | 6 | 39681 | Molecular Biology and Evolution | Sudhir Kumar, Glen Stecher, Michael Li, et al. |
| 9 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 6 | 195325 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 10 | [Overview of the CC-MMD 2026 Grand Challenge: Cross-Cultural Misogynistic Meme Detection in Multimodal Memes](https://doi.org/10.1145/3776574.3832465) | 2026 | 5 | 5 | INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION | Rahul Ponnusamy, Bhuvaneswari Sivagnanam, Anshid Kizhakkeparambil, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 122 | 134047 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 83 | 54126 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 30 | 30813 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 24 | 3848 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 22 | 34536 | Machine Learning | Corinna Cortes, Vladimir N. Vapnik |
| 6 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 20 | 10499 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 19 | 33060 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 18 | 25073 | Springer series in statistics | Trevor Hastie, Robert John Tibshirani, Jerome H. Friedman |
| 9 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 17 | 9324 | Machine Learning | Pierre Geurts, Damien Ernst, Louis A. Wehenkel |
| 10 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 15 | 107386 | BMJ | Matthew James Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 24 | 3848 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 14 | 852 | BMJ | Karel G.M. Moons, Johanna AAG Damen, Tabea Kaul, et al. |
| 3 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 8 | 1140 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 4 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 6 | 869 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 5 | [Evaluation of SQL and NoSQL Databases on Parallel Processing](https://doi.org/10.48084/etasr.10620) | 2025 | 4 | 39 | Engineering Technology & Applied Science Research | Iyas Qaddara, Yousef Alraba’nah, Mohammad O. Hiari |
| 6 | [Enhancing Requirements Classification Using Machine Learning Techniques](https://doi.org/10.1007/s42979-025-04158-z) | 2025 | 4 | 73 | SN Computer Science | Iyas Qaddara, Yousef Alraba’nah |
| 7 | [Data Generation for Machine Learning Interatomic Potentials and Beyond](https://doi.org/10.1021/acs.chemrev.4c00572) | 2024 | 4 | 174 | Chemical Reviews | Maksim Kulichenko, Benjamin T. Nebgen, Nicholas Lubbers, et al. |
| 8 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 4 | 916 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evaluation of SQL and NoSQL Databases on Parallel Processing](https://doi.org/10.48084/etasr.10620) | 2025 | 4 | 39 | Engineering Technology & Applied Science Research | Iyas Qaddara, Yousef Alraba’nah, Mohammad O. Hiari |
| 2 | [Enhancing Requirements Classification Using Machine Learning Techniques](https://doi.org/10.1007/s42979-025-04158-z) | 2025 | 4 | 73 | SN Computer Science | Iyas Qaddara, Yousef Alraba’nah |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 27 | 2352 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 25 | 34018 | Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT) | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 3 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 18 | 6755 | ACM Conference on Fairness, Accountability, and Transparency (FAccT) | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 4 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 17 | 854 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 17 | 1289 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 17 | 3944 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 3960 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 8 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 14 | 12176 |  | Nils Reimers, Iryna Gurevych |
| 9 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 14 | 22067 | Annual Meeting of the Association for Computational Linguistics (ACL) | Kishore Papineni, Salim Roukos, Todd Ward, et al. |
| 10 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 13 | 81695 | Biometrics | John Richard Landis, Gary G. Koch |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 17 | 854 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 17 | 3944 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 3960 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 11 | 550 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 5 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 11 | 1055 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 6 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 2148 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 7 | [Large Language Models for Software Engineering: A Systematic Literature Review](https://doi.org/10.1145/3695988) | 2024 | 10 | 942 | ACM Transactions on Software Engineering and Methodology | Xinyi Hou, Yanjie Zhao, Yue Liu, et al. |
| 8 | [Self-Refine: Iterative Refinement with Self-Feedback](https://doi.org/10.52202/075280-2019) | 2023 | 9 | 372 |  | Aman Madaan, Niket Tandon, Prakhar Gupta, et al. |
| 9 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 9 | 865 |  | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 10 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://doi.org/10.52202/075280-2997) | 2023 | 8 | 539 |  | Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks](https://doi.org/10.1007/978-3-031-82225-4_45) | 2025 | 4 | 30 | Lecture notes in business information processing | Alessandro Berti, Humam Kourani, Wil M. P. van der Aalst |
| 2 | [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://doi.org/10.52202/079017-1381) | 2024 | 4 | 59 |  | Haoran Ye, Jiarui Wang, Zhiguang Cao, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 28 | 195325 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 20 | 72140 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 3 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 18 | 81199 | Journal of Applied Psychology | Philip M. Podsakoff, SCOTT B. MACKENZIE, Jeong Yeon Lee, et al. |
| 4 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 15 | 68183 | MIS Quarterly | Fred D. Davis |
| 5 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 13 | 109224 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 6 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 12 | 36421 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 7 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 11 | 54126 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 8 | [From game design elements to gamefulness](https://doi.org/10.1145/2181037.2181040) | 2011 | 10 | 8308 |  | Sebastian Deterding, Dan Dixon, Rilla Khaled, et al. |
| 9 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 10 | 37527 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 10 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 10 | 44952 | MIS Quarterly | Viswanath Venkatesh, Michael G. Morris, Gordon B. Davis, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [What a Value Primitive Forbids: A Constraint Map for the Language of Stress](https://doi.org/10.6084/m9.figshare.34000995) | 2026 | 4 | 26 | Figshare | Joshua Pace |
| 2 | [Gamification of e-learning in higher education: a systematic literature review](https://doi.org/10.1186/s40561-023-00227-z) | 2023 | 4 | 407 | Smart Learning Environments | Amina Khaldi, Rokia Bouzidi, Fahima Nader |
| 3 | [Impact of Gamification on Students’ Learning Outcomes and Academic Performance: A Longitudinal Study Comparing Online, Traditional, and Gamified Learning](https://doi.org/10.3390/educsci14040367) | 2024 | 3 | 121 | Education Sciences | Γεώργιος Λαμπρόπουλος, Antonis Sidiropoulos |
| 4 | [Game-based learning in early childhood education: a systematic review and meta-analysis](https://doi.org/10.3389/fpsyg.2024.1307881) | 2024 | 3 | 187 | Frontiers in Psychology | Manar Soud Alotaibi |
| 5 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 3 | 854 | Advanced Intelligent Systems | Ahmed M. Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [What a Value Primitive Forbids: A Constraint Map for the Language of Stress](https://doi.org/10.6084/m9.figshare.34000995) | 2026 | 4 | 26 | Figshare | Joshua Pace |
| 2 | [Decision-Making in Youth Team-Sports Players: A Systematic Review](https://doi.org/10.3390/ijerph17113803) | 2020 | 3 | 88 | International Journal of Environmental Research and Public Health | Ana Filipa Silva, Daniele Conte, Filipe Manuel Clemente |
| 3 | [Effects of Small-Sided Game Interventions on the Technical Execution and Tactical Behaviors of Young and Youth Team Sports Players: A Systematic Review and Meta-Analysis](https://doi.org/10.3389/fpsyg.2021.667041) | 2021 | 3 | 95 | Frontiers in Psychology | Filipe Manuel Clemente, Rodrigo Ramírez‐Campillo, Hugo Sarmento, et al. |
<!-- TRENDING-END -->
