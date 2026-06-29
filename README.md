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

Last update: 2026-06-29 10:44 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Der Ethische Biosymbiose-Index (EBSI): Konzept eines psycho-sozialen Ethik-Index für Deutschland](https://doi.org/10.5281/zenodo.20297563) | 2026 | 15 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Maximilian Heiler |
| 2 | [Machine Wisdom (Verification Intelligence series, Paper 6 of 12)](https://doi.org/10.5281/zenodo.20973209) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 3 | [Quality Engineering for Intelligence (Verification Intelligence series, Paper 3 of 12)](https://doi.org/10.5281/zenodo.20973203) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 4 | [The Verification Substrate (Verification Intelligence series, Paper 5 of 12)](https://doi.org/10.5281/zenodo.20973207) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 5 | [Verification Intelligence (Verification Intelligence series, Paper 4 of 12)](https://doi.org/10.5281/zenodo.20973205) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 6 | [The Recursive Hallucination Principle (Verification Intelligence series, Paper 2 of 12)](https://doi.org/10.5281/zenodo.20973201) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 7 | [The Trust Layer (Verification Intelligence series, Paper 7 of 12)](https://doi.org/10.5281/zenodo.20973211) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 8 | [The Verification Deficit (Verification Intelligence series, Paper 1 of 12)](https://doi.org/10.5281/zenodo.20973199) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 9 | [Parenting the First Non-Human Minds (Verification Intelligence series, Paper 10 of 12)](https://doi.org/10.5281/zenodo.20973217) | 2026 | 10 | 20 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |
| 10 | [Civilisation-Scale Verification (Verification Intelligence series, Paper 12 of 12)](https://doi.org/10.5281/zenodo.20973223) | 2026 | 10 | 20 | Zenodo (CERN European Organization for Nuclear Research) | Darren Wright |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 101 | 126295 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 54 | 48662 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 30 | 29000 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 24 | 8962 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 19 | 33056 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 17 | 16151 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 7 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 17 | 23430 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 8 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 15 | 31217 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 9 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 14 | 7406 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |
| 10 | [The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation](https://doi.org/10.7717/peerj-cs.623) | 2021 | 13 | 4878 | PeerJ Computer Science | Davide Chicco, Matthijs J. Warrens, Giuseppe Jurman |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 598 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 7 | 2223 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13349 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 4 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 5 | 13879 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 5 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 4 | 187 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |
| 6 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 4 | 2807 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 7 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 4 | 4922 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 20 | 604 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 15 | 3337 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 3208 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 5170 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 9 | 288 |  | Sandhini Agarwal, Diogo Almeida, Amanda Askell, et al. |
| 6 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 9 | 5582 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 7 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 9 | 78988 | Biometrics | J. Richard Landis, Gary G. Koch |
| 8 | [Foundation models for generalist medical artificial intelligence](https://doi.org/10.1038/s41586-023-05881-4) | 2023 | 8 | 1584 | Nature | Michael Moor, Oishi Banerjee, Zahra Shakeri Hossein Abad, et al. |
| 9 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 7 | 348 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 10 | [Reflexion: language agents with verbal reinforcement learning](https://doi.org/10.52202/075280-0377) | 2023 | 6 | 150 |  | Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 15 | 3337 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 3208 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 5170 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 4 | [Foundation models for generalist medical artificial intelligence](https://doi.org/10.1038/s41586-023-05881-4) | 2023 | 8 | 1584 | Nature | Michael Moor, Oishi Banerjee, Zahra Shakeri Hossein Abad, et al. |
| 5 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 7 | 348 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 6 | [Reflexion: language agents with verbal reinforcement learning](https://doi.org/10.52202/075280-0377) | 2023 | 6 | 150 |  | Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, et al. |
| 7 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 6 | 448 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 8 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 6 | 576 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 9 | [Prompt Engineering as an Important Emerging Skill for Medical Professionals: Tutorial](https://doi.org/10.2196/50638) | 2023 | 6 | 670 | Journal of Medical Internet Research | Bertalan Meskó |
| 10 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 1551 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction](https://doi.org/10.18653/v1/2025.emnlp-main.1274) | 2025 | 3 | 3 |  | Alexander Scarlatos, Nigel Fernandez, Christopher M. Ormerod, et al. |
| 2 | [Can Large Language Models Match Tutoring System Adaptivity? A Benchmarking Study](https://doi.org/10.1007/978-3-031-98417-4_29) | 2025 | 4 | 12 | Lecture notes in computer science | Conrad Borchers, Tianze Shou |
| 3 | [Empowering Instructors With AI: Evaluating the Impact of an AI-Driven Feedback Tool in Learning Analytics](https://doi.org/10.1109/tlt.2025.3562379) | 2025 | 3 | 14 | IEEE Transactions on Learning Technologies | Cleon Xavier, Luiz Rodrigues, Newarney Torrezão da Costa, et al. |
| 4 | [A knowledge graph-enhanced large language model for question answering of hydraulic structure safety management](https://doi.org/10.1016/j.aei.2025.103468) | 2025 | 3 | 23 | Advanced Engineering Informatics | Dongliang Zhang, Gang Ma, Tongming Qu, et al. |
| 5 | [Automated safety risk management guidance enhanced by retrieval-augmented large language model](https://doi.org/10.1016/j.autcon.2025.106255) | 2025 | 4 | 34 | Automation in Construction | Seungwon Baek, Chan Young Park, Wooyong Jung |
| 6 | [Evaluating large language models in analysing classroom dialogue](https://doi.org/10.1038/s41539-024-00273-3) | 2024 | 5 | 52 | npj Science of Learning | Yun Liang Long, Haifeng Luo, Yu Zhang |
| 7 | [Large language models in real-world clinical workflows: a systematic review of applications and implementation](https://doi.org/10.3389/fdgth.2025.1659134) | 2025 | 3 | 32 | Frontiers in Digital Health | Yaara Artsi, Vera Sorin, Benjamin S. Glicksberg, et al. |
| 8 | [Performance of GPT-4 on the American College of Radiology In-training Examination: Evaluating Accuracy, Model Drift, and Fine-tuning](https://doi.org/10.1016/j.acra.2024.04.006) | 2024 | 3 | 34 | Academic Radiology | David Payne, Kush Purohit, Walter Morales Borrero, et al. |
| 9 | [Qualitative Coding with GPT-4](https://doi.org/10.18608/jla.2025.8575) | 2025 | 3 | 35 | Journal of Learning Analytics | Xiner Liu, Andres Felipe Zambrano, Ryan S. Baker, et al. |
| 10 | [Self-Refine: Iterative Refinement with Self-Feedback](https://doi.org/10.52202/075280-2019) | 2023 | 5 | 75 |  | Uri Alon, Peter Clark, Nouha Dziri, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 29 | 183549 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 20 | 95238 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 13 | 105466 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 4 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 12 | 64589 | MIS Quarterly | Fred D. Davis |
| 5 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 12 | 67969 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 6 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 11 | 34529 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 7 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 11 | 48662 |  | Tianqi Chen, Carlos Guestrin |
| 8 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 11 | 126295 | Machine Learning | Leo Breiman |
| 9 | [When to use and how to report the results of PLS-SEM](https://doi.org/10.1108/ebr-11-2018-0203) | 2018 | 9 | 24251 | European Business Review | Joseph F. Hair, Jeffrey J. Risher, Marko Sarstedt, et al. |
| 10 | [A conceptual and methodological critique of internet addiction research: Towards a model of compensatory internet use](https://doi.org/10.1016/j.chb.2013.10.059) | 2013 | 8 | 2222 | Computers in Human Behavior | Daniel Kardefelt‐Winther |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Omega Sandbox: Excitable Engine Edition — an interactive FitzHugh–Nagumo visualization with a pluggable-engine architecture](https://doi.org/10.5281/zenodo.20881579) | 2026 | 4 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Jonathan Williams, Matthew Arthur Carlo |
| 2 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 3 | 46 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy](https://doi.org/10.1016/j.ijinfomgt.2023.102642) | 2023 | 3 | 3735 | International Journal of Information Management | Yogesh K. Dwivedi, Nir Kshetri, Laurie Hughes, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 3 | 5170 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Omega Sandbox: Excitable Engine Edition — an interactive FitzHugh–Nagumo visualization with a pluggable-engine architecture](https://doi.org/10.5281/zenodo.20881579) | 2026 | 4 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Jonathan Williams, Matthew Arthur Carlo |
| 2 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 3 | 46 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
<!-- TRENDING-END -->
