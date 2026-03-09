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

Last update: 2026-03-09 06:54 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Citizenship in the global struggles for democracy](https://doi.org/10.1080/1369183x.2026.2631868) | 2026 | 8 | 8 | Journal of Ethnic and Migration Studies | Jelena Džankić, Eleanor Knott, Szabolcs Pogonyi |
| 2 | [Class and migration: interrogating class across borders](https://doi.org/10.1080/1369183x.2026.2630302) | 2026 | 7 | 7 | Journal of Ethnic and Migration Studies | Rose Butler, Sylvia Ang, Christina Ho |
| 3 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 7 | 171966 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 4 | [Democratic decline and the rise of illiberal citizenship in Hungary](https://doi.org/10.1080/1369183x.2026.2631896) | 2026 | 6 | 6 | Journal of Ethnic and Migration Studies | Szabolcs Pogonyi |
| 5 | [‘Seeing the world from my parents’ shoulders’: temporary middle-class Asian migrants, privilege, woes and boundary work](https://doi.org/10.1080/1369183x.2026.2630304) | 2026 | 6 | 6 | Journal of Ethnic and Migration Studies | Sylvia Ang |
| 6 | [SΔϕ-28 — Default Power as Low-Cost Path Assignment: Minimal Conditions for Invisible Fixation after SΔϕ-27 (v1.0)](https://doi.org/10.5281/zenodo.18823396) | 2026 | 6 | 15 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 7 | [Clinical Rating Systems for the Ankle-Hindfoot, Midfoot, Hallux, and Lesser Toes](https://doi.org/10.1177/107110079401500701) | 1994 | 6 | 4434 | Foot & Ankle International | Harold B. Kitaoka, Ian J. Alexander, Robert S. Adelaar, et al. |
| 8 | [Redefining the demos: a tool for ethnodemographic security or a sign of backsliding? Evidence from Abkhazia](https://doi.org/10.1080/1369183x.2026.2631871) | 2026 | 5 | 5 | Journal of Ethnic and Migration Studies | Ramesh Ganohariti |
| 9 | [‘Like aces in a game of cards’: embodied cultural capital, educational achievement and the social im/mobility of migrants](https://doi.org/10.1080/1369183x.2026.2630307) | 2026 | 5 | 5 | Journal of Ethnic and Migration Studies | Megan Watkins |
| 10 | [The Lucian Universe: How Chladni's 1787 Experiment Predicted the Geometric Architecture of Reality](https://doi.org/10.5281/zenodo.18791921) | 2026 | 5 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lucian Randolph |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 100 | 119921 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 73 | 44595 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 32 | 27493 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 21 | 31871 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 19 | 7823 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 78515 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 16 | 22141 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 16 | 94202 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 15 | 29739 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Physics-informed machine learning](https://doi.org/10.1038/s42254-021-00314-5) | 2021 | 12 | 5604 | Nature Reviews Physics | George Em Karniadakis, Ioannis G. Kevrekidis, Lu Lu, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 10 | 13084 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 2 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 7 | 11126 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 3 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 6 | 1406 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 4 | [Predicting aqueous sorption of organic pollutants on microplastics with machine learning](https://doi.org/10.1016/j.watres.2023.120503) | 2023 | 5 | 76 | Water Research | Ye Qiu, Zhejun Li, Tong Zhang, et al. |
| 5 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 379 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 6 | [An Introduction to Statistical Learning](https://doi.org/10.1007/978-3-031-38747-0) | 2023 | 5 | 1740 | Springer texts in statistics | Gareth James, Daniela Witten, Trevor Hastie, et al. |
| 7 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 5 | 4220 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |
| 8 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 19968 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 9 | [Air Quality Forecasting Using Machine Learning: Comparative Analysis and Ensemble Strategies for Enhanced Prediction](https://doi.org/10.1007/s11270-025-08122-8) | 2025 | 4 | 30 | Water Air & Soil Pollution | Yıldırım ÖZÜPAK, Feyyaz Alpsalaz, Emrah Aslan |
| 10 | [Machine learning for microbiologists](https://doi.org/10.1038/s41579-023-00984-1) | 2023 | 4 | 199 | Nature Reviews Microbiology | Francesco Asnicar, Andrew Maltez Thomas, Andrea Passerini, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Air Quality Forecasting Using Machine Learning: Comparative Analysis and Ensemble Strategies for Enhanced Prediction](https://doi.org/10.1007/s11270-025-08122-8) | 2025 | 4 | 30 | Water Air & Soil Pollution | Yıldırım ÖZÜPAK, Feyyaz Alpsalaz, Emrah Aslan |
| 2 | [Predicting aqueous sorption of organic pollutants on microplastics with machine learning](https://doi.org/10.1016/j.watres.2023.120503) | 2023 | 5 | 76 | Water Research | Ye Qiu, Zhejun Li, Tong Zhang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2668 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 11 | 9942 |  | Nils Reimers, Iryna Gurevych |
| 3 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 2852 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2883 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3303 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 6 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 9 | 20961 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 7 | [A systematic review of large language models and their implications in medical education](https://doi.org/10.1111/medu.15402) | 2024 | 8 | 180 | Medical Education | Harrison Lucas, Jeffrey S. Upperman, Jamie R. Robinson |
| 8 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 8 | 4744 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 9 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 8 | 76747 | Biometrics | J. Richard Landis, Gary G. Koch |
| 10 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 7 | 305 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2668 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2883 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3303 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [A systematic review of large language models and their implications in medical education](https://doi.org/10.1111/medu.15402) | 2024 | 8 | 180 | Medical Education | Harrison Lucas, Jeffrey S. Upperman, Jamie R. Robinson |
| 5 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 7 | 305 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |
| 6 | [Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0) | 2024 | 7 | 453 | Nature | Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, et al. |
| 7 | [A survey on large language model based autonomous agents](https://doi.org/10.1007/s11704-024-40231-1) | 2024 | 7 | 856 | Frontiers of Computer Science | Lei Wang, Chen Ma, Xueyang Feng, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 2124 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [THE FAISS LIBRARY](https://doi.org/10.1109/tbdata.2025.3618474) | 2025 | 6 | 214 | IEEE Transactions on Big Data | Matthijs Douze, Alexandr Guzhva, Chengqi Deng, et al. |
| 10 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 6 | 220 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 3 | 15 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 2 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 3 | 22 |  | Maarten Bosma, Ed Chi, Brian Ichter, et al. |
| 3 | [Improving Steering and Verification in AI-Assisted Data Analysis with Interactive Task Decomposition](https://doi.org/10.1145/3654777.3676345) | 2024 | 3 | 33 |  | Majeed Kazemitabaar, Jack M. Williams, Ian Drosos, et al. |
| 4 | [Generalization bias in large language model summarization of scientific research](https://doi.org/10.1098/rsos.241776) | 2025 | 3 | 45 | Royal Society Open Science | Uwe Peters, Benjamin Chin‐Yee |
| 5 | [Large Language Models in Worldwide Medical Exams: Platform Development and Comprehensive Analysis](https://doi.org/10.2196/66114) | 2024 | 3 | 54 | Journal of Medical Internet Research | Hui Zong, Rongrong Wu, Jiaxue Cha, et al. |
| 6 | [A Review of Large Language Models in Medical Education, Clinical Decision Support, and Healthcare Administration](https://doi.org/10.3390/healthcare13060603) | 2025 | 4 | 89 | Healthcare | Josip Vrdoljak, Zvonimir Boban, Marino Vilović, et al. |
| 7 | [Applications and Concerns of ChatGPT and Other Conversational Large Language Models in Health Care: Systematic Review](https://doi.org/10.2196/22769) | 2024 | 3 | 91 | Journal of Medical Internet Research | Leyao Wang, Zhiyu Wan, Congning Ni, et al. |
| 8 | [The role of agentic AI in shaping a smart future: A systematic review](https://doi.org/10.1016/j.array.2025.100399) | 2025 | 3 | 94 | Array | Soodeh Hosseini, Hossein Seilani |
| 9 | [AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways](https://doi.org/10.1145/3716628) | 2025 | 3 | 97 | ACM Computing Surveys | Zehang Deng, Yongjian Guo, Changzhou Han, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Cybertext](https://doi.org/10.56021/9780801855788) | 1997 | 3 | 1229 | Johns Hopkins University Press eBooks | Espen Aarseth |
| 2 | [Foundations of Game-Based Learning](https://doi.org/10.1080/00461520.2015.1122533) | 2015 | 3 | 1430 | Educational Psychologist | Jan L. Plass, Bruce D. Homer, Charles K. Kinzer |
| 3 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 3 | 15189 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |
| 4 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 3 | 33077 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 5 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 3 | 171966 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 6 | [Stochastic game analysis of effective utility-scale photovoltaic recycling under extended producer responsibility framework in China](https://doi.org/10.1016/j.energy.2025.135252) | 2025 | 2 | 6 | Energy | Ningbo Chen, Beijia Huang, Chen Zhang, et al. |
| 7 | [Logic Chain-Driven Complex System Prediction_ A New Paradigm Beyond Pure Mathematical Derivation](https://doi.org/10.5281/zenodo.18337817) | 2025 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 8 | [Empirical Regime Taxonomy in Boundary-Constrained Generative Systems](https://doi.org/10.5281/zenodo.18745468) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 9 | [Morphological Completeness of Positional Bases: Classification, Minimum Threshold, and the Structural Obstruction of Historical Number System](https://doi.org/10.5281/zenodo.18552397) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 10 | [Morphological Saturation in Positional Bases: Finiteness of Exceptions, Early Completion, and the Mixed-Form Bottleneck](https://doi.org/10.5281/zenodo.18745384) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Stochastic game analysis of effective utility-scale photovoltaic recycling under extended producer responsibility framework in China](https://doi.org/10.1016/j.energy.2025.135252) | 2025 | 2 | 6 | Energy | Ningbo Chen, Beijia Huang, Chen Zhang, et al. |
| 2 | [Logic Chain-Driven Complex System Prediction_ A New Paradigm Beyond Pure Mathematical Derivation](https://doi.org/10.5281/zenodo.18337817) | 2025 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 3 | [Empirical Regime Taxonomy in Boundary-Constrained Generative Systems](https://doi.org/10.5281/zenodo.18745468) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 4 | [Morphological Completeness of Positional Bases: Classification, Minimum Threshold, and the Structural Obstruction of Historical Number System](https://doi.org/10.5281/zenodo.18552397) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 5 | [Morphological Saturation in Positional Bases: Finiteness of Exceptions, Early Completion, and the Mixed-Form Bottleneck](https://doi.org/10.5281/zenodo.18745384) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 6 | [Sub-Limit Dynamics: Boundary Interaction as the Structural Determinant in Finitely Constrained Generative Systems](https://doi.org/10.5281/zenodo.18838634) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Lugli Davide |
| 7 | [Constrained Walks on de Bruijn Graphs and the Dynamics of Exhaustion Systems](https://doi.org/10.5281/zenodo.18458103) | 2026 | 2 | 10 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 8 | [Stateless Agents in Exhaustion Systems: Memory, Criterion, and the Geometry of Failure](https://doi.org/10.5281/zenodo.18838360) | 2026 | 2 | 10 | Zenodo (CERN European Organization for Nuclear Research) | davide lugli |
| 9 | [Which policy can effectively promote the formal recycling of power batteries in China?](https://doi.org/10.1016/j.energy.2024.131445) | 2024 | 2 | 43 | Energy | Jingjing Li, Zhaoxin Wang, Hui Li, et al. |
| 10 | [Delegation with strategic complements and substitutes](https://doi.org/10.1007/s00199-024-01628-y) | 2025 | 1 | 1 | Economic Theory | Yadi Yang, Jan Potters |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Delegation with strategic complements and substitutes](https://doi.org/10.1007/s00199-024-01628-y) | 2025 | 1 | 1 | Economic Theory | Yadi Yang, Jan Potters |
| 2 | [Moral reference points: theory and experimental evidence](https://doi.org/10.1007/s00199-025-01639-3) | 2025 | 1 | 1 | Economic Theory | James C. Cox, John A. List, Michael Price, et al. |
| 3 | [Bargaining over communal endowments after prior interaction: experimental evidence](https://doi.org/10.1007/s00199-025-01663-3) | 2025 | 1 | 1 | Economic Theory | Lian Xue, Stefania Sitzia, Theodore L. Turocy |
| 4 | [Testing the simplicity of strategy-proof mechanisms](https://doi.org/10.1007/s00199-025-01684-y) | 2025 | 1 | 1 | Economic Theory | Alexander L. Brown, Daniel Stephenson, Rodrigo A. Velez |
| 5 | [Sorting of trustees: the good and the bad stay in the game](https://doi.org/10.1007/s00199-023-01491-3) | 2023 | 1 | 2 | Economic Theory | Eberhard Feess, Florian Kerzenmacher |
| 6 | [Beyond Hawks and Doves: Can inequality ease coordination?](https://doi.org/10.1007/s00199-024-01603-7) | 2024 | 1 | 2 | Economic Theory | Maria Bigoni, Mario Blázquez de Paz, Chloé Le Coq |
| 7 | [Social aspiration reinforcement learning in Cournot games](https://doi.org/10.1007/s00199-024-01560-1) | 2024 | 1 | 2 | Economic Theory | Enrique Fatás, Antonio J. Morales, Ainhoa Jaramillo-Gutiérrez |
| 8 | [Viable Nash equilibria: an experiment](https://doi.org/10.1007/s00199-024-01585-6) | 2024 | 1 | 2 | Economic Theory | Duk Gyoo Kim, Daehong Min, John Wooders |
| 9 | [Correlated equilibria and forecasts based on Naïve play in Hawk–Dove games](https://doi.org/10.1007/s00199-024-01608-2) | 2024 | 1 | 2 | Economic Theory | Timothy N. Cason, Tridib Sharma, Radovan Vadovič |
| 10 | [Selection through information acquisition in coordination games](https://doi.org/10.1007/s00199-025-01658-0) | 2025 | 1 | 2 | Economic Theory | Michal Szkup, Isabel Trevino |
<!-- TRENDING-END -->
