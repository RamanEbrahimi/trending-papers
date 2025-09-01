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

Last update: 2025-09-01 06:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 10 | 57432 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 9 | 148106 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 7 | 5194 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 4 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 7 | 56829 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 5 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 7 | 75031 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 6 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 7 | 94509 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 7 | [Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) | 1995 | 7 | 99572 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Yoav Benjamini, Yosef Hochberg |
| 8 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 12687 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 9 | [Firm Resources and Sustained Competitive Advantage](https://doi.org/10.1177/014920639101700108) | 1991 | 6 | 40500 | Journal of Management | Jay B. Barney |
| 10 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 6 | 92112 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 114 | 108482 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 37 | 24691 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 27 | 6063 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 4 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 25 | 12038 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 19 | 70731 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 18 | 26090 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 15 | 47985 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 8 | [Regularization Paths for Generalized Linear Models via Coordinate Descent](https://doi.org/10.18637/jss.v033.i01) | 2010 | 14 | 14178 | Journal of Statistical Software | Jerome H. Friedman, Trevor Hastie, Robert Tibshirani |
| 9 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 14 | 30117 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 10 | [limma powers differential expression analyses for RNA-sequencing and microarray studies](https://doi.org/10.1093/nar/gkv007) | 2015 | 14 | 33966 | Nucleic Acids Research | Matthew E. Ritchie, Belinda Phipson, Di Wu, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [<i>ggtranscript</i>: an R package for the visualization and interpretation of transcript isoforms using<i>ggplot2</i>](https://doi.org/10.1093/bioinformatics/btac409) | 2022 | 5 | 318 | Bioinformatics | Emil K. Gustavsson, David Zhang, Regina H. Reynolds, et al. |
| 2 | [A comparative analysis of K-Nearest Neighbor, Genetic, Support Vector Machine, Decision Tree, and Long Short Term Memory algorithms in machine learning](https://doi.org/10.1016/j.dajour.2022.100071) | 2022 | 5 | 465 | Decision Analytics Journal | Malti Bansal, Apoorva Goyal, Apoorva Choudhary |
| 3 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 5 | 530 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 4 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 5 | 1080 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 5 | [Ensemble deep learning: A review](https://doi.org/10.1016/j.engappai.2022.105151) | 2022 | 5 | 1437 | Engineering Applications of Artificial Intelligence | M. A. Ganaie, Minghui Hu, A. K. Malik, et al. |
| 6 | [The STRING database in 2023: protein–protein association networks and functional enrichment analyses for any sequenced genome of interest](https://doi.org/10.1093/nar/gkac1000) | 2022 | 5 | 4734 | Nucleic Acids Research | Damian Szklarczyk, Rebecca Kirsch, Mikaela Koutrouli, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 16 | 13535 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 1780 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 10 | 2659 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 1833 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 8 | 19925 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 6 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 1499 | arXiv (Cornell University) | OpenAI |
| 7 | [Testing theory of mind in large language models and humans](https://doi.org/10.1038/s41562-024-01882-z) | 2024 | 6 | 97 | Nature Human Behaviour | James W. A. Strachan, Dalila Albergo, Giulia Borghini, et al. |
| 8 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 98 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 9 | [A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly](https://doi.org/10.1016/j.hcc.2024.100211) | 2024 | 6 | 333 | High-Confidence Computing | Yifan Yao, Jinhao Duan, Kaidi Xu, et al. |
| 10 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 6 | 1690 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 12 | 1780 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 2 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 10 | 2659 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 1833 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 1499 | arXiv (Cornell University) | OpenAI |
| 5 | [Testing theory of mind in large language models and humans](https://doi.org/10.1038/s41562-024-01882-z) | 2024 | 6 | 97 | Nature Human Behaviour | James W. A. Strachan, Dalila Albergo, Giulia Borghini, et al. |
| 6 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 98 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 7 | [A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly](https://doi.org/10.1016/j.hcc.2024.100211) | 2024 | 6 | 333 | High-Confidence Computing | Yifan Yao, Jinhao Duan, Kaidi Xu, et al. |
| 8 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 6 | 1690 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 9 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via
  Reinforcement Learning](https://doi.org/10.48550/arxiv.2501.12948) | 2025 | 5 | 163 | arXiv (Cornell University) | DeepSeek-AI, Daya Guo, Dejian Yang, et al. |
| 10 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 5 | 2858 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [NetConfEval: Can LLMs Facilitate Network Configuration?](https://doi.org/10.1145/3656296) | 2024 | 2 | 9 | Proceedings of the ACM on Networking | Changjie Wang, Mariano Scazzariello, Alireza Farshin, et al. |
| 2 | [Sociodemographic biases in medical decision making by large language models](https://doi.org/10.1038/s41591-025-03626-6) | 2025 | 3 | 14 | Nature Medicine | Mahmud Omar, Shelly Soffer, Reem Agbareia, et al. |
| 3 | [Using large language models (<scp>ChatGPT</scp>, Copilot, <scp>PaLM</scp>, Bard, and Gemini) in Gross Anatomy course: Comparative analysis](https://doi.org/10.1002/ca.24244) | 2024 | 3 | 17 | Clinical Anatomy | Volodymyr Mavrych, Paul Ganguly, Olena Bolgova |
| 4 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 4 | 28 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |
| 5 | [FFA-GPT: an automated pipeline for fundus fluorescein angiography interpretation and question-answer](https://doi.org/10.1038/s41746-024-01101-z) | 2024 | 3 | 27 | npj Digital Medicine | Xiaolan Chen, Weiyi Zhang, Pusheng Xu, et al. |
| 6 | [Empowering digital twins with large language models for global temporal feature learning](https://doi.org/10.1016/j.jmsy.2024.02.015) | 2024 | 3 | 30 | Journal of Manufacturing Systems | Yicheng Sun, Qi Zhang, Jinsong Bao, et al. |
| 7 | [The impact of large language models on higher education: exploring the connection between AI and Education 4.0](https://doi.org/10.3389/feduc.2024.1392091) | 2024 | 2 | 21 | Frontiers in Education | Iris Cristina Peláez‐Sánchez, Davis Velarde-Camaqui, Leonardo David Glasserman‐Morales |
| 8 | [The Opportunities and Risks of Large Language Models in Mental Health](https://doi.org/10.2196/59479) | 2024 | 3 | 39 | JMIR Mental Health | Hannah R. Lawrence, Renee Schneider, Susan B. Rubin, et al. |
| 9 | [LLaVA-MR: Large Language-and-Vision Assistant for Video Moment Retrieval](https://doi.org/10.32388/vlxb6m) | 2024 | 3 | 39 |  | Jianping Li |
| 10 | [Current applications and challenges in large language models for patient care: a systematic review](https://doi.org/10.1038/s43856-024-00717-2) | 2025 | 3 | 44 | Communications Medicine | Felix Busch, Lena Hoffmann, Christopher Rueger, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary stable strategies and game dynamics](https://doi.org/10.1016/0025-5564(78)90077-9) | 1978 | 2 | 3329 | Mathematical Biosciences | Peter Taylor, Leo Jonker |
| 2 | [Equilibrium points in <i>n</i> -person games](https://doi.org/10.1073/pnas.36.1.48) | 1950 | 2 | 7051 | Proceedings of the National Academy of Sciences | John F. Nash |
| 3 | [Study on Local Architectural Heritage Protection Based on the Concept of Ecomuseum](https://doi.org/10.2991/ahti-19.2019.65) | 2019 | 1 | 1 |  | Tianhang Wang |
| 4 | [GeoShapley: A Game Theory Approach to Measuring Spatial Effects in Machine Learning Models](https://doi.org/10.48550/arxiv.2312.03675) | 2023 | 1 | 1 | arXiv (Cornell University) | Ziqi Li |
| 5 | [Buffer zone policy and its impact on the land value and the quality of the built environment in world heritage sites: the case of kampung jawa, melaka, malaysia](https://doi.org/10.23968/2500-0055-2024-9-1-91-102) | 2024 | 1 | 1 | Architecture and Engineering | Seyed Mohammad Mousavi, S. Mohammad E. Hosseini-Nasab, Waqas Ahmed Mahar |
| 6 | [Social and Ecological Impacts of Agricultural Land Use Change](https://openalex.org/W3197589697) | 2018 | 1 | 1 |  | Doroudian Hamidreza, Doroudian Atefeh |
| 7 | [Agricultural Lands Preservation Plans and Laws in Iran: A Case Study](https://doi.org/10.5772/intechopen.107288) | 2022 | 1 | 0 | IntechOpen eBooks | Mohsen Armin |
| 8 | [Delineating protective boundaries using the HUL approach a case study: heritage waterways of Isfahan](https://doi.org/10.1108/jchmsd-03-2022-0035) | 2023 | 1 | 3 | Journal of Cultural Heritage Management and Sustainable Development | Elnaz Chitsazzadeh, Mahsa Chizfahm Daneshmandian, Najmeh Jahani, et al. |
| 9 | [The World Heritage Convention and the Buffer Zone](https://doi.org/10.11588/hr.2008.0.19884) | 2015 | 1 | 4 | Heritage at risk | Icomos Iclafi |
| 10 | [Application of a Coordination Model for a Large Number of Stakeholders with a New Game Theory Model](https://doi.org/10.1007/s11269-019-02431-4) | 2019 | 1 | 4 | Water Resources Management | Mohammad Ehteram, Samira Ghotbi, Özgür Kişi, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [GeoShapley: A Game Theory Approach to Measuring Spatial Effects in Machine Learning Models](https://doi.org/10.48550/arxiv.2312.03675) | 2023 | 1 | 1 | arXiv (Cornell University) | Ziqi Li |
| 2 | [Buffer zone policy and its impact on the land value and the quality of the built environment in world heritage sites: the case of kampung jawa, melaka, malaysia](https://doi.org/10.23968/2500-0055-2024-9-1-91-102) | 2024 | 1 | 1 | Architecture and Engineering | Seyed Mohammad Mousavi, S. Mohammad E. Hosseini-Nasab, Waqas Ahmed Mahar |
| 3 | [Agricultural Lands Preservation Plans and Laws in Iran: A Case Study](https://doi.org/10.5772/intechopen.107288) | 2022 | 1 | 0 | IntechOpen eBooks | Mohsen Armin |
| 4 | [Delineating protective boundaries using the HUL approach a case study: heritage waterways of Isfahan](https://doi.org/10.1108/jchmsd-03-2022-0035) | 2023 | 1 | 3 | Journal of Cultural Heritage Management and Sustainable Development | Elnaz Chitsazzadeh, Mahsa Chizfahm Daneshmandian, Najmeh Jahani, et al. |
| 5 | [Exploring mechanisms affecting environmental risk coping behaviors: evidence from China](https://doi.org/10.1007/s11356-023-31221-0) | 2023 | 1 | 4 | Environmental Science and Pollution Research | Lan Lan, Tianjing Huang, Yanqiang Du, et al. |
| 6 | [Analysing urban local cold air dynamics and climate functional zones using interpretable machine learning: A case study of Tianhe district, Guangzhou](https://doi.org/10.1016/j.scs.2024.105731) | 2024 | 1 | 5 | Sustainable Cities and Society | Shifu Wang, Xiangcheng Zeng, Yueyang Huang, et al. |
| 7 | [Smallholder agriculture in African dryland agroecosystems has limited impact on trophic group composition, but affects arthropod provision of ecosystem services](https://doi.org/10.1016/j.agee.2023.108860) | 2023 | 1 | 6 | Agriculture Ecosystems & Environment | Klaus Birkhofer, Tharina L. Bird, Martha Alfeus, et al. |
| 8 | [Analysis of internal processes of conflict behavior among Iranian rangeland exploiters: Application of environmental psychology](https://doi.org/10.3389/fpsyg.2022.957760) | 2022 | 1 | 7 | Frontiers in Psychology | Latif Haji, Dariush Hayati |
| 9 | [Sustaining tranquility in small urban green parks: A modeling approach to identify noise pollution contributors](https://doi.org/10.1016/j.scs.2024.105655) | 2024 | 1 | 8 | Sustainable Cities and Society | Maryam Arsalan, Atefeh Chamani, Rasool Zamani‐Ahmadmahmoodi |
| 10 | [Explainable dimensionality reduction (XDR) to unbox AI ‘black box’ models: A study of AI perspectives on the ethnic styles of village dwellings](https://doi.org/10.1057/s41599-023-01505-4) | 2023 | 1 | 11 | Humanities and Social Sciences Communications | Xun Li, Dongsheng Chen, Weipan Xu, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Study on Local Architectural Heritage Protection Based on the Concept of Ecomuseum](https://doi.org/10.2991/ahti-19.2019.65) | 2019 | 1 | 1 |  | Tianhang Wang |
| 2 | [GeoShapley: A Game Theory Approach to Measuring Spatial Effects in Machine Learning Models](https://doi.org/10.48550/arxiv.2312.03675) | 2023 | 1 | 1 | arXiv (Cornell University) | Ziqi Li |
| 3 | [Buffer zone policy and its impact on the land value and the quality of the built environment in world heritage sites: the case of kampung jawa, melaka, malaysia](https://doi.org/10.23968/2500-0055-2024-9-1-91-102) | 2024 | 1 | 1 | Architecture and Engineering | Seyed Mohammad Mousavi, S. Mohammad E. Hosseini-Nasab, Waqas Ahmed Mahar |
| 4 | [Social and Ecological Impacts of Agricultural Land Use Change](https://openalex.org/W3197589697) | 2018 | 1 | 1 |  | Doroudian Hamidreza, Doroudian Atefeh |
| 5 | [Agricultural Lands Preservation Plans and Laws in Iran: A Case Study](https://doi.org/10.5772/intechopen.107288) | 2022 | 1 | 0 | IntechOpen eBooks | Mohsen Armin |
| 6 | [Delineating protective boundaries using the HUL approach a case study: heritage waterways of Isfahan](https://doi.org/10.1108/jchmsd-03-2022-0035) | 2023 | 1 | 3 | Journal of Cultural Heritage Management and Sustainable Development | Elnaz Chitsazzadeh, Mahsa Chizfahm Daneshmandian, Najmeh Jahani, et al. |
| 7 | [The World Heritage Convention and the Buffer Zone](https://doi.org/10.11588/hr.2008.0.19884) | 2015 | 1 | 4 | Heritage at risk | Icomos Iclafi |
| 8 | [Application of a Coordination Model for a Large Number of Stakeholders with a New Game Theory Model](https://doi.org/10.1007/s11269-019-02431-4) | 2019 | 1 | 4 | Water Resources Management | Mohammad Ehteram, Samira Ghotbi, Özgür Kişi, et al. |
| 9 | [Monthly Allocation of Water Resources and Pollutant Loads in a Basin Based on the Water Footprint and Fallback Bargaining](https://doi.org/10.3390/su11236836) | 2019 | 1 | 4 | Sustainability | Yinglan Xue, Yan Chen, Dan Cui, et al. |
| 10 | [Exploring mechanisms affecting environmental risk coping behaviors: evidence from China](https://doi.org/10.1007/s11356-023-31221-0) | 2023 | 1 | 4 | Environmental Science and Pollution Research | Lan Lan, Tianjing Huang, Yanqiang Du, et al. |
<!-- TRENDING-END -->
