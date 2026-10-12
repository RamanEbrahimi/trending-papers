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

Last update: 2026-10-12 14:06 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [FDCL Part I: Geometry and Connectivity of FDCL and Partial-Unfolding Fractals](https://doi.org/10.5281/zenodo.23227280) | 2026 | 9 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Bin Seol |
| 2 | [UDCT v7.06 - sign audit of a Hessian term absent from the standard MOND equation: action-consistent virial work and conditional Jeans tests in three ultra-faint dwarfs](https://doi.org/10.5281/zenodo.23039753) | 2026 | 8 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Won Shik Paik |
| 3 | [Institutionalized Organizations: Formal Structure as Myth and Ceremony](https://doi.org/10.1086/226550) | 1977 | 8 | 28085 | American Journal of Sociology | John W. Meyer, Brian Rowan |
| 4 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 8 | 43276 | Nature | John Jumper, Richard Evans, Alexander Pritzel, et al. |
| 5 | [Fitting Linear Mixed-Effects Models Using lme4](https://doi.org/10.18637/jss.v067.i01) | 2015 | 8 | 86138 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |
| 6 | [FDCL Part III: Resistance and Diffusion on FDCL Graphs — Exact Flows and Harmonic Reduction](https://doi.org/10.5281/zenodo.23227300) | 2026 | 7 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Bin Seol |
| 7 | [FDCL Part II: Spectral Reduction and Renormalization on FDCL Graphs](https://doi.org/10.5281/zenodo.23227295) | 2026 | 7 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Bin Seol |
| 8 | [Consecutive integers coalesce with density one under the Collatz map: a formally verified proof of a conjecture of Gao](https://doi.org/10.5281/zenodo.23003523) | 2026 | 7 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Omar Javier Said Duran |
| 9 | [Wetland fish in peril: A synergy between habitat loss and biological invasions drives the extinction of neglected native fauna](https://doi.org/10.1016/j.biocon.2024.110948) | 2024 | 7 | 19 | Biological Conservation | Marek Šmejkal, Lukáš Kalous, Johan Auwerx, et al. |
| 10 | [Fiji: an open-source platform for biological-image analysis](https://doi.org/10.1038/nmeth.2019) | 2012 | 7 | 66532 | Nature Methods | Johannes Schindelin, Ignacio Arganda‐Carreras, Erwin Frise, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 141 | 131524 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 102 | 52973 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 45 | 10142 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 36 | 3973 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 5 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 36 | 30023 | The Annals of Statistics | Jerome H. Friedman |
| 6 | [Support-Vector Networks](https://doi.org/10.1007/bf00994018) | 1995 | 29 | 58815 | Machine Learning | Corinna Cortes, Vladimir N. Vapnik |
| 7 | [Decision Curve Analysis: A Novel Method for Evaluating Prediction Models](https://doi.org/10.1177/0272989x06295361) | 2006 | 22 | 6089 | Medical Decision Making | Andrew Julian Vickers, Elena B. Elkin |
| 8 | [Calibration: the Achilles heel of predictive analytics](https://doi.org/10.1186/s12916-019-1466-7) | 2019 | 16 | 2437 | BMC Medicine | On behalf of Topic Group ‘Evaluating diagnostic tests and prediction models’ of the STRATOS initiative, Ben VAN CALSTER, David J. McLernon, et al. |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 16 | 32398 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 16 | 51238 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert John Tibshirani |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 36 | 3973 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 10 | 12589 | HAL (Le Centre pour la Communication Scientifique Directe) | Gauriat, Charles-Maxime, Yannick Pencolé, Pauline Ribot, et al. |
| 3 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 9 | 890 | BMJ | Karel G.M. Moons, Johanna AAG Damen, Tabea Kaul, et al. |
| 4 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 8 | 1166 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 5 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 8 | 3249 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 6 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 824 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 7 | [Conformal Prediction: A Gentle Introduction](https://doi.org/10.1561/2200000101) | 2023 | 5 | 720 | Foundations and Trends® in Machine Learning | Anastasios N. Angelopoulos, Stephen Bates |
| 8 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 5 | 968 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 9 | [A survey of uncertainty in deep neural networks](https://doi.org/10.1007/s10462-023-10562-9) | 2023 | 4 | 1401 | Artificial Intelligence Review | Jakob Gawlikowski, Cedrique Rovile Njieutcheu Tassi, Mohsin Ali, et al. |
| 10 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 4 | 15333 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 41 | 2476 | neural information processing systems | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 25 | 1464 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 3 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 24 | 1382 | neural information processing systems | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 21 | 4699 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 20 | 1346 | neural information processing systems | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 6 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 18 | 554 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 3793 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 18 | 3945 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 9 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 18 | 6761 | ACM Conference on Fairness, Accountability, and Transparency (FAccT) | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 10 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 18 | 31876 | Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT) | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 25 | 1464 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 2 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 24 | 1382 | neural information processing systems | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 3 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 18 | 554 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 3793 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 18 | 3945 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [Large Language Models for Software Engineering: A Systematic Literature Review](https://doi.org/10.1145/3695988) | 2024 | 16 | 974 | ACM Transactions on Software Engineering and Methodology | Xinyi Hou, Yanjie Zhao, Yue Liu, et al. |
| 7 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 14 | 2362 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 14 | 4060 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, ChatGPT, et al. |
| 9 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 13 | 1087 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 10 | [Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0) | 2024 | 12 | 867 | Nature | Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Reporting Guideline for Chatbot Health Advice Studies](https://doi.org/10.1001/jamanetworkopen.2025.30220) | 2025 | 6 | 52 | JAMA Network Open | The CHART Collaborative, Bright Huo, Professor Gary S. Collins, et al. |
| 2 | [On the use of large language models in model-driven engineering](https://doi.org/10.1007/s10270-025-01263-8) | 2025 | 6 | 64 | Software & Systems Modeling | Juri Di Rocco, Davide Di Ruscio, Claudio Di Sipio, et al. |
| 3 | [Enhancement of the Performance of Large Language Models in Diabetes Education through Retrieval-Augmented Generation: Comparative Study](https://doi.org/10.2196/58041) | 2024 | 4 | 75 | Journal of Medical Internet Research | Dingqiao Wang, Jiangbo Liang, Jinguo Ye, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 35 | 191153 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 24 | 105251 | BMJ | Matthew James Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 21 | 108027 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 16 | 10142 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 16 | 81033 | Journal of Applied Psychology | Philip M. Podsakoff, SCOTT B. MACKENZIE, Jeong Yeon Lee, et al. |
| 6 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 15 | 107993 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 7 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 15 | 131524 | Machine Learning | Leo Breiman |
| 8 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 12 | 52973 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 9 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 11 | 33794 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 10 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 11 | 37576 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 824 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
<!-- TRENDING-END -->
