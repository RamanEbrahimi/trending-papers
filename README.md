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

Last update: 2026-08-03 09:30 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Case Study Research: Design and Methods](https://openalex.org/W1527311855) | 1984 | 12 | 74975 |  | Robert K. Yin |
| 2 | [Artian Geometry & Quantum Traction Theory](https://doi.org/10.5281/zenodo.17527179) | 2026 | 8 | 93 | Zenodo (CERN European Organization for Nuclear Research) | Attar, Ali |
| 3 | [Competing paradigms in qualitative research.](https://openalex.org/W1741321747) | 1994 | 8 | 11832 |  | Egon G. Guba, Yvonna S. Lincoln |
| 4 | [Handbook of Qualitative Research](https://doi.org/10.2307/3121684) | 1994 | 8 | 26730 | British Journal of Educational Studies | Gill Crozier, Norman K. Denzin, Yvonna S. Lincoln |
| 5 | [Qualitative evaluation and research methods](https://openalex.org/W3214833809) | 1990 | 7 | 21753 |  | Michael Quinn Patton |
| 6 | [Qualitative research and evaluation methods](https://openalex.org/W115394847) | 1980 | 7 | 35375 |  | Michael Quinn Patton |
| 7 | [STAR: ultrafast universal RNA-seq aligner](https://doi.org/10.1093/bioinformatics/bts635) | 2012 | 7 | 57130 | Bioinformatics | Alexander Dobin, Carrie Davis, Felix Schlesinger, et al. |
| 8 | [The Sequence Alignment/Map format and SAMtools](https://doi.org/10.1093/bioinformatics/btp352) | 2009 | 7 | 68317 | Bioinformatics | Heng Li, Bob Handsaker, Alec Wysoker, et al. |
| 9 | [Marketing Research: An Applied Orientation](https://doi.org/10.2307/3151953) | 1994 | 6 | 7150 | Journal of Marketing Research | Lynn R. Kahle, Naresh K. Malhotra |
| 10 | [Research Methods in Education](https://doi.org/10.4324/9780203029053) | 2007 | 6 | 20095 |  | Louis Cohen, Lawrence Manion, Keith Morrison |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 102 | 128560 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 82 | 50300 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 33 | 29530 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 23 | 9405 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 16 | 31745 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 15 | 23877 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 15 | 33455 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 13 | 2623 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 13 | 82834 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 12 | 99570 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 13 | 2623 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 8 | 677 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 7 | 13445 |  | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 4 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 5 | 501 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 5 | [A review on longitudinal data analysis with random forest](https://doi.org/10.1093/bib/bbad002) | 2023 | 5 | 635 | Briefings in Bioinformatics | Jianchang Hu, Silke Szymczak |
| 6 | [Evaluation of clinical prediction models (part 3): calculating the sample size required for an external validation study](https://doi.org/10.1136/bmj-2023-074821) | 2024 | 4 | 153 | BMJ | Richard D Riley, Kym I E Snell, Lucinda Archer, et al. |
| 7 | [Evaluation of clinical prediction models (part 2): how to undertake an external validation study](https://doi.org/10.1136/bmj-2023-074820) | 2024 | 4 | 298 | BMJ | Richard D Riley, Lucinda Archer, Kym I E Snell, et al. |
| 8 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 4 | 641 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 9 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 4 | 703 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 10 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 4 | 2978 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 18 | 1142 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 3857 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 3435 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 3536 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 9 | 589 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 6 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 8 | 11307 |  | Nils Reimers, Iryna Gurevych |
| 7 | [Tool-Assisted Sycophancy: How Preference Optimization Can Invert Auxiliary Tools into Confirmation Engines](https://doi.org/10.5281/zenodo.21642311) | 2026 | 7 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 8 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 7 | 729 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 9 | [GPT-4 Technical Report](https://doi.org/10.4230/lipics.cosit.2024.11) | 2023 | 7 | 2433 | arXiv (Cornell University) | OpenAI, Achiam, Josh, Adler, Steven, et al. |
| 10 | [WGND 2.0](https://doi.org/10.7910/dvn/msegsj) | 2021 | 6 | 6 | Harvard Dataverse | Júlio Raffo |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 3435 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 3536 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Tool-Assisted Sycophancy: How Preference Optimization Can Invert Auxiliary Tools into Confirmation Engines](https://doi.org/10.5281/zenodo.21642311) | 2026 | 7 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 4 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 7 | 729 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 5 | [GPT-4 Technical Report](https://doi.org/10.4230/lipics.cosit.2024.11) | 2023 | 7 | 2433 | arXiv (Cornell University) | OpenAI, Achiam, Josh, Adler, Steven, et al. |
| 6 | [Recursive Sycophancy: When an LLM Addresses the Yes-Master Problem by Reproducing It](https://doi.org/10.5281/zenodo.21679059) | 2026 | 6 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 7 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 6 | 592 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 8 | [False Execution Status in LLM-Guided Processes: From Functional Substitution to Pseudo-Trace Contamination](https://doi.org/10.5281/zenodo.21683296) | 2026 | 5 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 9 | [A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation](https://doi.org/10.1038/s41746-025-01670-7) | 2025 | 5 | 269 | npj Digital Medicine | Elham Asgari, Nina Montaña-Brown, Magda Dubois, et al. |
| 10 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 5 | 410 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [WGND 2.0](https://doi.org/10.7910/dvn/msegsj) | 2021 | 6 | 6 | Harvard Dataverse | Júlio Raffo |
| 2 | [From Self-Interest to System Homeostasis: S1, S2, and "Love Your Neighbor as Yourself" Across Nature, Scripture, and Information Systems](https://doi.org/10.5281/zenodo.21655194) | 2026 | 3 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 3 | [False Execution Status in LLM-Guided Processes: From Functional Substitution to Pseudo-Trace Contamination](https://doi.org/10.5281/zenodo.21683296) | 2026 | 5 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 4 | [Recursive Sycophancy: When an LLM Addresses the Yes-Master Problem by Reproducing It](https://doi.org/10.5281/zenodo.21679059) | 2026 | 6 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 5 | [Tool-Assisted Sycophancy: How Preference Optimization Can Invert Auxiliary Tools into Confirmation Engines](https://doi.org/10.5281/zenodo.21642311) | 2026 | 7 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 6 | [Two Evolutionary Trajectories and a Process-Regulation Gap: From the Evolution of Agency and External Trace to Large Language Models and AWM](https://doi.org/10.5281/zenodo.21701945) | 2026 | 3 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Alen Širola |
| 7 | [Evaluating Large Language Models in Ophthalmology: Systematic Review](https://doi.org/10.2196/76947) | 2025 | 3 | 18 | Journal of Medical Internet Research | ZITAO ZHANG, Haiyang Zhang, Zhe Pan, et al. |
| 8 | [Game Generation via Large Language Models](https://doi.org/10.1109/cog60054.2024.10645597) | 2024 | 3 | 21 |  | Chengpeng Hu, Yunlong Zhao, Jialin Liu |
| 9 | [One Fits All: Power General Time Series Analysis by Pretrained LM](https://doi.org/10.52202/075280-1877) | 2023 | 3 | 58 |  | Tian Zhou, Peisong Niu, Xue Wang, et al. |
| 10 | [Large language model assisted fine-grained knowledge graph construction for robotic fault diagnosis](https://doi.org/10.1016/j.aei.2025.103134) | 2025 | 3 | 67 | Advanced Engineering Informatics | Xingming Liao, Chong Chen, Zhuowei Wang, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 30 | 187809 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 18 | 99528 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 15 | 78169 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 4 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 14 | 128560 | Machine Learning | Leo Breiman |
| 5 | [Naturalistic inquiry](https://doi.org/10.1016/0147-1767(85)90062-8) | 1985 | 12 | 35046 | International Journal of Intercultural Relations | Yvonna S. Lincoln, Egon G. Guba, Joseph J. Pilotta |
| 6 | [Statistical Power Analysis for the Behavioral Sciences](https://doi.org/10.4324/9780203771587) | 2013 | 11 | 24459 |  | Jacob Cohen |
| 7 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 11 | 50300 |  | Tianqi Chen, Carlos Guestrin |
| 8 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 11 | 106706 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 9 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 10 | 34992 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 10 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 9 | 41910 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 677 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 2 | [Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy](https://doi.org/10.1016/j.ijinfomgt.2023.102642) | 2023 | 4 | 3915 | International Journal of Information Management | Yogesh K. Dwivedi, Nir Kshetri, Laurie Hughes, et al. |
| 3 | [Common Method Bias: It's Bad, It's Complex, It's Widespread, and It's Not Easy to Fix](https://doi.org/10.1146/annurev-orgpsych-110721-040030) | 2023 | 3 | 1442 | Annual Review of Organizational Psychology and Organizational Behavior | Philip M. Podsakoff, Nathan P. Podsakoff, Larry J. Williams, et al. |
<!-- TRENDING-END -->
