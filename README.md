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

Last update: 2026-07-20 08:46 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Power and particle exhaust in the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae70a0) | 2026 | 10 | 10 | Nuclear Fusion | Matthew Robinson, A. Scarabosio, E. O. Vekshina, et al. |
| 2 | [Physics basis for the reference flat-top plasma scenario in the ST–E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae5f33) | 2026 | 10 | 10 | Nuclear Fusion | Steven McNamara, S. Abouelazayem, А. И. Алиева, et al. |
| 3 | [Design scoping and systems modelling of ST-E1 using the PyTok power plant simulation code](https://doi.org/10.1088/1741-4326/ae5d55) | 2026 | 9 | 9 | Nuclear Fusion | C.L. Wilson, J. Astbury, M.J. Ginsberg, et al. |
| 4 | [Integrated physics and magnet design for the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae773b) | 2026 | 8 | 8 | Nuclear Fusion | E. Maartensson, N. Welch, M. Scarpari, et al. |
| 5 | [Tokamak Energy’s pre-concept design for a fusion power plant: an overview of ST-E1](https://doi.org/10.1088/1741-4326/ae5545) | 2026 | 8 | 8 | Nuclear Fusion | J. Willis, Steven McNamara, E. Maartensson, et al. |
| 6 | [Tritium production and processing systems for ST-E1](https://doi.org/10.1088/1741-4326/ae773a) | 2026 | 8 | 8 | Nuclear Fusion | Emrah Yıldırım, J. Naish, J. Trueba, et al. |
| 7 | [Maintenance strategy, structural design, and site layout of the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae7c15) | 2026 | 7 | 7 | Nuclear Fusion | J. Willis, K. Chandrasekhar, P. Cheema, et al. |
| 8 | [Nuclear technology considerations and neutronics for the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae63e2) | 2026 | 7 | 7 | Nuclear Fusion | K. Chandrasekhar, Christopher Lister Wilson, Samara M. Levine, et al. |
| 9 | [Artian Geometry & Quantum Traction Theory](https://doi.org/10.5281/zenodo.17527179) | 2026 | 7 | 70 | Zenodo (CERN European Organization for Nuclear Research) | Attar, Ali |
| 10 | [Thermal management and net-power evaluation of the ST-E1 fusion power plant](https://doi.org/10.1088/1741-4326/ae5546) | 2026 | 6 | 6 | Nuclear Fusion | Mohamed Khalid Elsharif Mohamed, Alasdair Burchill, Liviu Maatescu, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 112 | 127705 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 82 | 49759 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 33 | 29332 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 26 | 9240 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 15 | 23711 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 14 | 8790 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 7 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 14 | 99119 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 8 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 12 | 31559 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 9 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 12 | 33303 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 10 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 11 | 16294 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Model Predictive Control: The Genesis of an Idea [Histories of Control]](https://doi.org/10.1109/mcs.2025.3573842) | 2025 | 9 | 49 | IEEE Control Systems | Manfred Morari |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 8 | 2447 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 6 | 626 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 4 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 6 | 645 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 5 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 4 | 454 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 6 | [Feature selection strategies: a comparative analysis of SHAP-value and importance-based methods](https://doi.org/10.1186/s40537-024-00905-w) | 2024 | 4 | 534 | Journal Of Big Data | Huanjing Wang, Qianxin Liang, John Hancock, et al. |
| 7 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 4 | 732 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 8 | [Evaluation metrics and statistical tests for machine learning](https://doi.org/10.1038/s41598-024-56706-x) | 2024 | 4 | 1079 | Scientific Reports | Oona Rainio, Jarmo Teuho, Riku Klén |
| 9 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 4 | 5101 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |
| 10 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 4 | 14375 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Model Predictive Control: The Genesis of an Idea [Histories of Control]](https://doi.org/10.1109/mcs.2025.3573842) | 2025 | 9 | 49 | IEEE Control Systems | Manfred Morari |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 35 | 994 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 2 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 19 | 483 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 3 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 18 | 32847 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 4 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 17 | 506 |  | Sandhini Agarwal, Diogo Almeida, Amanda Askell, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 13 | 3463 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 12 | 443 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 7 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 1703 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 8 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 3347 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 9 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://doi.org/10.52202/075280-2338) | 2023 | 11 | 161 |  | Stefano Ermon, Chelsea Finn, Eric Mitchell, et al. |
| 10 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 356 |  | Wei-Lin Chiang, Joseph Gonzalez, Dacheng Li, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 19 | 483 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 13 | 3463 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 12 | 443 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 1703 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 3347 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://doi.org/10.52202/075280-2338) | 2023 | 11 | 161 |  | Stefano Ermon, Chelsea Finn, Eric Mitchell, et al. |
| 7 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 356 |  | Wei-Lin Chiang, Joseph Gonzalez, Dacheng Li, et al. |
| 8 | [TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation](https://doi.org/10.1145/3604915.3608857) | 2023 | 10 | 378 |  | Keqin Bao, Jizhi Zhang, Yang Zhang, et al. |
| 9 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 10 | 694 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 10 | [Representation Learning with Large Language Models for Recommendation](https://doi.org/10.1145/3589334.3645458) | 2024 | 9 | 190 |  | Xubin Ren, Wei Wei, Lianghao Xia, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts](https://doi.org/10.1609/aaai.v39i22.34568) | 2025 | 4 | 44 | Proceedings of the AAAI Conference on Artificial Intelligence | Yichen Gong, Delong Ran, Jinyuan Liu, et al. |
| 2 | [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://doi.org/10.52202/079017-3018) | 2024 | 4 | 49 |  | Yubo Wang, Xueguang Ma, Ge Zhang, et al. |
| 3 | [LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation](https://doi.org/10.52202/079017-0839) | 2024 | 4 | 51 |  | Qidong Liu, Xian Wu, Yejing Wang, et al. |
| 4 | [Jailbroken: How Does LLM Safety Training Fail?](https://doi.org/10.52202/075280-3508) | 2023 | 5 | 66 |  | Nika Haghtalab, Jacob Steinhardt, Alexander Wei |
| 5 | [AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems](https://doi.org/10.1145/3589334.3645537) | 2024 | 4 | 72 |  | Junjie Zhang, Yupeng Hou, Ruobing Xie, et al. |
| 6 | [Knowledge-Augmented Language Model Prompting for Zero-Shot Knowledge Graph Question Answering](https://doi.org/10.18653/v1/2023.nlrse-1.7) | 2023 | 4 | 96 |  | Jinheon Baek, Alham Fikri Aji, Amir Saffari |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 26 | 186283 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 16 | 97896 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 11 | 41362 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 4 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 11 | 49759 |  | Tianqi Chen, Carlos Guestrin |
| 5 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 11 | 68765 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 6 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 10 | 77589 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 7 | [From game design elements to gamefulness](https://doi.org/10.1145/2181037.2181040) | 2011 | 9 | 7942 |  | Sebastian Deterding, Dan Dixon, Rilla Khaled, et al. |
| 8 | [Statistical Power Analysis for the Behavioral Sciences](https://doi.org/10.4324/9780203771587) | 2013 | 9 | 24253 |  | Jacob Cohen |
| 9 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 9 | 85519 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 10 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 8 | 34517 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [GPT-4 Technical Report](https://doi.org/10.4230/lipics.cosit.2024.11) | 2023 | 4 | 2409 | arXiv (Cornell University) | OpenAI, Achiam, Josh, Adler, Steven, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 5484 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 3 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection](https://doi.org/10.5281/zenodo.20130563) | 2026 | 3 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 3 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 3 | 49 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 3 | 54 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 8 | [Gamification enhances student intrinsic motivation, perceptions of autonomy and relatedness, but minimal impact on competency: a meta-analysis and systematic review](https://doi.org/10.1007/s11423-023-10337-7) | 2024 | 3 | 146 | Educational Technology Research and Development | Liuyufeng Li, Khe Foon Hew, Jiahui Du |
| 9 | [Transfer learning enables predictions in network biology](https://doi.org/10.1038/s41586-023-06139-9) | 2023 | 3 | 1081 | Nature | Christina V. Theodoris, Ling Xiao, Anant Chopra, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 3 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection](https://doi.org/10.5281/zenodo.20130563) | 2026 | 3 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 3 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 3 | 49 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 3 | 54 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
<!-- TRENDING-END -->
