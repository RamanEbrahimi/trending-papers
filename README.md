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

Last update: 2026-10-26 12:02 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [立体矩阵论基础:定义、直和结构与表征能力](https://doi.org/10.5281/zenodo.23430222) | 2026 | 15 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 2 | [立体矩阵的可认证计算与编码体系](https://doi.org/10.5281/zenodo.23430229) | 2026 | 14 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 3 | [立体矩阵的内蕴结构:胞腔复形与等价类全谱](https://doi.org/10.5281/zenodo.23430231) | 2026 | 13 | 13 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 4 | [Agentic AI Assurance Test Taxonomy v1](https://doi.org/10.5281/zenodo.23587406) | 2026 | 13 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Srinivas Padmanabhuni |
| 5 | [标准等价类的结构性能与归约动力学:兑换律守恒](https://doi.org/10.5281/zenodo.23430238) | 2026 | 12 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 6 | [Agentic AI Assurance Test Catalogue — Day 1 Addendum (Tests T1-001–T1-007)](https://doi.org/10.5281/zenodo.23592356) | 2026 | 12 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Srinivas Padmanabhuni |
| 7 | [立体矩阵的翻转图动力学与归约收敛](https://doi.org/10.5281/zenodo.23430245) | 2026 | 11 | 11 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 8 | [Agentic AI Assurance Test Catalogue — Day 2 Addendum (Tests T1-008–T1-014)](https://doi.org/10.5281/zenodo.23593960) | 2026 | 11 | 13 | Zenodo (CERN European Organization for Nuclear Research) | Srinivas Padmanabhuni |
| 9 | [遗忘的边界:有限容量下的记忆、智能与自我](https://doi.org/10.5281/zenodo.23323276) | 2026 | 11 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Li Yipeng |
| 10 | [区分的演化:统一值不值——一套压缩方法、一个图上的硬核定理、三次自我检视,与一堵没绕开的墙](https://doi.org/10.5281/zenodo.23345012) | 2026 | 11 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Li Yipeng |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 152 | 132621 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 91 | 53788 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 49 | 30397 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Support-Vector Networks](https://doi.org/10.1007/bf00994018) | 1995 | 37 | 59326 | Machine Learning | Corinna Cortes, Vladimir N. Vapnik |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 31 | 10434 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 30 | 4491 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 7 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 27 | 102124 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 8 | [Cross‐validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure](https://doi.org/10.1111/ecog.02881) | 2016 | 25 | 3596 | Ecography | David R. Roberts, Volker Bahn, Simone Ciuti, et al. |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 24 | 83980 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 19 | 32652 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 30 | 4491 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 11 | 1292 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 3 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 10 | 1006 | BMJ | Karel G.M. Moons, Johanna AAG Damen, Tabea Kaul, et al. |
| 4 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 10 | 12620 | HAL | Gauriat, Charles-Maxime, Yannick Pencolé, Pauline Ribot, et al. |
| 5 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 8 | 850 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 6 | [Conformal Prediction: A Gentle Introduction](https://doi.org/10.1561/2200000101) | 2023 | 7 | 814 | Foundations and Trends® in Machine Learning | Anastasios N. Angelopoulos, Stephen Bates |
| 7 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 6 | 3353 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 8 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 26753 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 25 | 48364 | Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT) | Jacob Devlin, Ming-Wei Chang, Kenton Lee, et al. |
| 2 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 21 | 4392 | neural information processing systems | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 4040 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 3878 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 16 | 4909 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 6 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 15 | 12705 |  | Nils Reimers, Iryna Gurevych |
| 7 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 12 | 3053 | neural information processing systems | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 8 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 11 | 783 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 9 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 11 | 1790 | neural information processing systems | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 10 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 6904 | ACM Conference on Fairness, Accountability, and Transparency (FAccT) | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 4040 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 3878 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 11 | 783 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 4 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 11 | 1790 | neural information processing systems | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 5 | [Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0) | 2024 | 10 | 913 | Nature | Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, et al. |
| 6 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 10 | 1830 | neural information processing systems | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 7 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 9 | 589 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 8 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 9 | 2154 | ACM Symposium on User Interface Software and Technology (UIST) | Joon-Sung Park, Joseph O'Brien, Carrie Jun Cai, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 9 | 2485 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 9 | 2581 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark H. Dredze, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [DAn building blocks for integrated care co-design, source 6: a regional law on family carers](https://doi.org/10.5281/zenodo.23506430) | 2026 | 5 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Angelo Rossi Mori |
| 2 | [DAn building blocks for integrated care co-design, source 2: integrated care initiatives from recent literature](https://doi.org/10.5281/zenodo.23506236) | 2026 | 5 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Angelo Rossi Mori |
| 3 | [DAn building blocks for integrated care co-design, source 1: Italian project sheets from a national conference](https://doi.org/10.5281/zenodo.23506196) | 2026 | 5 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Angelo Rossi Mori |
| 4 | [DAn building blocks for integrated care co-design, source 3: European practices with a community component](https://doi.org/10.5281/zenodo.23506252) | 2026 | 5 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Angelo Rossi Mori |
| 5 | [DAn building blocks for integrated care co-design, source 4: a white paper of policy proposals](https://doi.org/10.5281/zenodo.23506381) | 2026 | 5 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Angelo Rossi Mori |
| 6 | [DAn building blocks for integrated care co-design, source 5: a national decree broken down into nine goals](https://doi.org/10.5281/zenodo.23506407) | 2026 | 5 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Angelo Rossi Mori |
| 7 | [Special Session: ThreatLens: LLM-guided Threat Modeling and Test Plan Generation for Hardware Security Verification](https://doi.org/10.1109/vts65138.2025.11022932) | 2025 | 4 | 15 | Proceedings - IEEE VLSI Test Symposium/Proceedings of the ... IEEE VLSI Test Symposium | Dipayan Saha, Hasan Al Shaikh, Shams Tarek, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 26 | 193557 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037//0003-066x.55.1.68) | 2000 | 19 | 46775 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 3 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 16 | 132621 | Machine Learning | Leo Breiman |
| 4 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 15 | 107146 | BMJ | Matthew James Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 5 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 14 | 68214 | MIS Quarterly | Fred D. Davis |
| 6 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 14 | 81789 | Journal of Applied Psychology | Philip M. Podsakoff, SCOTT B. MACKENZIE, Jeong Yeon Lee, et al. |
| 7 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 13 | 108545 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 8 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 12 | 53788 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 9 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 10 | 108807 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 10 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 9 | 44905 | MIS Quarterly | Viswanath Venkatesh, Michael G. Morris, Gordon B. Davis, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using artificial intelligence in sustainability teaching and learning](https://doi.org/10.1186/s12302-025-01159-w) | 2025 | 4 | 48 | Environmental Sciences Europe | Walter Leal Filho, Eundeok Kim, Jaluza Maria Lima Silva Borsatto, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Bending the rules, breaking the rules: How corruption and lobbying affect the investment market selection of Swedish firms](https://doi.org/10.1111/twec.12488) | 2017 | 4 | 18 | World Economy | Susanna Thede, Nils‐Åke Gustafson |
| 2 | [Effects of corruption on foreign direct investment: Evidence from Swedish multinational enterprises](https://doi.org/10.1016/j.jce.2022.10.004) | 2022 | 4 | 26 | Journal of Comparative Economics | Susanna Thede, Patrik Karpaty |
| 3 | [Using artificial intelligence in sustainability teaching and learning](https://doi.org/10.1186/s12302-025-01159-w) | 2025 | 4 | 48 | Environmental Sciences Europe | Walter Leal Filho, Eundeok Kim, Jaluza Maria Lima Silva Borsatto, et al. |
| 4 | [Birds of a feather: Evidence on commonality of corruption and democracy in the origin and location of foreign investment in Russian regions](https://doi.org/10.1016/j.ejpoleco.2013.06.003) | 2013 | 4 | 56 | European Journal of Political Economy | Svetlana Ledyaeva, Päivi Karhunen, Riitta Kosonen |
<!-- TRENDING-END -->
