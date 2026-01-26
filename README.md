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

Last update: 2026-01-26 06:28 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Families on the move – Latin American perspectives](https://doi.org/10.1080/1369183x.2025.2609027) | 2026 | 7 | 7 | Journal of Ethnic and Migration Studies | Nuni Jorgensen, Patrícia Nabuco Martuscelli |
| 2 | [SciPy 1.0: fundamental algorithms for scientific computing in Python](https://doi.org/10.1038/s41592-019-0686-2) | 2020 | 6 | 34184 | Nature Methods | Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, et al. |
| 3 | [Doing family on the move: Venezuelan migration in Ecuador](https://doi.org/10.1080/1369183x.2025.2609029) | 2026 | 5 | 5 | Journal of Ethnic and Migration Studies | Gioconda Herrera, Tania Bonilla Mena |
| 4 | [Beyond separation and reunification: the ever-shifting trajectories of Venezuelan transnational families in South America](https://doi.org/10.1080/1369183x.2025.2609030) | 2026 | 5 | 5 | Journal of Ethnic and Migration Studies | Nuni Jorgensen |
| 5 | [Dynamic Medicine — Part II From Biomarkers to System Dynamics: Why Static Measurements Fail to Capture Disease](https://doi.org/10.5281/zenodo.18189271) | 2026 | 5 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Anita Domargård |
| 6 | [The Universal Resonance Model of Disease: A Primer on Cross-System Instability, Early-Warning Signals, and Predictive Transitions](https://doi.org/10.5281/zenodo.17883469) | 2025 | 5 | 35 | Zenodo (CERN European Organization for Nuclear Research) | Domargård, Anita |
| 7 | [Fast gapped-read alignment with Bowtie 2](https://doi.org/10.1038/nmeth.1923) | 2012 | 5 | 57624 | Nature Methods | Ben Langmead, Steven L. Salzberg |
| 8 | [Theory of Trotter Error with Commutator Scaling](https://doi.org/10.1103/physrevx.11.011020) | 2021 | 4 | 428 | Physical Review X | Andrew M. Childs, Yuan Su, Minh C. Tran, et al. |
| 9 | [Quantum Computation and Quantum Information](https://doi.org/10.1017/cbo9780511976667) | 2012 | 4 | 7967 | Cambridge University Press eBooks | Michael A. Nielsen, Isaac L. Chuang |
| 10 | [Matplotlib: A 2D Graphics Environment](https://doi.org/10.1109/mcse.2007.55) | 2007 | 4 | 36552 | Computing in Science & Engineering | John D. Hunter |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 101 | 117410 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 70 | 42956 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 26 | 26948 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 20 | 7441 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 21624 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 19 | 29048 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 19 | 31428 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 19 | 92221 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations](https://doi.org/10.1016/j.jcp.2018.10.045) | 2018 | 14 | 13648 | Journal of Computational Physics | Maziar Raissi, Paris Perdikaris, George Em Karniadakis |
| 10 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 14 | 49963 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 11 | 291 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 8 | 1193 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 8 | 1244 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 4 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 12986 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 18 | 2452 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 2661 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 2598 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 4 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 8 | 2156 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |
| 5 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 8 | 3906 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 6 | [Large language models in health care: Development, applications, and challenges](https://doi.org/10.1002/hcs2.61) | 2023 | 7 | 275 | Health care science | Rui Yang, Ting Fang Tan, Wei Lu, et al. |
| 7 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 7 | 503 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 8 | [BioGPT: generative pre-trained transformer for biomedical text generation and mining](https://doi.org/10.1093/bib/bbac409) | 2022 | 7 | 863 | Briefings in Bioinformatics | Renqian Luo, Liai Sun, Yingce Xia, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1919 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 7 | 9513 |  | Nils Reimers, Iryna Gurevych |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 18 | 2452 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 18 | 2661 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 8 | 2156 | arXiv (Cornell University) | OpenAI, Stock, Kristin, Jones, Christopher B. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 8 | 3906 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Large language models in health care: Development, applications, and challenges](https://doi.org/10.1002/hcs2.61) | 2023 | 7 | 275 | Health care science | Rui Yang, Ting Fang Tan, Wei Lu, et al. |
| 6 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 7 | 503 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 7 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1919 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 8 | [Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2) | 2025 | 6 | 82 | Nature Medicine | Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, et al. |
| 9 | [The application of large language models in medicine: A scoping review](https://doi.org/10.1016/j.isci.2024.109713) | 2024 | 6 | 239 | iScience | Xiangbin Meng, Xiangyu Yan, Kuo Zhang, et al. |
| 10 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 6 | 274 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Ophthalmological Question Answering and Reasoning Using OpenAI o1 vs Other Large Language Models](https://doi.org/10.1001/jamaophthalmol.2025.2413) | 2025 | 3 | 3 | JAMA Ophthalmology | Sahana Srinivasan, X. C. Ai, Minjie Zou, et al. |
| 2 | [Large Language Model Ability to Translate CT and MRI Free-Text Radiology Reports Into Multiple Languages](https://doi.org/10.1148/radiol.241736) | 2024 | 3 | 26 | Radiology | Aymen Meddeb, Sophia Lüken, Felix Busch, et al. |
| 3 | [The Evolution of Systems Biology and Systems Medicine: From Mechanistic Models to Uncertainty Quantification](https://doi.org/10.1146/annurev-bioeng-102723-065309) | 2025 | 2 | 20 | Annual Review of Biomedical Engineering | Lingxia Qiao, Ali Khalilimeybodi, Nathaniel Linden-Santangeli, et al. |
| 4 | [MedExpQA: Multilingual benchmarking of Large Language Models for Medical Question Answering](https://doi.org/10.1016/j.artmed.2024.102938) | 2024 | 3 | 31 | Artificial Intelligence in Medicine | Iñigo Alonso, Maite Oronoz, Rodrigo Agerri |
| 5 | [Biomni: A General-Purpose Biomedical AI Agent](https://doi.org/10.1101/2025.05.30.656746) | 2025 | 3 | 36 |  | Kexin Huang, Serena Zhang, Hanchen Wang, et al. |
| 6 | [Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2) | 2025 | 6 | 82 | Nature Medicine | Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, et al. |
| 7 | [Exploring automated energy optimization with unstructured building data: A multi-agent based framework leveraging large language models](https://doi.org/10.1016/j.enbuild.2024.114691) | 2024 | 3 | 44 | Energy and Buildings | Tong Xiao, Peng Xu |
| 8 | [Current Status of ChatGPT Use in Medical Education: Potentials, Challenges, and Strategies](https://doi.org/10.2196/57896) | 2024 | 3 | 55 | Journal of Medical Internet Research | Tianhui Xu, Huiting Weng, Fang Liu, et al. |
| 9 | [Improving Passage Retrieval with Zero-Shot Question Generation](https://doi.org/10.18653/v1/2022.emnlp-main.249) | 2022 | 3 | 61 |  | Devendra Singh Sachan, Michael Lewis, Mandar Joshi, et al. |
| 10 | [Chain of Thought Utilization in Large Language Models and Application in Nephrology](https://doi.org/10.3390/medicina60010148) | 2024 | 3 | 71 | Medicina | Jing Miao, Charat Thongprayoon, Supawadee Suppadungsuk, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Online Movements Reflect Ongoing Deliberation](https://doi.org/10.1523/jneurosci.1913-24.2025) | 2025 | 2 | 3 | Journal of Neuroscience | Jan A. Calalo, Truc Ngo, Seth R. Sullivan, et al. |
| 2 | [Computational joint action: Dynamical models to understand the development of joint coordination](https://doi.org/10.1371/journal.pcbi.1011948) | 2024 | 2 | 3 | PLoS Computational Biology | Cecilia De Vicariis, Vinil T. Chackochan, Laura Bandini, et al. |
| 3 | [Accuracy and effort costs together lead to temporal asynchrony of multiple motor commands](https://doi.org/10.1152/jn.00435.2022) | 2022 | 2 | 4 | Journal of Neurophysiology | Daniel Tanis, Jan A. Calalo, Joshua G. A. Cashaback, et al. |
| 4 | [Punishment Leads to Greater Sensorimotor Learning But Less Movement Variability Compared to Reward](https://doi.org/10.1016/j.neuroscience.2024.01.004) | 2024 | 2 | 7 | Neuroscience | Adam M. Roth, Rakshith Lokesh, Jiaqiao Tang, et al. |
| 5 | [Complex Spatiotemporal Tuning in Human Upper-Limb Muscles](https://doi.org/10.1152/jn.00791.2009) | 2009 | 2 | 9 | Journal of Neurophysiology | J. Andrew Pruszynski, Timothy Lillicrap, Stephen H. Scott |
| 6 | [Visual accuracy dominates over haptic speed for state estimation of a partner during collaborative sensorimotor interactions](https://doi.org/10.1152/jn.00053.2023) | 2023 | 2 | 15 | Journal of Neurophysiology | Rakshith Lokesh, Seth R. Sullivan, Laura St. Germain, et al. |
| 7 | [Signaling equilibria in sensorimotor interactions](https://doi.org/10.1016/j.cognition.2015.03.008) | 2015 | 2 | 17 | Cognition | Felix Leibfried, Jordi Grau-Moya, Daniel A. Braun |
| 8 | [Collaborative decision making is grounded in representations of other people’s competence and effort.](https://doi.org/10.1037/xge0001336) | 2023 | 2 | 17 | Journal of Experimental Psychology General | Yang Xiang, Natalia Vélez, Samuel J. Gershman |
| 9 | [Reinforcement-based processes actively regulate motor exploration along redundant solution manifolds](https://doi.org/10.1098/rspb.2023.1475) | 2023 | 2 | 17 | Proceedings of the Royal Society B Biological Sciences | Adam M. Roth, Jan A. Calalo, Rakshith Lokesh, et al. |
| 10 | [The sensorimotor system modulates muscular co-contraction relative to visuomotor feedback responses to regulate movement variability](https://doi.org/10.1152/jn.00472.2022) | 2023 | 2 | 21 | Journal of Neurophysiology | Jan A. Calalo, Adam M. Roth, Rakshith Lokesh, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Online Movements Reflect Ongoing Deliberation](https://doi.org/10.1523/jneurosci.1913-24.2025) | 2025 | 2 | 3 | Journal of Neuroscience | Jan A. Calalo, Truc Ngo, Seth R. Sullivan, et al. |
| 2 | [Computational joint action: Dynamical models to understand the development of joint coordination](https://doi.org/10.1371/journal.pcbi.1011948) | 2024 | 2 | 3 | PLoS Computational Biology | Cecilia De Vicariis, Vinil T. Chackochan, Laura Bandini, et al. |
| 3 | [Punishment Leads to Greater Sensorimotor Learning But Less Movement Variability Compared to Reward](https://doi.org/10.1016/j.neuroscience.2024.01.004) | 2024 | 2 | 7 | Neuroscience | Adam M. Roth, Rakshith Lokesh, Jiaqiao Tang, et al. |
| 4 | [Visual accuracy dominates over haptic speed for state estimation of a partner during collaborative sensorimotor interactions](https://doi.org/10.1152/jn.00053.2023) | 2023 | 2 | 15 | Journal of Neurophysiology | Rakshith Lokesh, Seth R. Sullivan, Laura St. Germain, et al. |
| 5 | [Collaborative decision making is grounded in representations of other people’s competence and effort.](https://doi.org/10.1037/xge0001336) | 2023 | 2 | 17 | Journal of Experimental Psychology General | Yang Xiang, Natalia Vélez, Samuel J. Gershman |
| 6 | [Reinforcement-based processes actively regulate motor exploration along redundant solution manifolds](https://doi.org/10.1098/rspb.2023.1475) | 2023 | 2 | 17 | Proceedings of the Royal Society B Biological Sciences | Adam M. Roth, Jan A. Calalo, Rakshith Lokesh, et al. |
| 7 | [The sensorimotor system modulates muscular co-contraction relative to visuomotor feedback responses to regulate movement variability](https://doi.org/10.1152/jn.00472.2022) | 2023 | 2 | 21 | Journal of Neurophysiology | Jan A. Calalo, Adam M. Roth, Rakshith Lokesh, et al. |
| 8 | [Gamification enhances student intrinsic motivation, perceptions of autonomy and relatedness, but minimal impact on competency: a meta-analysis and systematic review](https://doi.org/10.1007/s11423-023-10337-7) | 2024 | 2 | 79 | Educational Technology Research and Development | Liuyufeng Li, Khe Foon Hew, Jiahui Du |
| 9 | [Critical Risks and Opportunities of AI, Economics, Social Network Theory](https://doi.org/10.5281/zenodo.16748934) | 2025 | 1 | 0 | arXiv (Cornell University) | Michael Harré |
| 10 | [Cultivating Organizational Inclusion: An Evolutionary Game Analysis of Dei Implementation Barriers](https://doi.org/10.2139/ssrn.5212481) | 2025 | 1 | 0 | SSRN Electronic Journal | Xu Chu, Qing‐Long Han |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Critical Risks and Opportunities of AI, Economics, Social Network Theory](https://doi.org/10.5281/zenodo.16748934) | 2025 | 1 | 0 | arXiv (Cornell University) | Michael Harré |
| 2 | [Cultivating Organizational Inclusion: An Evolutionary Game Analysis of Dei Implementation Barriers](https://doi.org/10.2139/ssrn.5212481) | 2025 | 1 | 0 | SSRN Electronic Journal | Xu Chu, Qing‐Long Han |
| 3 | [A Networked Game Theoretic Model for Evaluating Resilience in Megaprojects: Integrating Stakeholder Interactions and Lifecycle Adaptability](https://doi.org/10.3390/systems13020122) | 2025 | 1 | 0 | Systems | Hongsi Zhang, Jiang Shu-kai, Xingwu Lin, et al. |
| 4 | [Online Movements Reflect Ongoing Deliberation](https://doi.org/10.1523/jneurosci.1913-24.2025) | 2025 | 2 | 3 | Journal of Neuroscience | Jan A. Calalo, Truc Ngo, Seth R. Sullivan, et al. |
| 5 | [Computational joint action: Dynamical models to understand the development of joint coordination](https://doi.org/10.1371/journal.pcbi.1011948) | 2024 | 2 | 3 | PLoS Computational Biology | Cecilia De Vicariis, Vinil T. Chackochan, Laura Bandini, et al. |
| 6 | [Accuracy and effort costs together lead to temporal asynchrony of multiple motor commands](https://doi.org/10.1152/jn.00435.2022) | 2022 | 2 | 4 | Journal of Neurophysiology | Daniel Tanis, Jan A. Calalo, Joshua G. A. Cashaback, et al. |
| 7 | [Indonesia’s Renewable Natural Resource Management in the Low-Carbon Transition: A Conundrum in Changing Trajectories](https://doi.org/10.3390/su151410997) | 2023 | 1 | 3 | Sustainability | Aloysius Suratin, Suyud Warno Utomo, Dwi Nowo Martono, et al. |
| 8 | [Punishment Leads to Greater Sensorimotor Learning But Less Movement Variability Compared to Reward](https://doi.org/10.1016/j.neuroscience.2024.01.004) | 2024 | 2 | 7 | Neuroscience | Adam M. Roth, Rakshith Lokesh, Jiaqiao Tang, et al. |
| 9 | [Engineering 101: How to Construct a Realist Bridge? Start with Endogenous Foundations](https://doi.org/10.1007/s41111-025-00288-0) | 2025 | 1 | 4 | Chinese Political Science Review | Dwayne Woods |
| 10 | [Complex Spatiotemporal Tuning in Human Upper-Limb Muscles](https://doi.org/10.1152/jn.00791.2009) | 2009 | 2 | 9 | Journal of Neurophysiology | J. Andrew Pruszynski, Timothy Lillicrap, Stephen H. Scott |
<!-- TRENDING-END -->
