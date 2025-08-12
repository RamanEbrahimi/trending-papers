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

Last update: 2025-08-12 22:38 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR and the 2−ΔΔCT Method](https://doi.org/10.1006/meth.2001.1262) | 2001 | 10 | 164306 | Methods | Kenneth J. Livak, Thomas D. Schmittgen |
| 2 | [Teaching Humanities and Social Sciences in the Primary School](https://openalex.org/W566037704) | 2019 | 8 | 9 |  | Ruth Reynolds |
| 3 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 78301 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 4 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 7 | 27785 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 5 | [limma powers differential expression analyses for RNA-sequencing and microarray studies](https://doi.org/10.1093/nar/gkv007) | 2015 | 6 | 33734 | Nucleic Acids Research | Matthew E. Ritchie, Belinda Phipson, Di Wu, et al. |
| 6 | [Fitting Linear Mixed-Effects Models Using<b>lme4</b>](https://doi.org/10.18637/jss.v067.i01) | 2015 | 6 | 72632 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |
| 7 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 6 | 94062 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 8 | [Cohort Profile: The China Health and Retirement Longitudinal Study (CHARLS)](https://doi.org/10.1093/ije/dys203) | 2012 | 5 | 3182 | International Journal of Epidemiology | Yaohui Zhao, Yisong Hu, James P. Smith, et al. |
| 9 | [Inferring tumour purity and stromal and immune cell admixture from expression data](https://doi.org/10.1038/ncomms3612) | 2013 | 5 | 7830 | Nature Communications | Kosuke Yoshihara, Maria Shahmoradgoli, Emmanuel Martínez, et al. |
| 10 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |

### Topic: games on networks

Topic: games on networks — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Temporal interaction and its role in the evolution of cooperation](https://doi.org/10.1103/physreve.110.024210) | 2024 | 1 | 1 | Physical review. E | Yujie He, Tianyu Ren, Xiao‐Jun Zeng, et al. |
| 2 | [Transfer learning approach for identifying negative sentiment in tweets directed to football players](https://doi.org/10.1016/j.engappai.2024.108377) | 2024 | 1 | 1 | Engineering Applications of Artificial Intelligence | Nanlir Sallau Mullah, Wan Mohd Nazmee Wan Zainon, Mohd Nadhir Ab Wahab |
| 3 | [Efficient Resource Management for Real-time AI Systems in the Cloud using Reinforcement Learning](https://doi.org/10.1109/ic3i61595.2024.10828656) | 2024 | 1 | 1 |  | Vinay Mallikarjunaradhya, Madhusudhan Dasari Sreeramulu, Abdul Sajid Mohammed, et al. |
| 4 | [Distributed Streaming Storage Performance Benchmarking: Pravega and Pulsar](https://doi.org/10.48084/etasr.8076) | 2024 | 1 | 2 | Engineering Technology & Applied Science Research | Ramesh Kadaba Vasudevamurthy, G T Raju |
| 5 | [DIBTBL: A novel text sentiment analysis model based on an improved swarm intelligence algorithm and deep learning](https://doi.org/10.1109/access.2024.3487752) | 2024 | 1 | 2 | IEEE Access | Guangyu Mu, Li Dai, Xiurong Li, et al. |
| 6 | [Multimodal Sentiment Analysis of Government Information Comments Based on Contrastive Learning and Cross-Attention Fusion Networks](https://doi.org/10.1109/access.2024.3493933) | 2024 | 1 | 2 | IEEE Access | Guangyu Mu, Chuanzhi Chen, Xiurong Li, et al. |
| 7 | [Optimizing Real-time Task Scheduling in Cloud-based AI Systems using Genetic Algorithms](https://doi.org/10.1109/ic3i61595.2024.10829055) | 2024 | 1 | 2 |  | Abdul Sajid Mohammed, Vinay Mallikarjunaradhya, Madhusudhan Dasari Sreeramulu, et al. |
| 8 | [Optimizing and dimensioning a data intensive cloud application for soccer player tracking](https://doi.org/10.2478/ijcss-2022-0004) | 2022 | 1 | 2 | International Journal of Computer Science in Sport | Gergely Dobreff, Márton Molnár, László Toka |
| 9 | [A Survey on Noncooperative Games and Distributed Nash Equilibrium Seeking over Multi-Agent Networks](https://doi.org/10.26599/air.2022.9150002) | 2022 | 1 | 4 | CAAI Artificial Intelligence Research | Peng Yi, Jinlong Lei, Xiuxian Li, et al. |
| 10 | [Leveraging Multilingual Transformer for Multiclass Sentiment Analysis in Code-Mixed Data of Low-Resource Languages](https://doi.org/10.1109/access.2025.3527710) | 2025 | 1 | 4 | IEEE Access | Muhammad Kashif Nazir, C. M. Nadeem Faisal, Muhammad Asif Habib, et al. |

### Topic: network science in finance

Topic: network science in finance — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|

### Topic: influence maximization

Topic: influence maximization — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Scalable influence maximization for prevalent viral marketing in large-scale social networks](https://doi.org/10.1145/1835804.1835934) | 2010 | 3 | 1713 |  | Wei Chen, Chi Wang, Yajun Wang |
| 2 | [ToupleGDD: A Fine-Designed Solution of Influence Maximization by Deep Reinforcement Learning](https://doi.org/10.1109/tcss.2023.3272331) | 2023 | 2 | 32 | IEEE Transactions on Computational Social Systems | Tiantian Chen, Siwen Yan, Jianxiong Guo, et al. |
| 3 | [Effect of infill pattern and infill density on mechanical behaviour of FDM 3D printed Parts- a current review](https://doi.org/10.1016/j.matpr.2022.02.310) | 2022 | 2 | 150 | Materials Today Proceedings | Md Qamar Tanveer, Gautam Mishra, Siddharth Mishra, et al. |
| 4 | [Printing parameters and materials affecting mechanical properties of FDM-3D printed Parts: Perspective and prospects](https://doi.org/10.1016/j.matpr.2021.10.003) | 2021 | 2 | 152 | Materials Today Proceedings | Manav Doshi, Ameya Mahale, Suraj Singh, et al. |
| 5 | [Mining the network value of customers](https://doi.org/10.1145/502512.502525) | 2001 | 2 | 2835 |  | Pedro Domingos, Matt Richardson |
| 6 | [A Cognitive Model of the Antecedents and Consequences of Satisfaction Decisions](https://doi.org/10.1177/002224378001700405) | 1980 | 2 | 6412 | Journal of Marketing Research | Richard L. Oliver |
| 7 | [An adaptive differential evolution algorithm driven by multiple probabilistic mutation strategies for influence maximization in social networks](https://doi.org/10.1142/s0129183124502322) | 2024 | 1 | 0 | International Journal of Modern Physics C | Jianxin Tang, Qian Du |
| 8 | [CLDE: a competitive learning-driven differential evolution optimization for the influence maximization problem in social networks](https://doi.org/10.1007/s11227-025-07175-0) | 2025 | 1 | 0 | The Journal of Supercomputing | Baoqiang Chai, Ruisheng Zhang, Xinyue Li, et al. |
| 9 | [Software-defined network aided lightweight group key management for resource-constrained Internet of Things devices](https://doi.org/10.1016/j.suscom.2022.100807) | 2022 | 1 | 2 | Sustainable Computing Informatics and Systems | Antony Taurshia, G. Jaspher W. Kathrine, Alireza Souri, et al. |
| 10 | [A high-performance algorithm for finding influential nodes in large-scale social networks](https://doi.org/10.1007/s11227-022-04418-2) | 2022 | 1 | 3 | The Journal of Supercomputing | Mohsen Taherinia, Mahdi Esmaeili, Behrouz Minaei‐Bidgoli |

### Topic: graph neural networks

Topic: graph neural networks — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Graph Neural Networks for Social Recommendation](https://doi.org/10.1145/3308558.3313488) | 2019 | 6 | 1562 |  | Wenqi Fan, Yao Ma, Qing Li, et al. |
| 2 | [Advances in Neural Information Processing Systems 19](https://doi.org/10.7551/mitpress/7503.001.0001) | 2007 | 5 | 14539 | The MIT Press eBooks | Unknown |
| 3 | [Pick and Choose: A GNN-based Imbalanced Learning Approach for Fraud Detection](https://doi.org/10.1145/3442381.3449989) | 2021 | 4 | 240 |  | Yang Liu, Xiang Ao, Zidi Qin, et al. |
| 4 | [Graph Convolutional Neural Networks for Web-Scale Recommender Systems](https://doi.org/10.1145/3219819.3219890) | 2018 | 4 | 3191 |  | Rex Ying, Ruining He, Kaifeng Chen, et al. |
| 5 | [DeepWalk](https://doi.org/10.1145/2623330.2623732) | 2014 | 4 | 8947 |  | Bryan Perozzi, Rami Al‐Rfou, Steven Skiena |
| 6 | [Label Information Enhanced Fraud Detection against Low Homophily in Graphs](https://doi.org/10.1145/3543507.3583373) | 2023 | 3 | 24 | Proceedings of the ACM Web Conference 2022 | Yuchen Wang, Jinghui Zhang, Zhengjie Huang, et al. |
| 7 | [Addressing Heterophily in Graph Anomaly Detection: A Perspective of Graph Spectrum](https://doi.org/10.1145/3543507.3583268) | 2023 | 3 | 58 | Proceedings of the ACM Web Conference 2022 | Yuan Gao, Xiang Wang, Xiangnan He, et al. |
| 8 | [H2-FDetector: A GNN-based Fraud Detector with Homophilic and Heterophilic Connections](https://doi.org/10.1145/3485447.3512195) | 2022 | 3 | 66 | Proceedings of the ACM Web Conference 2022 | Fengzhao Shi, Yanan Cao, Yanmin Shang, et al. |
| 9 | [Alleviating the Inconsistency Problem of Applying Graph Neural Network to Fraud Detection](https://doi.org/10.1145/3397271.3401253) | 2020 | 3 | 243 |  | Zhiwei Liu, Yingtong Dou, Philip S. Yu, et al. |
| 10 | [A Semi-Supervised Graph Attentive Network for Financial Fraud Detection](https://doi.org/10.1109/icdm.2019.00070) | 2019 | 3 | 317 | 2021 IEEE International Conference on Data Mining (ICDM) | Daixin Wang, Qi Yuan, Jianbin Lin, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 69 | 107723 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 28 | 24495 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 18 | 5561 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 4 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 16 | 11830 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 16 | 25921 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 16 | 70108 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 14 | 5839 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 14 | 29971 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 9 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 13 | 189283 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 10 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 11 | 192837 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
<!-- TRENDING-END -->
