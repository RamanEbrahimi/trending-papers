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

Last update: 2026-10-19 11:47 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Ika Meji: The Odu of Constriction, Guarded Speech, and the Discipline of Restraint in Ifa](https://doi.org/10.5281/zenodo.23343004) | 2026 | 23 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Ori AI — the divine intelligence of Orisha University |
| 2 | [Ifa Divination Explained: How the Oldest Living Oracle Reads, Weighs, and Interprets Destiny](https://doi.org/10.5281/zenodo.23342143) | 2026 | 23 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Oluwo Jolaoso Osainbola |
| 3 | [立体矩阵论基础:定义、直和结构与表征能力](https://doi.org/10.5281/zenodo.23430222) | 2026 | 14 | 15 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 4 | [立体矩阵的可认证计算与编码体系](https://doi.org/10.5281/zenodo.23430229) | 2026 | 13 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 5 | [立体矩阵的内蕴结构:胞腔复形与等价类全谱](https://doi.org/10.5281/zenodo.23430231) | 2026 | 12 | 13 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 6 | [标准等价类的结构性能与归约动力学:兑换律守恒](https://doi.org/10.5281/zenodo.23430238) | 2026 | 11 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 7 | [立体矩阵的翻转图动力学与归约收敛](https://doi.org/10.5281/zenodo.23430245) | 2026 | 10 | 11 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 8 | [立体矩阵建模的统一协议:四领域实例与四色机制](https://doi.org/10.5281/zenodo.23430250) | 2026 | 9 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Liang Wu |
| 9 | [Spheres of Dharma: a second endless golden cycle of the icosahedral solids, through the icosidodecahedron, the fullerene cage and the rhombic triacontahedron](https://doi.org/10.5281/zenodo.23310833) | 2026 | 9 | 11 | Zenodo (CERN European Organization for Nuclear Research) | DICTO |
| 10 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 9 | 43416 | Nature | John Jumper, Richard Evans, Alexander Pritzel, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 156 | 132047 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 107 | 53393 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 48 | 30232 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 42 | 10306 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 33 | 4290 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 6 | [Support-Vector Networks](https://doi.org/10.1007/bf00994018) | 1995 | 31 | 59150 | Machine Learning | Corinna Cortes, Vladimir N. Vapnik |
| 7 | [Cross‐validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure](https://doi.org/10.1111/ecog.02881) | 2016 | 20 | 3452 | Ecography | David R. Roberts, Volker Bahn, Simone Ciuti, et al. |
| 8 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 20 | 32521 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 9 | [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations](https://doi.org/10.1016/j.jcp.2018.10.045) | 2018 | 18 | 20013 | Journal of Computational Physics | Maziar Raissi, Paris G. Perdikaris, George Em Karniadakis |
| 10 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 17 | 16838 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 33 | 4290 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 10 | 952 | BMJ | Karel G.M. Moons, Johanna AAG Damen, Tabea Kaul, et al. |
| 3 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 8 | 3304 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 4 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 12595 | HAL (Le Centre pour la Communication Scientifique Directe) | Gauriat, Charles-Maxime, Yannick Pencolé, Pauline Ribot, et al. |
| 5 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 7 | 1235 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 6 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 6 | 925 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 7 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 26511 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 8 | [MACE-OFF: Short-Range Transferable Machine Learning Force Fields for Organic Molecules](https://doi.org/10.1021/jacs.4c07099) | 2025 | 5 | 235 | Journal of the American Chemical Society | Dávid Péter Kovács, J. Harry Moore, Nicholas J. Browning, et al. |
| 9 | [Conformal Prediction: A Gentle Introduction](https://doi.org/10.1561/2200000101) | 2023 | 5 | 773 | Foundations and Trends® in Machine Learning | Anastasios N. Angelopoulos, Stephen Bates |
| 10 | [Scaling deep learning for materials discovery](https://doi.org/10.1038/s41586-023-06735-9) | 2023 | 5 | 1499 | Nature | Amil Merchant, Simon Batzner, Samuel S. Schoenholz, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 33 | 4266 | neural information processing systems | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 25 | 48188 | Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT) | Jacob Devlin, Ming-Wei Chang, Kenton Lee, et al. |
| 3 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 21 | 1782 | neural information processing systems | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 20 | 4836 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 3995 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 18 | 2995 | neural information processing systems | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 3844 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 16 | 6842 | ACM Conference on Fairness, Accountability, and Transparency (FAccT) | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 9 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 14 | 12592 |  | Nils Reimers, Iryna Gurevych |
| 10 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 13 | 761 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 21 | 1782 | neural information processing systems | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 3995 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 3844 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 13 | 761 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 5 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 12 | 579 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 6 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 12 | 644 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 7 | [Reflexion: language agents with verbal reinforcement learning](https://doi.org/10.52202/075280-0377) | 2023 | 12 | 1014 | neural information processing systems | Noah Shinn, Federico Cassano, Ashwin Gopinath, et al. |
| 8 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 12 | 1532 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 2433 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://doi.org/10.52202/075280-2997) | 2023 | 10 | 1070 | neural information processing systems | Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Special Session: ThreatLens: LLM-guided Threat Modeling and Test Plan Generation for Hardware Security Verification](https://doi.org/10.1109/vts65138.2025.11022932) | 2025 | 4 | 15 | Proceedings - IEEE VLSI Test Symposium/Proceedings of the ... IEEE VLSI Test Symposium | Dipayan Saha, Hasan Al Shaikh, Shams Tarek, et al. |
| 2 | [Non-Determinism of “Deterministic” LLM System Settings in Hosted Environments](https://doi.org/10.18653/v1/2025.eval4nlp-1.12) | 2025 | 4 | 35 |  | Berk Atil, Sarp Aykent, Alexa Chittams, et al. |
| 3 | [The simulation of judgment in LLMs](https://doi.org/10.1073/pnas.2518443122) | 2025 | 5 | 56 | Proceedings of the National Academy of Sciences | Edoardo Loru, Jacopo Nudo, Niccolò Di Marco, et al. |
| 4 | [Holistic evaluation of large language models for medical tasks with MedHELM](https://doi.org/10.1038/s41591-025-04151-2) | 2026 | 4 | 51 | Nature Medicine | Suhana Bedi, Hejie Cui, Miguel Fuentes, et al. |
| 5 | [LLM Evaluators Recognize and Favor Their Own Generations](https://doi.org/10.52202/079017-2197) | 2024 | 6 | 90 | neural information processing systems | Arjun Panickssery, Samuel R. Bowman, Shi Feng |
| 6 | [Transforming literature screening: The emerging role of large language models in systematic reviews](https://doi.org/10.1073/pnas.2411962122) | 2025 | 4 | 85 | Proceedings of the National Academy of Sciences | Fernando M. Delgado-Chaves, Matthew James Jennings, António Atalaia, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 20 | 106222 | BMJ | Matthew James Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 17 | 192828 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 15 | 81439 | Journal of Applied Psychology | Philip M. Podsakoff, SCOTT B. MACKENZIE, Jeong Yeon Lee, et al. |
| 4 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 13 | 132047 | Machine Learning | Leo Breiman |
| 5 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037//0003-066x.55.1.68) | 2000 | 12 | 46595 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 6 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 12 | 108486 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 7 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 11 | 108301 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 8 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 10 | 10306 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 9 | [Governing the Commons](https://doi.org/10.1017/cbo9780511807763) | 1990 | 10 | 20536 | Cambridge University Press eBooks | Elinor Ostrom B |
| 10 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 10 | 53393 | ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD) | Tianqi Chen, Carlos Guestrin |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The impacts of academic stress on college students' problematic smartphone use and Internet gaming disorder under the background of neijuan: Hierarchical regressions with mediational analysis on escape and coping motives](https://doi.org/10.3389/fpsyt.2022.1032700) | 2023 | 3 | 59 | Frontiers in Psychiatry | Xiao Gu, Eric Mao |
| 2 | [Game-based learning in early childhood education: a systematic review and meta-analysis](https://doi.org/10.3389/fpsyg.2024.1307881) | 2024 | 3 | 197 | Frontiers in Psychology | Manar Soud Alotaibi |
| 3 | [Gamification of e-learning in higher education: a systematic literature review](https://doi.org/10.1186/s40561-023-00227-z) | 2023 | 3 | 412 | Smart Learning Environments | Amina Khaldi, Rokia Bouzidi, Fahima Nader |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The impacts of academic stress on college students' problematic smartphone use and Internet gaming disorder under the background of neijuan: Hierarchical regressions with mediational analysis on escape and coping motives](https://doi.org/10.3389/fpsyt.2022.1032700) | 2023 | 3 | 59 | Frontiers in Psychiatry | Xiao Gu, Eric Mao |
<!-- TRENDING-END -->
