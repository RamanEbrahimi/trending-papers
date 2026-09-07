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

Last update: 2026-09-07 11:16 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Closure of a Deuterium–Helium-3 Tandem Mirror with Direct Conversion: A 35-Simulation Validation Package](https://doi.org/10.5281/zenodo.21746479) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, G.L. Kulcinski |
| 2 | [Hyperion: A Simulation and Validation Data Package for a Deuterium–Tritium Spherical-Tokamak Tritium / Helium-3 Breeder](https://doi.org/10.5281/zenodo.21746157) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford |
| 3 | [Direct Energy Conversion for a D-3He Magnetic-Mirror Burner: the Electron Channel is the Larger Axial Stream, and a Quasineutral Expander Can Recover It — Reproducible Code and Data](https://doi.org/10.5281/zenodo.21842864) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, G.L. Kulcinski |
| 4 | [Physics-Informed AI and Quantum Technologies for Certifiable Real-Time Control of Compact Fusion Generators — reproducibility deposit (code, data, figures)](https://doi.org/10.5281/zenodo.21842371) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford |
| 5 | [An Integrated High-Field REBCO Conductor and Winding System for Compact Fusion Magnets: Strain-First Design, Bore-Resolved Mechanics, and a Two-Machine Feasibility Map — Reproducible Code and Data](https://doi.org/10.5281/zenodo.21842514) | 2026 | 38 | 76 | Zenodo (CERN European Organization for Nuclear Research) | Priyanca Ford, Carl Frederick Weggel, J.V. Minervini |
| 6 | [The Kronos Integrated Platform: A Spherical-Tokamak Breeder and a Deuterium-Helium-3 Burner as One Strategic-Materials and Power Architecture](https://doi.org/10.5281/zenodo.22132156) | 2026 | 37 | 86 | OSF Preprints (OSF Preprints) | Priyanca Ford, G L Kulcinski |
| 7 | [Readout Genesis Standalone Synthesis: Information Epistemic Foundation, Conditioned Agency, and Meta-Readout Governance](https://doi.org/10.5281/zenodo.21529456) | 2026 | 20 | 245 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 8 | [The Readout Condition: Distinguishability, Access, and Epistemic Warrant](https://doi.org/10.5281/zenodo.22301318) | 2026 | 17 | 117 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 9 | [Written by AI. Still True. Knower Fetishism, Epistemic Pedigree, and the Human Face as a Bad Theory of Truth](https://doi.org/10.5281/zenodo.22301202) | 2026 | 16 | 114 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |
| 10 | [When AI Expands Human Potential: Reflective Dissonance, Epistemic Agency, and Constraint](https://doi.org/10.5281/zenodo.19215748) | 2026 | 13 | 56 | Zenodo (CERN European Organization for Nuclear Research) | Yaoharee Lahtee |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 44 | 131352 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 25 | 52466 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 12 | 33948 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 11 | 30191 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 10 | 9991 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 8 | 32456 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 8 | 101482 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 8 | [Commentary: The Materials Project: A materials genome approach to accelerating materials innovation](https://doi.org/10.1063/1.4812323) | 2013 | 7 | 13168 | APL Materials | Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, et al. |
| 9 | [Double/debiased machine learning for treatment and structural parameters](https://doi.org/10.1111/ectj.12097) | 2017 | 6 | 2792 | Econometrics Journal | Victor Chernozhukov, Denis Chetverikov, Mert Demirer, et al. |
| 10 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 6 | 84282 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 5 | 780 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 5 | 3213 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 4 | 274 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |
| 4 | [Machine Learning Descriptors for Data‐Driven Catalysis Study](https://doi.org/10.1002/advs.202301020) | 2023 | 3 | 149 | Advanced Science | Li-Hui Mou, TianTian Han, Pieter E. S. Smith, et al. |
| 5 | [Explainable artificial intelligence: A survey of needs, techniques, applications, and future direction](https://doi.org/10.1016/j.neucom.2024.128111) | 2024 | 3 | 213 | Neurocomputing | Melkamu Abay Mersha, Khang Nhứt Lâm, Joseph Wood, et al. |
| 6 | [The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts](https://doi.org/10.1021/acscatal.2c05426) | 2023 | 3 | 318 | ACS Catalysis | Richard Tran, Janice Lan, Muhammed Shuaibi, et al. |
| 7 | [A Survey of Decision Trees: Concepts, Algorithms, and Applications](https://doi.org/10.1109/access.2024.3416838) | 2024 | 3 | 344 | IEEE Access | Ibomoiye Domor Mienye, Nobert Jere |
| 8 | [Chemprop: A Machine Learning Package for Chemical Property Prediction](https://doi.org/10.1021/acs.jcim.3c01250) | 2023 | 3 | 609 | Journal of Chemical Information and Modeling | Esther Heid, Kevin P. Greenman, Yunsie Chung, et al. |
| 9 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 3 | 676 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 10 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 3 | 871 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Machine-Learning-Based High-Resolution Earthquake Catalog For the 2016-2017 Central Italy Sequence](https://doi.org/10.5281/zenodo.4736089) | 2021 | 3 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Yen Joe Tan, F. Waldhauser, William L. Ellsworth |
| 2 | [Evaluating Predictive Accuracy in Asymmetric Catalysis: A Machine Learning Perspective on Local Reaction Space](https://doi.org/10.1021/acscatal.5c01051) | 2025 | 2 | 6 | ACS Catalysis | Isaiah O. Betinol, Aleksandra Demchenko, Jolene P. Reid |
| 3 | [Battery Life Prediction With Scarce Data Using Physics-Informed Data Generation and Adaptive Autoencoder](https://doi.org/10.1109/tte.2025.3626389) | 2025 | 2 | 19 | IEEE Transactions on Transportation Electrification | Song Zhang, Mengru Liu, Ruohan Guo, et al. |
| 4 | [Forecasting Hospital Readmissions with Machine Learning](https://doi.org/10.3390/healthcare10060981) | 2022 | 2 | 26 | Healthcare | Panagiotis Michailidis, Athanasia Dimitriadou, Théophilos Papadimitriou, et al. |
| 5 | [Evaluation of Machine Learning Models on Electrochemical CO2 Reduction Using Human Curated Datasets](https://doi.org/10.1021/acssuschemeng.2c02941) | 2022 | 2 | 32 | ACS Sustainable Chemistry & Engineering | Brianna R. Farris, Tevin Niang-Trost, Michael S. Branicky, et al. |
| 6 | [Analysis of photocatalytic CO 2 reduction over MOFs using machine learning](https://doi.org/10.1039/d3ta07001h) | 2024 | 2 | 36 | Journal of Materials Chemistry A | Simay Özsoysal, Burcu Oral, Ramazan Yıldırım |
| 7 | [Discrepancies and error evaluation metrics for machine learning interatomic potentials](https://doi.org/10.1038/s41524-023-01123-3) | 2023 | 2 | 55 | npj Computational Materials | Yunsheng Liu, Xingfeng He, Yifei Mo |
| 8 | [Large‐Scale Fracture Systems Are Permeable Pathways for Fault Activation During Hydraulic Fracturing](https://doi.org/10.1029/2020jb020311) | 2021 | 3 | 84 | Journal of Geophysical Research Solid Earth | Nadine Igonin, James P. Verdon, J. M. Kendall, et al. |
| 9 | [Effective hospital readmission prediction models using machine-learned features](https://doi.org/10.1186/s12913-022-08748-y) | 2022 | 2 | 58 | BMC Health Services Research | Sacha E. Davis, Jin Zhang, Ilbin Lee, et al. |
| 10 | [Searches for the BSM scenarios at the LHC using decision tree-based machine learning algorithms: a comparative study and review of random forest, AdaBoost, XGBoost and LightGBM frameworks](https://doi.org/10.1140/epjs/s11734-024-01308-x) | 2024 | 2 | 65 | The European Physical Journal Special Topics | Arghya Choudhury, Arpita Mondal, Subhadeep Sarkar |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 25 | 1837 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 25 | 3741 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 18 | 4307 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 4 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 17 | 966 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 3772 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 16 | 6453 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 7 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.18653/v1/n19-1423) | 2019 | 15 | 33468 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 8 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 14 | 923 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 13 | 2748 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 12 | 478 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 25 | 3741 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 3772 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 14 | 923 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 4 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 13 | 2748 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 5 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 12 | 478 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 6 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 12 | 648 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 7 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 2001 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 11 | 3798 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 9 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 10 | 2545 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 10 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 9 | 6358 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants](https://doi.org/10.18653/v1/2024.acl-long.44) | 2024 | 4 | 43 |  | Lucas Bandarkar, Davis Liang, Benjamin Müller, et al. |
| 2 | [LLM-assisted systematic review of large language models in clinical medicine](https://doi.org/10.1038/s41591-026-04229-5) | 2026 | 4 | 50 | Nature Medicine | Sully F. Chen, Anton Alyakin, Andreas Seas, et al. |
| 3 | [Assessment of Large Language Models in Clinical Reasoning: A Novel Benchmarking Study](https://doi.org/10.1056/aidbp2500120) | 2025 | 4 | 50 | NEJM AI | Liam G. McCoy, Rajiv Swamy, Nidhish Sagar, et al. |
| 4 | [Roles and potential of Large language models in healthcare: A comprehensive review](https://doi.org/10.1016/j.bj.2025.100868) | 2025 | 3 | 86 | Biomedical Journal | Chi‐Hung Lin, Chang‐Fu Kuo |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 39 | 192159 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 21 | 131352 | Machine Learning | Leo Breiman |
| 3 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 19 | 103820 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 4 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 16 | 52466 |  | Tianqi Chen, Carlos Guestrin |
| 5 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 16 | 70854 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 6 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 15 | 35738 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 7 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 15 | 67197 | MIS Quarterly | Fred D. Davis |
| 8 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 15 | 79851 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 9 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 11 | 18899 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |
| 10 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 11 | 33392 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking](https://doi.org/10.3390/soc15010006) | 2025 | 5 | 919 | Societies | Michael Gerlich |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 5 | 6358 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
<!-- TRENDING-END -->
