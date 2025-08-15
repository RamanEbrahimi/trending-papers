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

Last update: 2025-08-15 00:36 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 11 | 189283 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 2 | [Projector augmented-wave method](https://doi.org/10.1103/physrevb.50.17953) | 1994 | 10 | 80879 | Physical review. B, Condensed matter | Peter E. Blöchl |
| 3 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 10 | 147595 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 4 | [Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set](https://doi.org/10.1016/0927-0256(96)00008-0) | 1996 | 9 | 66555 | Computational Materials Science | Georg Kresse, J. Furthmüller |
| 5 | [Efficient iterative schemes for<i>ab initio</i>total-energy calculations using a plane-wave basis set](https://doi.org/10.1103/physrevb.54.11169) | 1996 | 9 | 107280 | Physical review. B, Condensed matter | Georg Kresse, J. Furthmüller |
| 6 | [A consistent and accurate<i>ab initio</i>parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu](https://doi.org/10.1063/1.3382344) | 2010 | 8 | 47407 | The Journal of Chemical Physics | Stefan Grimme, Jens Antony, Stephan Ehrlich, et al. |
| 7 | [Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR and the 2−ΔΔCT Method](https://doi.org/10.1006/meth.2001.1262) | 2001 | 8 | 164306 | Methods | Kenneth J. Livak, Thomas D. Schmittgen |
| 8 | [Multiwfn: A multifunctional wavefunction analyzer](https://doi.org/10.1002/jcc.22885) | 2011 | 7 | 33259 | Journal of Computational Chemistry | Tian Lu, Feiwu Chen |
| 9 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 7 | 107723 | Machine Learning | Leo Breiman |
| 10 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 47 | 107723 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 20 | 24495 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 14 | 70108 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 4 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 12 | 5561 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 11 | 25921 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 9 | 5839 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 7 | [Regularization Paths for Generalized Linear Models via Coordinate Descent](https://doi.org/10.18637/jss.v033.i01) | 2010 | 9 | 14147 | Journal of Statistical Software | Jerome H. Friedman, Trevor Hastie, Robert Tibshirani |
| 8 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 9 | 30050 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 9 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 9 | 189283 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 10 | [Untitled](https://doi.org/10.1023/a:1018054314350) | 1996 | 8 | 16192 | Machine Learning | Leo Breiman |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 68 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Development and validation of an interpretable machine learning model for predicting the risk of distant metastasis in papillary thyroid cancer: a multicenter study](https://doi.org/10.1016/j.eclinm.2024.102913) | 2024 | 3 | 17 | EClinicalMedicine | Fei Hou, Yun Zhu, Hongbo Zhao, et al. |
| 4 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 3 | 67 | Deleted Journal | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 5 | [Developing clinical prediction models: a step-by-step guide](https://doi.org/10.1136/bmj-2023-078276) | 2024 | 3 | 71 | BMJ | Orestis Efthimiou, Michael Seo, Konstantina Chalkou, et al. |
| 6 | [Extracting spatial effects from machine learning model using local interpretation method: An example of SHAP and XGBoost](https://doi.org/10.1016/j.compenvurbsys.2022.101845) | 2022 | 3 | 512 | Computers Environment and Urban Systems | Ziqi Li |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Development and validation of an interpretable machine learning model for predicting the risk of distant metastasis in papillary thyroid cancer: a multicenter study](https://doi.org/10.1016/j.eclinm.2024.102913) | 2024 | 3 | 17 | EClinicalMedicine | Fei Hou, Yun Zhu, Hongbo Zhao, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 68 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 3 | 67 | Deleted Journal | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 4 | [Developing clinical prediction models: a step-by-step guide](https://doi.org/10.1136/bmj-2023-078276) | 2024 | 3 | 71 | BMJ | Orestis Efthimiou, Michael Seo, Konstantina Chalkou, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 11 | 13449 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://doi.org/10.48550/arxiv.1810.04805) | 2018 | 9 | 38233 | arXiv (Cornell University) | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 3 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://doi.org/10.48550/arxiv.1910.10683) | 2019 | 5 | 8262 | arXiv (Cornell University) | Colin Raffel, Noam Shazeer, Adam Roberts, et al. |
| 4 | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://doi.org/10.48550/arxiv.2307.09288) | 2023 | 4 | 1857 | arXiv (Cornell University) | Hugo Touvron, Louis Martin, Kevin H. Stone, et al. |
| 5 | [LLaMA: Open and Efficient Foundation Language Models](https://doi.org/10.48550/arxiv.2302.13971) | 2023 | 4 | 2920 | arXiv (Cornell University) | Hugo Touvron, Thibaut Lavril, Gautier Izacard, et al. |
| 6 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 4 | 60613 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 7 | [A Survey on Multimodal Large Language Models](https://doi.org/10.1093/nsr/nwae403) | 2024 | 3 | 143 | National Science Review | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 8 | [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://doi.org/10.1109/tkde.2024.3352100) | 2024 | 3 | 394 | IEEE Transactions on Knowledge and Data Engineering | Shirui Pan, Linhao Luo, Yufei Wang, et al. |
| 9 | [ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/pnas.2305016120) | 2023 | 3 | 535 | Proceedings of the National Academy of Sciences | Fabrizio Gilardi, Meysam Alizadeh, Maël Kubli |
| 10 | [Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining](https://doi.org/10.1145/3637528) | 2024 | 3 | 553 |  | Unknown |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://doi.org/10.48550/arxiv.2307.09288) | 2023 | 4 | 1857 | arXiv (Cornell University) | Hugo Touvron, Louis Martin, Kevin H. Stone, et al. |
| 2 | [LLaMA: Open and Efficient Foundation Language Models](https://doi.org/10.48550/arxiv.2302.13971) | 2023 | 4 | 2920 | arXiv (Cornell University) | Hugo Touvron, Thibaut Lavril, Gautier Izacard, et al. |
| 3 | [A Survey on Multimodal Large Language Models](https://doi.org/10.1093/nsr/nwae403) | 2024 | 3 | 143 | National Science Review | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 4 | [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://doi.org/10.1109/tkde.2024.3352100) | 2024 | 3 | 394 | IEEE Transactions on Knowledge and Data Engineering | Shirui Pan, Linhao Luo, Yufei Wang, et al. |
| 5 | [ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/pnas.2305016120) | 2023 | 3 | 535 | Proceedings of the National Academy of Sciences | Fabrizio Gilardi, Meysam Alizadeh, Maël Kubli |
| 6 | [Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining](https://doi.org/10.1145/3637528) | 2024 | 3 | 553 |  | Unknown |
| 7 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 3 | 1496 | arXiv (Cornell University) | OpenAI |
| 8 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 3 | 1667 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 9 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 3 | 1813 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 10 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 3 | 2334 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [An outline of Prognostics and health management Large Model: Concepts, Paradigms, and challenges](https://doi.org/10.1016/j.ymssp.2025.112683) | 2025 | 2 | 1 | Mechanical Systems and Signal Processing | Laifa Tao, Shangyu Li, Haifei Liu, et al. |
| 2 | [The imperative of diversity and equity for the adoption of responsible AI in healthcare](https://doi.org/10.3389/frai.2025.1577529) | 2025 | 2 | 2 | Frontiers in Artificial Intelligence | Denise E. Hilling, Imane Ihaddouchen, Stefan N. R. Buijsman, et al. |
| 3 | [Literacy Deep Reinforcement Learning-Based Federated Digital Twin Scheduling for the Software-Defined Factory](https://doi.org/10.3390/electronics13224452) | 2024 | 2 | 0 | Electronics | Je Ahn, Seongjin Yun, Jin-Woo Kwon, et al. |
| 4 | [Benchmarking PathCLIP for Pathology Image Analysis](https://doi.org/10.1007/s10278-024-01128-4) | 2024 | 2 | 5 | Deleted Journal | Sunyi Zheng, Xiaonan Cui, Yuxuan Sun, et al. |
| 5 | [A span-based model for extracting overlapping PICO entities from randomized controlled trial publications](https://doi.org/10.1093/jamia/ocae065) | 2024 | 2 | 6 | Journal of the American Medical Informatics Association | Gongbo Zhang, Yiliang Zhou, Yan Hu, et al. |
| 6 | [CASIT: Collective Intelligent Agent System for Internet of Things](https://doi.org/10.1109/jiot.2024.3366906) | 2024 | 2 | 9 | IEEE Internet of Things Journal | Ningze Zhong, Yi Wang, Rui Xiong, et al. |
| 7 | [Smart grid architecture model standardization and the applicability of domain language specific modeling tools](https://doi.org/10.1109/isie.2017.8001239) | 2017 | 1 | 6 |  | Stefan Wilker, Marcus Meisel, Thilo Sauter |
| 8 | [Knowledge sharing in manufacturing using LLM-powered tools: user study and model benchmarking](https://doi.org/10.3389/frai.2024.1293084) | 2024 | 2 | 15 | Frontiers in Artificial Intelligence | Samuel Kernan Freire, Chaofan Wang, Mina Foosherian, et al. |
| 9 | [Performance of two large language models for data extraction in evidence synthesis](https://doi.org/10.1002/jrsm.1732) | 2024 | 2 | 16 | Research Synthesis Methods | Amanda Konet, Ian B. Thomas, Gerald Gartlehner, et al. |
| 10 | [A survey on potentials, pathways and challenges of large language models in new-generation intelligent manufacturing](https://doi.org/10.1016/j.rcim.2024.102883) | 2024 | 2 | 16 | Robotics and Computer-Integrated Manufacturing | Chao Zhang, Qingfeng Xu, Yongrui Yu, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary Games in Economics](https://doi.org/10.2307/2938222) | 1991 | 2 | 1724 | Econometrica | Daniel Friedman |
| 2 | [A Game Theoretic Model of Struggle with Corruption in Auctions: Computer Simulation](https://doi.org/10.3390/math10193653) | 2022 | 1 | 1 | Mathematics | K. V. Kozlov, G. A. Ougolnitsky |
| 3 | [Evolutionary game analysis of polluting NIMBY facilities reconstruction based on public participation behavior](https://doi.org/10.1371/journal.pone.0276272) | 2022 | 1 | 1 | PLoS ONE | Hui Zhao, Mengran Zhang, Weihan Wang |
| 4 | [Incentive Mechanism Design for Promoting High-Quality Green Buildings in China's Multi-Level Governance System](https://doi.org/10.1016/j.buildenv.2024.112358) | 2024 | 1 | 1 | Building and Environment | Qidan Hu, Feng Xiong, Qiping Shen, et al. |
| 5 | [An auction-based airport slot reallocation scheme considering the grandfather rights of airlines](https://doi.org/10.1016/j.jairtraman.2024.102612) | 2024 | 1 | 2 | Journal of Air Transport Management | Lee Hee-Yeon, Jihyeok Jung, Deok-Joo Lee |
| 6 | [U.S. spent nuclear fuel management: Political, fiscal, and technical feasibility](https://doi.org/10.1016/j.enpol.2013.06.049) | 2013 | 1 | 2 | Energy Policy | Clifford E. Singer |
| 7 | [The demand hierarchy of the government and investors in PPP projects](https://doi.org/10.1108/ecam-01-2022-0052) | 2022 | 1 | 2 | Engineering Construction & Architectural Management | Jiaqi Liu, Jicai Liu |
| 8 | [Dynamic simulation of local acceptance of NIMBY facilities based on the RAS-Deffuant model: The influence of government and media information](https://doi.org/10.1016/j.eiar.2025.107842) | 2025 | 1 | 2 | Environmental Impact Assessment Review | Xin Wan, Rubing Wang, Xiaoyu Dong, et al. |
| 9 | [An Overview of Current Knowledge Concerning the Environmental Consequences of the Nuclear Pollution: Sources, Effects and Control](https://doi.org/10.1007/978-981-10-7185-0_13) | 2017 | 1 | 3 | Energy, environment, and sustainability | Shashi Kant Verma, Shobha Lata Sinha, D. K. Chandraker |
| 10 | [Range dependent expected utility theory based model for NIMBY conflicts in China: An evolutionary game analysis](https://doi.org/10.1371/journal.pone.0271120) | 2022 | 1 | 3 | PLoS ONE | Hui Zhao, Weihan Wang, Mengran Zhang |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Game Theoretic Model of Struggle with Corruption in Auctions: Computer Simulation](https://doi.org/10.3390/math10193653) | 2022 | 1 | 1 | Mathematics | K. V. Kozlov, G. A. Ougolnitsky |
| 2 | [Evolutionary game analysis of polluting NIMBY facilities reconstruction based on public participation behavior](https://doi.org/10.1371/journal.pone.0276272) | 2022 | 1 | 1 | PLoS ONE | Hui Zhao, Mengran Zhang, Weihan Wang |
| 3 | [Incentive Mechanism Design for Promoting High-Quality Green Buildings in China's Multi-Level Governance System](https://doi.org/10.1016/j.buildenv.2024.112358) | 2024 | 1 | 1 | Building and Environment | Qidan Hu, Feng Xiong, Qiping Shen, et al. |
| 4 | [An auction-based airport slot reallocation scheme considering the grandfather rights of airlines](https://doi.org/10.1016/j.jairtraman.2024.102612) | 2024 | 1 | 2 | Journal of Air Transport Management | Lee Hee-Yeon, Jihyeok Jung, Deok-Joo Lee |
| 5 | [The demand hierarchy of the government and investors in PPP projects](https://doi.org/10.1108/ecam-01-2022-0052) | 2022 | 1 | 2 | Engineering Construction & Architectural Management | Jiaqi Liu, Jicai Liu |
| 6 | [Dynamic simulation of local acceptance of NIMBY facilities based on the RAS-Deffuant model: The influence of government and media information](https://doi.org/10.1016/j.eiar.2025.107842) | 2025 | 1 | 2 | Environmental Impact Assessment Review | Xin Wan, Rubing Wang, Xiaoyu Dong, et al. |
| 7 | [Range dependent expected utility theory based model for NIMBY conflicts in China: An evolutionary game analysis](https://doi.org/10.1371/journal.pone.0271120) | 2022 | 1 | 3 | PLoS ONE | Hui Zhao, Weihan Wang, Mengran Zhang |
| 8 | [Promoting strategy of rural energy consumption electrification: a network game theory approach](https://doi.org/10.1007/s10668-024-04643-0) | 2024 | 1 | 3 | Environment Development and Sustainability | Yong Sun, Yunhe Pei, Pei Zhang, et al. |
| 9 | [Urban security challenges in major cities, with a specific emphasis on privacy management in the metropolises](https://doi.org/10.1007/s44274-024-00116-3) | 2024 | 1 | 3 | Discover Environment | Mohammad Ali Khaliji, Kamran Jafarpour Ghalehteimouri |
| 10 | [The behavioral strategies of multiple stakeholders in environmental nimby conflicts: An evolutionary game theoretical research](https://doi.org/10.3389/fenvs.2022.973555) | 2022 | 1 | 4 | Frontiers in Environmental Science | Zhaoyang Long, Sisi Wang, Muhammad Tayyab Sohail |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Game Theoretic Model of Struggle with Corruption in Auctions: Computer Simulation](https://doi.org/10.3390/math10193653) | 2022 | 1 | 1 | Mathematics | K. V. Kozlov, G. A. Ougolnitsky |
| 2 | [Evolutionary game analysis of polluting NIMBY facilities reconstruction based on public participation behavior](https://doi.org/10.1371/journal.pone.0276272) | 2022 | 1 | 1 | PLoS ONE | Hui Zhao, Mengran Zhang, Weihan Wang |
| 3 | [Incentive Mechanism Design for Promoting High-Quality Green Buildings in China's Multi-Level Governance System](https://doi.org/10.1016/j.buildenv.2024.112358) | 2024 | 1 | 1 | Building and Environment | Qidan Hu, Feng Xiong, Qiping Shen, et al. |
| 4 | [An auction-based airport slot reallocation scheme considering the grandfather rights of airlines](https://doi.org/10.1016/j.jairtraman.2024.102612) | 2024 | 1 | 2 | Journal of Air Transport Management | Lee Hee-Yeon, Jihyeok Jung, Deok-Joo Lee |
| 5 | [U.S. spent nuclear fuel management: Political, fiscal, and technical feasibility](https://doi.org/10.1016/j.enpol.2013.06.049) | 2013 | 1 | 2 | Energy Policy | Clifford E. Singer |
| 6 | [The demand hierarchy of the government and investors in PPP projects](https://doi.org/10.1108/ecam-01-2022-0052) | 2022 | 1 | 2 | Engineering Construction & Architectural Management | Jiaqi Liu, Jicai Liu |
| 7 | [Dynamic simulation of local acceptance of NIMBY facilities based on the RAS-Deffuant model: The influence of government and media information](https://doi.org/10.1016/j.eiar.2025.107842) | 2025 | 1 | 2 | Environmental Impact Assessment Review | Xin Wan, Rubing Wang, Xiaoyu Dong, et al. |
| 8 | [An Overview of Current Knowledge Concerning the Environmental Consequences of the Nuclear Pollution: Sources, Effects and Control](https://doi.org/10.1007/978-981-10-7185-0_13) | 2017 | 1 | 3 | Energy, environment, and sustainability | Shashi Kant Verma, Shobha Lata Sinha, D. K. Chandraker |
| 9 | [Range dependent expected utility theory based model for NIMBY conflicts in China: An evolutionary game analysis](https://doi.org/10.1371/journal.pone.0271120) | 2022 | 1 | 3 | PLoS ONE | Hui Zhao, Weihan Wang, Mengran Zhang |
| 10 | [Promoting strategy of rural energy consumption electrification: a network game theory approach](https://doi.org/10.1007/s10668-024-04643-0) | 2024 | 1 | 3 | Environment Development and Sustainability | Yong Sun, Yunhe Pei, Pei Zhang, et al. |

### Topic: computer science

Topic: computer science — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A robótica como alternativa para o ensino e aprendizagem da Matemática na educação infantil: revisão sistemática da literatura](https://doi.org/10.55905/revconv.16n.4-010) | 2023 | 1 | 1 | Contribuciones a las Ciencias Sociales | Rosimere Cleide Souza Desidério, Paulo Sérgio Teixeira Do Prado |
| 2 | [Avaliação da eficiência das metodologias de problem based learning e rotação por estações em conjunto durante o ensino de robótica](https://doi.org/10.22456/1679-1916.134380) | 2023 | 1 | 1 | RENOTE | Lucielton Manoel da Silva, Marco Leite, L. Melo, et al. |
| 3 | [Randic and reciprocal randic spectral radii and energies of some graph operations](https://doi.org/10.3233/jifs-221938) | 2023 | 1 | 1 | Journal of Intelligent & Fuzzy Systems | Ahmad Raza Bilal, Mobeen Munir |
| 4 | [Albertson (Alb) spectral radii and Albertson (Alb) energies of graph operation](https://doi.org/10.3389/fchem.2023.1267291) | 2023 | 1 | 1 | Frontiers in Chemistry | Mobeen Munir, Urwah Tul Wusqa |
| 5 | [SDD Spectral Radii and SDD Energies of Graph Operations](https://doi.org/10.1016/j.tcs.2024.114651) | 2024 | 1 | 1 | Theoretical Computer Science | Ahmad Raza Bilal, Mobeen Munir |
| 6 | [Theoretical foundations for recommender systems](https://doi.org/10.1049/pbpc035f_ch2) | 2019 | 1 | 1 | Institution of Engineering and Technology eBooks | Mirza Zaeem Baig, Hasina Khatoon, Syeda Saleha Raza, et al. |
| 7 | [Recommender Systems: Algorithms and their Applications](https://doi.org/10.1007/978-981-97-0538-2) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 8 | [Collaborative Filtering and Content-Based Systems](https://doi.org/10.1007/978-981-97-0538-2_3) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 9 | [Overview of Recommendation Systems](https://doi.org/10.1007/978-981-97-0538-2_2) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 10 | [Educação Climática 4.0: Como Potencializar o Papel dos Professores com PLN e KG?](https://doi.org/10.5753/laai-ethics.2024.32455) | 2024 | 1 | 0 |  | Marco Aurélio Schünke, Dante Augusto Couto Barone, Rodrigo de Cássio da Silva |

#### Recent Movers in computer science

Papers from the last 3 years (2022-2025) with most recent citations in **computer science**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A robótica como alternativa para o ensino e aprendizagem da Matemática na educação infantil: revisão sistemática da literatura](https://doi.org/10.55905/revconv.16n.4-010) | 2023 | 1 | 1 | Contribuciones a las Ciencias Sociales | Rosimere Cleide Souza Desidério, Paulo Sérgio Teixeira Do Prado |
| 2 | [Avaliação da eficiência das metodologias de problem based learning e rotação por estações em conjunto durante o ensino de robótica](https://doi.org/10.22456/1679-1916.134380) | 2023 | 1 | 1 | RENOTE | Lucielton Manoel da Silva, Marco Leite, L. Melo, et al. |
| 3 | [Randic and reciprocal randic spectral radii and energies of some graph operations](https://doi.org/10.3233/jifs-221938) | 2023 | 1 | 1 | Journal of Intelligent & Fuzzy Systems | Ahmad Raza Bilal, Mobeen Munir |
| 4 | [Albertson (Alb) spectral radii and Albertson (Alb) energies of graph operation](https://doi.org/10.3389/fchem.2023.1267291) | 2023 | 1 | 1 | Frontiers in Chemistry | Mobeen Munir, Urwah Tul Wusqa |
| 5 | [SDD Spectral Radii and SDD Energies of Graph Operations](https://doi.org/10.1016/j.tcs.2024.114651) | 2024 | 1 | 1 | Theoretical Computer Science | Ahmad Raza Bilal, Mobeen Munir |
| 6 | [Recommender Systems: Algorithms and their Applications](https://doi.org/10.1007/978-981-97-0538-2) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 7 | [Collaborative Filtering and Content-Based Systems](https://doi.org/10.1007/978-981-97-0538-2_3) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 8 | [Overview of Recommendation Systems](https://doi.org/10.1007/978-981-97-0538-2_2) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 9 | [Educação Climática 4.0: Como Potencializar o Papel dos Professores com PLN e KG?](https://doi.org/10.5753/laai-ethics.2024.32455) | 2024 | 1 | 0 |  | Marco Aurélio Schünke, Dante Augusto Couto Barone, Rodrigo de Cássio da Silva |
| 10 | [PSO and the Traveling Salesman Problem: An Intelligent Optimization
  Approach](https://doi.org/10.48550/arxiv.2501.15319) | 2025 | 1 | 0 | arXiv (Cornell University) | Kael Silva Araújo, Francisco Márcio Barboza |

#### Future Hits in computer science

Papers with high recency ratio but < 100 total citations in **computer science**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A robótica como alternativa para o ensino e aprendizagem da Matemática na educação infantil: revisão sistemática da literatura](https://doi.org/10.55905/revconv.16n.4-010) | 2023 | 1 | 1 | Contribuciones a las Ciencias Sociales | Rosimere Cleide Souza Desidério, Paulo Sérgio Teixeira Do Prado |
| 2 | [Avaliação da eficiência das metodologias de problem based learning e rotação por estações em conjunto durante o ensino de robótica](https://doi.org/10.22456/1679-1916.134380) | 2023 | 1 | 1 | RENOTE | Lucielton Manoel da Silva, Marco Leite, L. Melo, et al. |
| 3 | [Randic and reciprocal randic spectral radii and energies of some graph operations](https://doi.org/10.3233/jifs-221938) | 2023 | 1 | 1 | Journal of Intelligent & Fuzzy Systems | Ahmad Raza Bilal, Mobeen Munir |
| 4 | [Albertson (Alb) spectral radii and Albertson (Alb) energies of graph operation](https://doi.org/10.3389/fchem.2023.1267291) | 2023 | 1 | 1 | Frontiers in Chemistry | Mobeen Munir, Urwah Tul Wusqa |
| 5 | [SDD Spectral Radii and SDD Energies of Graph Operations](https://doi.org/10.1016/j.tcs.2024.114651) | 2024 | 1 | 1 | Theoretical Computer Science | Ahmad Raza Bilal, Mobeen Munir |
| 6 | [Theoretical foundations for recommender systems](https://doi.org/10.1049/pbpc035f_ch2) | 2019 | 1 | 1 | Institution of Engineering and Technology eBooks | Mirza Zaeem Baig, Hasina Khatoon, Syeda Saleha Raza, et al. |
| 7 | [Recommender Systems: Algorithms and their Applications](https://doi.org/10.1007/978-981-97-0538-2) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 8 | [Collaborative Filtering and Content-Based Systems](https://doi.org/10.1007/978-981-97-0538-2_3) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 9 | [Overview of Recommendation Systems](https://doi.org/10.1007/978-981-97-0538-2_2) | 2024 | 1 | 1 | Transactions on computer systems and networks | Pushpendu Kar, Monideepa Roy, Sujoy Datta |
| 10 | [Educação Climática 4.0: Como Potencializar o Papel dos Professores com PLN e KG?](https://doi.org/10.5753/laai-ethics.2024.32455) | 2024 | 1 | 0 |  | Marco Aurélio Schünke, Dante Augusto Couto Barone, Rodrigo de Cássio da Silva |
<!-- TRENDING-END -->
