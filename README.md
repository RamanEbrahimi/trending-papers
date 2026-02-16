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

Last update: 2026-02-16 06:56 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Predictive Rendezvous: Time--Intent--Deterministic Peer Coordination Without Infrastructure](https://doi.org/10.5281/zenodo.18528430) | 2026 | 11 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Riaan de Beer |
| 2 | [Coordination by Foreknowledge: Semantic Rendezvous Tokens, Time--Based Addressing, and Deterministic Peer Systems](https://doi.org/10.5281/zenodo.18542183) | 2026 | 10 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Riaan de Beer |
| 3 | [Phenomenological Rendezvous: Serverless Peer Coordination Through Matched Internal Representational Patterns](https://doi.org/10.5281/zenodo.18558066) | 2026 | 9 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Riaan De Beer |
| 4 | [Eliminationist politics: an analytical framework](https://doi.org/10.1080/1369183x.2025.2595805) | 2026 | 7 | 7 | Journal of Ethnic and Migration Studies | Meghan Garrity, Harris Mylonas |
| 5 | [Irreversible Commitment as the Basis of Preference](https://doi.org/10.5281/zenodo.18601902) | 2026 | 7 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Riaan De Beer |
| 6 | [Phenomenological Invariants as Internal Rendezvous Tokens Under Irreversible Time](https://doi.org/10.5281/zenodo.18598801) | 2026 | 7 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Riaan de Beer |
| 7 | [A Unified Kaluza-Klein Framework for Processing-Driven Dark Sector Dynamics and Gauge Coupling Evolution (MetaTime v35.6)](https://doi.org/10.5281/zenodo.18405786) | 2026 | 7 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Dario Peyru |
| 8 | [Ethnopopulism and genocidal eliminationism: a discourse analysis of hate speech in the 1994 Rwandan genocide](https://doi.org/10.1080/1369183x.2025.2595808) | 2026 | 6 | 6 | Journal of Ethnic and Migration Studies | Erin K. Jenne, Promise Frank Ejiofor |
| 9 | [Don’t count me out: erasure of ethnicity and ethnic groups from national censuses](https://doi.org/10.1080/1369183x.2025.2595815) | 2026 | 6 | 6 | Journal of Ethnic and Migration Studies | Avital Livny |
| 10 | [The various facets of eliminationist politics: Conflict, nation-building, and forced migration](https://doi.org/10.1177/01925121241260429) | 2024 | 6 | 7 | International Political Science Review | Meghan Garrity, Harris Mylonas |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 91 | 118780 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 61 | 43723 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 28 | 7631 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 23 | 27218 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 22 | 93233 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 18 | 31675 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 17 | 203266 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 8 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 16 | 21875 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 9 | [Efficient iterative schemes for<i>ab initio</i>total-energy calculations using a plane-wave basis set](https://doi.org/10.1103/physrevb.54.11169) | 1996 | 14 | 115764 | Physical review. B, Condensed matter | Georg Kresse, J. Furthmüller |
| 10 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 13 | 29365 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 6 | 333 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 13034 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 3 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 5 | 52 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |
| 4 | [Learning local equivariant representations for large-scale atomistic dynamics](https://doi.org/10.1038/s41467-023-36329-y) | 2023 | 5 | 535 | Nature Communications | Albert Musaelian, Simon Batzner, Anders Johansson, et al. |
| 5 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 4 | 616 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A foundation model for atomistic materials chemistry](https://doi.org/10.1063/5.0297006) | 2025 | 5 | 52 | The Journal of Chemical Physics | Ilyes Batatia, Philipp Benner, Yuan Chiang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2560 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 12 | 31107 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 10 | 2023 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 8 | 455 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 2775 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [Towards accurate differential diagnosis with large language models](https://doi.org/10.1038/s41586-025-08869-4) | 2025 | 7 | 108 | Nature | Daniel McDuff, Mike Schaekermann, Tao Tu, et al. |
| 7 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 7 | 412 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 8 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 7 | 9707 |  | Nils Reimers, Iryna Gurevych |
| 9 | [GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](https://doi.org/10.1038/s41591-024-03456-y) | 2025 | 6 | 91 | Nature Medicine | Ethan Goh, Robert J. Gallo, Eric Strong, et al. |
| 10 | [Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis](https://doi.org/10.2196/53164) | 2024 | 6 | 209 | Journal of Medical Internet Research | Mikaël Chelli, Jules Descamps, Vincent Lavoué, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2560 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 10 | 2023 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 3 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 8 | 455 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 2775 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Towards accurate differential diagnosis with large language models](https://doi.org/10.1038/s41586-025-08869-4) | 2025 | 7 | 108 | Nature | Daniel McDuff, Mike Schaekermann, Tao Tu, et al. |
| 6 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 7 | 412 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 7 | [GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](https://doi.org/10.1038/s41591-024-03456-y) | 2025 | 6 | 91 | Nature Medicine | Ethan Goh, Robert J. Gallo, Eric Strong, et al. |
| 8 | [Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews: Comparative Analysis](https://doi.org/10.2196/53164) | 2024 | 6 | 209 | Journal of Medical Internet Research | Mikaël Chelli, Jules Descamps, Vincent Lavoué, et al. |
| 9 | [Large Language Models for Software Engineering: A Systematic Literature Review](https://doi.org/10.1145/3695988) | 2024 | 6 | 540 | ACM Transactions on Software Engineering and Methodology | Xinyi Hou, Yanjie Zhao, Yue Liu, et al. |
| 10 | [Large Language Models in Healthcare and Medical Applications: A Review](https://doi.org/10.3390/bioengineering12060631) | 2025 | 5 | 52 | Bioengineering | Subhankar Maity, Manob Jyoti Saikia |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large Language Models in Healthcare and Medical Applications: A Review](https://doi.org/10.3390/bioengineering12060631) | 2025 | 5 | 52 | Bioengineering | Subhankar Maity, Manob Jyoti Saikia |
| 2 | [Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation](https://doi.org/10.1136/bmjhci-2024-101139) | 2025 | 3 | 35 | BMJ Health & Care Informatics | Vasileios Ntinopoulos, Hector Rodriguez Cetina Biefer, I. Tudorache, et al. |
| 3 | [DeepSeek’s “Low-Cost” Adoption Across China’s Hospital Systems](https://doi.org/10.1001/jama.2025.6571) | 2025 | 3 | 38 | JAMA | Dian Zeng, Yiming Qin, Bin Sheng, et al. |
| 4 | [Large language models for disease diagnosis: a scoping review](https://doi.org/10.1038/s44387-025-00011-z) | 2025 | 3 | 42 | npj Artificial Intelligence | Shuang Zhou, Zidu Xu, Mian Zhang, et al. |
| 5 | [GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](https://doi.org/10.1038/s41591-024-03456-y) | 2025 | 6 | 91 | Nature Medicine | Ethan Goh, Robert J. Gallo, Eric Strong, et al. |
| 6 | [Privacy-preserving large language models for structured medical information retrieval](https://doi.org/10.1038/s41746-024-01233-2) | 2024 | 4 | 75 | npj Digital Medicine | Isabella C. Wiest, Dyke Ferber, Jiefu Zhu, et al. |
| 7 | [Data Augmentation using LLMs: Data Perspectives, Learning Paradigms and Challenges](https://doi.org/10.18653/v1/2024.findings-acl.97) | 2024 | 3 | 57 |  | Bosheng Ding, Chengwei Qin, R. P. Zhao, et al. |
| 8 | [Benchmarking large language models for biomedical natural language processing applications and recommendations](https://doi.org/10.1038/s41467-025-56989-2) | 2025 | 4 | 77 | Nature Communications | Qingyu Chen, Yan Hu, Xueqing Peng, et al. |
| 9 | [Evaluating the Efficacy of ChatGPT as a Patient Education Tool in Prostate Cancer: Multimetric Assessment](https://doi.org/10.2196/55939) | 2024 | 3 | 59 | Journal of Medical Internet Research | Damien Gibson, Stuart Jackson, Ramesh Shanmugasundaram, et al. |
| 10 | [Comparative benchmarking of the DeepSeek large language model on medical tasks and clinical reasoning](https://doi.org/10.1038/s41591-025-03726-3) | 2025 | 4 | 85 | Nature Medicine | Mickaël Tordjman, Zelong Liu, Murat Yüce, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Fine-Structure Constant: A Geometric Derivation from Simplicial Spacetime (Universe Engine v13.3.1)](https://doi.org/10.5281/zenodo.18407713) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 2 | [Electromagnetic Induction and the Nature of Motion in Simplicial Spacetime (Universe Engine v13.3.3)](https://doi.org/10.5281/zenodo.18407892) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 3 | [Derivation of Lorentz Invariance from Euclidean Simplicial Geometry (Universe Engine v13.3.4)](https://doi.org/10.5281/zenodo.18408280) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 4 | [Cosmological Phenomena and the Unification of Forces in the Simplicial Universe Engine v13.3.6](https://doi.org/10.5281/zenodo.18408426) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 5 | [Gravity as Lattice Elasticity: A Geometric Derivation from the Universe Engine v13.3.5](https://doi.org/10.5281/zenodo.18408375) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 6 | [The Neuroscience of Social Decision-Making](https://doi.org/10.1146/annurev.psych.121208.131647) | 2010 | 2 | 757 | Annual Review of Psychology | James K. Rilling, Alan G. Sanfey |
| 7 | [Research on the Mechanism of Cooperative Defense Against DDoS Attacks Based on Game Theory](https://doi.org/10.1007/978-981-99-2233-8_14) | 2023 | 1 | 1 | Lecture notes in computer science | Tong Wang, Zihan Lai, Weiqing Yu, et al. |
| 8 | [Optimal Strategy for Moving Target Defense on the Internet of Vehicles Based on Game Theory and Reinforcement Learning](https://doi.org/10.1109/tvt.2025.3602902) | 2025 | 1 | 1 | IEEE Transactions on Vehicular Technology | Chao Guo, Tingting Zhu, Buxin Guo, et al. |
| 9 | [GUARDS: game theoretic security allocation on a national scale](https://doi.org/10.65109/lfvz6644) | 2011 | 1 | 1 |  | James Pita, Milind Tambe, Chris Kiekintveld, et al. |
| 10 | [Game based DDoS Attack Strategies in Cloud of Things](https://doi.org/10.2991/icimm-16.2016.137) | 2016 | 1 | 2 |  | Yichuan Wang, Yefei Zhang, Liumei Zhang, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Fine-Structure Constant: A Geometric Derivation from Simplicial Spacetime (Universe Engine v13.3.1)](https://doi.org/10.5281/zenodo.18407713) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 2 | [Electromagnetic Induction and the Nature of Motion in Simplicial Spacetime (Universe Engine v13.3.3)](https://doi.org/10.5281/zenodo.18407892) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 3 | [Derivation of Lorentz Invariance from Euclidean Simplicial Geometry (Universe Engine v13.3.4)](https://doi.org/10.5281/zenodo.18408280) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 4 | [Cosmological Phenomena and the Unification of Forces in the Simplicial Universe Engine v13.3.6](https://doi.org/10.5281/zenodo.18408426) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 5 | [Gravity as Lattice Elasticity: A Geometric Derivation from the Universe Engine v13.3.5](https://doi.org/10.5281/zenodo.18408375) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 6 | [Research on the Mechanism of Cooperative Defense Against DDoS Attacks Based on Game Theory](https://doi.org/10.1007/978-981-99-2233-8_14) | 2023 | 1 | 1 | Lecture notes in computer science | Tong Wang, Zihan Lai, Weiqing Yu, et al. |
| 7 | [Optimal Strategy for Moving Target Defense on the Internet of Vehicles Based on Game Theory and Reinforcement Learning](https://doi.org/10.1109/tvt.2025.3602902) | 2025 | 1 | 1 | IEEE Transactions on Vehicular Technology | Chao Guo, Tingting Zhu, Buxin Guo, et al. |
| 8 | [Intelligent Analysis and Application of Judicial Big Data Sharing Based on Blockchain](https://doi.org/10.1109/icaibd57115.2023.10206326) | 2023 | 1 | 3 |  | Yuanmin Zhang, Junjun Jiang, Yanjun Li |
| 9 | [Dynamic Credible Spectrum Sharing Based on Smart Contract in Vehicular Networks](https://doi.org/10.3390/math12131929) | 2024 | 1 | 4 | Mathematics | Qinchi Li, Qin Wang, Haitao Zhao, et al. |
| 10 | [SafeDriveRL: Combining Non-cooperative Game Theory with Reinforcement Learning to Explore and Mitigate Human-based Uncertainty for Autonomous Vehicles](https://doi.org/10.1145/3643915.3644089) | 2024 | 1 | 5 |  | Kenneth H. Chan, Sol Zilberman, Nick Polanco, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Fine-Structure Constant: A Geometric Derivation from Simplicial Spacetime (Universe Engine v13.3.1)](https://doi.org/10.5281/zenodo.18407713) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 2 | [Electromagnetic Induction and the Nature of Motion in Simplicial Spacetime (Universe Engine v13.3.3)](https://doi.org/10.5281/zenodo.18407892) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 3 | [Derivation of Lorentz Invariance from Euclidean Simplicial Geometry (Universe Engine v13.3.4)](https://doi.org/10.5281/zenodo.18408280) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 4 | [Cosmological Phenomena and the Unification of Forces in the Simplicial Universe Engine v13.3.6](https://doi.org/10.5281/zenodo.18408426) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 5 | [Gravity as Lattice Elasticity: A Geometric Derivation from the Universe Engine v13.3.5](https://doi.org/10.5281/zenodo.18408375) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 6 | [Research on the Mechanism of Cooperative Defense Against DDoS Attacks Based on Game Theory](https://doi.org/10.1007/978-981-99-2233-8_14) | 2023 | 1 | 1 | Lecture notes in computer science | Tong Wang, Zihan Lai, Weiqing Yu, et al. |
| 7 | [Optimal Strategy for Moving Target Defense on the Internet of Vehicles Based on Game Theory and Reinforcement Learning](https://doi.org/10.1109/tvt.2025.3602902) | 2025 | 1 | 1 | IEEE Transactions on Vehicular Technology | Chao Guo, Tingting Zhu, Buxin Guo, et al. |
| 8 | [GUARDS: game theoretic security allocation on a national scale](https://doi.org/10.65109/lfvz6644) | 2011 | 1 | 1 |  | James Pita, Milind Tambe, Chris Kiekintveld, et al. |
| 9 | [Game based DDoS Attack Strategies in Cloud of Things](https://doi.org/10.2991/icimm-16.2016.137) | 2016 | 1 | 2 |  | Yichuan Wang, Yefei Zhang, Liumei Zhang, et al. |
| 10 | [Mathematical simulation of countermeasures to attacks of “denial of service” type with the use of game theory approach](https://doi.org/10.1088/1742-6596/1203/1/012076) | 2019 | 1 | 2 | Journal of Physics Conference Series | E.O. Bukharov, D G Zybin, A S Soloviev, et al. |
<!-- TRENDING-END -->
