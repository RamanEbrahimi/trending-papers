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

Last update: 2026-06-08 10:23 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TA-14 Admissible Execution Architecture: Volume 1 Foundational Monograph v1.2](https://doi.org/10.5281/zenodo.20463927) | 2026 | 13 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Greggory Don Butler |
| 2 | [TA-14 Admissible Evidence Architecture: The Upstream Foundation of Admissible Execution](https://doi.org/10.5281/zenodo.20467543) | 2026 | 13 | 26 | Open MIND | Greggory Don Butler |
| 3 | [TA-14 Reliance Governance Architecture: The Governance of Reliance Before Consequence](https://doi.org/10.5281/zenodo.20467871) | 2026 | 13 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Greggory Don Butler |
| 4 | [TA-14 Evidence Governance Architecture: Foundational Reference Monograph v1.4](https://doi.org/10.5281/zenodo.20466835) | 2026 | 13 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Greggory Don Butler |
| 5 | [TA-14 Corpus Self-Governance Architecture: The Governance of Governance Before Authority](https://doi.org/10.5281/zenodo.20479707) | 2026 | 13 | 26 | Open MIND | Greggory Don Butler |
| 6 | [TA-14 Authority Governance Architecture: The Governance of Legitimate Authority Before Binding, Commit, and Execution](https://doi.org/10.5281/zenodo.20480271) | 2026 | 12 | 24 | Open MIND | Greggory Don Butler |
| 7 | [TA-14 Legitimacy Governance Architecture: The Governance of Legitimate Authority Before Consequence Formation, Attachment, Binding, Commit, Execution, and Outcome](https://doi.org/10.5281/zenodo.20480776) | 2026 | 11 | 22 | Open MIND | Greggory Don Butler |
| 8 | [TA-14 Consequence Formation Governance Architecture: The Governance of Consequence Before Attachment, Binding, Commit, Execution, and Outcome](https://doi.org/10.5281/zenodo.20481403) | 2026 | 9 | 20 | Open MIND | Greggory Don Butler |
| 9 | [Provenance Erasure Rate: A Compression-Survival Metric for Attribution Loss in AI-Composed Search Outputs](https://doi.org/10.5281/zenodo.20004379) | 2026 | 9 | 53 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 10 | [TA-14 Consequence Formation Governance Architecture: The Governance of Consequence Before Attachment, Binding, Commit, Execution, and Outcome](https://doi.org/10.5281/zenodo.20481402) | 2026 | 8 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Greggory Don Butler |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 96 | 125086 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 58 | 47940 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 27 | 8735 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 20 | 28696 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 23184 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 18 | 2009 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 17 | 32852 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 16 | 51611 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 15 | 30941 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 13 | 8822 | Nature Machine Intelligence | Cynthia Rudin |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 18 | 2009 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 553 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Machine Learning in Environmental Research: Common Pitfalls and Best Practices](https://doi.org/10.1021/acs.est.3c00026) | 2023 | 6 | 557 | Environmental Science & Technology | Jun‐Jie Zhu, Meiqi Yang, Zhiyong Jason Ren |
| 4 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 5 | 552 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 5 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13298 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 6 | [Distinct hydrologic response patterns and trends worldwide revealed by physics-embedded learning](https://doi.org/10.1038/s41467-025-64367-1) | 2025 | 4 | 4 | Nature Communications | H. Ji, Yalan Song, Tadd Bindas, et al. |
| 7 | [Global Daily Discharge Estimation Based on Grid Long Short‐Term Memory (LSTM) Model and River Routing](https://doi.org/10.1029/2024wr039764) | 2025 | 4 | 21 | Water Resources Research | Yuan Yang, Dapeng Feng, Hylke E. Beck, et al. |
| 8 | [Harmonizing physical and deep learning modeling: A computationally efficient and interpretable approach for property prediction](https://doi.org/10.1016/j.scriptamat.2024.116350) | 2024 | 4 | 191 | Scripta Materialia | Da Ren, Chenchong Wang, Xiaolu Wei, et al. |
| 9 | [A survey on imbalanced learning: latest research, applications and future directions](https://doi.org/10.1007/s10462-024-10759-6) | 2024 | 4 | 373 | Artificial Intelligence Review | Wuxing Chen, Kaixiang Yang, Zhiwen Yu, et al. |
| 10 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 4 | 2689 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Distinct hydrologic response patterns and trends worldwide revealed by physics-embedded learning](https://doi.org/10.1038/s41467-025-64367-1) | 2025 | 4 | 4 | Nature Communications | H. Ji, Yalan Song, Tadd Bindas, et al. |
| 2 | [Global Daily Discharge Estimation Based on Grid Long Short‐Term Memory (LSTM) Model and River Routing](https://doi.org/10.1029/2024wr039764) | 2025 | 4 | 21 | Water Resources Research | Yuan Yang, Dapeng Feng, Hylke E. Beck, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 3242 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 3098 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 8 | 3517 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 692 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 7 | 1454 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2416 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 7 | 10741 |  | Nils Reimers, Iryna Gurevych |
| 8 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 6 | 3417 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 9 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 6 | 32339 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 10 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 6 | 78546 | Biometrics | J. Richard Landis, Gary G. Koch |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 3242 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 3098 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 8 | 3517 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 692 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 7 | 1454 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2416 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation](https://doi.org/10.1038/s41746-025-01670-7) | 2025 | 5 | 200 | npj Digital Medicine | Elham Asgari, Nina Montaña-Brown, Magda Dubois, et al. |
| 8 | [A systematic review of large language model (LLM) evaluations in clinical medicine](https://doi.org/10.1186/s12911-025-02954-4) | 2025 | 5 | 229 | BMC Medical Informatics and Decision Making | Sina Shool, Sara Adimi, Reza Saboori Amleshi, et al. |
| 9 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 5 | 641 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 10 | [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://doi.org/10.1109/tkde.2024.3352100) | 2024 | 5 | 921 | IEEE Transactions on Knowledge and Data Engineering | Shirui Pan, Linhao Luo, Yufei Wang, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Development of a Bariatric Surgery Specific Artificial Intelligence Large Language Model: BariatricSurgeryGPT](https://doi.org/10.1177/15533506251400130) | 2025 | 2 | 3 | Surgical Innovation | Berk B. Özmen, İbrahim Berber, Jerry T. Dang, et al. |
| 2 | [Evaluating the concordance of ChatGPT and physician recommendations for bariatric surgery](https://doi.org/10.1139/cjpp-2024-0026) | 2024 | 2 | 4 | Canadian Journal of Physiology and Pharmacology | Sunny Kahlon, Mary Sleet, Joseph Sujka, et al. |
| 3 | [Large Language Models in Gastroenterology and Gastrointestinal Surgery: A New Frontier in Patient Communication and Education](https://doi.org/10.14740/gr2011) | 2025 | 2 | 5 | Gastroenterology Research | Dushyant Singh Dahiya, Hassam Ali, Vishali Moond, et al. |
| 4 | [Training ChatGPT for surgical decisions: Bariatric surgery analysis using algorithms and evidence](https://doi.org/10.1016/j.orcp.2025.08.002) | 2025 | 2 | 5 | Obesity Research & Clinical Practice | Sergi Sánchez-Cordero, Ruth Lopez-Gonzalez, H Fernandez, et al. |
| 5 | [Evaluation of the Performance of Three Large Language Models in Clinical Decision Support: A Comparative Study Based on Actual Cases](https://doi.org/10.1007/s10916-025-02152-9) | 2025 | 2 | 14 | Journal of Medical Systems | Xueqi Wang, Haiyan Ye, S. H. Zhang, et al. |
| 6 | [Revisiting One-Stage Deep Uncalibrated Photometric Stereo via Fourier Embedding](https://doi.org/10.1109/tpami.2025.3557245) | 2025 | 2 | 15 | IEEE Transactions on Pattern Analysis and Machine Intelligence | Yakun Ju, Boxin Shi, Bihan Wen, et al. |
| 7 | [Evaluation of the performance of large language models in clinical decision-making in endodontics](https://doi.org/10.1186/s12903-025-06050-x) | 2025 | 3 | 23 | BMC Oral Health | Yağız Özbay, Deniz Erdoğan, Gözde Akbal Dinçer |
| 8 | [Evaluation of the Impact of ChatGPT on the Selection of Surgical Technique in Bariatric Surgery](https://doi.org/10.1007/s11695-024-07279-1) | 2024 | 2 | 18 | Obesity Surgery | Ruth Lopez-Gonzalez, Sergi Sánchez-Cordero, Jordi Pujol-Gebellí, et al. |
| 9 | [Quantifying large language model usage in scientific papers](https://doi.org/10.1038/s41562-025-02273-8) | 2025 | 3 | 34 | Nature Human Behaviour | Weixin Liang, Yaohui Zhang, Zhengxuan Wu, et al. |
| 10 | [LLM Agents for Education: Advances and Applications](https://doi.org/10.18653/v1/2025.findings-emnlp.743) | 2025 | 3 | 44 |  | Zhendong Chu, Shen Wang, Jianhe Xie, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 21 | 181340 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 11 | 92981 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 9 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 9 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 7 | 15 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [Governing Knowledge Commons](https://doi.org/10.1093/acprof:oso/9780199972036.001.0001) | 2014 | 7 | 265 | Oxford University Press eBooks | Brett M. Frischmann |
| 7 | [Intrinsic and extrinsic motivation from a self-determination theory perspective: Definitions, theory, practices, and future directions](https://doi.org/10.1016/j.cedpsych.2020.101860) | 2020 | 7 | 5043 | Contemporary Educational Psychology | Richard M. Ryan, Edward L. Deci |
| 8 | ["Why Should I Trust You?"](https://doi.org/10.1145/2939672.2939778) | 2016 | 7 | 15051 |  | Marco Túlio Ribeiro, Sameer Singh, Carlos Guestrin |
| 9 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 7 | 16916 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |
| 10 | [Intrinsic and Extrinsic Motivations: Classic Definitions and New Directions](https://doi.org/10.1006/ceps.1999.1020) | 2000 | 7 | 18077 | Contemporary Educational Psychology | Richard M. Ryan, Edward L. Deci |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 9 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 9 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 7 | 15 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection (DRAFT)](https://doi.org/10.5281/zenodo.20130563) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Working Bibliography: The Weaponization of Dutch Cartography in Challenging Spanish Maritime Trade Fortifications in Panama, 1609 to 1714](https://doi.org/10.5281/zenodo.20448560) | 2026 | 4 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Eric Hoppe |
| 6 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 11 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [Artificial intelligence literacy for technology education](https://doi.org/10.1016/j.caeo.2024.100159) | 2024 | 4 | 203 | Computers and Education Open | Karin Stolpe, Jonas Hällström |
| 8 | [Working Bibliography, Technical Supplement: Computational Methods, Game Theory, and Spatial Analysis for the Study of Dutch Colonial Cartography and Knowledge Asymmetry, 1609 to 1714](https://doi.org/10.5281/zenodo.20448633) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Eric Hoppe |
| 9 | [Institutional theory for corporate law: an invitation](https://doi.org/10.1080/14735970.2024.2414465) | 2024 | 3 | 6 | Journal of Corporate Law Studies | David Gindis, Eva Micheler |
| 10 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 3 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Working Bibliography: The Weaponization of Dutch Cartography in Challenging Spanish Maritime Trade Fortifications in Panama, 1609 to 1714](https://doi.org/10.5281/zenodo.20448560) | 2026 | 4 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Eric Hoppe |
| 2 | [Working Bibliography, Technical Supplement: Computational Methods, Game Theory, and Spatial Analysis for the Study of Dutch Colonial Cartography and Knowledge Asymmetry, 1609 to 1714](https://doi.org/10.5281/zenodo.20448633) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Eric Hoppe |
| 3 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection (DRAFT)](https://doi.org/10.5281/zenodo.20130563) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Institutional theory for corporate law: an invitation](https://doi.org/10.1080/14735970.2024.2414465) | 2024 | 3 | 6 | Journal of Corporate Law Studies | David Gindis, Eva Micheler |
| 5 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 7 | 15 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 3 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 11 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 8 | [The K41 Spectrum as the Unique Variational Minimiser of a Scale-Resolved Free Energy](https://doi.org/10.5281/zenodo.20131305) | 2026 | 3 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 9 | [Functional Stability Theory — Physical Instantiation via the Renormalized Free Energy Principle](https://doi.org/10.5281/zenodo.19036190) | 2026 | 9 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 10 | [From Landscape to Atlas: Multi-Route Cartography of an Ongoing Expedition Toward the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 9 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
<!-- TRENDING-END -->
