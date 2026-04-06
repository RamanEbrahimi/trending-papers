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

Last update: 2026-04-06 07:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [THE THREE COMPRESSIONS: Lossy, Predatory, and Witness — A Semiotic Thermodynamics](https://doi.org/10.5281/zenodo.19053469) | 2026 | 8 | 56 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil, Rex Fraction |
| 2 | [Alien-Corrected Borel Probes in Class C (Paper 20 in the Non-Holomorphic Fractal Series)](https://doi.org/10.5281/zenodo.19338894) | 2026 | 7 | 17 | Zenodo (CERN European Organization for Nuclear Research) | Michael Bird |
| 3 | [Ghost Meaning: The Semantic Entropy Crisis and the Architecture That Was Already Waiting DOI: 10.5281/zenodo.18804767 — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18804767) | 2026 | 7 | 34 | Open MIND | Lee Sharks, Johannes Sigil, Rex Fraction, et al. |
| 4 | [Borel-Plane Probes at the Aether Limit: Extended Negative Atlas for the Non-Holomorphic Bird Map (Paper 21 in the Non-Holomorphic Fractal Series)](https://doi.org/10.5281/zenodo.19342017) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Michael Bird |
| 5 | [RC-1 — Residue Communication A Reversible Continuity Layer Between Stateless Interaction and Total Storage Continuity Through Chromatic Afterfields in Messaging, Telephony, and Interface Systems](https://doi.org/10.5281/zenodo.19157929) | 2026 | 6 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Raynor Eissens |
| 6 | [The $650 Billion Gap: Physical Infrastructure, Semantic Governance, and the Architecture of Compression-Survival](https://doi.org/10.5281/zenodo.19338708) | 2026 | 6 | 16 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 7 | [2024 ESC Guidelines for the management of chronic coronary syndromes](https://doi.org/10.1093/eurheartj/ehae177) | 2024 | 6 | 1981 | European Heart Journal | Christiaan Vrints, Felicita Andreotti, Konstantinos C. Koskinas, et al. |
| 8 | [International Norm Dynamics and Political Change](https://doi.org/10.1162/002081898550789) | 1998 | 6 | 7994 | International Organization | Martha Finnemore, Kathryn Sikkink |
| 9 | [Chessboard politics: the contested emergence of EU return and readmission norms](https://doi.org/10.1080/1369183x.2025.2601254) | 2026 | 5 | 5 | Journal of Ethnic and Migration Studies | Sandra Lavenex, Frowin Rausis |
| 10 | [Changing norms in EU return policy? A longitudinal analysis of commission documents on return](https://doi.org/10.1080/1369183x.2026.2633666) | 2026 | 5 | 5 | Journal of Ethnic and Migration Studies | Paula Hoffmeyer-Zlotnik, Philipp Stutz |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 116 | 121673 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 78 | 45671 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 36 | 27905 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 31 | 8126 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 29 | 32205 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 22 | 22500 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 20 | 30129 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 1597 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 13 | 79462 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 13 | 95334 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 14 | 1597 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 12 | 13164 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 3 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 441 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 4 | [Insights into geospatial heterogeneity of landslide susceptibility based on the SHAP-XGBoost model](https://doi.org/10.1016/j.jenvman.2023.117357) | 2023 | 5 | 520 | Journal of Environmental Management | Junyi Zhang, Junyi Zhang, Xianglong Ma, et al. |
| 5 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 5 | 11828 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2818 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 15 | 2985 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 10 | 31643 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 9 | 578 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 9 | 1182 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3379 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 9 | 4398 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 8 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 9 | 4921 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 9 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 9 | 10206 |  | Nils Reimers, Iryna Gurevych |
| 10 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 2235 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 17 | 2818 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 15 | 2985 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 9 | 578 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 9 | 1182 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3379 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 6 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 9 | 4398 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 7 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 2235 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 8 | [Current applications and challenges in large language models for patient care: a systematic review](https://doi.org/10.1038/s43856-024-00717-2) | 2025 | 7 | 162 | Communications Medicine | Felix Busch, Lena Hoffmann, Christopher Rueger, et al. |
| 9 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 6 | 465 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 10 | [Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0) | 2024 | 6 | 502 | Nature | Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [All Languages Matter: On the Multilingual Safety of LLMs](https://doi.org/10.18653/v1/2024.findings-acl.349) | 2024 | 3 | 14 |  | Wenxuan Wang, Zhaopeng Tu, Chang Chen, et al. |
| 2 | [A Paradigm Shift from “Human Writing” to “Machine Generation” in Personality Test Development: an Application of State-of-the-Art Natural Language Processing](https://doi.org/10.1007/s10869-022-09864-6) | 2022 | 3 | 39 | Journal of Business and Psychology | Philseok Lee, Shea Fyffe, Mina Son, et al. |
| 3 | [Scientific Large Language Models: A Survey on Biological &amp; Chemical Domains](https://doi.org/10.1145/3715318) | 2025 | 4 | 55 | ACM Computing Surveys | Qiang Zhang, Keyan Ding, Tingting Lv, et al. |
| 4 | [The AI‐IP: Minimizing the guesswork of personality scale item development through artificial intelligence](https://doi.org/10.1111/peps.12543) | 2022 | 3 | 46 | Personnel Psychology | Ivan Hernandez, Weiwen Nie |
| 5 | [The Clinicians’ Guide to Large Language Models: A General Perspective With a Focus on Hallucinations](https://doi.org/10.2196/59823) | 2025 | 4 | 68 | Interactive Journal of Medical Research | Dimitri Roustan, François Bastardot |
| 6 | [Retrieval augmented generation for large language models in healthcare: A systematic review](https://doi.org/10.1371/journal.pdig.0000877) | 2025 | 4 | 87 | PLOS Digital Health | Lameck Mbangula Amugongo, Pietro Mascheroni, Steven E. Brooks, et al. |
| 7 | [Data Augmentation using LLMs: Data Perspectives, Learning Paradigms and Challenges](https://doi.org/10.18653/v1/2024.findings-acl.97) | 2024 | 3 | 70 |  | Bosheng Ding, Chengwei Qin, R. P. Zhao, et al. |
| 8 | [NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails](https://doi.org/10.18653/v1/2023.emnlp-demo.40) | 2023 | 3 | 75 |  | Traian Rebedea, Razvan Dinu, Makesh Narsimhan Sreedhar, et al. |
| 9 | [Effective test generation using pre-trained Large Language Models and mutation testing](https://doi.org/10.1016/j.infsof.2024.107468) | 2024 | 3 | 84 | Information and Software Technology | Arghavan Moradi Dakhel, Amin Nikanjam, Vahid Majdinasab, et al. |
| 10 | [Exploring DeepSeek: A Survey on Advances, Applications, Challenges and Future Directions](https://doi.org/10.1109/jas.2025.125498) | 2025 | 3 | 86 | IEEE/CAA Journal of Automatica Sinica | Zehang Deng, Wanlun Ma, Qing‐Long Han, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 26 | 175046 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 13 | 102874 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 3 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 13 | 121673 | Machine Learning | Leo Breiman |
| 4 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 12 | 87307 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 10 | 8126 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [Statistical Power Analysis for the Behavioral Sciences](https://doi.org/10.4324/9780203771587) | 2013 | 10 | 22518 |  | Jacob Cohen |
| 7 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 10 | 45671 |  | Tianqi Chen, Carlos Guestrin |
| 8 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 10 | 73835 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 9 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 9 | 40949 | MIS Quarterly | Venkatesh, Jeremy Morris, Davis, et al. |
| 10 | [Diagnostic and Statistical Manual of Mental Disorders](https://doi.org/10.1176/appi.books.9780890425596) | 2013 | 9 | 111906 | American Psychiatric Association eBooks | Annette Lolk |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 4 | 516 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 4398 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [Game-based learning in early childhood education: a systematic review and meta-analysis](https://doi.org/10.3389/fpsyg.2024.1307881) | 2024 | 3 | 93 | Frontiers in Psychology | Manar Soud Alotaibi |
| 4 | [Effectiveness of AI-assisted game-based learning on science learning outcomes, intrinsic motivation, cognitive load, and learning behavior](https://doi.org/10.1007/s10639-024-12553-x) | 2024 | 3 | 95 | Education and Information Technologies | Ching‐Huei Chen, Ching-Ling Chang |
| 5 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 3 | 1497 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Game-based learning in early childhood education: a systematic review and meta-analysis](https://doi.org/10.3389/fpsyg.2024.1307881) | 2024 | 3 | 93 | Frontiers in Psychology | Manar Soud Alotaibi |
| 2 | [Effectiveness of AI-assisted game-based learning on science learning outcomes, intrinsic motivation, cognitive load, and learning behavior](https://doi.org/10.1007/s10639-024-12553-x) | 2024 | 3 | 95 | Education and Information Technologies | Ching‐Huei Chen, Ching-Ling Chang |
<!-- TRENDING-END -->
