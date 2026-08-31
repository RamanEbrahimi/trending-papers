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

Last update: 2026-08-31 12:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Kronos Integrated Platform: A Spherical-Tokamak Breeder and a Deuterium-Helium-3 Burner as One Strategic-Materials and Power Architecture](https://doi.org/10.5281/zenodo.22132156) | 2026 | 42 | 86 | OSF Preprints (OSF Preprints) | Priyanca Ford, G L Kulcinski |
| 2 | [Closure of a Deuterium–Helium-3 Tandem Mirror with Direct Conversion: A 35-Simulation Validation Package](https://doi.org/10.5281/zenodo.21746479) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, G.L. Kulcinski |
| 3 | [Hyperion: A Simulation and Validation Data Package for a Deuterium–Tritium Spherical-Tokamak Tritium / Helium-3 Breeder](https://doi.org/10.5281/zenodo.21746157) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford |
| 4 | [Direct Energy Conversion for a D-3He Magnetic-Mirror Burner: the Electron Channel is the Larger Axial Stream, and a Quasineutral Expander Can Recover It — Reproducible Code and Data](https://doi.org/10.5281/zenodo.21842864) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, G.L. Kulcinski |
| 5 | [Physics-Informed AI and Quantum Technologies for Certifiable Real-Time Control of Compact Fusion Generators — reproducibility deposit (code, data, figures)](https://doi.org/10.5281/zenodo.21842371) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford |
| 6 | [An Integrated High-Field REBCO Conductor and Winding System for Compact Fusion Magnets: Strain-First Design, Bore-Resolved Mechanics, and a Two-Machine Feasibility Map — Reproducible Code and Data](https://doi.org/10.5281/zenodo.21842514) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, Carl Frederick Weggel, J.V. Minervini |
| 7 | [STAR: ultrafast universal RNA-seq aligner](https://doi.org/10.1093/bioinformatics/bts635) | 2012 | 8 | 57557 | Bioinformatics | Alexander Dobin, Carrie Davis, Felix Schlesinger, et al. |
| 8 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 103210 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 9 | [The Vocabulary Fingerprint of AI Rewriting: Common Words AI Language Models Prioritize](https://doi.org/10.5281/zenodo.22028377) | 2026 | 7 | 27 | Zenodo (CERN European Organization for Nuclear Research) | TextPulse Research |
| 10 | [Do AI Models Invent References? A Verification Audit of Citations in AI-Generated Academic Text](https://doi.org/10.5281/zenodo.22010511) | 2026 | 7 | 30 | Zenodo (CERN European Organization for Nuclear Research) | TextPulse Research |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 118 | 130802 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 75 | 52124 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 40 | 30065 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 27 | 9871 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 22 | 3087 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 21 | 33863 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 19 | 32347 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations](https://doi.org/10.1016/j.jcp.2018.10.045) | 2018 | 15 | 18926 | Journal of Computational Physics | Maziar Raissi, Paris Perdikaris, George Em Karniadakis |
| 9 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 14 | 9036 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 10 | [A tutorial on support vector regression](https://doi.org/10.1023/b:stco.0000035301.49549.88) | 2004 | 14 | 13318 | Statistics and Computing | Alex Smola, Bernhard Schölkopf |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 22 | 3087 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 11 | 750 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 13517 | OASIcs : OpenAccess Series in Informatics | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 4 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 6 | 643 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 5 | [Evaluation metrics and statistical tests for machine learning](https://doi.org/10.1038/s41598-024-56706-x) | 2024 | 5 | 1193 | Scientific Reports | Oona Rainio, Jarmo Teuho, Riku Klén |
| 6 | [Advancing water quality assessment and prediction using machine learning models, coupled with explainable artificial intelligence (XAI) techniques like shapley additive explanations (SHAP) for interpreting the black-box nature](https://doi.org/10.1016/j.rineng.2024.102831) | 2024 | 4 | 208 | Results in Engineering | Randika K. Makumbura, Lakindu Mampitiya, Namal Rathnayake, et al. |
| 7 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 4 | 703 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 8 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 4 | 909 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 9 | [Scaling deep learning for materials discovery](https://doi.org/10.1038/s41586-023-06735-9) | 2023 | 4 | 1331 | Nature | Amil Merchant, Simon Batzner, Samuel S. Schoenholz, et al. |
| 10 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 4 | 3138 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 32 | 1743 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 3697 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 13 | 916 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 4 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 6390 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 5 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 11 | 11760 |  | Nils Reimers, Iryna Gurevych |
| 6 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 11 | 33353 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 7 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 10 | 1960 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 8 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 3733 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 9 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://doi.org/10.52202/075280-0517) | 2023 | 9 | 314 |  | Shunyu Yao, Dian Yu, Jeffrey Zhao, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 9 | 2512 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 3697 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 10 | 1960 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 3733 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://doi.org/10.52202/075280-0517) | 2023 | 9 | 314 |  | Shunyu Yao, Dian Yu, Jeffrey Zhao, et al. |
| 5 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 9 | 2512 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 6 | [Self-Refine: Iterative Refinement with Self-Feedback](https://doi.org/10.52202/075280-2019) | 2023 | 8 | 257 |  | Aman Madaan, Niket Tandon, Prakhar Gupta, et al. |
| 7 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 8 | 613 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 8 | 3773 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 9 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 8 | 6260 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 10 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 7 | 685 |  | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Systematic Survey on Large Language Models for Algorithm Design](https://doi.org/10.1145/3787585) | 2026 | 3 | 25 | ACM Computing Surveys | Fei Liu, Yiming Yao, Ping Guo, et al. |
| 2 | [VisualSiteDiary: A detector-free Vision-Language Transformer model for captioning photologs for daily construction reporting and image retrievals](https://doi.org/10.1016/j.autcon.2024.105483) | 2024 | 4 | 38 | Automation in Construction | Yoonhwa Jung, Ikhyun Cho, Shun-Hsiang Hsu, et al. |
| 3 | [LIMA: Less Is More for Alignment](https://doi.org/10.52202/075280-2400) | 2023 | 4 | 49 |  | Chunting Zhou, Pengfei Liu, Puxin Xu, et al. |
| 4 | [An integrated approach for automatic safety inspection in construction: Domain knowledge with multimodal large language model](https://doi.org/10.1016/j.aei.2025.103246) | 2025 | 4 | 57 | Advanced Engineering Informatics | Yiheng Wang, Hanbin Luo, Weili Fang |
| 5 | [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://doi.org/10.52202/079017-1381) | 2024 | 3 | 43 |  | Haoran Ye, Jiarui Wang, Zhiguang Cao, et al. |
| 6 | [Accelerating clinical evidence synthesis with large language models](https://doi.org/10.1038/s41746-025-01840-7) | 2025 | 3 | 51 | npj Digital Medicine | Zifeng Wang, Lang Cao, Benjamin Danek, et al. |
| 7 | [AutoRepo: A general framework for multimodal LLM-based automated construction reporting](https://doi.org/10.1016/j.eswa.2024.124601) | 2024 | 4 | 97 | Expert Systems with Applications | Hongxu Pu, Xincong Yang, Jing Li, et al. |
| 8 | [LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics](https://doi.org/10.1109/tevc.2024.3497793) | 2024 | 3 | 86 | IEEE Transactions on Evolutionary Computation | Bas van Stein, Thomas Bäck |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 33 | 191403 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 16 | 102961 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 15 | 79472 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 4 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 14 | 33288 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 5 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 14 | 130802 | Machine Learning | Leo Breiman |
| 6 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 12 | 70534 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 7 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 11 | 52124 |  | Tianqi Chen, Carlos Guestrin |
| 8 | [G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences](https://doi.org/10.3758/bf03193146) | 2007 | 11 | 65767 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Albert-Georg Lang, et al. |
| 9 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 11 | 66931 | MIS Quarterly | Fred D. Davis |
| 10 | ["Why Should I Trust You?"](https://doi.org/10.1145/2939672.2939778) | 2016 | 10 | 16168 |  | Marco Túlio Ribeiro, Sameer Singh, Carlos Guestrin |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Game-based learning in early childhood education: a systematic review and meta-analysis](https://doi.org/10.3389/fpsyg.2024.1307881) | 2024 | 3 | 166 | Frontiers in Psychology | Manar Soud Alotaibi |
<!-- TRENDING-END -->
