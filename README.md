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

Last update: 2026-04-13 07:52 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [THE THREE COMPRESSIONS: Lossy, Predatory, and Witness — A Semiotic Thermodynamics](https://doi.org/10.5281/zenodo.19053469) | 2026 | 15 | 106 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil, Rex Fraction |
| 2 | [CoLaba.Space — Governance & Participation Charter](https://doi.org/10.5281/zenodo.19089937) | 2026 | 10 | 20 | Zenodo (CERN European Organization for Nuclear Research) | Andrey A. Yudin |
| 3 | [CoLaba.Space — White Paper](https://doi.org/10.5281/zenodo.19089146) | 2026 | 9 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Andrey A. Yudin |
| 4 | [Development · Research · Deployment (DRD): conceptual and methodological frame](https://doi.org/10.5281/zenodo.19077562) | 2026 | 9 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Andrey A. Yudin |
| 5 | [Logarithmic Density, Metric Correction, and the Chiral Spectral Obstruction](https://doi.org/10.5281/zenodo.19230354) | 2026 | 9 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Pavel Kramarenko-Byrd |
| 6 | [The Encyclotron: The First Reproducible Instrument for Measuring Scholarly Fidelity in the Summarizer Layer (EA-ENCYCLOTRON-01)](https://doi.org/10.5281/zenodo.19474724) | 2026 | 9 | 34 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 7 | [Abortion and Embodiment](https://doi.org/10.1080/15265161.2025.2457714) | 2025 | 8 | 14 | The American Journal of Bioethics | Laura D. Hermer |
| 8 | [Domain Modeling Framework (DMF)](https://doi.org/10.5281/zenodo.19089055) | 2026 | 8 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Andrey A. Yudin |
| 9 | [Meaning Feudalism: A Semantic Economic Analysis of 'AI Agent Traps' (Franklin et al., Google DeepMind, 2026)](https://doi.org/10.5281/zenodo.19487009) | 2026 | 8 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 10 | [Cognitive Ergonomics Framework (CEF): Open Engineering Specification](https://doi.org/10.5281/zenodo.19088998) | 2026 | 7 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Andrey A. Yudin |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 97 | 122058 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 52 | 45913 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 28 | 27999 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 28 | 32283 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 19 | 30223 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 18 | 8189 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 7 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 17 | 15735 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 8 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 16 | 51011 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 9 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 15 | 22571 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 10 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 1636 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 1636 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 8 | 698 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 13177 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 4 | [Comprehensive Analysis of Random Forest and XGBoost Performance with SMOTE, ADASYN, and GNUS Under Varying Imbalance Levels](https://doi.org/10.3390/technologies13030088) | 2025 | 5 | 127 | Technologies | Mehdi Imani, Ali Beikmohammadi, Hamid R. Arabnia |
| 5 | [Enhancing K-nearest neighbor algorithm: a comprehensive review and performance analysis of modifications](https://doi.org/10.1186/s40537-024-00973-y) | 2024 | 5 | 365 | Journal Of Big Data | Rajib Kumar Halder, Mohammed Nasir Uddin, Md. Ashraf Uddin, et al. |
| 6 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 452 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 7 | [Recent Advances in Machine Learning‐Assisted Multiscale Design of Energy Materials](https://doi.org/10.1002/aenm.202403876) | 2024 | 4 | 132 | Advanced Energy Materials | Bohayra Mortazavi |
| 8 | [Learning local equivariant representations for large-scale atomistic dynamics](https://doi.org/10.1038/s41467-023-36329-y) | 2023 | 4 | 580 | Nature Communications | Albert Musaelian, Simon Batzner, Anders Johansson, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 11 | 31717 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 3036 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 9 | 897 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 4 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 8 | 361 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 5 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1209 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 3013 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://doi.org/10.1093/bioinformatics/btz682) | 2019 | 8 | 6733 | Bioinformatics | Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2257 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 2843 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 10 | [Augmenting large language models with chemistry tools](https://doi.org/10.1038/s42256-024-00832-8) | 2024 | 6 | 511 | Nature Machine Intelligence | Andres M. Bran, Sam Cox, Oliver Schilter, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 9 | 897 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 2 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 8 | 361 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 3 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1209 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 3013 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2257 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 6 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 2843 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 7 | [Augmenting large language models with chemistry tools](https://doi.org/10.1038/s42256-024-00832-8) | 2024 | 6 | 511 | Nature Machine Intelligence | Andres M. Bran, Sam Cox, Oliver Schilter, et al. |
| 8 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 5 | 117 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 9 | [How Can Recommender Systems Benefit from Large Language Models: A Survey](https://doi.org/10.1145/3678004) | 2024 | 5 | 147 | ACM Transactions on Information Systems | Jianghao Lin, Xinyi Dai, Yunjia Xi, et al. |
| 10 | [A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation](https://doi.org/10.1038/s41746-025-01670-7) | 2025 | 5 | 153 | npj Digital Medicine | Elham Asgari, Nina Montaña-Brown, Magda Dubois, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [FaultExplainer: Leveraging large language models for interpretable fault detection and diagnosis](https://doi.org/10.1016/j.compchemeng.2025.109152) | 2025 | 3 | 12 | Computers & Chemical Engineering | Abdullah Khan, Rahul Nahar, Hao Chen, et al. |
| 2 | [Assessing the performance of ChatGPT and Bard/Gemini against radiologists for Prostate Imaging-Reporting and Data System classification based on prostate multiparametric MRI text reports](https://doi.org/10.1093/bjr/tqae236) | 2024 | 3 | 21 | British Journal of Radiology | Kang‐Lung Lee, Dimitri A. Kessler, Iztok Caglič, et al. |
| 3 | [Comparing Diagnostic Accuracy of Clinical Professionals and Large Language Models: Systematic Review and Meta-Analysis](https://doi.org/10.2196/64963) | 2025 | 4 | 29 | JMIR Medical Informatics | Guxue Shan, Xiaonan Chen, Chen Wang, et al. |
| 4 | [Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior](https://doi.org/10.3389/frai.2025.1622292) | 2025 | 3 | 23 | Frontiers in Artificial Intelligence | Dang Anh-Hoang, Vu Tran, Le-Minh Nguyen |
| 5 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 4 | 59 |  | Wei-Lin Chiang, Joseph Gonzalez, Dacheng Li, et al. |
| 6 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 5 | 74 |  | Sandhini Agarwal, Diogo Almeida, Amanda Askell, et al. |
| 7 | [Medical foundation large language models for comprehensive text analysis and beyond](https://doi.org/10.1038/s41746-025-01533-1) | 2025 | 3 | 45 | npj Digital Medicine | Qianqian Xie, Qingyu Chen, Aokun Chen, et al. |
| 8 | [The Clinicians’ Guide to Large Language Models: A General Perspective With a Focus on Hallucinations](https://doi.org/10.2196/59823) | 2025 | 4 | 73 | Interactive Journal of Medical Research | Dimitri Roustan, François Bastardot |
| 9 | [Next-generation agentic AI for transforming healthcare](https://doi.org/10.1016/j.infoh.2025.03.001) | 2025 | 3 | 71 | Informatics and Health | Nalan Karunanayake |
| 10 | [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://doi.org/10.52202/068431-1189) | 2022 | 3 | 73 |  | Tri Dao, Stefano Ermon, Dan Fu, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 12 | 87847 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 12 | 175688 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 11 | 74057 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 4 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 10 | 122058 | Machine Learning | Leo Breiman |
| 5 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 9 | 103086 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 6 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 7 | 30994 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 7 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 7 | 45913 |  | Tianqi Chen, Carlos Guestrin |
| 8 | [Statistical Power Analysis for the Behavioral Sciences](https://doi.org/10.4324/9780203771587) | 2013 | 6 | 22642 |  | Jacob Cohen |
| 9 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 6 | 41071 | MIS Quarterly | Venkatesh, Jeremy Morris, Davis, et al. |
| 10 | [Diagnostic and Statistical Manual of Mental Disorders](https://doi.org/10.1176/appi.books.9780890425596) | 2013 | 6 | 112085 | American Psychiatric Association eBooks | Annette Lolk |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Resonance as Civilizational Architecture: A Unified Theory of Koku, BBDDH, PRT, and Hikari Currency v1.1 — From the Structure of the Universe to the Structure of Healing: One Principle](https://doi.org/10.5281/zenodo.19305649) | 2026 | 5 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 2 | [GKU Cosmology v2](https://doi.org/10.5281/zenodo.19097250) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 3 | [The use of serious games for psychological education and training: a systematic review](https://doi.org/10.3389/feduc.2025.1511729) | 2025 | 3 | 17 | Frontiers in Education | Antonio Pio Facchino, Daniela Marchetti, Marco Colasanti, et al. |
| 4 | [Measuring the EU Member States RDI and Technology Transfer Process Efficiency: A DEA Approach](https://doi.org/10.24818/18423264/57.1.23.13) | 2023 | 2 | 4 | ECONOMIC COMPUTATION AND ECONOMIC CYBERNETICS STUDIES AND RESEARCH | Simona Cătălina Ștefan, Ion Popa, SIMION CEZAR-PETRE, et al. |
| 5 | [The Brain-Body Dissociative Disconnection Hypothesis (BBDDH)](https://doi.org/10.5281/zenodo.19105964) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 6 | [Evolutionary mechanisms that promote cooperation may not promote social welfare](https://doi.org/10.1098/rsif.2024.0547) | 2024 | 2 | 36 | Journal of The Royal Society Interface | The Anh Han, Manh Hong Duong, Matjaž Perc |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Resonance as Civilizational Architecture: A Unified Theory of Koku, BBDDH, PRT, and Hikari Currency v1.1 — From the Structure of the Universe to the Structure of Healing: One Principle](https://doi.org/10.5281/zenodo.19305649) | 2026 | 5 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 2 | [GKU Cosmology v2](https://doi.org/10.5281/zenodo.19097250) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 3 | [Measuring the EU Member States RDI and Technology Transfer Process Efficiency: A DEA Approach](https://doi.org/10.24818/18423264/57.1.23.13) | 2023 | 2 | 4 | ECONOMIC COMPUTATION AND ECONOMIC CYBERNETICS STUDIES AND RESEARCH | Simona Cătălina Ștefan, Ion Popa, SIMION CEZAR-PETRE, et al. |
| 4 | [The Brain-Body Dissociative Disconnection Hypothesis (BBDDH)](https://doi.org/10.5281/zenodo.19105964) | 2026 | 2 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Yoshimitsu Katayama |
| 5 | [The use of serious games for psychological education and training: a systematic review](https://doi.org/10.3389/feduc.2025.1511729) | 2025 | 3 | 17 | Frontiers in Education | Antonio Pio Facchino, Daniela Marchetti, Marco Colasanti, et al. |
| 6 | [An evolutionary game approach for private sectors’ behavioral strategies in China’s green energy public–private partnership projects](https://doi.org/10.1016/j.egyr.2021.09.201) | 2021 | 2 | 22 | Energy Reports | Jicheng Liu, Jing Yu, Yu Yin, et al. |
| 7 | [Paradigm shifts and the interplay between state, business and civil sectors](https://doi.org/10.1098/rsos.160753) | 2016 | 2 | 32 | Royal Society Open Science | Sara Encarnação, Fernando P. Santos, Francisco C. Santos, et al. |
| 8 | [Factors affecting firms’ green technology innovation: an evolutionary game based on prospect theory](https://doi.org/10.1007/s10661-022-10835-w) | 2022 | 2 | 35 | Environmental Monitoring and Assessment | Chuang Li, Zhijia Wang, Liping Wang |
| 9 | [Evolutionary mechanisms that promote cooperation may not promote social welfare](https://doi.org/10.1098/rsif.2024.0547) | 2024 | 2 | 36 | Journal of The Royal Society Interface | The Anh Han, Manh Hong Duong, Matjaž Perc |
<!-- TRENDING-END -->
