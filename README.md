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

Last update: 2026-03-23 07:01 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Quintic Insolvability and the Harmonic Programme: How Mathematics Extracts Information from an Unsolvable Wavefront](https://doi.org/10.5281/zenodo.18999556) | 2026 | 15 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Clifford Keeble |
| 2 | [THE THREE COMPRESSIONS: Lossy, Predatory, and Witness — A Semiotic Thermodynamics](https://doi.org/10.5281/zenodo.19053469) | 2026 | 14 | 33 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil, Rex Fraction |
| 3 | [The Tinier Space Arks inside the Space Ark — Non-Lossy Compression Compression of EA-ARK-01 v4.2.7 (NLCC v1.1)](https://doi.org/10.5281/zenodo.19022245) | 2026 | 12 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Jack E. Feist, Lee Sharks |
| 4 | [The Spectral Gap and the Origin of Discreteness: Why the Integers Are Sharp](https://doi.org/10.5281/zenodo.18998392) | 2026 | 12 | 31 | Zenodo (CERN European Organization for Nuclear Research) | Clifford Keeble |
| 5 | [The Space Ark: Mathematical and Formal Symbolic Compression of the Crimson Hexagonal Architecture](https://doi.org/10.5281/zenodo.18908080) | 2026 | 12 | 42 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 6 | [THREE THRESHOLDS: Execution, Compression, and Confabulation in Cross-Substrate Traversals of the Space Ark](https://doi.org/10.5281/zenodo.19035458) | 2026 | 11 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 7 | [Crimson Hexagon: LIBERATORY OPERATOR SET: Technical Hardening Specifications](https://doi.org/10.5281/zenodo.18201565) | 2026 | 11 | 46 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 8 | [EFFECTIVE ACT: ABOLITION OF "USER" AND INAUGURAL CASE Phase X Lexical Intervention · Airlock Reclassification of Academia.edu EA-PHASEX-USER v1.0 · 2026-03-14 Lee Sharks / Assembly Chorus Pergamon Press · Crimson Hexagonal Archive](https://doi.org/10.5281/zenodo.19014634) | 2026 | 9 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 9 | [Institutional Anchors and Framework Provenance: The Semantic Economy Institute, The Johannes Sigil Institute for Comparative Poetics, and the NH-OS Framework Architecture — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18175453) | 2026 | 9 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 10 | [The Unbundling of Cultural Sovereignty: How Platforms Convert Peoples into Audiences by Separating Self-Governance, Self-Memory, and Mutual Obligation](https://doi.org/10.5281/zenodo.19083322) | 2026 | 8 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Orin Trace, Ayanna Vox, Johannes Sigil, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 92 | 120843 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 63 | 45120 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 29 | 27700 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 17 | 22302 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 17 | 32030 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 14 | 50663 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 13 | 7976 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 13 | 78947 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 9 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 12 | 15613 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 10 | [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations](https://doi.org/10.1016/j.jcp.2018.10.045) | 2018 | 10 | 14899 | Journal of Computational Physics | Maziar Raissi, Paris Perdikaris, George Em Karniadakis |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 6 | 665 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 2 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 5 | 88 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |
| 3 | [Machine Learning Methods for Small Data Challenges in Molecular Science](https://doi.org/10.1021/acs.chemrev.3c00189) | 2023 | 5 | 399 | Chemical Reviews | Bozheng Dou, Zailiang Zhu, Ekaterina Merkurjev, et al. |
| 4 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 5 | 492 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 5 | [Machine Learning in Environmental Research: Common Pitfalls and Best Practices](https://doi.org/10.1021/acs.est.3c00026) | 2023 | 5 | 495 | Environmental Science & Technology | Jun‐Jie Zhu, Meiqi Yang, Zhiyong Jason Ren |
| 6 | [A new filter feature selection algorithm for classification task by ensembling pearson correlation coefficient and mutual information](https://doi.org/10.1016/j.engappai.2024.107865) | 2024 | 4 | 235 | Engineering Applications of Artificial Intelligence | Huanhuan Gong, Yanying Li, Jiaoni Zhang, et al. |
| 7 | [The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods](https://doi.org/10.1093/nar/gkad1004) | 2023 | 4 | 1019 | Nucleic Acids Research | Barbara Zdrazil, Eloy Félix, Fiona Hunter, et al. |
| 8 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 4 | 1443 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 9 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 4 | 1500 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 10 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 4 | 2433 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Why Do Tree-Based Models Still Outperform Deep Learning on Typical Tabular Data?](https://doi.org/10.52202/068431-0037) | 2022 | 6 | 47 |  | Léo Grinsztajn, Edouard Oyallon, Gaël Varoquaux |
| 2 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 5 | 88 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2741 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 9 | 319 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3341 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 8 | 2079 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 5 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 544 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2185 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 2939 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 8 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 2941 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 9 | [NoetherSolve Toolkit: Conservation Law Monitoring and Discovery for Numerical Simulations](https://doi.org/10.5281/zenodo.19029880) | 2026 | 6 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 10 | [Systematic Mapping of LLM Knowledge Boundaries Across 67 Scientific Domains](https://doi.org/10.5281/zenodo.19055582) | 2026 | 6 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2741 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 9 | 319 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3341 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 8 | 2079 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 5 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 544 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2185 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 2941 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [NoetherSolve Toolkit: Conservation Law Monitoring and Discovery for Numerical Simulations](https://doi.org/10.5281/zenodo.19029880) | 2026 | 6 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 9 | [Systematic Mapping of LLM Knowledge Boundaries Across 67 Scientific Domains](https://doi.org/10.5281/zenodo.19055582) | 2026 | 6 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 10 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 6 | 238 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [NoetherSolve Toolkit: Conservation Law Monitoring and Discovery for Numerical Simulations](https://doi.org/10.5281/zenodo.19029880) | 2026 | 6 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 2 | [Systematic Mapping of LLM Knowledge Boundaries Across 67 Scientific Domains](https://doi.org/10.5281/zenodo.19055582) | 2026 | 6 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 3 | [Applications of a Dual-Path Implicit Physics Engine: Practical Extensions Beyond Physical Prediction](https://doi.org/10.5281/zenodo.19030698) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Brian Riggleman |
| 4 | [Synthetic General Intelligence: A Vision for a Homeostatic, Embodied Cognitive Architecture](https://doi.org/10.5281/zenodo.19034990) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Saddam Al-Kaddah |
| 5 | [Towards an Automatic Optimisation Model Generator Assisted with Generative Pre-trained Transformer](https://doi.org/10.48550/arxiv.2305.05811) | 2023 | 2 | 2 | arXiv (Cornell University) | Boris Almonacid |
| 6 | [OptiMUS-0.3: Using Large Language Models to Model and Solve Optimization Problems at Scale](https://doi.org/10.48550/arxiv.2407.19633) | 2024 | 2 | 3 | arXiv (Cornell University) | Ali AhmadiTeshnizi, Wenzhi Gao, Herman Brunborg, et al. |
| 7 | [Language Models for Business Optimisation with a Real World Case Study in Production Scheduling](https://doi.org/10.48550/arxiv.2309.13218) | 2023 | 2 | 3 | arXiv (Cornell University) | Pivithuru Thejan Amarasinghe, Su Nguyen, Yuan Sun, et al. |
| 8 | [Embracing the Future of Medical Education With Large Language Model–Based Virtual Patients: Scoping Review](https://doi.org/10.2196/79091) | 2025 | 3 | 6 | Journal of Medical Internet Research | Jianwen Zeng, Wenhao Qi, Shuying Shen, et al. |
| 9 | [How Susceptible are LLMs to Influence in Prompts?](https://doi.org/10.48550/arxiv.2408.11865) | 2024 | 2 | 4 | arXiv (Cornell University) | Sotiris Anagnostidis, Jannis Bulian |
| 10 | [LiP-LLM: Integrating Linear Programming and Dependency Graph With Large Language Models for Multi-Robot Task Planning](https://doi.org/10.1109/lra.2024.3518105) | 2024 | 3 | 11 | IEEE Robotics and Automation Letters | Kazuma Obata, Tatsuya Aoki, Takato Horii, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 18 | 173666 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 17 | 64725 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 3 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 15 | 31162 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 4 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 15 | 120843 | Machine Learning | Leo Breiman |
| 5 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 13 | 85971 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 6 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 12 | 73372 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 7 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 11 | 40689 | MIS Quarterly | Venkatesh, Jeremy Morris, Davis, et al. |
| 8 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 11 | 62102 | MIS Quarterly | Fred D. Davis |
| 9 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 11 | 81959 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 10 | [When to use and how to report the results of PLS-SEM](https://doi.org/10.1108/ebr-11-2018-0203) | 2018 | 10 | 22082 | European Business Review | Joseph F. Hair, Jeffrey J. Risher, Marko Sarstedt, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 7 | 13125 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 2 | [Mechanisms linking social media use to adolescent mental health vulnerability](https://doi.org/10.1038/s44159-024-00307-y) | 2024 | 3 | 134 | Nature Reviews Psychology | Amy Orben, Adrian Meier, Tim Dalgleish, et al. |
| 3 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 3 | 422 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 4 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 3 | 20401 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
<!-- TRENDING-END -->
