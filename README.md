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

Last update: 2026-02-02 06:55 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Globally enhanced calcification across the coccolithophore Gephyrocapsa complex during the mid-Brunhes interval](https://doi.org/10.1016/j.quascirev.2023.108375) | 2023 | 6 | 7 | Quaternary Science Reviews | Alba González‐Lanchas, Rosalind E. M. Rickaby, Francisco Javier Sierro, et al. |
| 2 | [Revision of the Quaternary calcareous nannofossil biochronology of Arctic Ocean sediments](https://doi.org/10.1016/j.quascirev.2023.108382) | 2023 | 6 | 14 | Quaternary Science Reviews | mohammad javad razmjooei, Jorijntje Henderiks, Helen K. Coxall, et al. |
| 3 | [Quaternary dinoflagellate cysts in the Arctic Ocean: Potential and limitations for stratigraphy and paleoenvironmental reconstructions](https://doi.org/10.1016/j.quascirev.2017.12.020) | 2018 | 6 | 21 | Quaternary Science Reviews | Jens Matthießen, Michael Schreck, Stijn De Schepper, et al. |
| 4 | [Arctic planktic foraminiferal assemblages: Implications for subsurface temperature reconstructions](https://doi.org/10.1016/j.marmicro.2012.07.001) | 2012 | 6 | 65 | Marine Micropaleontology | Katrine Husum, Morten Hald |
| 5 | [Handbook For Shipboard Paleomagnetists](https://doi.org/10.2973/odp.tn.34.2007) | 2007 | 6 | 71 |  | Carl Richter, Gary D Acton, C. Endris, et al. |
| 6 | [Distribution of common modern dinoflagellate cyst taxa in surface sediments of the Northern Hemisphere in relation to environmental parameters: The new n=1968 database](https://doi.org/10.1016/j.marmicro.2019.101796) | 2019 | 6 | 117 | Marine Micropaleontology | Anne de Vernal, Taoufik Radi, Sébastien Zaragosi, et al. |
| 7 | [Global synchroneity of late Quaternary coccolith datum levels Validation by oxygen isotopes](https://doi.org/10.1130/0091-7613(1977)5<400:gsolqc>2.0.co;2) | 1977 | 6 | 610 | Geology | Hans R. Thierstein, Kurt R. Geitzenauer, B. Molfino, et al. |
| 8 | [Expedition 403 methods](https://doi.org/10.14379/iodp.proc.403.102.2026) | 2026 | 5 | 5 | Proceedings of the International Ocean Discovery Program. Expedition reports | Rg Lucchi, K.E.K. St. John, T.A. Ronge, et al. |
| 9 | [A Saturated Spacetime Framework: A Conceptual Extension of General Relativity](https://doi.org/10.5281/zenodo.18371346) | 2026 | 5 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Trevor Neil Kelleher |
| 10 | [Dinoflagellate Cyst Ecostratigraphy of PliocenePleistocene Sediments from the Yermak Plateau (Arctic Ocean, Hole 911A)](https://doi.org/10.2973/odp.proc.sr.151.109.1996) | 1996 | 5 | 33 |  | Jens Matthießen, Wolfram W. Brenner |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 102 | 117705 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 67 | 42956 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 24 | 26948 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 23 | 7441 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 17 | 21624 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 16 | 29048 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 16 | 49963 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 8 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 13 | 15203 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 9 | [Regularization and Variable Selection Via the Elastic Net](https://doi.org/10.1111/j.1467-9868.2005.00503.x) | 2005 | 13 | 19956 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Hui Zou, Trevor Hastie |
| 10 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 13 | 31428 | Machine Learning | Corinna Cortes, Vladimir Vapnik |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 7 | 1263 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 2 | [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336) | 2023 | 6 | 875 | Science | Rémi Lam, Álvaro Sánchez‐González, Matthew Willson, et al. |
| 3 | [The ChEMBL Database in 2023: a drug discovery platform spanning multiple bioactivity data types and time periods](https://doi.org/10.1093/nar/gkad1004) | 2023 | 6 | 894 | Nucleic Acids Research | Barbara Zdrazil, Eloy Félix, Fiona Hunter, et al. |
| 4 | [DrugBank 6.0: the DrugBank Knowledgebase for 2024](https://doi.org/10.1093/nar/gkad976) | 2023 | 6 | 1161 | Nucleic Acids Research | Craig Knox, Michael Wilson, Christen M. Klinger, et al. |
| 5 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 12996 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 6 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 5 | 314 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2452 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2688 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 9 | 20623 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 8 | 2651 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [High-performance medicine: the convergence of human and artificial intelligence](https://doi.org/10.1038/s41591-018-0300-7) | 2018 | 8 | 6990 | Nature Medicine | Eric J. Topol |
| 6 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 6 | 375 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 7 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 407 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 8 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 6 | 30812 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 9 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 5 | 359 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 10 | [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://doi.org/10.18653/v1/2022.acl-long.229) | 2022 | 5 | 431 | Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) | Stephanie Lin, Jacob Hilton, Owain Evans |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2452 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2688 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 6 | 375 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 407 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 5 | 359 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 6 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 4 | 150 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 7 | [A systematic review of large language models and their implications in medical education](https://doi.org/10.1111/medu.15402) | 2024 | 4 | 158 | Medical Education | Harrison Lucas, Jeffrey S. Upperman, Jamie R. Robinson |
| 8 | [Large language models in health care: Development, applications, and challenges](https://doi.org/10.1002/hcs2.61) | 2023 | 4 | 280 | Health care science | Rui Yang, Ting Fang Tan, Wei Lu, et al. |
| 9 | [FLEX: Fault Localization and Explanation Using Open-Source Large Language Models in Powertrain Systems (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.25) | 2024 | 4 | 288 | arXiv (Cornell University) | Mohamed Ettaleb, Mouna Kamel |
| 10 | [ChatGPT Chemistry Assistant for Text Mining and the Prediction of MOF Synthesis](https://doi.org/10.1021/jacs.3c05819) | 2023 | 4 | 396 | Journal of the American Chemical Society | Zhiling Zheng, Oufan Zhang, Christian Borgs, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The .causal Format: Deterministic Inference for AI-Assisted Hypothesis Amplification](https://doi.org/10.5281/zenodo.18326222) | 2026 | 3 | 0 | Zenodo (CERN European Organization for Nuclear Research) | David Tom Foss |
| 2 | [From Signal Amplification to Autonomous Discovery: The Sovereign Gap-Driven Knowledge Engine](https://doi.org/10.5281/zenodo.18336249) | 2026 | 3 | 0 | Zenodo (CERN European Organization for Nuclear Research) | David Tom Foss |
| 3 | [TELOS Governance Benchmark Dataset: Out-of-Scope Detection for Task-Oriented Dialogue Systems](https://doi.org/10.5281/zenodo.18009153) | 2025 | 3 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Jeffrey Brunner |
| 4 | [Toward Edge General Intelligence With Multiple-Large Language Model (Multi-LLM): Architecture, Trust, and Orchestration](https://doi.org/10.1109/tccn.2025.3612760) | 2025 | 2 | 5 | IEEE Transactions on Cognitive Communications and Networking | Haoxiang Luo, Yinqiu Liu, Ruichen Zhang, et al. |
| 5 | [FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://doi.org/10.1609/aaaiss.v3i1.31290) | 2024 | 2 | 21 | Proceedings of the AAAI Symposium Series | Yangyang Yu, Haohang Li, Zhi Chen, et al. |
| 6 | [Using Large Language Models to Detect Depression From User-Generated Diary Text Data as a Novel Approach in Digital Mental Health Screening: Instrument Validation Study](https://doi.org/10.2196/54617) | 2024 | 3 | 32 | Journal of Medical Internet Research | Daun Shin, Hyoseung Kim, Seunghwan Lee, et al. |
| 7 | [Agent-based learning of materials datasets from the scientific literature](https://doi.org/10.1039/d4dd00252k) | 2024 | 2 | 23 | Digital Discovery | Mehrad Ansari, Seyed Mohamad Moosavi |
| 8 | [Evaluating large language model workflows in clinical decision support for triage and referral and diagnosis](https://doi.org/10.1038/s41746-025-01684-1) | 2025 | 3 | 41 | npj Digital Medicine | Farieda Gaber, Maqsood Shaik, Fabio Allega, et al. |
| 9 | [Large Language Models in Healthcare and Medical Applications: A Review](https://doi.org/10.3390/bioengineering12060631) | 2025 | 3 | 42 | Bioengineering | Subhankar Maity, Manob Jyoti Saikia |
| 10 | [Retrieval augmented generation for large language models in healthcare: A systematic review](https://doi.org/10.1371/journal.pdig.0000877) | 2025 | 3 | 46 | PLOS Digital Health | Lameck Mbangula Amugongo, Pietro Mascheroni, Steven E. Brooks, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Floor-Specified No-Meta Autonomy](https://doi.org/10.5281/zenodo.18258262) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 2 | [Observable-Only No-Meta Causal Autonomy Protocol (ONCAP)](https://doi.org/10.5281/zenodo.18371930) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 3 | [Friction-Minimal Intersubjective Contracts for No-Meta Autonomous Agents](https://doi.org/10.5281/zenodo.18308030) | 2026 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 4 | [Adversarial Participation Without a Judge: Fail-Closed Containment for No-Meta, Observable-Only Agents](https://doi.org/10.5281/zenodo.18382670) | 2026 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 5 | [Government participation in low-carbon technology transfer: An evolutionary game study](https://doi.org/10.1016/j.techfore.2023.122320) | 2023 | 2 | 66 | Technological Forecasting and Social Change | Chen Zou, Yongchun Huang, Shiliang Hu, et al. |
| 6 | [Energy Storage Sharing in Smart Grid: A Modified Auction-Based Approach](https://doi.org/10.1109/tsg.2015.2512267) | 2016 | 2 | 357 | IEEE Transactions on Smart Grid | Wayes Tushar, Bo Chai, Chau Yuen, et al. |
| 7 | [Evolutionary Games in Economics](https://doi.org/10.2307/2938222) | 1991 | 2 | 1826 | Econometrica | Daniel Friedman |
| 8 | [Risk management in guaranteed maximum price (GMP) contracts](https://doi.org/10.1108/sasbe-09-2021-0176) | 2022 | 1 | 1 | Smart and Sustainable Built Environment | Asha Dulanjalie Palihakkara, B.A.K.S. Perera |
| 9 | [Industrial relocation or shorter shipping routes? Examining the impact of the EU’s carbon border adjustment mechanism on global emissions using structural gravity](https://doi.org/10.1016/j.eap.2025.07.019) | 2025 | 1 | 1 | Economic Analysis and Policy | Aline Mortha, Toshi H. Arimura, Shiro Takeda, et al. |
| 10 | [Current Practices in the Development of Guaranteed Maximum Price (GMP) Contracts](https://doi.org/10.1061/9780784485286.015) | 2024 | 1 | 0 |  | Tolulope I. Ogundare, Rebecca Kassa, Omar Maali, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Floor-Specified No-Meta Autonomy](https://doi.org/10.5281/zenodo.18258262) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 2 | [Observable-Only No-Meta Causal Autonomy Protocol (ONCAP)](https://doi.org/10.5281/zenodo.18371930) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 3 | [Friction-Minimal Intersubjective Contracts for No-Meta Autonomous Agents](https://doi.org/10.5281/zenodo.18308030) | 2026 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 4 | [Adversarial Participation Without a Judge: Fail-Closed Containment for No-Meta, Observable-Only Agents](https://doi.org/10.5281/zenodo.18382670) | 2026 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 5 | [Government participation in low-carbon technology transfer: An evolutionary game study](https://doi.org/10.1016/j.techfore.2023.122320) | 2023 | 2 | 66 | Technological Forecasting and Social Change | Chen Zou, Yongchun Huang, Shiliang Hu, et al. |
| 6 | [Industrial relocation or shorter shipping routes? Examining the impact of the EU’s carbon border adjustment mechanism on global emissions using structural gravity](https://doi.org/10.1016/j.eap.2025.07.019) | 2025 | 1 | 1 | Economic Analysis and Policy | Aline Mortha, Toshi H. Arimura, Shiro Takeda, et al. |
| 7 | [Current Practices in the Development of Guaranteed Maximum Price (GMP) Contracts](https://doi.org/10.1061/9780784485286.015) | 2024 | 1 | 0 |  | Tolulope I. Ogundare, Rebecca Kassa, Omar Maali, et al. |
| 8 | [Qualifications-Driven Procurement Selection Criteria for Design–Build and Construction Manager at Risk Firms](https://doi.org/10.1061/jsdccc.sceng-1495) | 2025 | 1 | 0 | Journal of structural design and construction practice. | Hala Sanboskani, Mounir El Asmar |
| 9 | [Framework for Estimating Quality-Related Incentive and Disincentive in Construction Projects](https://doi.org/10.1061/jcemd4.coeng-12259) | 2023 | 1 | 2 | Journal of Construction Engineering and Management | Sahil Garg, Sudhir Misra |
| 10 | [BIPV in India: Opportunities, challenges, and pathways for urban planning and smart cities](https://doi.org/10.1016/j.solcom.2025.100133) | 2025 | 1 | 3 | Solar Compass | Kedar Mehta, Ravita Lamba, Sunanda Sinha, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Floor-Specified No-Meta Autonomy](https://doi.org/10.5281/zenodo.18258262) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 2 | [Observable-Only No-Meta Causal Autonomy Protocol (ONCAP)](https://doi.org/10.5281/zenodo.18371930) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 3 | [Friction-Minimal Intersubjective Contracts for No-Meta Autonomous Agents](https://doi.org/10.5281/zenodo.18308030) | 2026 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 4 | [Adversarial Participation Without a Judge: Fail-Closed Containment for No-Meta, Observable-Only Agents](https://doi.org/10.5281/zenodo.18382670) | 2026 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 5 | [Risk management in guaranteed maximum price (GMP) contracts](https://doi.org/10.1108/sasbe-09-2021-0176) | 2022 | 1 | 1 | Smart and Sustainable Built Environment | Asha Dulanjalie Palihakkara, B.A.K.S. Perera |
| 6 | [Industrial relocation or shorter shipping routes? Examining the impact of the EU’s carbon border adjustment mechanism on global emissions using structural gravity](https://doi.org/10.1016/j.eap.2025.07.019) | 2025 | 1 | 1 | Economic Analysis and Policy | Aline Mortha, Toshi H. Arimura, Shiro Takeda, et al. |
| 7 | [Current Practices in the Development of Guaranteed Maximum Price (GMP) Contracts](https://doi.org/10.1061/9780784485286.015) | 2024 | 1 | 0 |  | Tolulope I. Ogundare, Rebecca Kassa, Omar Maali, et al. |
| 8 | [Qualifications-Driven Procurement Selection Criteria for Design–Build and Construction Manager at Risk Firms](https://doi.org/10.1061/jsdccc.sceng-1495) | 2025 | 1 | 0 | Journal of structural design and construction practice. | Hala Sanboskani, Mounir El Asmar |
| 9 | [OPTID: Optimal Incentives and Disincentives](https://doi.org/10.1061/(asce)me.1943-5479.0000946) | 2021 | 1 | 2 | Journal of Management in Engineering | Kunhee Choi, Junseo Bae, Young Hoon Kwak |
| 10 | [Framework for Estimating Quality-Related Incentive and Disincentive in Construction Projects](https://doi.org/10.1061/jcemd4.coeng-12259) | 2023 | 1 | 2 | Journal of Construction Engineering and Management | Sahil Garg, Sudhir Misra |
<!-- TRENDING-END -->
