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

Last update: 2026-01-12 06:28 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Trust Anchor Core — Capability-Based MCP Server for Supply Chain Defense](https://doi.org/10.5281/zenodo.18209328) | 2026 | 9 | 40 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 2 | [Bootstrap Foundations: The Complete Derivation of Physical Reality from Self-Reference](https://doi.org/10.5281/zenodo.18085102) | 2025 | 8 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Clifford Keeble |
| 3 | [Trust Anchor Client — SecureBuildWorkflow Library](https://doi.org/10.5281/zenodo.18209330) | 2026 | 8 | 36 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 4 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 92682 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 5 | [Trust Anchor Monitor — Active Security Monitoring and Intrusion Detection](https://doi.org/10.5281/zenodo.18209332) | 2026 | 7 | 32 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 6 | [PCORnet® 2020: current state, accomplishments, and future directions](https://doi.org/10.1016/j.jclinepi.2020.09.036) | 2020 | 7 | 164 | Journal of Clinical Epidemiology | Christopher B. Forrest, Kathleen M. McTigue, Adrian F. Hernandez, et al. |
| 7 | [Trust Anchor Active Defense — Countermeasure Implementation](https://doi.org/10.5281/zenodo.18209334) | 2026 | 6 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Thomas Jr. Perry |
| 8 | [The Molecular Signatures Database Hallmark Gene Set Collection](https://doi.org/10.1016/j.cels.2015.12.004) | 2015 | 6 | 13160 | Cell Systems | Arthur Liberzon, Chet Birger, Helga Thorvaldsdóttir, et al. |
| 9 | [STAR: ultrafast universal RNA-seq aligner](https://doi.org/10.1093/bioinformatics/bts635) | 2012 | 6 | 52181 | Bioinformatics | Alexander Dobin, Carrie Davis, Felix Schlesinger, et al. |
| 10 | [Fiji: an open-source platform for biological-image analysis](https://doi.org/10.1038/nmeth.2019) | 2012 | 6 | 66434 | Nature Methods | Johannes Schindelin, Ignacio Arganda‐Carreras, Erwin Frise, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 105 | 116780 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 73 | 42428 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 28 | 26776 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 23 | 7347 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 18 | 28838 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 18 | 31295 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 16 | 21481 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 8 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 14 | 49802 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 13 | 76639 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Machine Learning: Algorithms, Real-World Applications and Research Directions](https://doi.org/10.1007/s42979-021-00592-x) | 2021 | 12 | 4567 | SN Computer Science | Iqbal H. Sarker |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 9 | 1194 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 2 | [Machine learning and SHAP value interpretation for predicting comorbidity of cardiovascular disease and cancer with dietary antioxidants](https://doi.org/10.1016/j.redox.2024.103470) | 2024 | 5 | 104 | Redox Biology | Xiangjun Qi, Shujing Wang, Caishan Fang, et al. |
| 3 | [Enhancing K-nearest neighbor algorithm: a comprehensive review and performance analysis of modifications](https://doi.org/10.1186/s40537-024-00973-y) | 2024 | 5 | 260 | Journal Of Big Data | Rajib Kumar Halder, Mohammed Nasir Uddin, Md. Ashraf Uddin, et al. |
| 4 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 18275 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 5 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 4 | 288 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 6 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 4 | 300 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 7 | [An improved random forest based on the classification accuracy and correlation measurement of decision trees](https://doi.org/10.1016/j.eswa.2023.121549) | 2023 | 4 | 377 | Expert Systems with Applications | Zhigang Sun, Guotao Wang, Pengfei Li, et al. |
| 8 | [DeePMD-kit v2: A software package for deep potential models](https://doi.org/10.1063/5.0155600) | 2023 | 4 | 419 | The Journal of Chemical Physics | Jinzhe Zeng, Duo Zhang, Denghui Lu, et al. |
| 9 | [Machine Learning in Environmental Research: Common Pitfalls and Best Practices](https://doi.org/10.1021/acs.est.3c00026) | 2023 | 4 | 432 | Environmental Science & Technology | Jun‐Jie Zhu, Meiqi Yang, Zhiyong Jason Ren |
| 10 | [A review on longitudinal data analysis with random forest](https://doi.org/10.1093/bib/bbad002) | 2023 | 4 | 464 | Briefings in Bioinformatics | Jianchang Hu, Silke Szymczak |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 2602 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1873 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 3 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4418 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 10 | 2374 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 10 | 30704 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 9 | 407 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 7 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 9 | 2535 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 8 | [Performance of Large Language Models on a Neurology Board–Style Examination](https://doi.org/10.1001/jamanetworkopen.2023.46721) | 2023 | 6 | 97 | JAMA Network Open | Marc C. Schubert, Wolfgang Wick, Varun Venkataramani |
| 9 | [How Does ChatGPT Perform on the United States Medical Licensing Examination (USMLE)? The Implications of Large Language Models for Medical Education and Knowledge Assessment](https://doi.org/10.2196/45312) | 2023 | 6 | 1831 | JMIR Medical Education | Aidan Gilson, Conrad Safranek, Thomas Huang, et al. |
| 10 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 6 | 2134 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 2602 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1873 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 10 | 2374 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 9 | 407 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 5 | [Performance of Large Language Models on a Neurology Board–Style Examination](https://doi.org/10.1001/jamanetworkopen.2023.46721) | 2023 | 6 | 97 | JAMA Network Open | Marc C. Schubert, Wolfgang Wick, Varun Venkataramani |
| 6 | [How Does ChatGPT Perform on the United States Medical Licensing Examination (USMLE)? The Implications of Large Language Models for Medical Education and Knowledge Assessment](https://doi.org/10.2196/45312) | 2023 | 6 | 1831 | JMIR Medical Education | Aidan Gilson, Conrad Safranek, Thomas Huang, et al. |
| 7 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 6 | 2134 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |
| 8 | [ChatGPT Utility in Healthcare Education, Research, and Practice: Systematic Review on the Promising Perspectives and Valid Concerns](https://doi.org/10.3390/healthcare11060887) | 2023 | 6 | 2445 | Healthcare | Malik Sallam |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 6 | 3142 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [Current applications and challenges in large language models for patient care: a systematic review](https://doi.org/10.1038/s43856-024-00717-2) | 2025 | 5 | 112 | Communications Medicine | Felix Busch, Lena Hoffmann, Christopher Rueger, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Comparative evaluation and performance of large language models on expert level critical care questions: a benchmark study](https://doi.org/10.1186/s13054-025-05302-0) | 2025 | 3 | 15 | Critical Care | Jessica D. Workum, Bas W. S. Volkers, Davy van de Sande, et al. |
| 2 | [Large Language Models in Healthcare and Medical Applications: A Review](https://doi.org/10.3390/bioengineering12060631) | 2025 | 4 | 31 | Bioengineering | Subhankar Maity, Manob Jyoti Saikia |
| 3 | [Claude, ChatGPT, Copilot, and Gemini performance versus students in different topics of neuroscience](https://doi.org/10.1152/advan.00093.2024) | 2025 | 3 | 25 | AJP Advances in Physiology Education | Volodymyr Mavrych, Ahmed Yaqinuddin, Olena Bolgova |
| 4 | [AI, Machine Learning, and ChatGPT in Hypertension](https://doi.org/10.1161/hypertensionaha.124.19468) | 2024 | 3 | 28 | Hypertension | Anita T. Layton |
| 5 | [Performance of Large Language Models on a Neurology Board–Style Examination](https://doi.org/10.1001/jamanetworkopen.2023.46721) | 2023 | 6 | 97 | JAMA Network Open | Marc C. Schubert, Wolfgang Wick, Varun Venkataramani |
| 6 | [A flood knowledge-constrained large language model interactable with GIS: enhancing public risk perception of floods](https://doi.org/10.1080/13658816.2024.2306167) | 2024 | 3 | 62 | International Journal of Geographical Information Systems | Jun Zhu, Pei Dang, Yungang Cao, et al. |
| 7 | [OpenMedLM: prompt engineering can out-perform fine-tuning in medical question-answering with open-source large language models](https://doi.org/10.1038/s41598-024-64827-6) | 2024 | 3 | 69 | Scientific Reports | Jenish Maharjan, Anurag Garikipati, Navan Preet Singh, et al. |
| 8 | [Large language models for generating medical examinations: systematic review](https://doi.org/10.1186/s12909-024-05239-y) | 2024 | 3 | 73 | BMC Medical Education | Yaara Artsi, Vera Sorin, Eli Konen, et al. |
| 9 | [Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks](https://doi.org/10.48550/arxiv.2302.08399) | 2023 | 3 | 79 | arXiv (Cornell University) | Tomer Ullman |
| 10 | [ChatGPT prompts for generating multiple-choice questions in medical education and evidence on their validity: a literature review](https://doi.org/10.1093/postmj/qgae065) | 2024 | 3 | 84 | Postgraduate Medical Journal | Yavuz Selim Kıyak, Emre Emekli |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Optimal Operation of Energy Hub: An Integrated Model Combined Distributionally Robust Optimization Method With Stackelberg Game](https://doi.org/10.1109/tste.2023.3252519) | 2023 | 2 | 103 | IEEE Transactions on Sustainable Energy | Junjie Zhong, Yong Li, Yan Wu, et al. |
| 2 | [The need to belong: Desire for interpersonal attachments as a fundamental human motivation.](https://doi.org/10.1037/0033-2909.117.3.497) | 1995 | 2 | 20764 | Psychological Bulletin | Roy F. Baumeister, Mark R. Leary |
| 3 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 2 | 42428 |  | Tianqi Chen, Carlos Guestrin |
| 4 | [Continuum-Model-Based Security Control of Multi-Tiered Re-Entrant Manufacturing Networks Under Cyber-Attacks](https://doi.org/10.1109/tase.2025.3611938) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Chenguang Liu, Qing Gao, Michael Basin, et al. |
| 5 | [Classification and comparison of IP traceback techniques for DoS/DDoS/DRDoS defence](https://doi.org/10.1504/ijaip.2024.141525) | 2024 | 1 | 1 | International Journal of Advanced Intelligence Paradigms | Marjan Kuchaki Rafsanjani, Hashem Bagherinezhad |
| 6 | [Optimal Secure Control for Cyber-Physical Systems Under False Data Injection Attacks via Incremental Iterative Q-Learning Algorithm](https://doi.org/10.1109/tase.2025.3610922) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Jinyan Li, Xiao‐Jie Peng, Yan Lei, et al. |
| 7 | [A Model Predictive Control Strategy Under Partial State Availability for Resilience and Maintenance Operations of Cyber-Physical Systems](https://doi.org/10.1109/tsmc.2025.3604291) | 2025 | 1 | 1 | IEEE Transactions on Systems Man and Cybernetics Systems | Domenico Famularo, Francesco Tedesco, Giuseppe Franzè |
| 8 | [Optimal Sensor Grouping Transmission Strategy for Multiple Processes Over Packet-Dropping Channels](https://doi.org/10.1109/tcyb.2025.3597143) | 2025 | 1 | 1 | IEEE Transactions on Cybernetics | Xiao-Hui Liu, Guang‐Hong Yang |
| 9 | [A Particle Swarm Optimization Event-Triggered Approach to Adaptive Sliding Mode Control of Markov Jump Networked Systems](https://doi.org/10.1109/tase.2025.3608783) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Haocheng Lou, Baoping Jiang, Zhen Liu |
| 10 | [Robust Load Frequency Control for Multi-Area Power Systems: A Delay-Induced-Source Dependent Approach](https://doi.org/10.1109/tase.2025.3598838) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Zhe-Li Yuan, Chuan‐Ke Zhang, Ju H. Park, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Optimal Operation of Energy Hub: An Integrated Model Combined Distributionally Robust Optimization Method With Stackelberg Game](https://doi.org/10.1109/tste.2023.3252519) | 2023 | 2 | 103 | IEEE Transactions on Sustainable Energy | Junjie Zhong, Yong Li, Yan Wu, et al. |
| 2 | [Continuum-Model-Based Security Control of Multi-Tiered Re-Entrant Manufacturing Networks Under Cyber-Attacks](https://doi.org/10.1109/tase.2025.3611938) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Chenguang Liu, Qing Gao, Michael Basin, et al. |
| 3 | [Classification and comparison of IP traceback techniques for DoS/DDoS/DRDoS defence](https://doi.org/10.1504/ijaip.2024.141525) | 2024 | 1 | 1 | International Journal of Advanced Intelligence Paradigms | Marjan Kuchaki Rafsanjani, Hashem Bagherinezhad |
| 4 | [Optimal Secure Control for Cyber-Physical Systems Under False Data Injection Attacks via Incremental Iterative Q-Learning Algorithm](https://doi.org/10.1109/tase.2025.3610922) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Jinyan Li, Xiao‐Jie Peng, Yan Lei, et al. |
| 5 | [A Model Predictive Control Strategy Under Partial State Availability for Resilience and Maintenance Operations of Cyber-Physical Systems](https://doi.org/10.1109/tsmc.2025.3604291) | 2025 | 1 | 1 | IEEE Transactions on Systems Man and Cybernetics Systems | Domenico Famularo, Francesco Tedesco, Giuseppe Franzè |
| 6 | [Optimal Sensor Grouping Transmission Strategy for Multiple Processes Over Packet-Dropping Channels](https://doi.org/10.1109/tcyb.2025.3597143) | 2025 | 1 | 1 | IEEE Transactions on Cybernetics | Xiao-Hui Liu, Guang‐Hong Yang |
| 7 | [A Particle Swarm Optimization Event-Triggered Approach to Adaptive Sliding Mode Control of Markov Jump Networked Systems](https://doi.org/10.1109/tase.2025.3608783) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Haocheng Lou, Baoping Jiang, Zhen Liu |
| 8 | [Robust Load Frequency Control for Multi-Area Power Systems: A Delay-Induced-Source Dependent Approach](https://doi.org/10.1109/tase.2025.3598838) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Zhe-Li Yuan, Chuan‐Ke Zhang, Ju H. Park, et al. |
| 9 | [Security Control of SMMS Teleoperation Systems Based on DTOD Scheduling Protocol](https://doi.org/10.1109/jiot.2025.3594371) | 2025 | 1 | 1 | IEEE Internet of Things Journal | Yuchao Huang, Xia Liu, Chengwei Pan, et al. |
| 10 | [Privacy-Preserving State Estimation Under Quantized Innovation via the Exponential Mechanism](https://doi.org/10.1109/jiot.2025.3592963) | 2025 | 1 | 1 | IEEE Internet of Things Journal | Huaiyu Yuan, Wen Yang, Jie Wang, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Continuum-Model-Based Security Control of Multi-Tiered Re-Entrant Manufacturing Networks Under Cyber-Attacks](https://doi.org/10.1109/tase.2025.3611938) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Chenguang Liu, Qing Gao, Michael Basin, et al. |
| 2 | [Classification and comparison of IP traceback techniques for DoS/DDoS/DRDoS defence](https://doi.org/10.1504/ijaip.2024.141525) | 2024 | 1 | 1 | International Journal of Advanced Intelligence Paradigms | Marjan Kuchaki Rafsanjani, Hashem Bagherinezhad |
| 3 | [Optimal Secure Control for Cyber-Physical Systems Under False Data Injection Attacks via Incremental Iterative Q-Learning Algorithm](https://doi.org/10.1109/tase.2025.3610922) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Jinyan Li, Xiao‐Jie Peng, Yan Lei, et al. |
| 4 | [A Model Predictive Control Strategy Under Partial State Availability for Resilience and Maintenance Operations of Cyber-Physical Systems](https://doi.org/10.1109/tsmc.2025.3604291) | 2025 | 1 | 1 | IEEE Transactions on Systems Man and Cybernetics Systems | Domenico Famularo, Francesco Tedesco, Giuseppe Franzè |
| 5 | [Optimal Sensor Grouping Transmission Strategy for Multiple Processes Over Packet-Dropping Channels](https://doi.org/10.1109/tcyb.2025.3597143) | 2025 | 1 | 1 | IEEE Transactions on Cybernetics | Xiao-Hui Liu, Guang‐Hong Yang |
| 6 | [A Particle Swarm Optimization Event-Triggered Approach to Adaptive Sliding Mode Control of Markov Jump Networked Systems](https://doi.org/10.1109/tase.2025.3608783) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Haocheng Lou, Baoping Jiang, Zhen Liu |
| 7 | [Robust Load Frequency Control for Multi-Area Power Systems: A Delay-Induced-Source Dependent Approach](https://doi.org/10.1109/tase.2025.3598838) | 2025 | 1 | 1 | IEEE Transactions on Automation Science and Engineering | Zhe-Li Yuan, Chuan‐Ke Zhang, Ju H. Park, et al. |
| 8 | [Security Control of SMMS Teleoperation Systems Based on DTOD Scheduling Protocol](https://doi.org/10.1109/jiot.2025.3594371) | 2025 | 1 | 1 | IEEE Internet of Things Journal | Yuchao Huang, Xia Liu, Chengwei Pan, et al. |
| 9 | [Privacy-Preserving State Estimation Under Quantized Innovation via the Exponential Mechanism](https://doi.org/10.1109/jiot.2025.3592963) | 2025 | 1 | 1 | IEEE Internet of Things Journal | Huaiyu Yuan, Wen Yang, Jie Wang, et al. |
| 10 | [Asynchronous Gain-Scheduling Secure Control of Nonlinear Cyber-Physical Systems Under Complex Transition Probabilities: A Dual-Domain Polynomial Framework](https://doi.org/10.1109/tii.2025.3586061) | 2025 | 1 | 1 | IEEE Transactions on Industrial Informatics | Xingchen Shao, Xiangpeng Xie, Xiaoli Luan |
<!-- TRENDING-END -->
