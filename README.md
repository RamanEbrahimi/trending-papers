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

Last update: 2026-06-01 11:19 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 23 | 180626 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Case Study Research: Design and Methods](https://openalex.org/W1527311855) | 1984 | 22 | 74955 |  | Robert K. Yin |
| 3 | [Paper 4 — Role Society, Human Discretion, Accountability, and Non-Identifiable Role Coordination](https://doi.org/10.5281/zenodo.20323405) | 2026 | 19 | 44 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 4 | [Paper 1 - BIFACE-Based Sentence Coordinate Documents: Human-Readable Surfaces and AI+AGI-Referable Coordinates Across Documents, Code, Media, and Conversations](https://doi.org/10.5281/zenodo.20322707) | 2026 | 19 | 44 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 5 | [Paper 2 — SCD + Security: Output Reference Boundary Structures in the AGI Era](https://doi.org/10.5281/zenodo.20322990) | 2026 | 19 | 44 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 6 | [Paper 3 — CHOPSTICK Architecture: Human Discretion and the Reconstruction of Human Intelligence in the AGI Era](https://doi.org/10.5281/zenodo.20323259) | 2026 | 19 | 44 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 7 | [Paper 5 — ARI in the AGI Era: ARI, ACHEUL, and BIFACE as a Post-Cloud Infrastructure Framework (A BIFACE-Based Framework for Human-Perceivable and Machine-Referable Coordination)](https://doi.org/10.5281/zenodo.20350468) | 2026 | 19 | 44 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 8 | [Paper 6 — Multi-Layer Cross Verification in the AGI Era: Role Feasibility, Output Reference, and Pre-Transaction Validation](https://doi.org/10.5281/zenodo.20350517) | 2026 | 19 | 44 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 9 | [Paper 7 — AGI Output Governance: Candidate Outputs, Human Discretion, and Evidentiary Boundaries in the AGI Era](https://doi.org/10.5281/zenodo.20351228) | 2026 | 18 | 41 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |
| 10 | [Paper 8 — HTS-Based Evidence Sealing in the AGI Era: Preserving Output History, Human Discretion, and Evidentiary References](https://doi.org/10.5281/zenodo.20351290) | 2026 | 17 | 38 | Zenodo (CERN European Organization for Nuclear Research) | The First Waters |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 86 | 124683 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 67 | 47641 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 20 | 8643 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 20 | 28590 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 18 | 23091 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 16 | 51516 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 15 | 32769 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 14 | 7146 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |
| 9 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 13 | 8744 | Nature Machine Intelligence | Cynthia Rudin |
| 10 | [WGCNA: an R package for weighted correlation network analysis](https://doi.org/10.1186/1471-2105-9-559) | 2008 | 13 | 28917 | BMC Bioinformatics | Peter Langfelder, Steve Horvath |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 9 | 1942 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 13281 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 3 | [Machine learning and SHAP value interpretation for predicting comorbidity of cardiovascular disease and cancer with dietary antioxidants](https://doi.org/10.1016/j.redox.2024.103470) | 2024 | 5 | 185 | Redox Biology | Xiangjun Qi, Shujing Wang, Caishan Fang, et al. |
| 4 | [Machine learning based prediction models for cardiovascular disease risk using electronic health records data: systematic review and meta-analysis](https://doi.org/10.1093/ehjdh/ztae080) | 2024 | 4 | 109 | European Heart Journal - Digital Health | Tianyi Liu, Andrew J. Krentz, Lei Lü, et al. |
| 5 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 4 | 540 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 6 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 540 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 7 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 4 | 626 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 8 | [PubChem 2025 update](https://doi.org/10.1093/nar/gkae1059) | 2024 | 4 | 943 | Nucleic Acids Research | Sunghwan Kim, Jie Chen, Tiejun Cheng, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 1416 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 3063 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 3206 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 682 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 3359 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 6 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 7 | 10658 |  | Nils Reimers, Iryna Gurevych |
| 7 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 7 | 78391 | Biometrics | J. Richard Landis, Gary G. Koch |
| 8 | [Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing](https://doi.org/10.1145/3458754) | 2021 | 5 | 1985 | ACM Transactions on Computing for Healthcare | 裕二 池谷, Robert Tinn, Hao Cheng, et al. |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 3502 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 5 | 3566 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 1416 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 3063 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 3206 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 682 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 3502 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 6 | [On the Conversational Persuasiveness of Large Language Models: A Randomized Controlled Trial](https://doi.org/10.21203/rs.3.rs-4429707/v1) | 2024 | 4 | 127 | Research Square | Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, et al. |
| 7 | [Can large language models reason about medical questions?](https://doi.org/10.1016/j.patter.2024.100943) | 2024 | 4 | 249 | Patterns | Valentin Liévin, Christoffer Hother, Andreas Geert Motzfeldt, et al. |
| 8 | [Improving large language models for clinical named entity recognition via prompt engineering](https://doi.org/10.1093/jamia/ocad259) | 2024 | 4 | 276 | Journal of the American Medical Informatics Association | Yan Hu, Qingyu Chen, Jingcheng Du, et al. |
| 9 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 4 | 318 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 10 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 4 | 542 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Amari-Schwarzian Cubic: Nodal Realisation and Empirical G_m Structure of Symplectic Integrators](https://doi.org/10.5281/zenodo.20031926) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Nicholas Maino |
| 2 | [Exact Half-Cauchy Emergence in Stormer-Verlet Integration of the Harmonic Oscillator via Kronecker-Weyl Equidistribution](https://doi.org/10.5281/zenodo.20078637) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Nicholas Maino |
| 3 | [The Conformity Gradient on Elliptic Fibrations: From Statistical Rigidity to Kodaira Classification and CFT](https://doi.org/10.5281/zenodo.19425788) | 2026 | 3 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Nicholas Daniel Maino |
| 4 | [Hallucinated citations are polluting the scientific literature. What can be done?](https://doi.org/10.1038/d41586-026-00969-z) | 2026 | 3 | 6 | Nature | Miryam Naddaf, Elizabeth Quill |
| 5 | [The Funnel as Capital: A Semantic Economic Reading of the Application Process](https://doi.org/10.5281/zenodo.20330816) | 2026 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 6 | [The Application as Extraction Surface: Semantic Labor, Induced Preparation, and Institutional Opacity in the Anthropic Fellows Screening Process](https://doi.org/10.5281/zenodo.20330670) | 2026 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 7 | [Cross-Institutional Evaluation of Large Language Models for Radiology Diagnosis Extraction: A Prompt-Engineering Perspective](https://doi.org/10.1007/s10278-025-01523-5) | 2025 | 2 | 4 | Journal of Imaging Informatics in Medicine | Mana Moassefi, Sina Houshmand, Shahriar Faghani, et al. |
| 8 | [Empirical Phenomenology: Action as Disclosure and the Science of Opaque Public Systems](https://doi.org/10.5281/zenodo.20326137) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 9 | [Weakly supervised language models for automated extraction of critical findings from radiology reports](https://doi.org/10.1038/s41746-025-01522-4) | 2025 | 2 | 11 | npj Digital Medicine | Avisha Das, Ish Talati, Juan Manuel Zambrano Chaves, et al. |
| 10 | [Jailbroken: How Does LLM Safety Training Fail?](https://doi.org/10.52202/075280-3508) | 2023 | 3 | 20 |  | Nika Haghtalab, Jacob Steinhardt, Alexander Wei |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 25 | 180626 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 15 | 92316 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [The Foundations of Social Research: Meaning and Perspective in the Research Process](https://openalex.org/W1510426010) | 1998 | 9 | 9410 |  | Michael Crotty |
| 4 | [Distinction: A Social Critique of the Judgement of Taste*](https://doi.org/10.4324/9781315680347-10) | 2018 | 9 | 20377 |  | Pierre Bourdıeu |
| 5 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 9 | 75672 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 6 | [Self-Determination Theory: Basic Psychological Needs in Motivation, Development, and Wellness](https://doi.org/10.1521/978.14625/28806) | 2017 | 8 | 11585 | Guilford Press eBooks | Unknown |
| 7 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 8 | 31733 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 8 | [Case Study Research: Design and Methods](https://openalex.org/W1527311855) | 1984 | 8 | 74955 |  | Robert K. Yin |
| 9 | [Fitting Linear Mixed-Effects Models Using <b>lme4</b>](https://doi.org/10.18637/jss.v067.i01) | 2015 | 7 | 84701 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |
| 10 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 7 | 104547 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 5 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 5 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 4 | 11 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Three-Dimensional Space Background Conservation and Positive-Negative Dimension Symmetry Cosmic Grand Unified Theory三维空间本底守恒与正负维度对称宇宙大一统理论](https://doi.org/10.5281/zenodo.19970854) | 2026 | 3 | 5 | Zenodo (CERN European Organization for Nuclear Research) | 洋洋 郭 |
| 6 | [Deepening Research on Synchronization Prediction of Multi-Oscillator Systems Based on General Deviation Convergence Paradigm基于通用偏差收敛范式的多振子系统同步预测深化研究](https://doi.org/10.5281/zenodo.20366371) | 2026 | 3 | 5 | Zenodo (CERN European Organization for Nuclear Research) | 洋洋 郭 |
| 7 | [Virtual vs. traditional learning in higher education: A systematic review of comparative studies](https://doi.org/10.1016/j.compedu.2024.105214) | 2024 | 3 | 45 | Computers & Education | Tommaso Santilli, Silvia Ceccacci, Maura Mengoni, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Three-Dimensional Space Background Conservation and Positive-Negative Dimension Symmetry Cosmic Grand Unified Theory三维空间本底守恒与正负维度对称宇宙大一统理论](https://doi.org/10.5281/zenodo.19970854) | 2026 | 3 | 5 | Zenodo (CERN European Organization for Nuclear Research) | 洋洋 郭 |
| 2 | [Deepening Research on Synchronization Prediction of Multi-Oscillator Systems Based on General Deviation Convergence Paradigm基于通用偏差收敛范式的多振子系统同步预测深化研究](https://doi.org/10.5281/zenodo.20366371) | 2026 | 3 | 5 | Zenodo (CERN European Organization for Nuclear Research) | 洋洋 郭 |
| 3 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 4 | 11 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 5 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 5 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [Virtual vs. traditional learning in higher education: A systematic review of comparative studies](https://doi.org/10.1016/j.compedu.2024.105214) | 2024 | 3 | 45 | Computers & Education | Tommaso Santilli, Silvia Ceccacci, Maura Mengoni, et al. |
<!-- TRENDING-END -->
