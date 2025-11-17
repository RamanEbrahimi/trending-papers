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

Last update: 2025-11-17 06:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [THE PRIMACY OF TRUTH AND THE ERROR OF ZERO](https://doi.org/10.5281/zenodo.17518273) | 2025 | 7 | 38 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 2 | [ENERGY FIRST: Matter as the Lowest State of Organized Energy and the Human Condition in a Finite Cosmos](https://doi.org/10.5281/zenodo.17545100) | 2025 | 6 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 3 | [AVOIDING COLLAPSE: The Mathematical Error Behind Modern Civilization, and the Path to Restoration](https://doi.org/10.5281/zenodo.17544580) | 2025 | 6 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 4 | [A–B–K: The Ancient Formula of Balanced Creation: From Avra K'davra to the Law A × B = K](https://doi.org/10.5281/zenodo.17538809) | 2025 | 6 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 5 | [THE MATHEMATICAL STRUCTURE OF GOOD AND EVIL: Why Morality is a Physical Law in a Finite Universe](https://doi.org/10.5281/zenodo.17534373) | 2025 | 6 | 21 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 6 | [THE SUPREMACY OF TRUTH: How Every Finite System in Reality Obeys a Single Law of Balance](https://doi.org/10.5281/zenodo.17534112) | 2025 | 6 | 23 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 7 | [LOVE AS THE STRUCTURAL PRINCIPLE OF LIFE: A Unified Framework for Growth, Connection, and Bound Autonomy](https://doi.org/10.5281/zenodo.17527799) | 2025 | 6 | 33 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 8 | [THE PRIMACY OF FINITUDE AND THE ERROR OF INFINITY](https://doi.org/10.5281/zenodo.17524360) | 2025 | 6 | 35 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 9 | [TRUE ALCHEMY: The Universal Law of Balance in Physical, Biological, and Moral Systems](https://doi.org/10.5281/zenodo.17523684) | 2025 | 6 | 35 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |
| 10 | [THE END OF CONTINUITY: Why Spacetime Cannot Be Infinitely Divisible, and Why Reality Requires a Minimal Unit](https://doi.org/10.5281/zenodo.17525939) | 2025 | 6 | 35 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 113 | 113989 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 80 | 40587 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 28 | 26138 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 20 | 28128 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 75077 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 16 | 5487 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 15 | 6882 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 14 | 14838 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 9 | [Support-vector networks](https://doi.org/10.1007/bf00994018) | 1995 | 14 | 39261 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 10 | [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | 1986 | 12 | 28682 | Nature | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 10 | 16770 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 8 | 875 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 6 | 212 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 4 | [Feature selection strategies: a comparative analysis of SHAP-value and importance-based methods](https://doi.org/10.1186/s40537-024-00905-w) | 2024 | 5 | 238 | Journal Of Big Data | Huanjing Wang, Qianxin Liang, John Hancock, et al. |
| 5 | [Data-Driven Machine Learning in Environmental Pollution: Gains and Problems](https://doi.org/10.1021/acs.est.1c06157) | 2022 | 5 | 398 | Environmental Science & Technology | Xian Liu, Dawei Lü, Aiqian Zhang, et al. |
| 6 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 12853 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 7 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 4 | 213 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 8 | [Support vector machine in structural reliability analysis: A review](https://doi.org/10.1016/j.ress.2023.109126) | 2023 | 4 | 360 | Reliability Engineering & System Safety | Atin Roy, Subrata Chakraborty |
| 9 | [A review on longitudinal data analysis with random forest](https://doi.org/10.1093/bib/bbad002) | 2023 | 4 | 417 | Briefings in Bioinformatics | Jianchang Hu, Silke Szymczak |
| 10 | [A comparative analysis of K-Nearest Neighbor, Genetic, Support Vector Machine, Decision Tree, and Long Short Term Memory algorithms in machine learning](https://doi.org/10.1016/j.dajour.2022.100071) | 2022 | 4 | 600 | Decision Analytics Journal | Malti Bansal, Apoorva Goyal, Apoorva Choudhary |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 13 | 2404 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 2319 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 2173 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 3554 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 10 | 30214 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 9 | 4120 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 7 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 9 | 9068 |  | Nils Reimers, Iryna Gurevych |
| 8 | [LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://doi.org/10.18653/v1/2024.acl-demos.38) | 2024 | 8 | 171 |  | Yaowei Zheng, Richong Zhang, Junhao Zhang, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 700 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [The Probabilistic Relevance Framework: BM25 and Beyond](https://doi.org/10.1561/1500000019) | 2009 | 8 | 2441 | Foundations and Trends® in Information Retrieval | Stephen Robertson, Hugo Zaragoza |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 13 | 2404 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 2319 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 2173 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 3554 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://doi.org/10.18653/v1/2024.acl-demos.38) | 2024 | 8 | 171 |  | Yaowei Zheng, Richong Zhang, Junhao Zhang, et al. |
| 6 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 700 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 7 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 7 | 341 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 8 | [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0) | 2023 | 7 | 532 | Nature | Daniil A. Boiko, Robert MacKnight, Ben Kline, et al. |
| 9 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 7 | 573 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 10 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 7 | 3511 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](https://doi.org/10.18653/v1/2024.findings-acl.774) | 2024 | 4 | 22 |  | Gagan Bhatia, El Moatez Billah Nagoudi, Hasan Cavusoglu, et al. |
| 2 | [Large Language Models Are Clinical Reasoners: Reasoning-Aware Diagnosis Framework with Prompt-Generated Rationales](https://doi.org/10.1609/aaai.v38i16.29802) | 2024 | 3 | 20 | Proceedings of the AAAI Conference on Artificial Intelligence | Taeyoon Kwon, Kai Tzu-iunn Ong, Dong-Jin Kang, et al. |
| 3 | [Shared functional specialization in transformer-based language models and the human brain](https://doi.org/10.1038/s41467-024-49173-5) | 2024 | 3 | 28 | Nature Communications | Sreejan Kumar, Theodore R. Sumers, Takateru Yamakoshi, et al. |
| 4 | [Benchmarking large language models for biomedical natural language processing applications and recommendations](https://doi.org/10.1038/s41467-025-56989-2) | 2025 | 4 | 39 | Nature Communications | Qingyu Chen, Yan Hu, Xueqing Peng, et al. |
| 5 | [A toolbox for surfacing health equity harms and biases in large language models](https://doi.org/10.1038/s41591-024-03258-2) | 2024 | 3 | 44 | Nature Medicine | Stephen Pfohl, Heather Cole-Lewis, Rory Sayres, et al. |
| 6 | [The Temperature Feature of ChatGPT: Modifying Creativity for Clinical Research](https://doi.org/10.2196/53559) | 2024 | 4 | 63 | JMIR Human Factors | Joshua Davis, Liesbet Van Bulck, Brigitte N Durieux, et al. |
| 7 | [Large Language Models and Empathy: Systematic Review](https://doi.org/10.2196/52597) | 2024 | 4 | 67 | Journal of Medical Internet Research | Vera Sorin, Dana Brin, Yiftach Barash, et al. |
| 8 | [Towards Open-World Recommendation with Knowledge Augmentation from Large Language Models](https://doi.org/10.1145/3640457.3688104) | 2024 | 4 | 69 |  | Yunjia Xi, Weiwen Liu, Jianghao Lin, et al. |
| 9 | [LLM Based Generation of Item-Description for Recommendation System](https://doi.org/10.1145/3604915.3610647) | 2023 | 4 | 72 |  | A. Seetharama Acharya, Brijraj Singh, Naoyuki Onoe |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [An innovative strategic choice for stakeholders in the chinese traditional commercial street renewal using evolutionary game theory](https://doi.org/10.1016/j.jik.2022.100225) | 2022 | 2 | 21 | Journal of Innovation & Knowledge | Zhu Xue-xin, Qing-Rui Mu, Wen-Zhe Liang |
| 2 | [Evolution and the Theory of Games](https://doi.org/10.1017/cbo9780511806292) | 1982 | 2 | 6818 | Cambridge University Press eBooks | John Maynard Smith |
| 3 | [Hotel average daily rate and room standard in game theory](https://doi.org/10.1080/13032917.2024.2321476) | 2024 | 1 | 1 | Anatolia | Xuan Tran, Declan Carr, Destiny Owens, et al. |
| 4 | [Do Stubborn Users Always Cause More Polarization and Disagreement? A Mathematical Study](https://doi.org/10.1145/3701551.3703510) | 2025 | 1 | 2 |  | Mohammad Shirzadi, Ahad N. Zehmakan |
| 5 | [Value-Chain Finance in Greek Agriculture](https://doi.org/10.3390/su16072922) | 2024 | 1 | 2 | Sustainability | Paraskevi Boufounou, Nikolaos Lathiras, Kanellos Toudas, et al. |
| 6 | [Operational Risk Assessment of Commercial Banks’ Supply Chain Finance](https://doi.org/10.3390/systems13020076) | 2025 | 1 | 2 | Systems | Wenying Xie, Juan He, Fuyou Huang, et al. |
| 7 | [Financial Vulnerability and Risks to Growth in Emerging Markets](https://doi.org/10.1177/00194662241292664) | 2024 | 1 | 2 | The Indian Economic Journal | Viral V. Acharya, Soumya Bhadury, Jay Surti |
| 8 | [Online influence maximization under continuous independent cascade model with node-edge-level feedback](https://doi.org/10.1007/s10115-023-01982-8) | 2023 | 1 | 3 | Knowledge and Information Systems | Chao Liu, Haichao Xu, Xiaoyang Liu |
| 9 | [The Effect of Short-Term Leases on Hotel’s Agglomeration and Market-Entry Strategies: A Game Theory Approach](https://doi.org/10.1177/10963480251328372) | 2025 | 1 | 3 | Journal of Hospitality & Tourism Research | Simone Bianco, F. Zach, Manisha Singal |
| 10 | [The best hop diffusion method for dynamic relationships under the independent cascade model](https://doi.org/10.1007/s10489-022-03460-0) | 2022 | 1 | 4 | Applied Intelligence | Liqing Qiu, Yuying Liu, Xiuliang Duan |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [An innovative strategic choice for stakeholders in the chinese traditional commercial street renewal using evolutionary game theory](https://doi.org/10.1016/j.jik.2022.100225) | 2022 | 2 | 21 | Journal of Innovation & Knowledge | Zhu Xue-xin, Qing-Rui Mu, Wen-Zhe Liang |
| 2 | [Hotel average daily rate and room standard in game theory](https://doi.org/10.1080/13032917.2024.2321476) | 2024 | 1 | 1 | Anatolia | Xuan Tran, Declan Carr, Destiny Owens, et al. |
| 3 | [Do Stubborn Users Always Cause More Polarization and Disagreement? A Mathematical Study](https://doi.org/10.1145/3701551.3703510) | 2025 | 1 | 2 |  | Mohammad Shirzadi, Ahad N. Zehmakan |
| 4 | [Value-Chain Finance in Greek Agriculture](https://doi.org/10.3390/su16072922) | 2024 | 1 | 2 | Sustainability | Paraskevi Boufounou, Nikolaos Lathiras, Kanellos Toudas, et al. |
| 5 | [Operational Risk Assessment of Commercial Banks’ Supply Chain Finance](https://doi.org/10.3390/systems13020076) | 2025 | 1 | 2 | Systems | Wenying Xie, Juan He, Fuyou Huang, et al. |
| 6 | [Financial Vulnerability and Risks to Growth in Emerging Markets](https://doi.org/10.1177/00194662241292664) | 2024 | 1 | 2 | The Indian Economic Journal | Viral V. Acharya, Soumya Bhadury, Jay Surti |
| 7 | [Online influence maximization under continuous independent cascade model with node-edge-level feedback](https://doi.org/10.1007/s10115-023-01982-8) | 2023 | 1 | 3 | Knowledge and Information Systems | Chao Liu, Haichao Xu, Xiaoyang Liu |
| 8 | [The Effect of Short-Term Leases on Hotel’s Agglomeration and Market-Entry Strategies: A Game Theory Approach](https://doi.org/10.1177/10963480251328372) | 2025 | 1 | 3 | Journal of Hospitality & Tourism Research | Simone Bianco, F. Zach, Manisha Singal |
| 9 | [The best hop diffusion method for dynamic relationships under the independent cascade model](https://doi.org/10.1007/s10489-022-03460-0) | 2022 | 1 | 4 | Applied Intelligence | Liqing Qiu, Yuying Liu, Xiuliang Duan |
| 10 | [A novel consensus model considering individual and social behaviors under the social trust network](https://doi.org/10.1016/j.ins.2024.120587) | 2024 | 1 | 6 | Information Sciences | Fei Teng, Xinran Liu, Xin Dong, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Hotel average daily rate and room standard in game theory](https://doi.org/10.1080/13032917.2024.2321476) | 2024 | 1 | 1 | Anatolia | Xuan Tran, Declan Carr, Destiny Owens, et al. |
| 2 | [Do Stubborn Users Always Cause More Polarization and Disagreement? A Mathematical Study](https://doi.org/10.1145/3701551.3703510) | 2025 | 1 | 2 |  | Mohammad Shirzadi, Ahad N. Zehmakan |
| 3 | [Value-Chain Finance in Greek Agriculture](https://doi.org/10.3390/su16072922) | 2024 | 1 | 2 | Sustainability | Paraskevi Boufounou, Nikolaos Lathiras, Kanellos Toudas, et al. |
| 4 | [Operational Risk Assessment of Commercial Banks’ Supply Chain Finance](https://doi.org/10.3390/systems13020076) | 2025 | 1 | 2 | Systems | Wenying Xie, Juan He, Fuyou Huang, et al. |
| 5 | [Financial Vulnerability and Risks to Growth in Emerging Markets](https://doi.org/10.1177/00194662241292664) | 2024 | 1 | 2 | The Indian Economic Journal | Viral V. Acharya, Soumya Bhadury, Jay Surti |
| 6 | [Online influence maximization under continuous independent cascade model with node-edge-level feedback](https://doi.org/10.1007/s10115-023-01982-8) | 2023 | 1 | 3 | Knowledge and Information Systems | Chao Liu, Haichao Xu, Xiaoyang Liu |
| 7 | [The Effect of Short-Term Leases on Hotel’s Agglomeration and Market-Entry Strategies: A Game Theory Approach](https://doi.org/10.1177/10963480251328372) | 2025 | 1 | 3 | Journal of Hospitality & Tourism Research | Simone Bianco, F. Zach, Manisha Singal |
| 8 | [The best hop diffusion method for dynamic relationships under the independent cascade model](https://doi.org/10.1007/s10489-022-03460-0) | 2022 | 1 | 4 | Applied Intelligence | Liqing Qiu, Yuying Liu, Xiuliang Duan |
| 9 | [A novel consensus model considering individual and social behaviors under the social trust network](https://doi.org/10.1016/j.ins.2024.120587) | 2024 | 1 | 6 | Information Sciences | Fei Teng, Xinran Liu, Xin Dong, et al. |
| 10 | [Nonlinear Opinion Dynamics Models With Stubborn Individuals Over Signed Graphs](https://doi.org/10.1109/tcns.2022.3210293) | 2022 | 1 | 6 | IEEE Transactions on Control of Network Systems | Nima Zahabi, Daigo Shishika |
<!-- TRENDING-END -->
