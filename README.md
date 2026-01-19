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

Last update: 2026-01-19 06:29 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Trust Anchor Core — Capability-Based MCP Server for Supply Chain Defense](https://doi.org/10.5281/zenodo.18209328) | 2026 | 9 | 40 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 2 | [Trust Anchor Client — SecureBuildWorkflow Library](https://doi.org/10.5281/zenodo.18209330) | 2026 | 8 | 36 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 3 | [Trust Anchor Monitor — Active Security Monitoring and Intrusion Detection](https://doi.org/10.5281/zenodo.18209332) | 2026 | 7 | 32 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 4 | [Trust Anchor Active Defense — Countermeasure Implementation](https://doi.org/10.5281/zenodo.18209334) | 2026 | 6 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 5 | [MOND from 5D Geometry: Quadrature Addition and SPARC Validation](https://doi.org/10.5281/zenodo.17848223) | 2026 | 5 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Schrotz, Martin Helmut |
| 6 | [Trust Anchor Forensics — Evidence Collection and Analysis](https://doi.org/10.5281/zenodo.18209336) | 2026 | 5 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 7 | [Array programming with NumPy](https://doi.org/10.1038/s41586-020-2649-2) | 2020 | 5 | 19589 | Nature | Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, et al. |
| 8 | [SciPy 1.0: fundamental algorithms for scientific computing in Python](https://doi.org/10.1038/s41592-019-0686-2) | 2020 | 5 | 34016 | Nature Methods | Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, et al. |
| 9 | [Matplotlib: A 2D Graphics Environment](https://doi.org/10.1109/mcse.2007.55) | 2007 | 5 | 36395 | Computing in Science & Engineering | John D. Hunter |
| 10 | [Deriving the Galaxy Cluster MOND Enhancement from 7D Vlasov Dispersion](https://doi.org/10.5281/zenodo.17848242) | 2026 | 4 | 19 | Zenodo (CERN European Organization for Nuclear Research) | Schrotz, Martin Helmut |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 92 | 116780 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 59 | 42428 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 21 | 26776 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 20 | 31295 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 76808 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 17 | 91772 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 14 | 7394 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 14 | 21481 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 9 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 12 | 49802 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 10 | [Machine learning: Trends, perspectives, and prospects](https://doi.org/10.1126/science.aaa8415) | 2015 | 11 | 8898 | Science | Michael I. Jordan, Tom M. Mitchell |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 12960 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 261 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 7 | 302 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 4 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 7 | 18275 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 5 | [Applications of XGBoost in water resources engineering: A systematic literature review (Dec 2018–May 2023)](https://doi.org/10.1016/j.envsoft.2024.105971) | 2024 | 6 | 212 | Environmental Modelling & Software | Majid Niazkar, Andrea Menapace, Bruno Brentan, et al. |
| 6 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 6 | 1139 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 7 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 4 | 107 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 8 | [2024 Alzheimer's disease facts and figures](https://doi.org/10.1002/alz.13809) | 2024 | 4 | 1646 | Alzheimer s & Dementia | Unknown |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 2629 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 10 | 2399 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 2134 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 836 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [How Does ChatGPT Perform on the United States Medical Licensing Examination (USMLE)? The Implications of Large Language Models for Medical Education and Knowledge Assessment](https://doi.org/10.2196/45312) | 2023 | 6 | 1848 | JMIR Medical Education | Aidan Gilson, Conrad Safranek, Thomas Huang, et al. |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 6 | 3161 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 6 | 4418 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 5 | 191 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |
| 9 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 5 | 483 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 10 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 5 | 2535 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 2629 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 10 | 2399 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 2134 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 836 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [How Does ChatGPT Perform on the United States Medical Licensing Examination (USMLE)? The Implications of Large Language Models for Medical Education and Knowledge Assessment](https://doi.org/10.2196/45312) | 2023 | 6 | 1848 | JMIR Medical Education | Aidan Gilson, Conrad Safranek, Thomas Huang, et al. |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 6 | 3161 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 5 | 191 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |
| 8 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 5 | 483 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 9 | [Towards conversational diagnostic artificial intelligence](https://doi.org/10.1038/s41586-025-08866-7) | 2025 | 4 | 126 | Nature | Tao Tu, Mike Schaekermann, Anil Palepu, et al. |
| 10 | [Diagnostic reasoning prompts reveal the potential for large language model interpretability in medicine](https://doi.org/10.1038/s41746-024-01010-1) | 2024 | 4 | 190 | npj Digital Medicine | Thomas Savage, Ashwin Nayak, Robert Gallo, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [<scp>GPT</scp> models for text annotation: An empirical exploration in public policy research](https://doi.org/10.1111/psj.70034) | 2025 | 2 | 2 | Policy Studies Journal | Alexander Churchill, Shamitha Pichika, Chengxin Xu, et al. |
| 2 | [On the Relational Nature of Time: A Structural Inscription](https://doi.org/10.5281/zenodo.18211060) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Takayuki Takagi |
| 3 | [On the Structural Preconditions of Artificial General Intelligence: A Structural Inscription](https://doi.org/10.5281/zenodo.18211593) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Takayuki Takagi |
| 4 | [Exploring the potential of ChatGPT in generating unknown clinical questions about liver transplantation: A feasibility study](https://doi.org/10.1097/lvt.0000000000000246) | 2023 | 3 | 7 | Liver Transplantation | Miho Akabane, Kazuhiro Iwadoh, Marc L. Melcher, et al. |
| 5 | [AI-powered standardised patients: evaluating ChatGPT-4o’s impact on clinical case management in intern physicians](https://doi.org/10.1186/s12909-025-06877-6) | 2025 | 3 | 24 | BMC Medical Education | Selcen Öncü, Fulya Torun, Hilal Hatice Ülkü |
| 6 | [Risks from Language Models for Automated Mental Healthcare: Ethics and Structure for Implementation](https://doi.org/10.1101/2024.04.07.24305462) | 2024 | 2 | 16 |  | Declan Grabb, Max Lamparth, Nina Vasan |
| 7 | [A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models](https://doi.org/10.18653/v1/2024.findings-emnlp.685) | 2024 | 2 | 23 |  | Pranab Sahoo, Prabhash Meharia, Akash Ghosh, et al. |
| 8 | [Roles and potential of Large language models in healthcare: A comprehensive review](https://doi.org/10.1016/j.bj.2025.100868) | 2025 | 2 | 27 | Biomedical Journal | Chi‐Hung Lin, Chang‐Fu Kuo |
| 9 | [DeepSeek’s “Low-Cost” Adoption Across China’s Hospital Systems](https://doi.org/10.1001/jama.2025.6571) | 2025 | 2 | 31 | JAMA | Dian Zeng, Yiming Qin, Bin Sheng, et al. |
| 10 | [Evaluating and addressing demographic disparities in medical large language models: a systematic review](https://doi.org/10.1186/s12939-025-02419-0) | 2025 | 2 | 33 | International Journal for Equity in Health | Mahmud Omar, Vera Sorin, Reem Agbareia, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 2 | 4418 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 2 | [Blessing or curse? The role of the influencer’s quality-price ratio constraint in live streaming e-commerce](https://doi.org/10.1016/j.tre.2025.104372) | 2025 | 1 | 0 | Transportation Research Part E Logistics and Transportation Review | Yina Li, Yanrong Wang, Yu Ning, et al. |
| 3 | [Optimal digital product auctions with unlimited supply and rebidding behavior](https://doi.org/10.1007/s10479-021-04245-3) | 2021 | 1 | 2 | Annals of Operations Research | Yu Ning, Su Xiu Xu, George Q. Huang, et al. |
| 4 | [Swimming With the Shark: The Effects of Platform Price Promotion and In-Platform Advertising on Third-Party Retailer Performance in Hybrid Online Retailing](https://doi.org/10.1177/10591478241243385) | 2024 | 1 | 2 | Production and Operations Management | Haoyan Sun, Eric Fang, Beibei Dong, et al. |
| 5 | [Game Theory in Distributed Systems Security: Foundations, Challenges, and Future Directions](https://doi.org/10.1109/msec.2024.3407593) | 2024 | 1 | 3 | IEEE Security & Privacy | Mustafa Abdallah, Saurabh Bagchi, Shaunak D. Bopardikar, et al. |
| 6 | [Particle Swarm Optimization-Based Energy-Aware Task Scheduling Algorithm in Heterogeneous Cloud](https://doi.org/10.1007/978-981-19-4990-6_40) | 2022 | 1 | 4 | Lecture notes in networks and systems | Roshni Pradhan, Suresh Chandra Satapathy |
| 7 | [Production and coopetition strategies in remanufacturing involving knowledge spillovers](https://doi.org/10.1080/00207543.2025.2490979) | 2025 | 1 | 4 | International Journal of Production Research | Nannan Wang, Linda L. Zhang, Suresh Sethi, et al. |
| 8 | [Impacts of misleading product information in livestream e-commerce supply chains](https://doi.org/10.1080/00207543.2025.2490827) | 2025 | 1 | 6 | International Journal of Production Research | Qing‐Yu Liu, Bin Shen, Qingying Li, et al. |
| 9 | [Game theory-based virtual machine migration for energy sustainability in cloud data centers](https://doi.org/10.1016/j.apenergy.2024.123798) | 2024 | 1 | 8 | Applied Energy | Francisco Javier Maldonado Carrascosa, Sebastián García Galán, M. Valverde, et al. |
| 10 | [Improved snake optimization-based task scheduling in cloud computing](https://doi.org/10.1007/s00607-024-01323-9) | 2024 | 1 | 10 | Computing | Vijay Kumar Damera, G Vanitha, B. Indira, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Blessing or curse? The role of the influencer’s quality-price ratio constraint in live streaming e-commerce](https://doi.org/10.1016/j.tre.2025.104372) | 2025 | 1 | 0 | Transportation Research Part E Logistics and Transportation Review | Yina Li, Yanrong Wang, Yu Ning, et al. |
| 2 | [Swimming With the Shark: The Effects of Platform Price Promotion and In-Platform Advertising on Third-Party Retailer Performance in Hybrid Online Retailing](https://doi.org/10.1177/10591478241243385) | 2024 | 1 | 2 | Production and Operations Management | Haoyan Sun, Eric Fang, Beibei Dong, et al. |
| 3 | [Game Theory in Distributed Systems Security: Foundations, Challenges, and Future Directions](https://doi.org/10.1109/msec.2024.3407593) | 2024 | 1 | 3 | IEEE Security & Privacy | Mustafa Abdallah, Saurabh Bagchi, Shaunak D. Bopardikar, et al. |
| 4 | [Production and coopetition strategies in remanufacturing involving knowledge spillovers](https://doi.org/10.1080/00207543.2025.2490979) | 2025 | 1 | 4 | International Journal of Production Research | Nannan Wang, Linda L. Zhang, Suresh Sethi, et al. |
| 5 | [Impacts of misleading product information in livestream e-commerce supply chains](https://doi.org/10.1080/00207543.2025.2490827) | 2025 | 1 | 6 | International Journal of Production Research | Qing‐Yu Liu, Bin Shen, Qingying Li, et al. |
| 6 | [Game theory-based virtual machine migration for energy sustainability in cloud data centers](https://doi.org/10.1016/j.apenergy.2024.123798) | 2024 | 1 | 8 | Applied Energy | Francisco Javier Maldonado Carrascosa, Sebastián García Galán, M. Valverde, et al. |
| 7 | [Improved snake optimization-based task scheduling in cloud computing](https://doi.org/10.1007/s00607-024-01323-9) | 2024 | 1 | 10 | Computing | Vijay Kumar Damera, G Vanitha, B. Indira, et al. |
| 8 | [Position Auctions with Endogenous Product Information: Why Live-Streaming Advertising Is Thriving](https://doi.org/10.1287/mnsc.2021.01299) | 2025 | 1 | 10 | Management Science | Ying‐Ju Chen, Guillermo Gallego, Pin Gao, et al. |
| 9 | [Multi-Objective Optimization Techniques in Cloud Task Scheduling: A Systematic Literature Review](https://doi.org/10.1109/access.2025.3529839) | 2025 | 1 | 12 | IEEE Access | Olanrewaju L. Abraham, Md Asri Ngadi, Johan Bin Mohamad Sharif, et al. |
| 10 | [Enhanced Whale Optimization Algorithm for task scheduling in cloud computing environments](https://doi.org/10.1186/s44147-024-00445-3) | 2024 | 1 | 15 | Journal of Engineering and Applied Science | Yanfeng Zhang, Jiawei Wang |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Blessing or curse? The role of the influencer’s quality-price ratio constraint in live streaming e-commerce](https://doi.org/10.1016/j.tre.2025.104372) | 2025 | 1 | 0 | Transportation Research Part E Logistics and Transportation Review | Yina Li, Yanrong Wang, Yu Ning, et al. |
| 2 | [Optimal digital product auctions with unlimited supply and rebidding behavior](https://doi.org/10.1007/s10479-021-04245-3) | 2021 | 1 | 2 | Annals of Operations Research | Yu Ning, Su Xiu Xu, George Q. Huang, et al. |
| 3 | [Swimming With the Shark: The Effects of Platform Price Promotion and In-Platform Advertising on Third-Party Retailer Performance in Hybrid Online Retailing](https://doi.org/10.1177/10591478241243385) | 2024 | 1 | 2 | Production and Operations Management | Haoyan Sun, Eric Fang, Beibei Dong, et al. |
| 4 | [Game Theory in Distributed Systems Security: Foundations, Challenges, and Future Directions](https://doi.org/10.1109/msec.2024.3407593) | 2024 | 1 | 3 | IEEE Security & Privacy | Mustafa Abdallah, Saurabh Bagchi, Shaunak D. Bopardikar, et al. |
| 5 | [Particle Swarm Optimization-Based Energy-Aware Task Scheduling Algorithm in Heterogeneous Cloud](https://doi.org/10.1007/978-981-19-4990-6_40) | 2022 | 1 | 4 | Lecture notes in networks and systems | Roshni Pradhan, Suresh Chandra Satapathy |
| 6 | [Production and coopetition strategies in remanufacturing involving knowledge spillovers](https://doi.org/10.1080/00207543.2025.2490979) | 2025 | 1 | 4 | International Journal of Production Research | Nannan Wang, Linda L. Zhang, Suresh Sethi, et al. |
| 7 | [Impacts of misleading product information in livestream e-commerce supply chains](https://doi.org/10.1080/00207543.2025.2490827) | 2025 | 1 | 6 | International Journal of Production Research | Qing‐Yu Liu, Bin Shen, Qingying Li, et al. |
| 8 | [Game theory-based virtual machine migration for energy sustainability in cloud data centers](https://doi.org/10.1016/j.apenergy.2024.123798) | 2024 | 1 | 8 | Applied Energy | Francisco Javier Maldonado Carrascosa, Sebastián García Galán, M. Valverde, et al. |
| 9 | [Improved snake optimization-based task scheduling in cloud computing](https://doi.org/10.1007/s00607-024-01323-9) | 2024 | 1 | 10 | Computing | Vijay Kumar Damera, G Vanitha, B. Indira, et al. |
| 10 | [Position Auctions with Endogenous Product Information: Why Live-Streaming Advertising Is Thriving](https://doi.org/10.1287/mnsc.2021.01299) | 2025 | 1 | 10 | Management Science | Ying‐Ju Chen, Guillermo Gallego, Pin Gao, et al. |
<!-- TRENDING-END -->
