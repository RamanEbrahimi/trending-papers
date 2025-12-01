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

Last update: 2025-12-01 06:24 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Expertise in Management Research: A Review and Agenda for Future Research](https://doi.org/10.5465/annals.2022.0078) | 2023 | 14 | 22 | Academy of Management Annals | Maximilian Heimstädt, Tomi Koljonen, Kasper Trolle Elmholdt |
| 2 | [For a Sociology of Expertise: The Social Origins of the Autism Epidemic](https://doi.org/10.1086/668448) | 2013 | 14 | 589 | American Journal of Sociology | Gil Eyal |
| 3 | [To Hive or to Hold? Producing Professional Authority through Scut Work](https://doi.org/10.1177/0001839214560743) | 2014 | 12 | 170 | Administrative Science Quarterly | Ruthanne Huising |
| 4 | [The System of Professions](https://doi.org/10.7208/chicago/9780226189666.001.0001) | 1988 | 12 | 6725 |  | Andrew Abbott |
| 5 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 12 | 90778 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 6 | [What returnee bilinguals may teach us about language attrition, language stabilization, and individualvariation](https://doi.org/10.1075/lab.25021.flo) | 2025 | 11 | 0 | Linguistic Approaches to Bilingualism | Cristina Flores, Neal Snape |
| 7 | [Translating Expertise across Work Contexts: U.S. Puppeteers Move from Stage to Screen](https://doi.org/10.1177/0003122420987199) | 2021 | 11 | 24 | American Sociological Review | Michel Anteby, Audrey Holm |
| 8 | [Relational Expertise: What Machines Can't Know](https://doi.org/10.1111/joms.12915) | 2023 | 8 | 58 | Journal of Management Studies | Pauli Pakarinen, Ruthanne Huising |
| 9 | [Elements of Professional Expertise](https://doi.org/10.1177/0003122415601157) | 2015 | 8 | 101 | American Sociological Review | Rebecca L. Sandefur |
| 10 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 8 | 39232 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 128 | 114163 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 87 | 40708 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 37 | 26188 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 30 | 6906 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 25 | 28170 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 23 | 30776 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 21 | 14859 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 8 | [Machine Learning: Algorithms, Real-World Applications and Research Directions](https://doi.org/10.1007/s42979-021-00592-x) | 2021 | 20 | 4363 | SN Computer Science | Iqbal H. Sarker |
| 9 | [Machine learning for molecular and materials science](https://doi.org/10.1038/s41586-018-0337-2) | 2018 | 18 | 3941 | Nature | Keith T. Butler, Daniel W. Davies, Hugh Cartwright, et al. |
| 10 | [Bagging Predictors](https://doi.org/10.1023/a:1018054314350) | 1996 | 17 | 16262 | Machine Learning | Leo Breiman |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 12 | 892 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 9 | 1288 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 3 | [KEGG: biological systems database as a model of the real world](https://doi.org/10.1093/nar/gkae909) | 2024 | 8 | 1074 | Nucleic Acids Research | Minoru Kanehisa, Miho Furumichi, Yoko Sato, et al. |
| 4 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 12862 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 5 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 8 | 16884 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 6 | [A practical guide to machine learning interatomic potentials – Status and future](https://doi.org/10.1016/j.cossms.2025.101214) | 2025 | 7 | 57 | Current Opinion in Solid State and Materials Science | Ryan Jacobs, Dane Morgan, Siamak Attarian, et al. |
| 7 | [Feature selection strategies: a comparative analysis of SHAP-value and importance-based methods](https://doi.org/10.1186/s40537-024-00905-w) | 2024 | 7 | 240 | Journal Of Big Data | Huanjing Wang, Qianxin Liang, John Hancock, et al. |
| 8 | [PubChem 2023 update](https://doi.org/10.1093/nar/gkac956) | 2022 | 7 | 2585 | Nucleic Acids Research | Sunghwan Kim, Jie Chen, Tiejun Cheng, et al. |
| 9 | [The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts](https://doi.org/10.1021/acscatal.2c05426) | 2023 | 6 | 209 | ACS Catalysis | Richard Tran, Janice Lan, Muhammed Shuaibi, et al. |
| 10 | [A Review of Evaluation Metrics in Machine Learning Algorithms](https://doi.org/10.1007/978-3-031-35314-7_2) | 2023 | 6 | 255 | Lecture notes in networks and systems | Gireen Naidu, Tranos Zuva, Elias Mmbongeni Sibanda |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A practical guide to machine learning interatomic potentials – Status and future](https://doi.org/10.1016/j.cossms.2025.101214) | 2025 | 7 | 57 | Current Opinion in Solid State and Materials Science | Ryan Jacobs, Dane Morgan, Siamak Attarian, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 2185 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 16 | 9086 |  | Nils Reimers, Iryna Gurevych |
| 3 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 15 | 316 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 4 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 15 | 30258 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 5 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 14 | 289 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 14 | 1677 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 2418 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 14 | 2995 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 9 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4142 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 10 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 2334 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 19 | 2185 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 15 | 316 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 3 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 14 | 289 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 4 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 14 | 1677 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 2418 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 14 | 2995 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 2334 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 8 | [ChatGPT Utility in Healthcare Education, Research, and Practice: Systematic Review on the Promising Perspectives and Valid Concerns](https://doi.org/10.3390/healthcare11060887) | 2023 | 10 | 2342 | Healthcare | Malik Sallam |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 9 | 712 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [BioGPT: generative pre-trained transformer for biomedical text generation and mining](https://doi.org/10.1093/bib/bbac409) | 2022 | 9 | 792 | Briefings in Bioinformatics | Renqian Luo, Liai Sun, Yingce Xia, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [An outline of Prognostics and health management Large Model: Concepts, Paradigms, and challenges](https://doi.org/10.1016/j.ymssp.2025.112683) | 2025 | 4 | 5 | Mechanical Systems and Signal Processing | Laifa Tao, Shangyu Li, Haifei Liu, et al. |
| 2 | [Take caution in using LLMs as human surrogates](https://doi.org/10.1073/pnas.2501660122) | 2025 | 4 | 7 | Proceedings of the National Academy of Sciences | Yuan Gao, Dokyun Lee, Gordon Burtch, et al. |
| 3 | [LawBench: Benchmarking Legal Knowledge of Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.452) | 2024 | 6 | 32 |  | Zhiwei Fei, Xiaoyu Shen, Dawei Zhu, et al. |
| 4 | [How should the advancement of large language models affect the practice of science?](https://doi.org/10.1073/pnas.2401227121) | 2025 | 4 | 23 | Proceedings of the National Academy of Sciences | Marcel Binz, Stephan Alaniz, Adina L. Roskies, et al. |
| 5 | [Inadequacies of Large Language Model Benchmarks in the Era of Generative Artificial Intelligence](https://doi.org/10.1109/tai.2025.3569516) | 2025 | 5 | 32 | IEEE Transactions on Artificial Intelligence | Timothy R. McIntosh, Teo Sušnjak, Nalin Asanka Gamagedara Arachchilage, et al. |
| 6 | [Benchmarking large language models for biomedical natural language processing applications and recommendations](https://doi.org/10.1038/s41467-025-56989-2) | 2025 | 6 | 40 | Nature Communications | Qingyu Chen, Yan Hu, Xueqing Peng, et al. |
| 7 | [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?): A Comprehensive Evaluation, Framework, and Benchmarks](https://doi.org/10.1109/sp54263.2024.00210) | 2024 | 6 | 43 |  | Saad Ullah, Mingji Han, Saurabh Pujar, et al. |
| 8 | [Finetuning Large Language Models for Vulnerability Detection](https://doi.org/10.1109/access.2025.3546700) | 2025 | 4 | 33 | IEEE Access | Aleksei Shestov, Rodion Levichev, Ravil Mussabayev, et al. |
| 9 | [Harnessing attention mechanisms in a comprehensive deep learning approach for induction motor fault diagnosis using raw electrical signals](https://doi.org/10.1016/j.engappai.2023.107643) | 2023 | 4 | 39 | Engineering Applications of Artificial Intelligence | Thanh-Tung Vo, Meng‐Kun Liu, Minh‐Quang Tran |
| 10 | [Large Language Model Capabilities in Perioperative Risk Prediction and Prognostication](https://doi.org/10.1001/jamasurg.2024.1621) | 2024 | 5 | 51 | JAMA Surgery | Philip Chung, Christine T. Fong, Andrew M. Walters, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Much Realistic, Such Wow! A Systematic Literature Review of Realism in Digital Games](https://doi.org/10.1145/3491102.3501875) | 2022 | 4 | 36 | CHI Conference on Human Factors in Computing Systems | Katja Rogers, Sukran Karaosmanoglu, Maximilian Altmeyer, et al. |
| 2 | [Optimal pricing and remanufacturing decisions in supply chains: navigating internal and external competition in duopoly markets using a Stackelberg-Nash game theoretical framework](https://doi.org/10.1007/s13243-024-00144-5) | 2024 | 2 | 1 | Journal of remanufacturing | Najmeh Abbasi, M. M. Lotfi, Davood Shishebori, et al. |
| 3 | [Ocean Literacy, Climate Change and Health in Coastal Living Environments: A Scoping Review and Bibliometric Analysis (ScoRBA)](https://doi.org/10.1051/bioconf/202413300026) | 2024 | 2 | 1 | BIO Web of Conferences | Jazimatul Husna, Adi Wijaya, Izni Syahrizal Ibrahim, et al. |
| 4 | [Energy pricing and investigating international trade law considering renewable energy investments under the cap-and-trade system: A game theoretic approach](https://doi.org/10.1016/j.apenergy.2024.125155) | 2024 | 2 | 2 | Applied Energy | Sima Amiri-Pebdani, Mahdi Alinaghian, Hossein Khosroshahi |
| 5 | [Pricing and green quality decisions in two-stage green supply chain for substitutable green products: A game-theoretic approach](https://doi.org/10.1051/ro/2024143) | 2024 | 2 | 2 | RAIRO. Operations research | Shivendra Kumar Gupta, Vinod Kumar Mishra |
| 6 | [Under the context of competition between platform sales and live streaming sales, who has the pricing power of products?](https://doi.org/10.1057/s41599-024-03690-2) | 2024 | 2 | 0 | Humanities and Social Sciences Communications | Shizhen Bai, Yun Xu, Hao He, et al. |
| 7 | [Analyzing the Price Strategy of Closed-Loop Supply Chain, Carbon Emission Policy and Game Theory Perspective: A Systematic and Bibliometric Review](https://doi.org/10.46254/au01.20220314) | 2023 | 2 | 0 |  | Rita Desyanti, Niniet Indah Arvitrida |
| 8 | [Bearing remanufacturing practices: a case study in PT. SKF Indonesia](https://doi.org/10.31603/biseeng.372) | 2025 | 2 | 0 | BIS Energy and Engineering | Rita Desyanti, Suparno Suparno, Niniet Indah Arvitrida |
| 9 | [Remanufacturing Practices in Indonesia: Case Studies on Heavy-Duty and Off-Road, Bearings and Cartridges](https://doi.org/10.3233/atde250545) | 2025 | 2 | 0 | Advances in transdisciplinary engineering | Rita Desyanti, Suparno, Niniet Indah Arvitrida |
| 10 | [Sustainable supply chain modeling: a review based on the application of the system dynamics approach](https://doi.org/10.11591/ijeecs.v37.i3.pp1637-1649) | 2025 | 2 | 0 | Indonesian Journal of Electrical Engineering and Computer Science | Julia Kurniasih, Zuraida Abal Abas, Siti Azirah Asmai, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Much Realistic, Such Wow! A Systematic Literature Review of Realism in Digital Games](https://doi.org/10.1145/3491102.3501875) | 2022 | 4 | 36 | CHI Conference on Human Factors in Computing Systems | Katja Rogers, Sukran Karaosmanoglu, Maximilian Altmeyer, et al. |
| 2 | [Optimal pricing and remanufacturing decisions in supply chains: navigating internal and external competition in duopoly markets using a Stackelberg-Nash game theoretical framework](https://doi.org/10.1007/s13243-024-00144-5) | 2024 | 2 | 1 | Journal of remanufacturing | Najmeh Abbasi, M. M. Lotfi, Davood Shishebori, et al. |
| 3 | [Ocean Literacy, Climate Change and Health in Coastal Living Environments: A Scoping Review and Bibliometric Analysis (ScoRBA)](https://doi.org/10.1051/bioconf/202413300026) | 2024 | 2 | 1 | BIO Web of Conferences | Jazimatul Husna, Adi Wijaya, Izni Syahrizal Ibrahim, et al. |
| 4 | [Energy pricing and investigating international trade law considering renewable energy investments under the cap-and-trade system: A game theoretic approach](https://doi.org/10.1016/j.apenergy.2024.125155) | 2024 | 2 | 2 | Applied Energy | Sima Amiri-Pebdani, Mahdi Alinaghian, Hossein Khosroshahi |
| 5 | [Pricing and green quality decisions in two-stage green supply chain for substitutable green products: A game-theoretic approach](https://doi.org/10.1051/ro/2024143) | 2024 | 2 | 2 | RAIRO. Operations research | Shivendra Kumar Gupta, Vinod Kumar Mishra |
| 6 | [Under the context of competition between platform sales and live streaming sales, who has the pricing power of products?](https://doi.org/10.1057/s41599-024-03690-2) | 2024 | 2 | 0 | Humanities and Social Sciences Communications | Shizhen Bai, Yun Xu, Hao He, et al. |
| 7 | [Analyzing the Price Strategy of Closed-Loop Supply Chain, Carbon Emission Policy and Game Theory Perspective: A Systematic and Bibliometric Review](https://doi.org/10.46254/au01.20220314) | 2023 | 2 | 0 |  | Rita Desyanti, Niniet Indah Arvitrida |
| 8 | [Bearing remanufacturing practices: a case study in PT. SKF Indonesia](https://doi.org/10.31603/biseeng.372) | 2025 | 2 | 0 | BIS Energy and Engineering | Rita Desyanti, Suparno Suparno, Niniet Indah Arvitrida |
| 9 | [Remanufacturing Practices in Indonesia: Case Studies on Heavy-Duty and Off-Road, Bearings and Cartridges](https://doi.org/10.3233/atde250545) | 2025 | 2 | 0 | Advances in transdisciplinary engineering | Rita Desyanti, Suparno, Niniet Indah Arvitrida |
| 10 | [Sustainable supply chain modeling: a review based on the application of the system dynamics approach](https://doi.org/10.11591/ijeecs.v37.i3.pp1637-1649) | 2025 | 2 | 0 | Indonesian Journal of Electrical Engineering and Computer Science | Julia Kurniasih, Zuraida Abal Abas, Siti Azirah Asmai, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Optimal pricing and remanufacturing decisions in supply chains: navigating internal and external competition in duopoly markets using a Stackelberg-Nash game theoretical framework](https://doi.org/10.1007/s13243-024-00144-5) | 2024 | 2 | 1 | Journal of remanufacturing | Najmeh Abbasi, M. M. Lotfi, Davood Shishebori, et al. |
| 2 | [Ocean Literacy, Climate Change and Health in Coastal Living Environments: A Scoping Review and Bibliometric Analysis (ScoRBA)](https://doi.org/10.1051/bioconf/202413300026) | 2024 | 2 | 1 | BIO Web of Conferences | Jazimatul Husna, Adi Wijaya, Izni Syahrizal Ibrahim, et al. |
| 3 | [Energy pricing and investigating international trade law considering renewable energy investments under the cap-and-trade system: A game theoretic approach](https://doi.org/10.1016/j.apenergy.2024.125155) | 2024 | 2 | 2 | Applied Energy | Sima Amiri-Pebdani, Mahdi Alinaghian, Hossein Khosroshahi |
| 4 | [Pricing and green quality decisions in two-stage green supply chain for substitutable green products: A game-theoretic approach](https://doi.org/10.1051/ro/2024143) | 2024 | 2 | 2 | RAIRO. Operations research | Shivendra Kumar Gupta, Vinod Kumar Mishra |
| 5 | [Under the context of competition between platform sales and live streaming sales, who has the pricing power of products?](https://doi.org/10.1057/s41599-024-03690-2) | 2024 | 2 | 0 | Humanities and Social Sciences Communications | Shizhen Bai, Yun Xu, Hao He, et al. |
| 6 | [Analyzing the Price Strategy of Closed-Loop Supply Chain, Carbon Emission Policy and Game Theory Perspective: A Systematic and Bibliometric Review](https://doi.org/10.46254/au01.20220314) | 2023 | 2 | 0 |  | Rita Desyanti, Niniet Indah Arvitrida |
| 7 | [Bearing remanufacturing practices: a case study in PT. SKF Indonesia](https://doi.org/10.31603/biseeng.372) | 2025 | 2 | 0 | BIS Energy and Engineering | Rita Desyanti, Suparno Suparno, Niniet Indah Arvitrida |
| 8 | [Remanufacturing Practices in Indonesia: Case Studies on Heavy-Duty and Off-Road, Bearings and Cartridges](https://doi.org/10.3233/atde250545) | 2025 | 2 | 0 | Advances in transdisciplinary engineering | Rita Desyanti, Suparno, Niniet Indah Arvitrida |
| 9 | [Sustainable supply chain modeling: a review based on the application of the system dynamics approach](https://doi.org/10.11591/ijeecs.v37.i3.pp1637-1649) | 2025 | 2 | 0 | Indonesian Journal of Electrical Engineering and Computer Science | Julia Kurniasih, Zuraida Abal Abas, Siti Azirah Asmai, et al. |
| 10 | [Coordinating a closed-loop green supply chain for remanufactured product under competition](https://doi.org/10.24200/sci.2021.58167.5598) | 2021 | 2 | 0 | Scientia Iranica | Chirantan Mondal, Bibhas C. Giri |
<!-- TRENDING-END -->
