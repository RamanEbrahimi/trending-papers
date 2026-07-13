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

Last update: 2026-07-13 08:55 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [V01.01 — Mirror Theory I: A Minimal Computational Theory of Recursive Observerhood](https://doi.org/10.5281/zenodo.21142534) | 2026 | 13 | 33 | Zenodo (CERN European Organization for Nuclear Research) | Lloyd Christopher Smith |
| 2 | [V01.04 — Mirror Mathematics I: A Constraint Calculus for Recursive Observerhood](https://doi.org/10.5281/zenodo.21155861) | 2026 | 13 | 33 | Zenodo (CERN European Organization for Nuclear Research) | Lloyd Christopher Smith |
| 3 | [Mirror Observerhood Lab I: Recursive Self-Model Reliability Improves Viability Under Self-Relevant Perturbation](https://doi.org/10.5281/zenodo.21157523) | 2026 | 12 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Lloyd Christopher Smith |
| 4 | [Power and particle exhaust in the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae70a0) | 2026 | 10 | 10 | Nuclear Fusion | Matthew Robinson, A. Scarabosio, E. O. Vekshina, et al. |
| 5 | [Physics basis for the reference flat-top plasma scenario in the ST–E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae5f33) | 2026 | 10 | 10 | Nuclear Fusion | Steven McNamara, S. Abouelazayem, А. И. Алиева, et al. |
| 6 | [MP-00 — Mirror Programme Overview: A Recursive Research Architecture for Constraint, Observerhood and Modelled Reality](https://doi.org/10.5281/zenodo.21142318) | 2026 | 10 | 21 | Zenodo (CERN European Organization for Nuclear Research) | Lloyd Christopher Smith |
| 7 | [Mirror Observerhood Lab II: Channel-Decomposed Reliability and the Limits of Reliability Tracking Alone](https://doi.org/10.5281/zenodo.21159572) | 2026 | 10 | 25 | Zenodo (CERN European Organization for Nuclear Research) | Lloyd Christopher Smith |
| 8 | [Mirror Observerhood Lab III: Actionable Reliability and Cost-Sensitive Repair in Viability-Constrained Agents](https://doi.org/10.5281/zenodo.21161631) | 2026 | 10 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Lloyd Christopher Smith |
| 9 | [Design scoping and systems modelling of ST-E1 using the PyTok power plant simulation code](https://doi.org/10.1088/1741-4326/ae5d55) | 2026 | 9 | 9 | Nuclear Fusion | C.L. Wilson, J. Astbury, M.J. Ginsberg, et al. |
| 10 | [Integrated physics and magnet design for the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae773b) | 2026 | 8 | 8 | Nuclear Fusion | E. Maartensson, N. Welch, M. Scarpari, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 99 | 127209 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 62 | 49232 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 35 | 29213 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 33 | 9132 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 20 | 33229 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 18 | 23593 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 17 | 51992 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 8 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 14 | 8747 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 14 | 82128 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Decision Curve Analysis: A Novel Method for Evaluating Prediction Models](https://doi.org/10.1177/0272989x06295361) | 2006 | 13 | 5577 | Medical Decision Making | Andrew J. Vickers, Elena B. Elkin |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 11 | 2382 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 5 | 711 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 3 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 5 | 2873 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 4 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 5 | 5035 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |
| 5 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 629 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 6 | [KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease](https://doi.org/10.1016/j.kint.2023.10.018) | 2024 | 4 | 7586 | Kidney International | Paul E. Stevens, Sofia B. Ahmed, Juan Jesús Carrero, et al. |
| 7 | [The Matthews correlation coefficient (MCC) should replace the ROC AUC as the standard metric for assessing binary classification](https://doi.org/10.1186/s13040-023-00322-4) | 2023 | 3 | 531 | BioData Mining | Davide Chicco, Giuseppe Jurman |
| 8 | [Climate Change 2021 – The Physical Science Basis](https://doi.org/10.1017/9781009157896) | 2023 | 3 | 6371 | Cambridge University Press eBooks | Intergovernmental Panel on Climate Change |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 22 | 766 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 3287 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 12 | 408 |  | Sandhini Agarwal, Diogo Almeida, Amanda Askell, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 3413 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 3664 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 6 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 11 | 32724 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 7 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 10 | 621 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 8 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 10 | 21588 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 9 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 10 | 79408 | Biometrics | J. Richard Landis, Gary G. Koch |
| 10 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 8 | 473 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 3287 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 3413 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 10 | 621 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 4 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 8 | 473 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 5 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 7 | 279 |  | Wei-Lin Chiang, Joseph Gonzalez, Dacheng Li, et al. |
| 6 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 760 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 7 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2509 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 8 | [Reflexion: language agents with verbal reinforcement learning](https://doi.org/10.52202/075280-0377) | 2023 | 6 | 184 |  | Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, et al. |
| 9 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 6 | 386 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 10 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 6 | 590 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Knowledge-grounded large language model for personalized sports training plan generation](https://doi.org/10.1038/s41598-026-37075-z) | 2026 | 3 | 3 | Scientific Reports | Zhongliang He, Jiacheng Wang, Binggang Zhang, et al. |
| 2 | [The Absorption Gradient: A Testable Account of Where Originating Value Resides in Reading](https://doi.org/10.5281/zenodo.20682327) | 2026 | 4 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Asnia Asim |
| 3 | [Prompt engineering for accurate statistical reasoning with large language models in medical research](https://doi.org/10.3389/frai.2025.1658316) | 2025 | 3 | 17 | Frontiers in Artificial Intelligence | Sifiso Vilakati |
| 4 | [Evaluating large language models as graders of medical short answer questions: a comparative analysis with expert human graders](https://doi.org/10.1080/10872981.2025.2550751) | 2025 | 3 | 18 | Medical Education Online | Olena Bolgova, Paul Ganguly, Muhammad Faisal Ikram, et al. |
| 5 | [LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation](https://doi.org/10.52202/079017-0839) | 2024 | 3 | 45 |  | Qidong Liu, Feng Tian, Yejing Wang, et al. |
| 6 | [ProAgent: Building Proactive Cooperative Agents with Large Language Models](https://doi.org/10.1609/aaai.v38i16.29710) | 2024 | 3 | 50 | Proceedings of the AAAI Conference on Artificial Intelligence | Ceyao Zhang, Kaijie Yang, Siyi Hu, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 35 | 185480 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 16 | 96863 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 13 | 85267 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 4 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 12 | 77299 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 5 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 10 | 127209 | Machine Learning | Leo Breiman |
| 6 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 9 | 17636 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |
| 7 | [Institutions, Institutional Change and Economic Performance](https://doi.org/10.1017/cbo9780511808678) | 1990 | 9 | 31074 | Cambridge University Press eBooks | Douglass C. North |
| 8 | [Scoping studies: towards a methodological framework](https://doi.org/10.1080/1364557032000119616) | 2005 | 9 | 35938 | International Journal of Social Research Methodology | Hilary Arksey, Lisa O’Malley |
| 9 | [Statistical power analyses using G*Power 3.1: Tests for correlation and regression analyses](https://doi.org/10.3758/brm.41.4.1149) | 2009 | 9 | 36326 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Axel Buchner, et al. |
| 10 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 9 | 41084 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 5344 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 4 | 13396 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 3 | [Unlocking knowledge: a meta-analysis assessing the efficacy of educational escape rooms in health sciences education](https://doi.org/10.1007/s10459-024-10373-9) | 2024 | 3 | 22 | Advances in Health Sciences Education | Nicholas J. Kakos, Rebecca S. Lufler, Brendan Cyr, et al. |
| 4 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 3 | 2382 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Unlocking knowledge: a meta-analysis assessing the efficacy of educational escape rooms in health sciences education](https://doi.org/10.1007/s10459-024-10373-9) | 2024 | 3 | 22 | Advances in Health Sciences Education | Nicholas J. Kakos, Rebecca S. Lufler, Brendan Cyr, et al. |
<!-- TRENDING-END -->
