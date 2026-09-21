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

Last update: 2026-09-21 11:40 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [UED Reconstruction Programme — Programme Synthesis: Mathematical Status, Derived Results, Open Closures, and Falsification Targets Across Papers 1–20](https://doi.org/10.5281/zenodo.22746782) | 2026 | 18 | 40 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 2 | [UED Reconstruction Programme — Paper 2: Ripple Dynamics in SVE](https://doi.org/10.5281/zenodo.22748610) | 2026 | 16 | 32 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 3 | [UED Reconstruction Programme — Paper 5: Persistence and Matter](https://doi.org/10.5281/zenodo.22760413) | 2026 | 14 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 4 | [UED Reconstruction Programme — Paper 1: Energetic Reconstruction of Classical Mechanics](https://doi.org/10.5281/zenodo.22747761) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 5 | [UED Reconstruction Programme — Paper 4: Detection, Photon Events, and Quantized Manifestation](https://doi.org/10.5281/zenodo.22749921) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 6 | [UED Reconstruction Programme — Paper 3: Light at the Source-Field-Observer Boundary](https://doi.org/10.5281/zenodo.22749381) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 7 | [UED Reconstruction Programme — Paper 9: ATT, Clocks, and Ordered Consequential Resolution](https://doi.org/10.5281/zenodo.22765395) | 2026 | 11 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 8 | [UED Reconstruction Programme — Paper 6: Atomic Configuration and Spectral Resolution](https://doi.org/10.5281/zenodo.22760590) | 2026 | 9 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 9 | [UED Reconstruction Programme — Paper 7: Electrical and Magnetic Response](https://doi.org/10.5281/zenodo.22760714) | 2026 | 7 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |
| 10 | [UED Reconstruction Programme — Paper 8: Energetic Reconstruction of Thermal and Statistical Consequence](https://doi.org/10.5281/zenodo.22763781) | 2026 | 7 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Sandeep J Chavan Sandeep J Chavan |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 116 | 132486 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 73 | 53192 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 54 | 30486 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 30 | 10223 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 25 | 3508 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 6 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 24 | 9195 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 20 | 34161 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Cross‐validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure](https://doi.org/10.1111/ecog.02881) | 2016 | 18 | 3142 | Ecography | David R. Roberts, Volker Bahn, Simone Ciuti, et al. |
| 9 | [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | 1986 | 17 | 31889 | Nature | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |
| 10 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 84735 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 25 | 3508 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 11 | 796 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 11 | 1026 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 4 | [Physics constrained neural collision operators for hard sphere surrogates and ab initio angle prediction in direct simulation Monte Carlo](https://doi.org/10.1063/5.0328463) | 2026 | 9 | 12 | Physics of Fluids | Ehsan Roohi, Ahmad Shoja-Sani, Stefan Stefanov |
| 5 | [Evaluation metrics and statistical tests for machine learning](https://doi.org/10.1038/s41598-024-56706-x) | 2024 | 6 | 1238 | Scientific Reports | Oona Rainio, Jarmo Teuho, Riku Klén |
| 6 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 6 | 3289 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 7 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 5 | 894 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 8 | [Application of Machine Learning Models in Social Sciences: Managing Nonlinear Relationships](https://doi.org/10.3390/encyclopedia4040118) | 2024 | 4 | 103 | Encyclopedia | Theodoros Kyriazos, Mary Poga |
| 9 | [Conformal Prediction: A Gentle Introduction](https://doi.org/10.1561/2200000101) | 2023 | 4 | 626 | Foundations and Trends® in Machine Learning | Anastasios N. Angelopoulos, Stephen Bates |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Physics constrained neural collision operators for hard sphere surrogates and ab initio angle prediction in direct simulation Monte Carlo](https://doi.org/10.1063/5.0328463) | 2026 | 9 | 12 | Physics of Fluids | Ehsan Roohi, Ahmad Shoja-Sani, Stefan Stefanov |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 26 | 33774 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 20 | 4466 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 18 | 2123 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 16 | 3843 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 14 | 1115 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3846 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 13 | 6587 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 12 | 1304 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 9 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 12 | 6586 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 10 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 747 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 16 | 3843 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3846 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 12 | 1304 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 12 | 6586 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 747 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 6 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 11 | 1549 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 7 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://doi.org/10.52202/075280-2997) | 2023 | 9 | 452 |  | Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, et al. |
| 8 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 9 | 702 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 9 | 2072 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1) | 2024 | 8 | 1609 | Frontiers of Computer Science | Lei Wang, Chen Ma, Xueyang Feng, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Leveraging synthetic trace generation of modeling operations for intelligent modeling assistants using large language models](https://doi.org/10.1016/j.infsof.2025.107806) | 2025 | 3 | 6 | Information and Software Technology | Vittoriano Muttillo, Claudio Di Sipio, Riccardo Rubei, et al. |
| 2 | [Software Model Evolution with Large Language Models: Experiments on Simulated, Public, and Industrial Datasets](https://doi.org/10.1109/icse55347.2025.00112) | 2025 | 3 | 7 |  | Christof Tinnes, Alisa Welter, Sven Apel |
| 3 | [Accurate and Consistent Graph Model Generation from Text with Large Language Models](https://doi.org/10.1109/models67397.2025.00018) | 2025 | 3 | 7 |  | Boqi Chen, Wei Ou, Bingzhou Zheng, et al. |
| 4 | [Toward a Symbiotic Approach Leveraging Generative AI for Model Driven Engineering](https://doi.org/10.1109/models58315.2023.00039) | 2023 | 3 | 18 |  | Vinay Kulkarni, Sreedhar Reddy, Souvik Barat, et al. |
| 5 | [On the use of large language models in model-driven engineering](https://doi.org/10.1007/s10270-025-01263-8) | 2025 | 6 | 52 | Software & Systems Modeling | Juri Di Rocco, Davide Di Ruscio, Claudio Di Sipio, et al. |
| 6 | [Towards using Few-Shot Prompt Learning for Automating Model Completion](https://doi.org/10.1109/icse-nier58687.2023.00008) | 2023 | 4 | 58 |  | Meriem Ben Chaaben, Loli Burgueño, Houari Sahraoui |
| 7 | [LLM Evaluators Recognize and Favor Their Own Generations](https://doi.org/10.52202/079017-2197) | 2024 | 3 | 61 |  | Arjun Panickssery, Samuel R. Bowman, Shi Feng |
| 8 | [Model Generation with LLMs: From Requirements to UML Sequence Diagrams](https://doi.org/10.1109/rew61692.2024.00044) | 2024 | 4 | 85 |  | Alessio Ferrari, Sallam Abualhaija, Chetan Arora |
| 9 | [Benchmarking and Defending against Indirect Prompt Injection Attacks on Large Language Models](https://doi.org/10.1145/3690624.3709179) | 2025 | 3 | 67 |  | Jingwei Yi, Yueqi Xie, Bin Zhu, et al. |
| 10 | [Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages](https://doi.org/10.1177/08944393241286471) | 2024 | 4 | 92 | Social Science Computer Review | Petter Törnberg |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 17 | 193526 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 13 | 105510 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 11 | 67584 | MIS Quarterly | Fred D. Davis |
| 4 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 11 | 80486 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 5 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 10 | 43824 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 6 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 10 | 71469 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 7 | [When to use and how to report the results of PLS-SEM](https://doi.org/10.1108/ebr-11-2018-0203) | 2018 | 9 | 26414 | European Business Review | Joseph F. Hair, Jeffrey J. Risher, Marko Sarstedt, et al. |
| 8 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 9 | 87742 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 9 | [Common Method Bias in PLS-SEM](https://doi.org/10.4018/ijec.2015100101) | 2015 | 8 | 9589 | International Journal of e-Collaboration | Ned Kock |
| 10 | [Scoping studies: towards a methodological framework](https://doi.org/10.1080/1364557032000119616) | 2005 | 8 | 37357 | International Journal of Social Research Methodology | Hilary Arksey, Lisa O’Malley |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 4 | 3508 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 6586 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [[Depreciated and replaced by V3] Solving Chess Completely: Residue Field Partitioning and Algebraic Varieties of Game-Theoretic Outcomes](https://doi.org/10.5281/zenodo.20593743) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 4 | [[Depreciated and replaced by V3] The Hubble Calibration Ratio and the Cosmological Constant: One Finite Covering Ladder](https://doi.org/10.5281/zenodo.21482856) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 5 | [[Depreciated and replaced by V3] What a Self Is: The Hard Problem and Binding Problem Resolved as the Fold Reaching Unison](https://doi.org/10.5281/zenodo.21483274) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 6 | [[Depreciated and replaced by V3] There Is No Nothing: One Machine-Checked Self-Proven Theorem, Zero Axioms, and the Uniquely Forced Fold](https://doi.org/10.5281/zenodo.21482734) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 7 | [[Depreciated and replaced by V3] SUPERSEDED HISTORICAL RECORD — Fold Protein Super Parity Development Lineage](https://doi.org/10.5281/zenodo.21482794) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 8 | [[Depreciated and replaced by V3] Entanglement Without Spookiness: Shared Origin, Product Structure, and Correlation Without a Travelling Signal](https://doi.org/10.5281/zenodo.21483218) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 9 | [[Depreciated and replaced by V3] Fold Go: Exact Counted Legality, Certified Solves, and Zero-Parameter Competitive Play](https://doi.org/10.5281/zenodo.21483328) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 10 | [[Depreciated and replaced by V3] Smithium: Element 126, the Doubly Magic Island at 126/184, and the First g-Block Chemistry](https://doi.org/10.5281/zenodo.21483101) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [[Depreciated and replaced by V3] Solving Chess Completely: Residue Field Partitioning and Algebraic Varieties of Game-Theoretic Outcomes](https://doi.org/10.5281/zenodo.20593743) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 2 | [[Depreciated and replaced by V3] The Hubble Calibration Ratio and the Cosmological Constant: One Finite Covering Ladder](https://doi.org/10.5281/zenodo.21482856) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 3 | [[Depreciated and replaced by V3] What a Self Is: The Hard Problem and Binding Problem Resolved as the Fold Reaching Unison](https://doi.org/10.5281/zenodo.21483274) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 4 | [[Depreciated and replaced by V3] There Is No Nothing: One Machine-Checked Self-Proven Theorem, Zero Axioms, and the Uniquely Forced Fold](https://doi.org/10.5281/zenodo.21482734) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 5 | [[Depreciated and replaced by V3] SUPERSEDED HISTORICAL RECORD — Fold Protein Super Parity Development Lineage](https://doi.org/10.5281/zenodo.21482794) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 6 | [[Depreciated and replaced by V3] Entanglement Without Spookiness: Shared Origin, Product Structure, and Correlation Without a Travelling Signal](https://doi.org/10.5281/zenodo.21483218) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 7 | [[Depreciated and replaced by V3] Fold Go: Exact Counted Legality, Certified Solves, and Zero-Parameter Competitive Play](https://doi.org/10.5281/zenodo.21483328) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 8 | [[Depreciated and replaced by V3] Smithium: Element 126, the Doubly Magic Island at 126/184, and the First g-Block Chemistry](https://doi.org/10.5281/zenodo.21483101) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 9 | [[Depreciated and replaced by V3] The Law Inside Trained Weights: The Fold Decode Campaign](https://doi.org/10.5281/zenodo.21483332) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
| 10 | [[Depreciated and replaced by V3] UnisonAI: A Computational Proof of Derived Law with Zero Trained Parameters](https://doi.org/10.5281/zenodo.21483329) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Maria Smith |
<!-- TRENDING-END -->
