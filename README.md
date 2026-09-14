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

Last update: 2026-09-14 11:26 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Readout Genesis Standalone Synthesis: Information Epistemic Foundation, Conditioned Agency, and Meta-Readout Governance](https://doi.org/10.5281/zenodo.21529456) | 2026 | 20 | 256 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 2 | [The Readout Condition: Distinguishability, Access, and Epistemic Warrant](https://doi.org/10.5281/zenodo.22301318) | 2026 | 16 | 117 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 3 | [When AI Expands Human Potential: Reflective Dissonance, Epistemic Agency, and Constraint](https://doi.org/10.5281/zenodo.19215748) | 2026 | 15 | 62 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 4 | [Written by AI. Still True. Knower Fetishism, Epistemic Pedigree, and the Human Face as a Bad Theory of Truth](https://doi.org/10.5281/zenodo.22301202) | 2026 | 14 | 114 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 5 | [Reciprocal rank fusion outperforms condorcet and individual rank learning methods](https://doi.org/10.1145/1571941.1572114) | 2009 | 12 | 702 |  | Gordon V. Cormack, Charles L. A. Clarke, Stefan Buettcher |
| 6 | [What a Zero Readout Certifies Zero as the failure locus of retained distinction](https://doi.org/10.5281/zenodo.21665100) | 2026 | 11 | 25 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 7 | [The Standalone Scholar: A Dual-Track Architecture for AI-Native Scholarship](https://doi.org/10.5281/zenodo.22163849) | 2026 | 11 | 54 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 8 | [The Probabilistic Relevance Framework: BM25 and Beyond](https://doi.org/10.1561/1500000019) | 2009 | 11 | 3160 | Foundations and Trends® in Information Retrieval | Stephen Robertson, Hugo Zaragoza |
| 9 | [A Survey on Conversational Recommender Systems](https://doi.org/10.1145/3453154) | 2021 | 10 | 414 | ACM Computing Surveys | Dietmar Jannach, Ahtsham Manzoor, Wanling Cai, et al. |
| 10 | [From Problem to Hypothesis: Dynamic Semantic Mobility, Bounded Knowers, and the Readout-Discriminable Hypothesis Space](https://doi.org/10.5281/zenodo.22307148) | 2026 | 9 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 90 | 131828 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 46 | 52810 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 27 | 30317 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 15 | 3357 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 15 | 34004 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 14 | 10107 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 7 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 14 | 24549 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 8 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 13 | 9137 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 9 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 13 | 101723 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 10 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 12 | 10070 | Nature Machine Intelligence | Cynthia Rudin |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 15 | 3357 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 8 | 986 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13546 | OASIcs : OpenAccess Series in Informatics | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 4 | [Interpretable machine learning model for new-onset atrial fibrillation prediction in critically ill patients: a multi-center study](https://doi.org/10.1186/s13054-024-05138-0) | 2024 | 4 | 127 | Critical Care | Chengjian Guan, A. Gong, Yan Zhao, et al. |
| 5 | [Hyperspectral Identification of Milk Adulteration Using Advance Deep Learning](https://doi.org/10.1109/access.2024.3504334) | 2024 | 3 | 24 | IEEE Access | Muhammad Aqeel, Ahmed Sohaib, Muhammad Iqbal, et al. |
| 6 | [Polymer Informatics at Scale with Multitask Graph Neural Networks](https://doi.org/10.1021/acs.chemmater.2c02991) | 2023 | 3 | 116 | Chemistry of Materials | Rishi Gurnani, Christopher Kuenneth, Aubrey Toland, et al. |
| 7 | [polyBERT: a chemical language model to enable fully machine-driven ultrafast polymer informatics](https://doi.org/10.1038/s41467-023-39868-6) | 2023 | 3 | 266 | Nature Communications | Christopher Kuenneth, Rampi Ramprasad |
| 8 | [Practical guide to SHAP analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 3 | 779 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 9 | [Hyperparameter optimization: Foundations, algorithms, best practices, and open challenges](https://doi.org/10.1002/widm.1484) | 2023 | 3 | 907 | Wiley Interdisciplinary Reviews Data Mining and Knowledge Discovery | Bernd Bischl, Martin Binder, Michel Lang, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Hyperspectral Identification of Milk Adulteration Using Advance Deep Learning](https://doi.org/10.1109/access.2024.3504334) | 2024 | 3 | 24 | IEEE Access | Muhammad Aqeel, Ahmed Sohaib, Muhammad Iqbal, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 28 | 4396 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 2 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 20 | 33594 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 3 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 19 | 2014 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 16 | 3788 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 15 | 1054 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 13 | 3809 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 12 | 1518 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 8 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 2041 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 9 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 708 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 10 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 11 | 971 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 16 | 3788 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 13 | 3809 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 12 | 1518 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 12 | 2041 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 11 | 708 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 6 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 11 | 971 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 7 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 10 | 588 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 8 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 6474 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 9 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 9 | 492 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 10 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 9 | 1267 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Toward a Symbiotic Approach Leveraging Generative AI for Model Driven Engineering](https://doi.org/10.1109/models58315.2023.00039) | 2023 | 3 | 18 |  | Vinay Kulkarni, Sreedhar Reddy, Souvik Barat, et al. |
| 2 | [Large Language Model Performance and Clinical Reasoning Tasks](https://doi.org/10.1001/jamanetworkopen.2026.4003) | 2026 | 4 | 31 | JAMA Network Open | Arya S. Rao, Kaiz P. Esmail, Richard S. Lee, et al. |
| 3 | [On the use of large language models in model-driven engineering](https://doi.org/10.1007/s10270-025-01263-8) | 2025 | 6 | 50 | Software & Systems Modeling | Juri Di Rocco, Davide Di Ruscio, Claudio Di Sipio, et al. |
| 4 | [Towards using Few-Shot Prompt Learning for Automating Model Completion](https://doi.org/10.1109/icse-nier58687.2023.00008) | 2023 | 4 | 57 |  | Meriem Ben Chaaben, Loli Burgueño, Houari Sahraoui |
| 5 | [Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment](https://doi.org/10.1093/jamia/ocae254) | 2024 | 4 | 81 | Journal of the American Medical Informatics Association | Thomas Savage, John Wang, Robert J. Gallo, et al. |
| 6 | [In praise of empathic AI](https://doi.org/10.1016/j.tics.2023.12.003) | 2023 | 4 | 85 | Trends in Cognitive Sciences | Michael Inzlicht, C. Daryl Cameron, Jason D’Cruz, et al. |
| 7 | [SGLang: Efficient Execution of Structured Language Model Programs](https://doi.org/10.52202/079017-2000) | 2024 | 4 | 94 |  | Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, et al. |
| 8 | [Model Generation with LLMs: From Requirements to UML Sequence Diagrams](https://doi.org/10.1109/rew61692.2024.00044) | 2024 | 3 | 81 |  | Alessio Ferrari, Sallam Abualhaija, Chetan Arora |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 20 | 192846 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 15 | 80172 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 3 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 14 | 104713 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 4 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 13 | 67340 | MIS Quarterly | Fred D. Davis |
| 5 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 11 | 131828 | Machine Learning | Leo Breiman |
| 6 | [Cognitive Load During Problem Solving: Effects on Learning](https://doi.org/10.1207/s15516709cog1202_4) | 1988 | 9 | 9327 | Cognitive Science | John Sweller |
| 7 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 9 | 35878 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 8 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 9 | 52810 |  | Tianqi Chen, Carlos Guestrin |
| 9 | [Becoming a Self-Regulated Learner: An Overview](https://doi.org/10.1207/s15430421tip4102_2) | 2002 | 8 | 7152 | Theory Into Practice | Barry J. Zimmerman |
| 10 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 8 | 33498 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 6 | 6474 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [The Aegis Forward-Base Burner: Q_E Closure, Plug Requirement, and Mirror Confinement in an Islanded Low-Neutron D–³He Tandem Mirror](https://doi.org/10.5281/zenodo.22645693) | 2026 | 5 | 100 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, G L Kulcinski |
| 3 | [An Integrated High-Field REBCO Conductor and Winding System for Compact Fusion Magnets: Strain-First Design, Bore-Resolved Mechanics, and a Two-Machine Feasibility Map — Reproducible Code and Data](https://doi.org/10.5281/zenodo.21842514) | 2026 | 5 | 306 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, Carl Frederick Weggel, J.V. Minervini |
| 4 | [Physics-Informed AI and Quantum Technologies for Certifiable Real-Time Control of Compact Fusion Generators — reproducibility deposit (code, data, figures)](https://doi.org/10.5281/zenodo.21842371) | 2026 | 5 | 352 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford |
| 5 | [AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking](https://doi.org/10.3390/soc15010006) | 2025 | 5 | 946 | Societies | Michael Gerlich |
| 6 | [The MetroVolt Data-Center Burner: Direct-DC Campus Power, Q_E Closure, and the Plug Requirement in a Low-Neutron D–³He Tandem Mirror](https://doi.org/10.5281/zenodo.22645695) | 2026 | 4 | 100 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, G L Kulcinski |
| 7 | [GPT detectors are biased against non-native English writers](https://doi.org/10.1016/j.patter.2023.100779) | 2023 | 4 | 587 | Patterns | Weixin Liang, Mert Yüksekgönül, Yining Mao, et al. |
| 8 | [Social gaming: A systematic review](https://doi.org/10.1016/j.chb.2023.107851) | 2023 | 3 | 67 | Computers in Human Behavior | David Gonçalves, Pedro Pais, Kathrin Gerling, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Social gaming: A systematic review](https://doi.org/10.1016/j.chb.2023.107851) | 2023 | 3 | 67 | Computers in Human Behavior | David Gonçalves, Pedro Pais, Kathrin Gerling, et al. |
<!-- TRENDING-END -->
