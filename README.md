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

Last update: 2026-05-25 09:54 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Nociceptive Metaplasticity and Graceful Decay in Spiking Neural Networks: Towards Survival-Driven Continual Learning](https://doi.org/10.5281/zenodo.19151562) | 2026 | 16 | 40 | Open MIND | Venkatesh Swaminathan |
| 2 | [Maya-CL: Nociceptive Metaplasticity and Vairagya-Governed Heterosynaptic Decay for Continual Learning in Spiking Neural Networks](https://doi.org/10.5281/zenodo.19201768) | 2026 | 16 | 40 | Open MIND | Swaminathan, Venkatesh |
| 3 | [Maya-Manas: Oscillatory Thalamo-Cortical Gating for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19363005) | 2026 | 16 | 40 | Open MIND | Venkatesh Swaminathan |
| 4 | [cl-metrics: A Stateless Python Library for Continual Learning Evaluation with SNN Energy-Aware Extensions](https://doi.org/10.5281/zenodo.19389017) | 2026 | 16 | 40 | Open MIND | Venkatesh Swaminathan |
| 5 | [Maya-Śūnyatā: Karma-Weighted Synaptic Pruning for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19397010) | 2026 | 16 | 40 | Open MIND | Venkatesh Swaminathan |
| 6 | [Maya-Prana: Metabolic Plasticity Budget for Continual Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19451173) | 2026 | 16 | 40 | Open MIND | Venkatesh Swaminathan |
| 7 | [Maya-LLM-Defence: Sovereign Military LLM with Affective SNN Safety Substrate](https://doi.org/10.5281/zenodo.19708800) | 2026 | 16 | 40 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 8 | [morphe-metrics: A Stateless Python Library for Morphogenetic Computing Evaluation](https://doi.org/10.5281/zenodo.20107083) | 2026 | 16 | 41 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 9 | [Maya-Viveka: Viveka-Gated Synaptic Discrimination for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19279002) | 2026 | 16 | 41 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 10 | [Active Finite Distinction Systems: A Formal Core for Boundary Maintenance under Finite Capacity](https://doi.org/10.5281/zenodo.20158923) | 2026 | 16 | 51 | Zenodo (CERN European Organization for Nuclear Research) | Yining Wu |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 102 | 124313 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 74 | 47387 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 26 | 8574 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 23 | 32697 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 5 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 21 | 28522 | The Annals of Statistics | Jerome H. Friedman |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 20 | 23026 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 15 | 51441 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 8 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 13 | 15952 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 12 | 80790 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 11 | 7078 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 9 | 1899 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Machine learning and SHAP value interpretation for predicting comorbidity of cardiovascular disease and cancer with dietary antioxidants](https://doi.org/10.1016/j.redox.2024.103470) | 2024 | 5 | 181 | Redox Biology | Xiangjun Qi, Shujing Wang, Caishan Fang, et al. |
| 3 | [Machine Learning Methods for Small Data Challenges in Molecular Science](https://doi.org/10.1021/acs.chemrev.3c00189) | 2023 | 5 | 429 | Chemical Reviews | Bozheng Dou, Zailiang Zhu, Ekaterina Merkurjev, et al. |
| 4 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 527 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 5 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13265 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 6 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 4 | 614 | Patterns | Sayash Kapoor, Arvind Narayanan |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 1387 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 3177 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 3024 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 8 | 430 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 8 | 32198 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 3321 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 7 | 5299 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 6 | 531 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 9 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 667 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 10 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 6 | 855 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 1387 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 3177 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 3024 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 6 | 531 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 5 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 667 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 6 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 6 | 855 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 7 | [A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1) | 2024 | 5 | 1064 | Frontiers of Computer Science | Lei Wang, Chen Ma, Xueyang Feng, et al. |
| 8 | [How Does ChatGPT Perform on the United States Medical Licensing Examination (USMLE)? The Implications of Large Language Models for Medical Education and Knowledge Assessment](https://doi.org/10.2196/45312) | 2023 | 5 | 1993 | JMIR Medical Education | Aidan Gilson, Conrad Safranek, Thomas Huang, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 5 | 2369 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 5 | 4785 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Amari-Schwarzian Cubic: Nodal Realisation and Empirical G_m Structure of Symplectic Integrators](https://doi.org/10.5281/zenodo.20031926) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Nicholas Maino |
| 2 | [Exact Half-Cauchy Emergence in Stormer-Verlet Integration of the Harmonic Oscillator via Kronecker-Weyl Equidistribution](https://doi.org/10.5281/zenodo.20078637) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Nicholas Maino |
| 3 | [The Conformity Gradient on Elliptic Fibrations: From Statistical Rigidity to Kodaira Classification and CFT](https://doi.org/10.5281/zenodo.19425788) | 2026 | 3 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Nicholas Daniel Maino |
| 4 | [A systematic review of ethical considerations of large language models in healthcare and medicine](https://doi.org/10.3389/fdgth.2025.1653631) | 2025 | 3 | 18 | Frontiers in Digital Health | Muhammad Fareed, Madiha Fatima, Md Jamal Uddin, et al. |
| 5 | [Streamlining systematic reviews with large language models using prompt engineering and retrieval augmented generation](https://doi.org/10.1186/s12874-025-02583-5) | 2025 | 3 | 25 | BMC Medical Research Methodology | Fouad Trad, Ryan Yammine, Jana Charafeddine, et al. |
| 6 | [EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities](https://doi.org/10.18653/v1/2024.acl-long.829) | 2024 | 3 | 34 |  | Nian Li, Chen Gao, Mingyu Li, et al. |
| 7 | [Maya-OS: An Affective Spiking Neural Network as a Conversational Operating System Arbitration Layer](https://doi.org/10.5281/zenodo.19160122) | 2026 | 3 | 39 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 8 | [Maya-Smriti: Episodic Memory as a Biological Prior for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19228974) | 2026 | 3 | 39 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 9 | [Maya-Chitta: Endocannabinoid-Inspired Retrograde Gradient Gating for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19337040) | 2026 | 3 | 39 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 10 | [From Representation to Experience: An mPCI-Based Empirical Test of Internal Affective State in a Neuromorphic Spiking Neural Network](https://doi.org/10.5281/zenodo.19482793) | 2026 | 3 | 39 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 14 | 179962 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 10 | 31626 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 3 | [Statistical power analyses using G*Power 3.1: Tests for correlation and regression analyses](https://doi.org/10.3758/brm.41.4.1149) | 2009 | 8 | 35473 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Axel Buchner, et al. |
| 4 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 8 | 66739 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 5 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 8 | 91629 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 6 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 8 | 104338 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 7 | [Diagnostic and Statistical Manual of Mental Disorders](https://doi.org/10.1176/appi.books.9780890425596) | 2013 | 8 | 113213 | American Psychiatric Association eBooks | Annette Lolk |
| 8 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 7 | 75421 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 9 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 10 | [FST Spectrum Duality: The Renormalized Free Energy Principle as Physical Instantiation of Functional Stability Theory](https://doi.org/10.5281/zenodo.19036190) | 2026 | 6 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [FST Spectrum Duality: The Renormalized Free Energy Principle as Physical Instantiation of Functional Stability Theory](https://doi.org/10.5281/zenodo.19036190) | 2026 | 6 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [From Landscape to Proof: The Even-Dominance Route to the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 6 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection (DRAFT)](https://doi.org/10.5281/zenodo.20130563) | 2026 | 4 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 3 | 527 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 7 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 3 | 4785 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 8 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 2 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 9 | [Research on the collaborative mechanism of a data trading market based on a four-party evolutionary game in the context of digital intelligence](https://doi.org/10.1016/j.seps.2025.102238) | 2025 | 2 | 15 | Socio-Economic Planning Sciences | Yue Li, Guo‐Fu Li, Anfeng Xu, et al. |
| 10 | [Approximating the Shapley Value without Marginal Contributions](https://doi.org/10.1609/aaai.v38i12.29225) | 2024 | 2 | 25 | Proceedings of the AAAI Conference on Artificial Intelligence | Patrick Kolpaczki, Viktor Bengs, Maximilian Muschalik, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection (DRAFT)](https://doi.org/10.5281/zenodo.20130563) | 2026 | 4 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 2 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [FST Spectrum Duality: The Renormalized Free Energy Principle as Physical Instantiation of Functional Stability Theory](https://doi.org/10.5281/zenodo.19036190) | 2026 | 6 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [From Landscape to Proof: The Even-Dominance Route to the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 6 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [Research on the collaborative mechanism of a data trading market based on a four-party evolutionary game in the context of digital intelligence](https://doi.org/10.1016/j.seps.2025.102238) | 2025 | 2 | 15 | Socio-Economic Planning Sciences | Yue Li, Guo‐Fu Li, Anfeng Xu, et al. |
| 8 | [Approximating the Shapley Value without Marginal Contributions](https://doi.org/10.1609/aaai.v38i12.29225) | 2024 | 2 | 25 | Proceedings of the AAAI Conference on Artificial Intelligence | Patrick Kolpaczki, Viktor Bengs, Maximilian Muschalik, et al. |
| 9 | [The Player Experience and Design Implications of Narrative Games](https://doi.org/10.1080/10447318.2022.2085404) | 2022 | 2 | 29 | International Journal of Human-Computer Interaction | Weimin Toh |
| 10 | [Central environmental protection inspection and carbon emission reduction: A tripartite evolutionary game model from the perspective of carbon neutrality](https://doi.org/10.1016/j.petsci.2023.11.014) | 2023 | 2 | 56 | Petroleum Science | Zhenhua Zhang, Dan Ling, Qin-Xin Yang, et al. |
<!-- TRENDING-END -->
