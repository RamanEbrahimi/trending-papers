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

Last update: 2026-02-23 06:57 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Why Strong Governance Still Drifts: How Institutions Quietly Lose Alignment](https://doi.org/10.5281/zenodo.18471068) | 2026 | 8 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 2 | [The Field Protocol: Measuring Translation Coherence in Institutional Systems](https://doi.org/10.5281/zenodo.18657810) | 2026 | 8 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 3 | [The Sovereign Spine: How Institutions Stay True to Their Intent Over Time](https://doi.org/10.5281/zenodo.18646691) | 2026 | 8 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 4 | [AI-Augmented Impact Frames: A Closed-Loop Architecture for Purpose-Aligned Decisions](https://doi.org/10.5281/zenodo.18668799) | 2026 | 7 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 5 | [How Decision Systems Learn What Matters: Building Purpose-Aligned Governance](https://doi.org/10.5281/zenodo.17964280) | 2026 | 7 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 6 | [Designing the Meaning Infrastructure: Governing Interpretation in AI-Driven Institutions](https://doi.org/10.5281/zenodo.18494690) | 2026 | 7 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 7 | [Making Meaning Measurable: How to See Coherence in Decision Systems](https://doi.org/10.5281/zenodo.18486778) | 2026 | 7 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 8 | [Prologue – The Green Dashboard Trap: How Institutions Lose Sight of Their Intent](https://doi.org/10.5281/zenodo.18641907) | 2026 | 6 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 9 | [The Sovereign Spine: A New Theory of Institutional Coherence and Agency](https://doi.org/10.5281/zenodo.18649453) | 2026 | 6 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 10 | [Global burden of bacterial antimicrobial resistance 1990–2021: a systematic analysis with forecasts to 2050](https://doi.org/10.1016/s0140-6736(24)01867-1) | 2024 | 5 | 2176 | The Lancet | Mohsen Naghavi, Dan J. Stein, Kevin S Ikuta, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 103 | 119175 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 56 | 44108 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 32 | 27320 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 27 | 7696 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 20 | 31747 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 21983 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 18 | 203676 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 16 | 93711 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 15 | 29525 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 14 | 50314 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 13 | 1326 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 9 | 13055 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 3 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 8 | 355 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 4 | [Learning local equivariant representations for large-scale atomistic dynamics](https://doi.org/10.1038/s41467-023-36329-y) | 2023 | 7 | 543 | Nature Communications | Albert Musaelian, Simon Batzner, Anders Johansson, et al. |
| 5 | [Evaluation metrics and statistical tests for machine learning](https://doi.org/10.1038/s41598-024-56706-x) | 2024 | 6 | 806 | Scientific Reports | Oona Rainio, Jarmo Teuho, Riku Klén |
| 6 | [An Introduction to Statistical Learning](https://doi.org/10.1007/978-3-031-38747-0) | 2023 | 6 | 1725 | Springer texts in statistics | Gareth James, Daniela Witten, Trevor Hastie, et al. |
| 7 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 5 | 60 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |
| 8 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 5 | 625 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 9 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 5 | 10791 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 10 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 4 | 151 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 5 | 60 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 13 | 475 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 2763 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 12 | 9821 |  | Nils Reimers, Iryna Gurevych |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 2591 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4669 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 6 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 10 | 1014 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 7 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 9 | 20865 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 8 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 9 | 31188 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 9 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 7 | 1119 |  | Joon Sung Park, Joseph O’Brien, Carrie J. Cai, et al. |
| 10 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 2814 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 13 | 475 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 2591 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 10 | 1014 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 4 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 7 | 1119 |  | Joon Sung Park, Joseph O’Brien, Carrie J. Cai, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 2814 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 7 | 4116 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 7 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 6 | 274 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 6 | 2061 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [GPT-4 Technical Report](https://doi.org/10.4230/lipics.cosit.2024.11) | 2023 | 6 | 2209 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |
| 10 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 6 | 3271 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [SNN-Comprypto: High-Performance Compression and Encryption Using Spiking Neural Network Chaotic Reservoir Dynamics](https://doi.org/10.5281/zenodo.18265446) | 2026 | 4 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Hiroto Funasaki |
| 2 | [Fidelity of Medical Reasoning in Large Language Models](https://doi.org/10.1001/jamanetworkopen.2025.26021) | 2025 | 3 | 14 | JAMA Network Open | Suhana Bedi, Yixing Jiang, Philip Chung, et al. |
| 3 | [AI Agents in Clinical Medicine: A Systematic Review](https://doi.org/10.1101/2025.08.22.25334232) | 2025 | 3 | 15 |  | Alon Gorenshtein, Mahmud Omar, Benjamin S. Glicksberg, et al. |
| 4 | [Beyond the Hype: A Comprehensive Review of Current Trends in Generative AI Research, Teaching Practices, and Tools](https://doi.org/10.1145/3689187.3709614) | 2025 | 4 | 43 |  | James Prather, Juho Leinonen, Natalie Kiesler, et al. |
| 5 | [On the conversational persuasiveness of GPT-4](https://doi.org/10.1038/s41562-025-02194-6) | 2025 | 3 | 33 | Nature Human Behaviour | Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, et al. |
| 6 | [FD-LLM: Large language model for fault diagnosis of complex equipment](https://doi.org/10.1016/j.aei.2025.103208) | 2025 | 3 | 38 | Advanced Engineering Informatics | Lin Lin, Sihao Zhang, Fu Song, et al. |
| 7 | [Large Language Models in Medicine: Applications, Challenges, and Future Directions](https://doi.org/10.7150/ijms.111780) | 2025 | 3 | 47 | International Journal of Medical Sciences | Erlan Yu, Xuehong Chu, Wanwan Zhang, et al. |
| 8 | [Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation](https://doi.org/10.1109/icde60146.2024.00118) | 2024 | 4 | 68 |  | Bowen Zheng, Yupeng Hou, Hongyu Lu, et al. |
| 9 | [AI Supported Degradation of the Self Concept: A Theoretical Framework Grounded in Established Cognitive and Computational Mechanisms](https://doi.org/10.48550/arxiv.2310.13548) | 2023 | 3 | 61 | arXiv (Cornell University) | Mrinank Sharma |
| 10 | [Applications and Concerns of ChatGPT and Other Conversational Large Language Models in Health Care: Systematic Review](https://doi.org/10.2196/22769) | 2024 | 4 | 86 | Journal of Medical Internet Research | Leyao Wang, Zhiyu Wan, Congning Ni, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Social Cognitive Theory: An Agentic Perspective](https://doi.org/10.1146/annurev.psych.52.1.1) | 2001 | 3 | 14106 | Annual Review of Psychology | Albert Bandura |
| 2 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 3 | 63785 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 3 | [Prediction-Regulation Dual-Drive Game Theory (Positive Game) and Reverse Game: Theoretical Proof and Multi-Round Verification of Inevitable Human Victory Within Human-Machine Frameworks](https://doi.org/10.5281/zenodo.18339379) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 4 | [Trait Locking Science_ A New Interdisciplinary Subject for Rigid Control of Core Traits in Dynamic Systems](https://doi.org/10.5281/zenodo.18337462) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 5 | [Chaos Game Optimization: a novel metaheuristic algorithm](https://doi.org/10.1007/s10462-020-09867-w) | 2020 | 2 | 313 | Artificial Intelligence Review | Siamak Talatahari, Mahdi Azizi |
| 6 | [Evolutionary Selection in Normal-Form Games](https://doi.org/10.2307/2171774) | 1995 | 2 | 440 | Econometrica | Klaus Ritzberger, Jörgen W. Weibull |
| 7 | [Mass Communication and Para-Social Interaction](https://doi.org/10.1080/00332747.1956.11023049) | 1956 | 2 | 3756 | Psychiatry | Donald Horton, Robert Wohl |
| 8 | [Best-worst multi-criteria decision-making method](https://doi.org/10.1016/j.omega.2014.11.009) | 2014 | 2 | 3842 | Omega | Jafar Rezaei |
| 9 | [A Survey on Mobile Edge Computing: The Communication Perspective](https://doi.org/10.1109/comst.2017.2745201) | 2017 | 2 | 5180 | IEEE Communications Surveys & Tutorials | Yuyi Mao, Changsheng You, Jun Zhang, et al. |
| 10 | [Common Method Bias in PLS-SEM](https://doi.org/10.4018/ijec.2015100101) | 2015 | 2 | 7227 | International Journal of e-Collaboration | Ned Kock |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Prediction-Regulation Dual-Drive Game Theory (Positive Game) and Reverse Game: Theoretical Proof and Multi-Round Verification of Inevitable Human Victory Within Human-Machine Frameworks](https://doi.org/10.5281/zenodo.18339379) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 2 | [Trait Locking Science_ A New Interdisciplinary Subject for Rigid Control of Core Traits in Dynamic Systems](https://doi.org/10.5281/zenodo.18337462) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 3 | [Social user role value analysis and trusted user autonomous diffusion for participatory crowdsensing](https://doi.org/10.1016/j.comnet.2024.110680) | 2024 | 1 | 1 | Computer Networks | Wang Jian, Xin Cheng, Guosheng Zhao |
| 4 | [DSHCL: Dual-State Hypergraph Contrastive Learning for Information Diffusion Prediction](https://doi.org/10.1109/tkde.2025.3581419) | 2025 | 1 | 1 | IEEE Transactions on Knowledge and Data Engineering | Tianyang Shao, Weixin Zeng, Xiang Zhao |
| 5 | [Constructing a robust Short-Text Clustering Model for contrastive learning based on optimized adaptive optimal transport for pseudo-label generation](https://doi.org/10.1016/j.engappai.2025.112491) | 2025 | 1 | 1 | Engineering Applications of Artificial Intelligence | Jiahui Liu, Chun Yan, Wei Liu, et al. |
| 6 | [Symmetric Kullback–Leibler distance based generalized grey target decision method for mixed attributes](https://doi.org/10.1108/gs-01-2024-0001) | 2024 | 1 | 2 | Grey Systems Theory and Application | Jinshan Ma, Hongliang Zhu |
| 7 | [A deep multiple-instance text binary classification for topic relevant content extraction on social media](https://doi.org/10.1016/j.jksuci.2023.101883) | 2023 | 1 | 2 | Journal of King Saud University - Computer and Information Sciences | Juan Yin, Xiaoyang Liu, Zhewen Yang |
| 8 | [A machine reading comprehension framework for recognizing emotion cause in conversations](https://doi.org/10.1016/j.knosys.2024.111532) | 2024 | 1 | 2 | Knowledge-Based Systems | Jiajun Zou, Yexuan Zhang, Sixing Wu, et al. |
| 9 | [Modeling the Contributions of Participator, Content, and Network to Topic Duration in Online Social Group](https://doi.org/10.1109/tcss.2024.3414586) | 2024 | 1 | 2 | IEEE Transactions on Computational Social Systems | Guoshuai Zhang, Jiaji Wu, Gwanggil Jeon, et al. |
| 10 | [Grey multi-criteria group consensus decision-making based on cobweb model](https://doi.org/10.1108/gs-08-2023-0079) | 2024 | 1 | 3 | Grey Systems Theory and Application | Sandang Guo, Liuzhen Guan, Qian Li, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Prediction-Regulation Dual-Drive Game Theory (Positive Game) and Reverse Game: Theoretical Proof and Multi-Round Verification of Inevitable Human Victory Within Human-Machine Frameworks](https://doi.org/10.5281/zenodo.18339379) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 2 | [Trait Locking Science_ A New Interdisciplinary Subject for Rigid Control of Core Traits in Dynamic Systems](https://doi.org/10.5281/zenodo.18337462) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 3 | [A New Grey Target Evaluation Method of Science and Technology Talents Considering ‘Dominant-Implicit’ Reference Points](https://doi.org/10.3390/app12147160) | 2022 | 1 | 1 | Applied Sciences | Lin Jiang, Jianjun Zhu |
| 4 | [Social user role value analysis and trusted user autonomous diffusion for participatory crowdsensing](https://doi.org/10.1016/j.comnet.2024.110680) | 2024 | 1 | 1 | Computer Networks | Wang Jian, Xin Cheng, Guosheng Zhao |
| 5 | [DSHCL: Dual-State Hypergraph Contrastive Learning for Information Diffusion Prediction](https://doi.org/10.1109/tkde.2025.3581419) | 2025 | 1 | 1 | IEEE Transactions on Knowledge and Data Engineering | Tianyang Shao, Weixin Zeng, Xiang Zhao |
| 6 | [Constructing a robust Short-Text Clustering Model for contrastive learning based on optimized adaptive optimal transport for pseudo-label generation](https://doi.org/10.1016/j.engappai.2025.112491) | 2025 | 1 | 1 | Engineering Applications of Artificial Intelligence | Jiahui Liu, Chun Yan, Wei Liu, et al. |
| 7 | [Symmetric Kullback–Leibler distance based generalized grey target decision method for mixed attributes](https://doi.org/10.1108/gs-01-2024-0001) | 2024 | 1 | 2 | Grey Systems Theory and Application | Jinshan Ma, Hongliang Zhu |
| 8 | [A deep multiple-instance text binary classification for topic relevant content extraction on social media](https://doi.org/10.1016/j.jksuci.2023.101883) | 2023 | 1 | 2 | Journal of King Saud University - Computer and Information Sciences | Juan Yin, Xiaoyang Liu, Zhewen Yang |
| 9 | [A machine reading comprehension framework for recognizing emotion cause in conversations](https://doi.org/10.1016/j.knosys.2024.111532) | 2024 | 1 | 2 | Knowledge-Based Systems | Jiajun Zou, Yexuan Zhang, Sixing Wu, et al. |
| 10 | [Modeling the Contributions of Participator, Content, and Network to Topic Duration in Online Social Group](https://doi.org/10.1109/tcss.2024.3414586) | 2024 | 1 | 2 | IEEE Transactions on Computational Social Systems | Guoshuai Zhang, Jiaji Wu, Gwanggil Jeon, et al. |
<!-- TRENDING-END -->
