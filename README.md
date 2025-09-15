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

Last update: 2025-09-15 06:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 8 | 57281 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 2 | [R: A Language and Environment for Statistical Computing](https://doi.org/10.32614/r.manuals) | 2000 | 7 | 10804 |  | Unknown |
| 3 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 13289 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 4 | [Trimmomatic: a flexible trimmer for Illumina sequence data](https://doi.org/10.1093/bioinformatics/btu170) | 2014 | 6 | 57087 | Bioinformatics | Anthony Bolger, Marc Lohse, Björn Usadel |
| 5 | [Fitting Linear Mixed-Effects Models Using<b>lme4</b>](https://doi.org/10.18637/jss.v067.i01) | 2015 | 6 | 73510 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |
| 6 | [Efficient iterative schemes for<i>ab initio</i>total-energy calculations using a plane-wave basis set](https://doi.org/10.1103/physrevb.54.11169) | 1996 | 6 | 108283 | Physical review. B, Condensed matter | Georg Kresse, J. Furthmüller |
| 7 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 5 | 57784 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 8 | [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x) | 1948 | 5 | 76272 | Bell System Technical Journal | Claude E. Shannon |
| 9 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 5 | 79355 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 10 | [Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) | 1995 | 5 | 99817 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Yoav Benjamini, Yosef Hochberg |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 75 | 108986 | Machine Learning | Leo Breiman |
| 2 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 22 | 6289 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 3 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 20 | 71016 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 4 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 19 | 12278 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 5 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 18 | 30312 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 17 | 24839 | The Annals of Statistics | Jerome H. Friedman |
| 7 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 17 | 85825 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 8 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 16 | 92698 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |
| 9 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 15 | 194256 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 10 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 13 | 6004 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 8 | 13289 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 6 | 539 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [A Model for Predicting Cervical Cancer Using Machine Learning Algorithms](https://doi.org/10.3390/s22114132) | 2022 | 4 | 92 | Sensors | Naif Al Mudawi, Abdulwahab Alazeb |
| 4 | [Scientific discovery in the age of artificial intelligence](https://doi.org/10.1038/s41586-023-06221-2) | 2023 | 4 | 947 | Nature | Hanchen Wang, Tianfan Fu, Yuanqi Du, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Model for Predicting Cervical Cancer Using Machine Learning Algorithms](https://doi.org/10.3390/s22114132) | 2022 | 4 | 92 | Sensors | Naif Al Mudawi, Abdulwahab Alazeb |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 9 | 2733 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 9 | 13716 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 3 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://doi.org/10.48550/arxiv.1910.10683) | 2019 | 8 | 8400 | arXiv (Cornell University) | Colin Raffel, Noam Shazeer, Adam Roberts, et al. |
| 4 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 8 | 61603 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 5 | [A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1) | 2024 | 6 | 387 | Frontiers of Computer Science | Lei Wang, Chen Ma, Xueyang Feng, et al. |
| 6 | [BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://doi.org/10.1093/bioinformatics/btz682) | 2019 | 6 | 5548 | Bioinformatics | Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, et al. |
| 7 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 6 | 7954 |  | Nils Reimers, Iryna Gurevych |
| 8 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.48550/arxiv.1810.04805) | 2018 | 6 | 38545 | arXiv (Cornell University) | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 5 | 1070 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 5 | 1814 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 9 | 2733 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1) | 2024 | 6 | 387 | Frontiers of Computer Science | Lei Wang, Chen Ma, Xueyang Feng, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 5 | 1070 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 5 | 1814 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [Security and Privacy Challenges of Large Language Models: A Survey](https://doi.org/10.1145/3712001) | 2025 | 4 | 52 | ACM Computing Surveys | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu |
| 6 | [Large Language Models are Zero-Shot Rankers for Recommender Systems](https://doi.org/10.1007/978-3-031-56060-6_24) | 2024 | 4 | 130 | Lecture notes in computer science | Yupeng Hou, Junjie Zhang, Zihan Lin, et al. |
| 7 | [A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges](https://doi.org/10.1109/access.2024.3365742) | 2024 | 4 | 232 | IEEE Access | Mohaimenul Azam Khan Raiaan, Md. Saddam Hossain Mukta, Kaniz Fatema, et al. |
| 8 | [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0) | 2023 | 4 | 379 | Nature | Daniil A. Boiko, Robert MacKnight, Ben Kline, et al. |
| 9 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 4 | 1754 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 10 | [Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey](https://doi.org/10.18653/v1/2024.naacl-long.375) | 2024 | 3 | 7 |  | Zhichen Dong, Zhanhui Zhou, Chao Yang, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using Large Language Models to Compare Explainable Models for Smart Home Human Activity Recognition](https://doi.org/10.1145/3675094.3679000) | 2024 | 2 | 1 |  | Michele Fiori, Gabriele Civitarese, Cláudio Bettini |
| 2 | [<scp>PLeak:</scp> Prompt Leaking Attacks against Large Language Model Applications](https://doi.org/10.1145/3658644.3670370) | 2024 | 2 | 4 |  | Bo Hui, Haolin Yuan, Neil Zhenqiang Gong, et al. |
| 3 | [Intelligent Threat Detection—AI-Driven Analysis of Honeypot Data to Counter Cyber Threats](https://doi.org/10.3390/electronics13132465) | 2024 | 2 | 4 | Electronics | Phani Lanka, Khushi Gupta, Cihan Varol |
| 4 | [Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey](https://doi.org/10.18653/v1/2024.naacl-long.375) | 2024 | 3 | 7 |  | Zhichen Dong, Zhanhui Zhou, Chao Yang, et al. |
| 5 | [The emergence of large language models as tools in literature reviews: a large language model-assisted systematic review](https://doi.org/10.1093/jamia/ocaf063) | 2025 | 3 | 7 | Journal of the American Medical Informatics Association | Dmitry Scherbakov, Nina Hubig, Vinita Jansari, et al. |
| 6 | [Maximizing Penetration Testing Success with Effective Reconnaissance Techniques using ChatGPT](https://doi.org/10.22541/au.167947026.68710739/v1) | 2023 | 2 | 5 | Authorea (Authorea) | Sheetal Temara |
| 7 | [Detecting Personal Information in Training Corpora: an Analysis](https://doi.org/10.18653/v1/2023.trustnlp-1.18) | 2023 | 2 | 6 |  | Nishant Subramani, Alexandra Sasha Luccioni, Jesse Dodge, et al. |
| 8 | [Optimization-based Prompt Injection Attack to LLM-as-a-Judge](https://doi.org/10.1145/3658644.3690291) | 2024 | 3 | 10 |  | Jinqiao Shi, Zenghui Yuan, Yingmiao Liu, et al. |
| 9 | [Roles and Potential of Large Language Models in Healthcare: A Comprehensive Review](https://doi.org/10.1016/j.bj.2025.100868) | 2025 | 2 | 8 | Biomedical Journal | Chi‐Hung Lin, Chang‐Fu Kuo |
| 10 | [Large Language Models as Molecular Design Engines](https://doi.org/10.1021/acs.jcim.4c01396) | 2024 | 2 | 11 | Journal of Chemical Information and Modeling | Debjyoti Bhattacharya, Harrison J. Cassady, Michael A. Hickner, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Situated Learning](https://doi.org/10.1017/cbo9780511815355) | 1991 | 2 | 29204 |  | Jean Lave, Étienne Wenger |
| 2 | [Diffusion on assortative networks: from mean-field to agent-based, via Newman rewiring](https://doi.org/10.1140/epjb/s10051-024-00797-y) | 2024 | 1 | 1 | The European Physical Journal B | Loredana Di Lucchio, Giovanni Modanese |
| 3 | [Influence maximization under imbalanced heterogeneous networks via lightweight reinforcement learning with prior knowledge](https://doi.org/10.1007/s40747-024-01666-y) | 2024 | 1 | 1 | Complex & Intelligent Systems | K.-J. You, Sanyang Liu, Yiguang Bai |
| 4 | [Modeling public opinion dynamics in social networks using a GAN-SEIR framework](https://doi.org/10.1007/s13278-025-01426-x) | 2025 | 1 | 1 | Social Network Analysis and Mining | Jintao Wang, Yin Yulong, Lina Wei |
| 5 | [Information Diffusion Modeling in Social Networks: A Comparative Analysis of Delay Mechanisms Using Population Dynamics](https://doi.org/10.3390/app15116092) | 2025 | 1 | 1 | Applied Sciences | Kamila Bakenova, Alexandr Kuznetsov, Iryna Artyshchuk, et al. |
| 6 | [Delay-prioritized and Reliable Task Scheduling with Long-term Load Balancing in Computing Power Networks](https://doi.org/10.1109/tsc.2024.3495500) | 2024 | 1 | 0 | IEEE Transactions on Services Computing | Renchao Xie, Feng Li, Qinqin Tang, et al. |
| 7 | [Strategies of property developers in the context of carbon tax](https://doi.org/10.1371/journal.pone.0283527) | 2023 | 1 | 0 | PLoS ONE | Qingzhen Yao, Liangshan Shao, Zimin Yin, et al. |
| 8 | [Bayesian inference and ant colony optimization for multi-rumor mitigation in online social networks](https://doi.org/10.1007/s00500-024-09810-z) | 2024 | 1 | 0 | Soft Computing | Priyanka Parimi, Rashmi Ranjan Rout |
| 9 | [Rumor Containment in Hypergraph Representation of Social Networks: A Deep Reinforcement Learning-Based Solution](https://doi.org/10.1109/tcss.2024.3505205) | 2024 | 1 | 0 | IEEE Transactions on Computational Social Systems | Gouri Kundu, Smita Ghosh, Sankhayan Choudhury |
| 10 | [SIR-D-Based Information Processing for Multiplatform Complex Social Networks](https://doi.org/10.1109/tcss.2025.3525896) | 2025 | 1 | 0 | IEEE Transactions on Computational Social Systems | Cheng Ji, Dong Lv, Yiwen Xiong, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Diffusion on assortative networks: from mean-field to agent-based, via Newman rewiring](https://doi.org/10.1140/epjb/s10051-024-00797-y) | 2024 | 1 | 1 | The European Physical Journal B | Loredana Di Lucchio, Giovanni Modanese |
| 2 | [Influence maximization under imbalanced heterogeneous networks via lightweight reinforcement learning with prior knowledge](https://doi.org/10.1007/s40747-024-01666-y) | 2024 | 1 | 1 | Complex & Intelligent Systems | K.-J. You, Sanyang Liu, Yiguang Bai |
| 3 | [Modeling public opinion dynamics in social networks using a GAN-SEIR framework](https://doi.org/10.1007/s13278-025-01426-x) | 2025 | 1 | 1 | Social Network Analysis and Mining | Jintao Wang, Yin Yulong, Lina Wei |
| 4 | [Information Diffusion Modeling in Social Networks: A Comparative Analysis of Delay Mechanisms Using Population Dynamics](https://doi.org/10.3390/app15116092) | 2025 | 1 | 1 | Applied Sciences | Kamila Bakenova, Alexandr Kuznetsov, Iryna Artyshchuk, et al. |
| 5 | [Delay-prioritized and Reliable Task Scheduling with Long-term Load Balancing in Computing Power Networks](https://doi.org/10.1109/tsc.2024.3495500) | 2024 | 1 | 0 | IEEE Transactions on Services Computing | Renchao Xie, Feng Li, Qinqin Tang, et al. |
| 6 | [Strategies of property developers in the context of carbon tax](https://doi.org/10.1371/journal.pone.0283527) | 2023 | 1 | 0 | PLoS ONE | Qingzhen Yao, Liangshan Shao, Zimin Yin, et al. |
| 7 | [Bayesian inference and ant colony optimization for multi-rumor mitigation in online social networks](https://doi.org/10.1007/s00500-024-09810-z) | 2024 | 1 | 0 | Soft Computing | Priyanka Parimi, Rashmi Ranjan Rout |
| 8 | [Rumor Containment in Hypergraph Representation of Social Networks: A Deep Reinforcement Learning-Based Solution](https://doi.org/10.1109/tcss.2024.3505205) | 2024 | 1 | 0 | IEEE Transactions on Computational Social Systems | Gouri Kundu, Smita Ghosh, Sankhayan Choudhury |
| 9 | [SIR-D-Based Information Processing for Multiplatform Complex Social Networks](https://doi.org/10.1109/tcss.2025.3525896) | 2025 | 1 | 0 | IEEE Transactions on Computational Social Systems | Cheng Ji, Dong Lv, Yiwen Xiong, et al. |
| 10 | [241De Gruyter series on the applications of mathematics in engineering and information sciences](https://doi.org/10.1515/9783111646893-014) | 2025 | 1 | 0 | De Gruyter eBooks | Unknown |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Diffusion on assortative networks: from mean-field to agent-based, via Newman rewiring](https://doi.org/10.1140/epjb/s10051-024-00797-y) | 2024 | 1 | 1 | The European Physical Journal B | Loredana Di Lucchio, Giovanni Modanese |
| 2 | [Influence maximization under imbalanced heterogeneous networks via lightweight reinforcement learning with prior knowledge](https://doi.org/10.1007/s40747-024-01666-y) | 2024 | 1 | 1 | Complex & Intelligent Systems | K.-J. You, Sanyang Liu, Yiguang Bai |
| 3 | [Modeling public opinion dynamics in social networks using a GAN-SEIR framework](https://doi.org/10.1007/s13278-025-01426-x) | 2025 | 1 | 1 | Social Network Analysis and Mining | Jintao Wang, Yin Yulong, Lina Wei |
| 4 | [Information Diffusion Modeling in Social Networks: A Comparative Analysis of Delay Mechanisms Using Population Dynamics](https://doi.org/10.3390/app15116092) | 2025 | 1 | 1 | Applied Sciences | Kamila Bakenova, Alexandr Kuznetsov, Iryna Artyshchuk, et al. |
| 5 | [Delay-prioritized and Reliable Task Scheduling with Long-term Load Balancing in Computing Power Networks](https://doi.org/10.1109/tsc.2024.3495500) | 2024 | 1 | 0 | IEEE Transactions on Services Computing | Renchao Xie, Feng Li, Qinqin Tang, et al. |
| 6 | [Strategies of property developers in the context of carbon tax](https://doi.org/10.1371/journal.pone.0283527) | 2023 | 1 | 0 | PLoS ONE | Qingzhen Yao, Liangshan Shao, Zimin Yin, et al. |
| 7 | [Bayesian inference and ant colony optimization for multi-rumor mitigation in online social networks](https://doi.org/10.1007/s00500-024-09810-z) | 2024 | 1 | 0 | Soft Computing | Priyanka Parimi, Rashmi Ranjan Rout |
| 8 | [Rumor Containment in Hypergraph Representation of Social Networks: A Deep Reinforcement Learning-Based Solution](https://doi.org/10.1109/tcss.2024.3505205) | 2024 | 1 | 0 | IEEE Transactions on Computational Social Systems | Gouri Kundu, Smita Ghosh, Sankhayan Choudhury |
| 9 | [SIR-D-Based Information Processing for Multiplatform Complex Social Networks](https://doi.org/10.1109/tcss.2025.3525896) | 2025 | 1 | 0 | IEEE Transactions on Computational Social Systems | Cheng Ji, Dong Lv, Yiwen Xiong, et al. |
| 10 | [241De Gruyter series on the applications of mathematics in engineering and information sciences](https://doi.org/10.1515/9783111646893-014) | 2025 | 1 | 0 | De Gruyter eBooks | Unknown |
<!-- TRENDING-END -->
