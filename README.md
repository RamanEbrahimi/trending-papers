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

Last update: 2026-08-17 06:38 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 10 | 15092 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 2 | [Preregistration of a Regional Trial Protocol in Ontology (Ethical Ontology, Volume II) — V1.1](https://doi.org/10.5281/zenodo.21744060) | 2026 | 7 | 15 | Zenodo (CERN European Organization for Nuclear Research) | Alessio Montaruli |
| 3 | [STAR: ultrafast universal RNA-seq aligner](https://doi.org/10.1093/bioinformatics/bts635) | 2012 | 7 | 57321 | Bioinformatics | Alexander Dobin, Carrie Davis, Felix Schlesinger, et al. |
| 4 | [Ethical Ontology, Volume I: The Modal Coincidence](https://doi.org/10.5281/zenodo.21721619) | 2026 | 6 | 15 | Open MIND | Alessio Montaruli |
| 5 | [SciPy 1.0: fundamental algorithms for scientific computing in Python](https://doi.org/10.1038/s41592-019-0686-2) | 2020 | 6 | 39223 | Nature Methods | Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, et al. |
| 6 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 6 | 101215 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 7 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 6 | 189464 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 8 | [Ethical Ontology, Volume II: The Sacred Economy — Controlling Book Plan V8.2 Lean](https://doi.org/10.5281/zenodo.21802523) | 2026 | 5 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Alessio Montaruli |
| 9 | [Ethical Ontology, Volume II — Episode Registries, Parts II–VI, V1.1](https://doi.org/10.5281/zenodo.21744435) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Alessio Montaruli |
| 10 | [Preregistration of a Hypothesis-Emergence and Later-Test Protocol over the Registered Sacred-Economic Sample (Ethical Ontology, Volume II) — V1](https://doi.org/10.5281/zenodo.21843024) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Alessio Montaruli |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 101 | 129751 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 89 | 51381 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 37 | 29799 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 31 | 9658 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 24144 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 17 | 33650 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 15 | 8953 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 15 | 100574 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 2839 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 10 | [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations](https://doi.org/10.1016/j.jcp.2018.10.045) | 2018 | 14 | 18428 | Journal of Computational Physics | Maziar Raissi, Paris Perdikaris, George Em Karniadakis |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 2839 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 9 | 840 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 13477 | DROPS (Schloss Dagstuhl – Leibniz Center for Informatics) | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 4 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 7 | 563 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 5 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 24670 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 6 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 5 | 675 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 7 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 713 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 8 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 5 | 772 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 9 | [The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods](https://doi.org/10.1093/nar/gkad1004) | 2023 | 5 | 1313 | Nucleic Acids Research | Barbara Zdrazil, Eloy Félix, Fiona Hunter, et al. |
| 10 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 4 | 811 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 20 | 3567 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 19 | 800 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 3 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 16 | 623 |  | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 4 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 16 | 1503 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 5 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 16 | 4058 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3638 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 13 | 793 |  | Haotian Liu, Chunyuan Li, Qingyang Wu, et al. |
| 8 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 13 | 80352 | Biometrics | J. Richard Landis, Gary G. Koch |
| 9 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 12 | 6109 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 10 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 12 | 101215 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 20 | 3567 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 16 | 623 |  | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3638 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 13 | 793 |  | Haotian Liu, Chunyuan Li, Qingyang Wu, et al. |
| 5 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 539 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 6 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://doi.org/10.52202/075280-2338) | 2023 | 10 | 264 |  | Rafael Rafailov, Archit Sharma, Eric Mitchell, et al. |
| 7 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 10 | 853 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 8 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 10 | 1883 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 9 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 8 | 1361 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 8 | 2456 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Toward Abstraction-Level Event Retrieval in Large Video Collections: Leveraging Human Knowledge and LLM-Based Reasoning in the Ho Chi Minh City AI Challenge 2025](https://doi.org/10.1007/978-981-92-2584-2_10) | 2026 | 6 | 19 | Communications in computer and information science | Trong-Le Do, Viet-Tham Huynh, Hai-Dang Nguyen, et al. |
| 2 | [A systematic review of ethical considerations of large language models in healthcare and medicine](https://doi.org/10.3389/fdgth.2025.1653631) | 2025 | 4 | 36 | Frontiers in Digital Health | Muhammad Fareed, Madiha Fatima, Md Jamal Uddin, et al. |
| 3 | [Large language models in real-world clinical workflows: a systematic review of applications and implementation](https://doi.org/10.3389/fdgth.2025.1659134) | 2025 | 5 | 53 | Frontiers in Digital Health | Yaara Artsi, Vera Sorin, Benjamin S. Glicksberg, et al. |
| 4 | [HybridFlow: A Flexible and Efficient RLHF Framework](https://doi.org/10.1145/3689031.3696075) | 2025 | 4 | 43 |  | Guangming Sheng, Chi Zhang, Zilingfeng Ye, et al. |
| 5 | [A scoping review of large language model based approaches for information extraction from radiology reports](https://doi.org/10.1038/s41746-024-01219-0) | 2024 | 4 | 82 | npj Digital Medicine | Daniel Reichenpfader, Henning Müller, Kerstin Denecke |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 23 | 189464 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 18 | 101215 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality in Organizational Fields](https://doi.org/10.2307/2095101) | 1983 | 13 | 36859 | American Sociological Review | Paul DiMaggio, Walter W. Powell |
| 4 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 13 | 129751 | Machine Learning | Leo Breiman |
| 5 | [Institutions, Institutional Change and Economic Performance](https://doi.org/10.1017/cbo9780511808678) | 1990 | 8 | 31606 | Cambridge University Press eBooks | Douglass C. North |
| 6 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 8 | 32936 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 7 | [Naturalistic inquiry](https://doi.org/10.1016/0147-1767(85)90062-8) | 1985 | 8 | 35415 | International Journal of Intercultural Relations | Yvonna S. Lincoln, Egon G. Guba, Joseph J. Pilotta |
| 8 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 8 | 78812 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 9 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 7 | 9658 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 10 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 7 | 66234 | MIS Quarterly | Fred D. Davis |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 6 | 55 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 6 | 60 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection](https://doi.org/10.5281/zenodo.20130563) | 2026 | 4 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [Exploring the Impact of Artificial Intelligence in Teaching and Learning of Science: A Systematic Review of Empirical Research](https://doi.org/10.1007/s11165-024-10176-3) | 2024 | 3 | 292 | Research in Science Education | Firas Almasri |
| 7 | [The EAT–Lancet Commission on healthy, sustainable, and just food systems](https://doi.org/10.1016/s0140-6736(25)01201-2) | 2025 | 3 | 385 | The Lancet | Johan Rockström, Shakuntala H. Thilsted, Walter C. Willett, et al. |
| 8 | [The effects of over-reliance on AI dialogue systems on students' cognitive abilities: a systematic review](https://doi.org/10.1186/s40561-024-00316-7) | 2024 | 3 | 1205 | Smart Learning Environments | Chunpeng Zhai, Santoso Wibowo, Lily D. Li |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 3 | 3724 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 2 | 13 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection](https://doi.org/10.5281/zenodo.20130563) | 2026 | 4 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 2 | 13 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 6 | 55 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 6 | 60 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [Informality as Structure or Agency? Exploring Shed Housing in the UK as Informal Practice](https://doi.org/10.1111/1468-2427.12705) | 2019 | 3 | 65 | International Journal of Urban and Regional Research | Melanie Lombard |
| 8 | [Game Theory Integration in Construction Management: A Comprehensive Approach to Cost, Risk, and Coordination under Uncertainty](https://doi.org/10.1061/jcemd4.coeng-15109) | 2025 | 2 | 47 | Journal of Construction Engineering and Management | Ali Shehadeh, Odey Alshboul |
| 9 | [We’re not Superhuman, We’re Human: A Qualitative Description of Elite Athletes’ Experiences of Return to Sport After Childbirth](https://doi.org/10.1007/s40279-022-01730-y) | 2022 | 3 | 88 | Sports Medicine | Margie H. Davenport, Lauren Ray, Autumn Nesdoly, et al. |
<!-- TRENDING-END -->
