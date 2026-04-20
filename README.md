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

Last update: 2026-04-20 07:56 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 302 | 176731 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 111 | 16053 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |
| 3 | [Development of NASA-TLX (Task Load Index): Results of Empirical and Theoretical Research](https://doi.org/10.1016/s0166-4115(08)62386-9) | 1988 | 84 | 14090 | Advances in psychology | Sandra G. Hart, Lowell E. Staveland |
| 4 | [Reliability and Inter-rater Reliability in Qualitative Research](https://doi.org/10.1145/3359174) | 2019 | 54 | 1079 | Proceedings of the ACM on Human-Computer Interaction | Nora McDonald, Sarita Schoenebeck, Andrea Forte |
| 5 | [Guidelines for Human-AI Interaction](https://doi.org/10.1145/3290605.3300233) | 2019 | 49 | 1716 |  | Saleema Amershi, Dan Weld, Mihaela Vorvoreanu, et al. |
| 6 | [Thematic analysis.](https://doi.org/10.1037/13620-004) | 2012 | 48 | 6528 | American Psychological Association eBooks | Virginia Braun, Victoria Clarke |
| 7 | [Design Justice](https://doi.org/10.7551/mitpress/12255.001.0001) | 2020 | 44 | 1366 | The MIT Press eBooks | Sasha Costanza-Chock |
| 8 | [The aligned rank transform for nonparametric factorial analyses using only anova procedures](https://doi.org/10.1145/1978942.1978963) | 2011 | 44 | 2664 |  | Jacob O. Wobbrock, Leah Findlater, Darren Gergle, et al. |
| 9 | [One size fits all? What counts as quality practice in (reflexive) thematic analysis?](https://doi.org/10.1080/14780887.2020.1769238) | 2020 | 40 | 7774 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 10 | [Feminist HCI](https://doi.org/10.1145/1753326.1753521) | 2010 | 38 | 1047 |  | Shaowen Bardzell |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 90 | 122439 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 53 | 46136 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 23 | 28081 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 17 | 8256 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 17 | 32352 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 14 | 6810 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |
| 7 | [A tutorial on support vector regression](https://doi.org/10.1023/b:stco.0000035301.49549.88) | 2004 | 14 | 12785 | Statistics and Computing | Alex Smola, Bernhard Schölkopf |
| 8 | [Regularization and Variable Selection Via the Elastic Net](https://doi.org/10.1111/j.1467-9868.2005.00503.x) | 2005 | 14 | 20607 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Hui Zou, Trevor Hastie |
| 9 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 14 | 51088 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 10 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 12 | 15768 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 11 | 1680 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 10 | 471 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Enhancing K-nearest neighbor algorithm: a comprehensive review and performance analysis of modifications](https://doi.org/10.1186/s40537-024-00973-y) | 2024 | 6 | 376 | Journal Of Big Data | Rajib Kumar Halder, Mohammed Nasir Uddin, Md. Ashraf Uddin, et al. |
| 4 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 5 | 571 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 5 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 21217 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 6 | [A machine learning method to predict rate constants for various reactions in combustion kinetic models](https://doi.org/10.1016/j.combustflame.2024.113375) | 2024 | 4 | 21 | Combustion and Flame | Ning Li, Sanket Girhe, Mingzhi Zhang, et al. |
| 7 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 4 | 499 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A machine learning method to predict rate constants for various reactions in combustion kinetic models](https://doi.org/10.1016/j.combustflame.2024.113375) | 2024 | 4 | 21 | Combustion and Flame | Ning Li, Sanket Girhe, Mingzhi Zhang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 30 | 176731 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2875 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 17 | 3045 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 15 | 3085 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 12 | 31791 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [Development of NASA-TLX (Task Load Index): Results of Empirical and Theoretical Research](https://doi.org/10.1016/s0166-4115(08)62386-9) | 1988 | 11 | 14090 | Advances in psychology | Sandra G. Hart, Lowell E. Staveland |
| 7 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 10 | 217 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 8 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 10 | 2138 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 9 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 4494 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 10 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 10 | 5040 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2875 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 17 | 3045 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 10 | 2138 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 4494 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Why Johnny Can’t Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts](https://doi.org/10.1145/3544548.3581388) | 2023 | 9 | 739 |  | J.D. Zamfirescu-Pereira, Richmond Y. Wong, Bjoern Hartmann, et al. |
| 6 | ["I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust](https://doi.org/10.1145/3630106.3658941) | 2024 | 7 | 92 |  | Sunnie S. Y. Kim, Q. Vera Liao, Mihaela Vorvoreanu, et al. |
| 7 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 7 | 455 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2277 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Bridging the Gulf of Envisioning: Cognitive Challenges in Prompt Based Interactions with LLMs](https://doi.org/10.1145/3613904.3642754) | 2024 | 6 | 101 |  | Hari Subramonyam, Roy Pea, Christopher Pondoc, et al. |
| 10 | [Unveiling the ChatGPT phenomenon: Evaluating the consistency and accuracy of endodontic question answers](https://doi.org/10.1111/iej.13985) | 2023 | 6 | 163 | International Endodontic Journal | Ana Suárez, Víctor Díaz‐Flores García, Juan Algar, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evaluating the Response of AI-Based Large Language Models to Common Patient Concerns About Endodontic Root Canal Treatment: A Comparative Performance Analysis](https://doi.org/10.3390/jcm14217482) | 2025 | 4 | 7 | Journal of Clinical Medicine | Busra Demir Cicek, Orhan Çiçek |
| 2 | ["Kya family planning after marriage hoti hai?": Integrating Cultural Sensitivity in an LLM Chatbot for Reproductive Health](https://doi.org/10.1145/3706598.3713362) | 2025 | 5 | 11 |  | Roshini Deva, Dhruv Ramani, Tanvi Divate, et al. |
| 3 | [Beyond the Waiting Room: Patient's Perspectives on the Conversational Nuances of Pre-Consultation Chatbots](https://doi.org/10.1145/3613904.3641913) | 2024 | 4 | 28 |  | Brenna Li, Ofek Gross, Noah Crampton, et al. |
| 4 | [Supporting Sensemaking of Large Language Model Outputs at Scale](https://doi.org/10.1145/3613904.3642139) | 2024 | 4 | 42 |  | Katy Ilonka Gero, Chelse Swoopes, Ziwei Gu, et al. |
| 5 | [DiaryMate: Understanding User Perceptions and Experience in Human-AI Collaboration for Personal Journaling](https://doi.org/10.1145/3613904.3642693) | 2024 | 5 | 57 |  | Taewan Kim, Dong-Hoon Shin, Young‐Ho Kim, et al. |
| 6 | ["I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust](https://doi.org/10.1145/3630106.3658941) | 2024 | 7 | 92 |  | Sunnie S. Y. Kim, Q. Vera Liao, Mihaela Vorvoreanu, et al. |
| 7 | [EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria](https://doi.org/10.1145/3613904.3642216) | 2024 | 5 | 71 |  | Tae Soo Kim, Yoonjoo Lee, Jamin Shin, et al. |
| 8 | [Shaping Human-AI Collaboration: Varied Scaffolding Levels in Co-writing with Language Models](https://doi.org/10.1145/3613904.3642134) | 2024 | 5 | 74 |  | Paramveer S. Dhillon, Somayeh Molaei, Jiaqi Li, et al. |
| 9 | [How People Use ChatGPT](https://doi.org/10.3386/w34255) | 2025 | 5 | 77 | National Bureau of Economic Research | Aaron Chatterji, Thomas Cunningham, David Deming, et al. |
| 10 | [AI-Augmented Brainwriting: Investigating the use of LLMs in group ideation](https://doi.org/10.1145/3613904.3642414) | 2024 | 5 | 97 |  | Orit Shaer, Angelora Cooper, Osnat Mokryn, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 20 | 176731 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 13 | 88531 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [From game design elements to gamefulness](https://doi.org/10.1145/2181037.2181040) | 2011 | 10 | 7635 |  | Sebastian Deterding, Dan Dixon, Rilla Khaled, et al. |
| 4 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 9 | 46136 |  | Tianqi Chen, Carlos Guestrin |
| 5 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 9 | 74313 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 6 | [Does Gamification Work? -- A Literature Review of Empirical Studies on Gamification](https://doi.org/10.1109/hicss.2014.377) | 2014 | 8 | 4737 |  | Juho Hamari, Jonna Koivisto, Harri Sarsa |
| 7 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 8 | 31119 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 8 | [Self-Determination Theory: Basic Psychological Needs in Motivation, Development, and Wellness](https://doi.org/10.1521/978.14625/28806) | 2017 | 7 | 11347 | Guilford Press eBooks | Unknown |
| 9 | [Statistical power analyses using G*Power 3.1: Tests for correlation and regression analyses](https://doi.org/10.3758/brm.41.4.1149) | 2009 | 6 | 34903 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Axel Buchner, et al. |
| 10 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 6 | 65593 | Journal of Marketing Research | Claes Fornell, David F. Larcker |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Resonance as Civilizational Architecture: A Unified Theory of Koku, BBDDH, PRT, and Hikari Currency v1.1 — From the Structure of the Universe to the Structure of Healing: One Principle](https://doi.org/10.5281/zenodo.19305649) | 2026 | 5 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 2 | [GKU Cosmology v2](https://doi.org/10.5281/zenodo.19097250) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 3 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 4494 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 4 | [Adaptive Gamification in Science Education: An Analysis of the Impact of Implementation and Adapted Game Elements on Students’ Motivation](https://doi.org/10.3390/computers12070143) | 2023 | 3 | 99 | Computers | Alkinoos-Ioannis Zourmpakis, Michail Kalogiannakis, Stamatios Papadakis |
| 5 | [Impact of Gamification on Motivation and Academic Performance: A Systematic Review](https://doi.org/10.3390/educsci14060639) | 2024 | 3 | 113 | Education Sciences | Lorena Jaramillo-Mediavilla, Andrea Basantes-Andrade, Marcos Cabezas González, et al. |
| 6 | [The Brain-Body Dissociative Disconnection Hypothesis (BBDDH)](https://doi.org/10.5281/zenodo.19105964) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 7 | [Shapley value: from cooperative game to explainable artificial intelligence](https://doi.org/10.1007/s43684-023-00060-8) | 2024 | 2 | 133 | Autonomous Intelligent Systems | Meng Li, Hengyang Sun, Yanjun Huang, et al. |
| 8 | [The Coding Manual for Qualitative Researchers](https://doi.org/10.4135/9781036235611) | 2025 | 2 | 17891 |  | Johnny Saldaña |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Resonance as Civilizational Architecture: A Unified Theory of Koku, BBDDH, PRT, and Hikari Currency v1.1 — From the Structure of the Universe to the Structure of Healing: One Principle](https://doi.org/10.5281/zenodo.19305649) | 2026 | 5 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 2 | [GKU Cosmology v2](https://doi.org/10.5281/zenodo.19097250) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 3 | [The Brain-Body Dissociative Disconnection Hypothesis (BBDDH)](https://doi.org/10.5281/zenodo.19105964) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 4 | [Surrender at 20? Matchmaking in league of legends](https://doi.org/10.1109/gem.2015.7377234) | 2015 | 2 | 18 |  | Mark Claypool, Jonathan Michael Decelle, G. Emlin Hall, et al. |
| 5 | [Does Chatbot Language Formality Affect Users’ Self-Disclosure?](https://doi.org/10.1145/3543829.3543831) | 2022 | 3 | 38 |  | Samuel Rhys Cox, Wei Tsang Ooi |
| 6 | [The Ethics of Multiplayer Game Design and Community Management](https://doi.org/10.1145/3411764.3445363) | 2021 | 3 | 44 |  | Lucy A. Sparrow, Martin Gibbs, Matthew Arnold |
| 7 | [What Empirically Based Research Tells Us About Game Development](https://doi.org/10.1007/s40869-019-00085-1) | 2019 | 2 | 37 | The Computer Games Journal | Björn Berg Marklund, Henrik Engström, Marcus Hellkvist, et al. |
| 8 | [What Can We Learn From Studio Studies Ethnographies?: A “Messy” Account of Game Development Materiality, Learning, and Expertise](https://doi.org/10.1177/1555412018783320) | 2018 | 2 | 55 | Games and Culture | Jennifer R. Whitson |
| 9 | [Adaptive Gamification in Science Education: An Analysis of the Impact of Implementation and Adapted Game Elements on Students’ Motivation](https://doi.org/10.3390/computers12070143) | 2023 | 3 | 99 | Computers | Alkinoos-Ioannis Zourmpakis, Michail Kalogiannakis, Stamatios Papadakis |
<!-- TRENDING-END -->
