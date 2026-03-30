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

Last update: 2026-03-30 07:19 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Inertia Does No Work: An Energy-Constraint Interpretation from Energy-Efficiency Theory](https://doi.org/10.5281/zenodo.19224396) | 2026 | 20 | 71 | Zenodo (CERN European Organization for Nuclear Research) | Hongpu Yang |
| 2 | [Information Is Not a Substance: From Maxwell's Demon to an Energy Interpretation of Information Thermodynamics](https://doi.org/10.5281/zenodo.19233995) | 2026 | 18 | 56 | Zenodo (CERN European Organization for Nuclear Research) | Hongpu Yang |
| 3 | [The Two Fundamental Forms of Energy: Free State and Constrained State — A Physical Ontological Foundation of Energy-Efficiency Theory](https://doi.org/10.5281/zenodo.19233655) | 2026 | 18 | 62 | Zenodo (CERN European Organization for Nuclear Research) | Hongpu Yang |
| 4 | [The Principle of Minimum Time: A Unifying Constraint from Energy-Efficiency Theory](https://doi.org/10.5281/zenodo.19234494) | 2026 | 17 | 54 | Zenodo (CERN European Organization for Nuclear Research) | Hongpu Yang |
| 5 | [An Energy-Efficiency Interpretation of Light: The Extremity of Free-State Energy](https://doi.org/10.5281/zenodo.19235113) | 2026 | 16 | 48 | Zenodo (CERN European Organization for Nuclear Research) | Hongpu Yang |
| 6 | [Hidden behind the scene – high diversity, low connectivity of deep-sea Amphipoda in the polymetallic nodule fields in the Northeast Pacific](https://doi.org/10.5194/egusphere-2025-1794) | 2025 | 14 | 14 |  | Anna М. Jażdżewska, Karolina Biniek, Pedro Martínez Arbizu, et al. |
| 7 | [<scp>bold</scp>: The Barcode of Life Data System (http://www.barcodinglife.org)](https://doi.org/10.1111/j.1471-8286.2007.01678.x) | 2007 | 14 | 6123 | Molecular Ecology Notes | Sujeevan Ratnasingham, Paul D. N. Hebert |
| 8 | [The Ontology of Mass: Spatial Density of Constrained-State Energy — A Physical Foundation of Energy-Efficiency Theory](https://doi.org/10.5281/zenodo.19233822) | 2026 | 13 | 42 | Zenodo (CERN European Organization for Nuclear Research) | Hongpu Yang |
| 9 | [A 3D imaging and visualization workflow, using confocal microscopy and advanced image processing for brachyuran crab larvae](https://doi.org/10.1111/jmi.12540) | 2017 | 13 | 45 | Journal of Microscopy | Seyit Ali Kamanlı, Terue C. Kihara, Alexander D. Ball, et al. |
| 10 | [Crustacea amphipoda borealia et arctica, auctore Axel Boeck ...](https://doi.org/10.5962/bhl.title.2056) | 1870 | 13 | 69 |  | Axel Boeck |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 107 | 121231 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 83 | 45396 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 39 | 27793 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 33 | 8062 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 25 | 32106 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 20 | 22380 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 17 | 95068 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 8 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 1560 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 9 | [Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations](https://doi.org/10.1016/j.jcp.2018.10.045) | 2018 | 14 | 15043 | Journal of Computational Physics | Maziar Raissi, Paris Perdikaris, George Em Karniadakis |
| 10 | [The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation](https://doi.org/10.7717/peerj-cs.623) | 2021 | 13 | 4476 | PeerJ Computer Science | Davide Chicco, Matthijs J. Warrens, Giuseppe Jurman |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 1560 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 13138 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 3 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 428 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 4 | [Artificial Intelligence for Materials Discovery, Development, and Optimization](https://doi.org/10.1021/acsnano.5c04200) | 2025 | 5 | 69 | ACS Nano | Benediktus Madika, Aditi Saha, Chi Jung Kang, et al. |
| 5 | [The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts](https://doi.org/10.1021/acscatal.2c05426) | 2023 | 4 | 268 | ACS Catalysis | Richard Tran, Janice Lan, Muhammed Shuaibi, et al. |
| 6 | [Scaling deep learning for materials discovery](https://doi.org/10.1038/s41586-023-06735-9) | 2023 | 4 | 1040 | Nature | Amil Merchant, Simon Batzner, Samuel S. Schoenholz, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Artificial Intelligence for Materials Discovery, Development, and Optimization](https://doi.org/10.1021/acsnano.5c04200) | 2025 | 5 | 69 | ACS Nano | Benediktus Madika, Aditi Saha, Chi Jung Kang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2790 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 14 | 10155 |  | Nils Reimers, Iryna Gurevych |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 13 | 3364 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 13 | 4884 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 2966 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 11 | 4356 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 7 | [SOSA-MVU: Formal Validation Layer for Deterministic Output Control in LLM Systems](https://doi.org/10.5281/zenodo.19154913) | 2026 | 8 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Michele Bottino |
| 8 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 8 | 862 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 9 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 8 | 31549 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 10 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 7 | 78 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2790 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 13 | 3364 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 2966 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 11 | 4356 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [SOSA-MVU: Formal Validation Layer for Deterministic Output Control in LLM Systems](https://doi.org/10.5281/zenodo.19154913) | 2026 | 8 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Michele Bottino |
| 6 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 8 | 862 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 7 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 7 | 78 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 8 | [Large language models in patient education: a scoping review of applications in medicine](https://doi.org/10.3389/fmed.2024.1477898) | 2024 | 7 | 155 | Frontiers in Medicine | Serhat Aydın, Mert Karabacak, Victoria Vlachos, et al. |
| 9 | [A systematic review of large language model (LLM) evaluations in clinical medicine](https://doi.org/10.1186/s12911-025-02954-4) | 2025 | 7 | 167 | BMC Medical Informatics and Decision Making | Sina Shool, Sara Adimi, Reza Saboori Amleshi, et al. |
| 10 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 7 | 347 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [SOSA-MVU: Formal Validation Layer for Deterministic Output Control in LLM Systems](https://doi.org/10.5281/zenodo.19154913) | 2026 | 8 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Michele Bottino |
| 2 | [NoetherSolve Toolkit: Conservation Law Monitoring and Discovery for Numerical Simulations](https://doi.org/10.5281/zenodo.19029880) | 2026 | 5 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 3 | [Systematic Mapping of LLM Knowledge Boundaries Across 67 Scientific Domains](https://doi.org/10.5281/zenodo.19055582) | 2026 | 5 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Bryan Sanchez |
| 4 | [Jailbroken: How Does LLM Safety Training Fail?](https://doi.org/10.52202/075280-3508) | 2023 | 3 | 6 |  | Nika Haghtalab, Jacob Steinhardt, Alexander Wei |
| 5 | [‘Another DeepSeek moment’: Chinese AI model Kimi K2 stirs excitement](https://doi.org/10.1038/d41586-025-02275-6) | 2025 | 3 | 6 | Nature | Elizabeth Gibney |
| 6 | [Limitations of large language models in clinical problem-solving arising from inflexible reasoning](https://doi.org/10.1038/s41598-025-22940-0) | 2025 | 4 | 18 | Discovery Research Portal (University of Dundee) | Jonathan Kim, Anna Podlasek, Kie Shidara, et al. |
| 7 | [Prompt Engineering or Fine-Tuning: An Empirical Assessment of LLMs for Code](https://doi.org/10.1109/msr66628.2025.00082) | 2025 | 3 | 17 |  | Jiho Shin, C.J. Tang, Tahmineh Mohati, et al. |
| 8 | [Large Language Models Can Be Used to Estimate the Latent Positions of Politicians](https://doi.org/10.48550/arxiv.2303.12057) | 2023 | 3 | 29 | arXiv (Cornell University) | Patrick Y. Wu, Jonathan Nagler, Joshua A. Tucker, et al. |
| 9 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 7 | 78 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 10 | [Large language models overcome the challenges of unstructured text data in ecology](https://doi.org/10.1016/j.ecoinf.2024.102742) | 2024 | 3 | 35 | Ecological Informatics | Andry Castro, João Pinto, Luís Reino, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 23 | 174374 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 15 | 121231 | Machine Learning | Leo Breiman |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 11 | 8062 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 11 | 62260 | MIS Quarterly | Fred D. Davis |
| 5 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 11 | 86674 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 6 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 10 | 45396 |  | Tianqi Chen, Carlos Guestrin |
| 7 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 10 | 73624 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 8 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 10 | 102650 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 9 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 9 | 40825 | MIS Quarterly | Venkatesh, Jeremy Morris, Davis, et al. |
| 10 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 8 | 82169 | Organizational Behavior and Human Decision Processes | Icek Ajzen |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 428 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 2 | [Sport as a Tool for Inclusion and Sustainability in Secondary School: A Qualitative-Quantitative Analysis](https://doi.org/10.3280/riss2025oa19679) | 2025 | 3 | 5 | RIVISTA DI STUDI SULLA SOSTENIBILITA | Davide Di Palma, Livinus Ogbondah, Domenico Tafuri |
| 3 | [Digitalizing cultural heritage through metaverse applications: challenges, opportunities, and strategies](https://doi.org/10.1186/s40494-024-01403-1) | 2024 | 3 | 96 | Heritage Science | Dipima Buragohain, Yahui Meng, Chaoqun Deng, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Sport as a Tool for Inclusion and Sustainability in Secondary School: A Qualitative-Quantitative Analysis](https://doi.org/10.3280/riss2025oa19679) | 2025 | 3 | 5 | RIVISTA DI STUDI SULLA SOSTENIBILITA | Davide Di Palma, Livinus Ogbondah, Domenico Tafuri |
| 2 | [Digitalizing cultural heritage through metaverse applications: challenges, opportunities, and strategies](https://doi.org/10.1186/s40494-024-01403-1) | 2024 | 3 | 96 | Heritage Science | Dipima Buragohain, Yahui Meng, Chaoqun Deng, et al. |
<!-- TRENDING-END -->
