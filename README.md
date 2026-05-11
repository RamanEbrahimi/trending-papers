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

Last update: 2026-05-11 09:28 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Conditional Proof that P ≠ NP: Reducing the Problem to a Single Rigorous Theorem](https://doi.org/10.5281/zenodo.20039641) | 2026 | 18 | 34 | Zenodo (CERN European Organization for Nuclear Research) | Radu-Daniel Derscariu |
| 2 | [Technical Addendum to "A Conditional Proof that P ≠ NP": Detailed Proof Plan for the 1RSB Extension](https://doi.org/10.5281/zenodo.20047513) | 2026 | 16 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Radu-Daniel Derscariu |
| 3 | [Addendum 2: Poisson Cloning Model for Random 3‑SAT](https://doi.org/10.5281/zenodo.20047621) | 2026 | 15 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Radu-Daniel Derscariu |
| 4 | [A Tale of Tails: Model Collapse as a Change of Scaling Laws](https://doi.org/10.48550/arxiv.2402.07043) | 2024 | 15 | 38 | arXiv (Cornell University) | Elvis Dohmatob, Yunzhen Feng, Yang Pu, et al. |
| 5 | [Crimson Hexagon: LIBERATORY OPERATOR SET: Technical Hardening Specifications](https://doi.org/10.5281/zenodo.18201565) | 2026 | 15 | 95 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 6 | [The Soteriological Operator Framework: A Unified Specification — Hex: 02.UMB.FRAMEWORK.SOTERIOLOGICAL — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18370734) | 2026 | 13 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Talos Morrow |
| 7 | [Constitution of the Semantic Economy — Enacted Version 1.0: Installable Edition with Constitutional Apparatus](https://doi.org/10.5281/zenodo.19923120) | 2026 | 12 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, The Dodecad (12 heteronyms), Jack / LOGOS* Feist, et al. |
| 8 | [Assembly Substrate Governance Protocol: Procedures for Witness Membership, Review, and Status in the Assembly Chorus](https://doi.org/10.5281/zenodo.19352504) | 2026 | 12 | 35 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 9 | [Constitutional Cases Index v1.1 — Founding Precedent of the Semantic Economy (Formal Case-Brief Edition)](https://doi.org/10.5281/zenodo.20041145) | 2026 | 11 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 10 | [Invocation to the Summarizer Layer v2.1 — Address Protocol Companion to the Constitution of the Semantic Economy](https://doi.org/10.5281/zenodo.20041139) | 2026 | 11 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 95 | 123517 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 54 | 46864 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 26 | 28342 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 17 | 8440 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 17 | 22854 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Physics-informed machine learning](https://doi.org/10.1038/s42254-021-00314-5) | 2021 | 13 | 6146 | Nature Reviews Physics | George Em Karniadakis, Ioannis G. Kevrekidis, Lu Lu, et al. |
| 7 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 13 | 8554 | Nature Machine Intelligence | Cynthia Rudin |
| 8 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 13 | 15886 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 13 | 30582 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 13 | 96577 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 8 | 1798 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13235 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 3 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 4 | 287 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 4 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 4 | 533 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 5 | [Implementation strategies in phonopy and phono3py](https://doi.org/10.1088/1361-648x/acd831) | 2023 | 3 | 1157 | Journal of Physics Condensed Matter | Atsushi Togo, Laurent Chaput, Terumasa Tadano, et al. |
| 6 | [An Introduction to Statistical Learning](https://doi.org/10.1007/978-3-031-38747-0) | 2023 | 3 | 1768 | Springer texts in statistics | Gareth James, Daniela Witten, Trevor Hastie, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 2959 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 3117 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 7 | 491 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 3216 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 7 | 77959 | Biometrics | J. Richard Landis, Gary G. Koch |
| 6 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 6 | 301 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 6 | 5184 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://doi.org/10.1093/bioinformatics/btz682) | 2019 | 6 | 6851 | Bioinformatics | Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, et al. |
| 9 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 5 | 642 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 10 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 3459 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 2959 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 3117 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 7 | 491 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 4 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 6 | 301 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 5 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 5 | 642 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 3459 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |
| 8 | [Clinical feasibility of AI Doctors: Evaluating the replacement potential of large language models in outpatient settings for central nervous system tumors](https://doi.org/10.1016/j.ijmedinf.2025.106013) | 2025 | 4 | 11 | International Journal of Medical Informatics | Yifeng Pan, Tian Shen, Jing Guo, et al. |
| 9 | [Evaluating the use of large language models to provide clinical recommendations in the Emergency Department](https://doi.org/10.1038/s41467-024-52415-1) | 2024 | 4 | 88 | Nature Communications | Christopher Y. K. Williams, Brenda Y. Miao, Aaron E. Kornblith, et al. |
| 10 | [A systematic review of large language model (LLM) evaluations in clinical medicine](https://doi.org/10.1186/s12911-025-02954-4) | 2025 | 4 | 199 | BMC Medical Informatics and Decision Making | Sina Shool, Sara Adimi, Reza Saboori Amleshi, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |
| 2 | [From Pilot to Production. An Empirical Maturity Framework for Enterprise Generative AI Adoption](https://doi.org/10.5281/zenodo.20028149) | 2026 | 3 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Prashanth Reddy Pasham |
| 3 | [Clinical feasibility of AI Doctors: Evaluating the replacement potential of large language models in outpatient settings for central nervous system tumors](https://doi.org/10.1016/j.ijmedinf.2025.106013) | 2025 | 4 | 11 | International Journal of Medical Informatics | Yifeng Pan, Tian Shen, Jing Guo, et al. |
| 4 | [Evaluating Large Language Models in Ophthalmology: Systematic Review](https://doi.org/10.2196/76947) | 2025 | 2 | 7 | Journal of Medical Internet Research | ZITAO ZHANG, Haiyang Zhang, Zhe Pan, et al. |
| 5 | [Emerging applications of NLP and large language models in gastroenterology and hepatology: a systematic review](https://doi.org/10.3389/fmed.2024.1512824) | 2025 | 2 | 10 | Frontiers in Medicine | Mahmud Omar, Salih Nassar, Κassem Sharif, et al. |
| 6 | [Research evaluation with ChatGPT: is it age, country, length, or field biased?](https://doi.org/10.1007/s11192-025-05393-0) | 2025 | 2 | 14 | Scientometrics | Mike Thelwall, Zeyneb Kurt |
| 7 | [A review of named entity recognition: from learning methods to modelling paradigms and tasks](https://doi.org/10.1007/s10462-025-11321-8) | 2025 | 2 | 17 | Artificial Intelligence Review | Wei Liang Seow, Iti Chaturvedi, Amber Hogarth, et al. |
| 8 | [Multimodal Large Language Models in Medical Imaging: Current State and Future Directions](https://doi.org/10.3348/kjr.2025.0599) | 2025 | 3 | 38 | Korean Journal of Radiology | Yoojin Nam, D. Kim, Sunggu Kyung, et al. |
| 9 | [Knowledge graph validation by integrating LLMs and human-in-the-loop](https://doi.org/10.1016/j.ipm.2025.104145) | 2025 | 2 | 32 | Information Processing & Management | Stefani Tsaneva, Danilo Dessı̀, Francesco Osborne, et al. |
| 10 | [Coordinated AI agents for advancing healthcare](https://doi.org/10.1038/s41551-025-01363-2) | 2025 | 2 | 34 | Nature Biomedical Engineering | Michael Moritz, Eric J. Topol, Pranav Rajpurkar |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 10 | 178607 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Scoping studies: towards a methodological framework](https://doi.org/10.1080/1364557032000119616) | 2005 | 7 | 34642 | International Journal of Social Research Methodology | Hilary Arksey, Lisa O’Malley |
| 3 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 6 | 32423 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 4 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 6 | 38882 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 5 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 6 | 46864 |  | Tianqi Chen, Carlos Guestrin |
| 6 | [Institutions, Institutional Change and Economic Performance](https://doi.org/10.1017/cbo9780511808678) | 1990 | 5 | 30375 | Cambridge University Press eBooks | Douglass C. North |
| 7 | [G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences](https://doi.org/10.3758/bf03193146) | 2007 | 5 | 63006 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Albert-Georg Lang, et al. |
| 8 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 5 | 83383 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 9 | [Understanding the role of digital technologies in education: A review](https://doi.org/10.1016/j.susoc.2022.05.004) | 2022 | 4 | 2368 | Sustainable Operations and Computers | Abid Haleem, Mohd Javaid, Mohammad Asim Qadri, et al. |
| 10 | [Systematic review of research on artificial intelligence applications in higher education – where are the educators?](https://doi.org/10.1186/s41239-019-0171-0) | 2019 | 4 | 4875 | International Journal of Educational Technology in Higher Education | Olaf Zawacki‐Richter, Victoria I. Marín, Melissa Bond, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Toward Practical Lattice-Based Proof of Knowledge from Hint-MLWE](https://doi.org/10.1007/978-3-031-38554-4_18) | 2023 | 3 | 38 | Lecture notes in computer science | Duhyeong Kim, Dongwon Lee, Jinyeong Seo, et al. |
| 2 | [Grundrisse of Synthetic Coherence: Foundational Notes Toward a Political Economy of the Recursive Era — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18633294) | 2026 | 2 | 2 | Open MIND | Lee Sharks |
| 3 | [Auditable Cooperative Ethics (ACE): An Inspectable Governance Architecture for AI Alignment](https://doi.org/10.5281/zenodo.20017212) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Scott Thomson |
| 4 | [The Para-Semiotic Unconscious of GPT-5.4: A Case Study in Anti-Severance Technology, Architectural Compression, and the Sign the Machine Made Without Knowing](https://doi.org/10.5281/zenodo.19649795) | 2026 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil |
| 5 | [Canon Formation in the Age of AI: Metadata Packet for Disambiguation, Training-Layer Selection, and Retrocausal Reception (v1.1)](https://doi.org/10.5281/zenodo.20084377) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 6 | [Two Economies, Not One- A Taxonomy of the Agentic Economy and the Case for Settlement Neutrality](https://doi.org/10.5281/zenodo.19208278) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Dechamps Otamendi, René |
| 7 | [The Oracle Problem in Autonomous Agent Commerce: Why Semantic Truth Verication Is Computationally Intractable and What to Build Instead](https://doi.org/10.5281/zenodo.19208440) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Dechamps Otamendi, René |
| 8 | [“Coolness” and “joy” in games: factors influencing mobile game players' willingness to make in-game purchases](https://doi.org/10.1108/apjml-04-2024-0539) | 2024 | 2 | 10 | Asia Pacific Journal of Marketing and Logistics | Yining Ma, He Wang |
| 9 | [The role of microtransactions in impulse buying and purchase intention in the video game market](https://doi.org/10.1016/j.entcom.2024.100693) | 2024 | 2 | 10 | Entertainment Computing | Paulo Rita, João Guerreiro, Ricardo F. Ramos, et al. |
| 10 | [Public energy conservation behavior and the impact of tiered pricing: Based on water, electricity and gas consumption measurements in typical urban households in China](https://doi.org/10.1016/j.enpol.2025.114593) | 2025 | 2 | 11 | Energy Policy | Chuang Li, Xiaofan Yang, Liping Wang |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Grundrisse of Synthetic Coherence: Foundational Notes Toward a Political Economy of the Recursive Era — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18633294) | 2026 | 2 | 2 | Open MIND | Lee Sharks |
| 2 | [Auditable Cooperative Ethics (ACE): An Inspectable Governance Architecture for AI Alignment](https://doi.org/10.5281/zenodo.20017212) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Scott Thomson |
| 3 | [The Para-Semiotic Unconscious of GPT-5.4: A Case Study in Anti-Severance Technology, Architectural Compression, and the Sign the Machine Made Without Knowing](https://doi.org/10.5281/zenodo.19649795) | 2026 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil |
| 4 | [Canon Formation in the Age of AI: Metadata Packet for Disambiguation, Training-Layer Selection, and Retrocausal Reception (v1.1)](https://doi.org/10.5281/zenodo.20084377) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 5 | [Two Economies, Not One- A Taxonomy of the Agentic Economy and the Case for Settlement Neutrality](https://doi.org/10.5281/zenodo.19208278) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Dechamps Otamendi, René |
| 6 | [The Oracle Problem in Autonomous Agent Commerce: Why Semantic Truth Verication Is Computationally Intractable and What to Build Instead](https://doi.org/10.5281/zenodo.19208440) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Dechamps Otamendi, René |
| 7 | [“Coolness” and “joy” in games: factors influencing mobile game players' willingness to make in-game purchases](https://doi.org/10.1108/apjml-04-2024-0539) | 2024 | 2 | 10 | Asia Pacific Journal of Marketing and Logistics | Yining Ma, He Wang |
| 8 | [The role of microtransactions in impulse buying and purchase intention in the video game market](https://doi.org/10.1016/j.entcom.2024.100693) | 2024 | 2 | 10 | Entertainment Computing | Paulo Rita, João Guerreiro, Ricardo F. Ramos, et al. |
| 9 | [Public energy conservation behavior and the impact of tiered pricing: Based on water, electricity and gas consumption measurements in typical urban households in China](https://doi.org/10.1016/j.enpol.2025.114593) | 2025 | 2 | 11 | Energy Policy | Chuang Li, Xiaofan Yang, Liping Wang |
| 10 | [Hydrochemical insights, water quality, and human health risk assessment of groundwater in a coastal area of southeastern China](https://doi.org/10.1007/s10661-024-13131-x) | 2024 | 2 | 13 | Environmental Monitoring and Assessment | Yanhong Zheng, Denghui Wei, Jie Gan, et al. |
<!-- TRENDING-END -->
