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

Last update: 2026-04-27 08:10 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [THE THREE COMPRESSIONS: Lossy, Predatory, and Witness — A Semiotic Thermodynamics](https://doi.org/10.5281/zenodo.19053469) | 2026 | 11 | 177 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil, Rex Fraction |
| 2 | [Constitutional Physiology: Measuring Legitimacy as Care in a Living Civic Body](https://doi.org/10.5281/zenodo.19393267) | 2026 | 10 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Rick - PraxisFoundry001 |
| 3 | [SPXI (Semantic Packet for eXchange & Indexing): A Formal Specification — EA-SPXI-01](https://doi.org/10.5281/zenodo.19614870) | 2026 | 8 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Rex Fraction |
| 4 | [Lexique canonique de l'ontologie du passage](https://doi.org/10.5281/zenodo.19698146) | 2026 | 7 | 16 | Zenodo (CERN European Organization for Nuclear Research) | FREDERIC DENJOY |
| 5 | [Constitutional Vital Signs: A White Paper on Legitimacy, Care, and Civic Consciousness](https://doi.org/10.5281/zenodo.19499261) | 2026 | 7 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Rick - PraxisFoundry001 |
| 6 | [Helical Rydberg Scars as Mixed-Dimensional Phase Closure of the Existence Equation](https://doi.org/10.5281/zenodo.19329296) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 7 | [Dark Matter as Topological Phase Persistence of the Existence Equation](https://doi.org/10.5281/zenodo.19329314) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 8 | [Non-Commutativity from Geometric Constraint: Projected Algebra of the Existence Equation](https://doi.org/10.5281/zenodo.19329300) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 9 | [Quantum Many-Body Scars as Temporal Phase Closure of the Existence Equation](https://doi.org/10.5281/zenodo.19327776) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 10 | [Fractional Quantum Hall States as Spatial Phase Closure of the Existence Equation](https://doi.org/10.5281/zenodo.19329294) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 107 | 122848 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 60 | 46386 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 31 | 28166 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 28 | 8329 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 21 | 22717 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 19 | 51179 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 17 | 32438 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Regularization and Variable Selection Via the Elastic Net](https://doi.org/10.1111/j.1467-9868.2005.00503.x) | 2005 | 14 | 20648 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Hui Zou, Trevor Hastie |
| 9 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 14 | 207917 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 10 | [A tutorial on support vector regression](https://doi.org/10.1023/b:stco.0000035301.49549.88) | 2004 | 13 | 12812 | Statistics and Computing | Alex Smola, Bernhard Schölkopf |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 10 | 1722 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 7 | 13205 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 3 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 6 | 482 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 4 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 478 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 5 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 5 | 539 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 6 | [Hyperparameter Optimization with Genetic Algorithms and XGBoost: A Step Forward in Smart Grid Fraud Detection](https://doi.org/10.3390/s24041230) | 2024 | 4 | 68 | Sensors | Adil Mehdary, Abdellah Chehri, Abdeslam Jakimi, et al. |
| 7 | [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336) | 2023 | 4 | 1069 | Science | Rémi Lam, Álvaro Sánchez‐González, Matthew Willson, et al. |
| 8 | [Accurate medium-range global weather forecasting with 3D neural networks](https://doi.org/10.1038/s41586-023-06185-3) | 2023 | 4 | 1320 | Nature | Kaifeng Bi, Lingxi Xie, Hengheng Zhang, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Hyperparameter Optimization with Genetic Algorithms and XGBoost: A Step Forward in Smart Grid Fraud Detection](https://doi.org/10.3390/s24041230) | 2024 | 4 | 68 | Sensors | Adil Mehdary, Abdellah Chehri, Abdeslam Jakimi, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [MizAR 60 for Mizar 50](https://doi.org/10.4230/lipics.itp.2023.19) | 2023 | 24 | 75201 | DROPS (Schloss Dagstuhl – Leibniz Center for Informatics) | Jakubův, Jan, Chvalovský, Karel, Goertzel, Zarathustra, et al. |
| 2 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 23 | 283 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 3 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 22 | 426 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 4 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 19 | 131 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 5 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 16 | 124 |  | Sandhini Agarwal, Diogo Almeida, Amanda Askell, et al. |
| 6 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 16 | 21262 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 7 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 15 | 2902 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 8 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 15 | 10374 |  | Nils Reimers, Iryna Gurevych |
| 9 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3070 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 10 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 14 | 3140 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [MizAR 60 for Mizar 50](https://doi.org/10.4230/lipics.itp.2023.19) | 2023 | 24 | 75201 | DROPS (Schloss Dagstuhl – Leibniz Center for Informatics) | Jakubův, Jan, Chvalovský, Karel, Goertzel, Zarathustra, et al. |
| 2 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 22 | 426 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 3 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 19 | 131 |  | Yong Jae Lee, Chunyuan Li, Haotian Liu, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 15 | 2902 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3070 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [Improved Baselines with Visual Instruction Tuning](https://doi.org/10.1109/cvpr52733.2024.02484) | 2024 | 11 | 1029 |  | Haotian Liu, Chunyuan Li, Yuheng Li, et al. |
| 7 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 11 | 1275 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 8 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://doi.org/10.52202/075280-0517) | 2023 | 10 | 50 |  | Yuan Cao, Tom Griffiths, Karthik Narasimhan, et al. |
| 9 | [Jailbreaking Black Box Large Language Models in Twenty Queries](https://doi.org/10.1109/satml64287.2025.00010) | 2025 | 10 | 76 |  | Patrick Chao, Alexander Robey, Edgar Dobriban, et al. |
| 10 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 10 | 933 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large Language Model Unlearning](https://doi.org/10.52202/079017-3346) | 2024 | 5 | 12 |  | YangLiu YangLiu, Xiaojun Xu, Yuanshun Yao |
| 2 | [Locating and Editing Factual Associations in GPT](https://doi.org/10.52202/068431-1262) | 2022 | 8 | 20 |  | Alex Andonian, David Bau, Yonatan Belinkov, et al. |
| 3 | [Learn to Explain: Multimodal Reasoning Via Thought Chains for Science Question Answering](https://doi.org/10.52202/068431-0182) | 2022 | 4 | 11 |  | Kai-Wei Chang, Peter Clark, Ashwin Kalyan, et al. |
| 4 | [LLM-Pruner: On the Structural Pruning of Large Language Models](https://doi.org/10.52202/075280-0950) | 2023 | 4 | 13 |  | Gongfan Fang, Xinyin Ma, Xinchao Wang |
| 5 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://doi.org/10.52202/075280-0517) | 2023 | 10 | 50 |  | Yuan Cao, Tom Griffiths, Karthik Narasimhan, et al. |
| 6 | [AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension](https://doi.org/10.18653/v1/2024.acl-long.109) | 2024 | 5 | 26 |  | Qian Yang, Jin Xu, Wenrui Liu, et al. |
| 7 | [Self-Refine: Iterative Refinement with Self-Feedback](https://doi.org/10.52202/075280-2019) | 2023 | 4 | 27 |  | Uri Alon, Peter Clark, Nouha Dziri, et al. |
| 8 | [Jailbreaking Black Box Large Language Models in Twenty Queries](https://doi.org/10.1109/satml64287.2025.00010) | 2025 | 10 | 76 |  | Patrick Chao, Alexander Robey, Edgar Dobriban, et al. |
| 9 | [Laypeople’s Use of and Attitudes Toward Large Language Models and Search Engines for Health Queries: Survey Study](https://doi.org/10.2196/64290) | 2024 | 4 | 36 | Journal of Medical Internet Research | Tamir Mendel, Nina Singh, David Mann, et al. |
| 10 | [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://doi.org/10.52202/075280-2142) | 2023 | 5 | 51 |  | Wei‐Min Dai, Pascale N Fung, Steven Chu Hong Hoi, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 17 | 89186 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 14 | 177371 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 9 | 122848 | Machine Learning | Leo Breiman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 6 | 8329 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Statistical Power Analysis for the Behavioral Sciences](https://doi.org/10.4324/9780203771587) | 2013 | 6 | 22905 |  | Jacob Cohen |
| 6 | [Institutions, Institutional Change and Economic Performance](https://doi.org/10.1017/cbo9780511808678) | 1990 | 6 | 30182 | Cambridge University Press eBooks | Douglass C. North |
| 7 | [Naturalistic inquiry](https://doi.org/10.1016/0147-1767(85)90062-8) | 1985 | 6 | 33068 | International Journal of Intercultural Relations | Yvonna S. Lincoln, Egon G. Guba, Joseph J. Pilotta |
| 8 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 6 | 33726 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 9 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 6 | 46386 |  | Tianqi Chen, Carlos Guestrin |
| 10 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 5 | 5087 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [How climate change and groundwater extraction will shape the global terrestrial water cycle pattern](https://doi.org/10.1016/j.jhydrol.2024.131780) | 2024 | 2 | 9 | Journal of Hydrology | Longhuan Wang, Binghao Jia, Zhenghui Xie |
| 2 | [Quality decline of prepared dishes stored at 4 °C: Microbial regulation of nitrite and biogenic amine formation](https://doi.org/10.1016/j.fm.2025.104730) | 2025 | 2 | 11 | Food Microbiology | Jiaxin Liu, Wang Yin, Ping Yang, et al. |
| 3 | [Optimized groundwater quality evaluation using unsupervised machine learning, game theory and Monte-Carlo simulation](https://doi.org/10.1016/j.jenvman.2024.122902) | 2024 | 2 | 28 | Journal of Environmental Management | Yuting Yan, Yunhui Zhang, Shiming Yang, et al. |
| 4 | [Differential game theoretic analysis of the blockchain technology investment and carbon reduction strategy in digital supply chain with government intervention](https://doi.org/10.1016/j.cie.2024.109953) | 2024 | 2 | 46 | Computers & Industrial Engineering | Yuwei Kang, Peiwu Dong, Yanbing Ju, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [How climate change and groundwater extraction will shape the global terrestrial water cycle pattern](https://doi.org/10.1016/j.jhydrol.2024.131780) | 2024 | 2 | 9 | Journal of Hydrology | Longhuan Wang, Binghao Jia, Zhenghui Xie |
| 2 | [Quality decline of prepared dishes stored at 4 °C: Microbial regulation of nitrite and biogenic amine formation](https://doi.org/10.1016/j.fm.2025.104730) | 2025 | 2 | 11 | Food Microbiology | Jiaxin Liu, Wang Yin, Ping Yang, et al. |
| 3 | [Optimized groundwater quality evaluation using unsupervised machine learning, game theory and Monte-Carlo simulation](https://doi.org/10.1016/j.jenvman.2024.122902) | 2024 | 2 | 28 | Journal of Environmental Management | Yuting Yan, Yunhui Zhang, Shiming Yang, et al. |
| 4 | [Game theory in the death galaxy: interaction of cancer and stromal cells in tumour microenvironment](https://doi.org/10.1098/rsfs.2014.0028) | 2014 | 2 | 40 | Interface Focus | Amy Wu, David Liao, Thea D. Tlsty, et al. |
| 5 | [Differential game theoretic analysis of the blockchain technology investment and carbon reduction strategy in digital supply chain with government intervention](https://doi.org/10.1016/j.cie.2024.109953) | 2024 | 2 | 46 | Computers & Industrial Engineering | Yuwei Kang, Peiwu Dong, Yanbing Ju, et al. |
<!-- TRENDING-END -->
