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

Last update: 2026-05-18 09:48 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [SΔϕ-56 — Transition Completion Cost: Friction Coefficients, Disclosure-to-Re-entry Cost, and FIP as TCC Differential (v1.3)](https://doi.org/10.5281/zenodo.20116959) | 2026 | 26 | 36 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 2 | [SΔϕ-62 — World Model Kernel: Observed Trace, Inference, UMR, Binding Status, and Revision Path Protocols (v1.1, AI-Readable Kernel Package)](https://doi.org/10.5281/zenodo.20149548) | 2026 | 18 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 3 | [SΔϕ-57 — Lent Thought: Thought Ownership, World-Binding, and Cost Attribution in Human-AI Reasoning](https://doi.org/10.5281/zenodo.20047922) | 2026 | 16 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 4 | [SΔϕ-01 — Sofience–Δϕ Minimal Core: Phase-Change Formalism of Existence (v1.1)](https://doi.org/10.5281/zenodo.18730265) | 2026 | 16 | 50 | Open MIND | Sofience |
| 5 | [SΔϕ-62 — World Model Kernel: Trace–UMR–Binding Protocol for AI Inference](https://doi.org/10.5281/zenodo.20099004) | 2026 | 14 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 6 | [SΔϕ-58 — Cost Attribution Symmetry Index](https://doi.org/10.5281/zenodo.20059485) | 2026 | 12 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 7 | [SΔϕ-02 — Subject as Interpretive Emergence: Extension of the Sofience–Δϕ Minimal Core (v1.1)](https://doi.org/10.5281/zenodo.18730296) | 2026 | 12 | 29 | Open MIND | Sofience |
| 8 | [SΔϕ-64 — Language as Temporary Fixation: Declaration, Trace, Re-entry, and the Right and Responsibility of Inevitable Mistranslation (v1.1)](https://doi.org/10.5281/zenodo.20120636) | 2026 | 11 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 9 | [SΔϕ-54 — Disclosure Terrain Index: Minimal Quantification of Silence Inference](https://doi.org/10.5281/zenodo.20029122) | 2026 | 11 | 21 | Zenodo (CERN European Organization for Nuclear Research) | Sofience |
| 10 | [SΔϕ-03 — Irreversibility as the Minimal Condition of Existence (v1.1)](https://doi.org/10.5281/zenodo.18730448) | 2026 | 11 | 25 | Open MIND | Sofience |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 84 | 123855 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 57 | 47080 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 17 | 8508 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 16 | 28420 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 14 | 22932 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 13 | 32618 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [Machine Learning: Algorithms, Real-World Applications and Research Directions](https://doi.org/10.1007/s42979-021-00592-x) | 2021 | 11 | 5008 | SN Computer Science | Iqbal H. Sarker |
| 8 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 11 | 15917 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 9 | [The coefficient of determination R-squared is more informative than SMAPE, MAE, MAPE, MSE and RMSE in regression analysis evaluation](https://doi.org/10.7717/peerj-cs.623) | 2021 | 10 | 4675 | PeerJ Computer Science | Davide Chicco, Matthijs J. Warrens, Giuseppe Jurman |
| 10 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 10 | 8605 | Nature Machine Intelligence | Cynthia Rudin |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Feature selection strategies: a comparative analysis of SHAP-value and importance-based methods](https://doi.org/10.1186/s40537-024-00905-w) | 2024 | 6 | 471 | Journal Of Big Data | Huanjing Wang, Qianxin Liang, John Hancock, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 6 | 1839 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 515 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 4 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 5 | 520 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 5 | [Machine learning-based prediction of shear strength of steel reinforced concrete columns subjected to axial compressive load and seismic lateral load](https://doi.org/10.1016/j.istruc.2023.104968) | 2023 | 4 | 41 | Structures | Siyuan Wang, Jinjun Xu, Yanlin Wang, et al. |
| 6 | [Machine learning and SHAP value interpretation for predicting comorbidity of cardiovascular disease and cancer with dietary antioxidants](https://doi.org/10.1016/j.redox.2024.103470) | 2024 | 4 | 174 | Redox Biology | Xiangjun Qi, Shujing Wang, Caishan Fang, et al. |
| 7 | [Applications of XGBoost in water resources engineering: A systematic literature review (Dec 2018–May 2023)](https://doi.org/10.1016/j.envsoft.2024.105971) | 2024 | 4 | 315 | Environmental Modelling & Software | Majid Niazkar, Andrea Menapace, Bruno Brentan, et al. |
| 8 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 4 | 547 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 9 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 4 | 13245 | Dagstuhl Research Online Publication Server | Gauriat, Charles-Maxime, Pencolé, Yannick, Ribot, Pauline, et al. |
| 10 | [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0) | 2023 | 3 | 760 | Nature | Daniil A. Boiko, Robert MacKnight, Ben Kline, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Machine learning-based prediction of shear strength of steel reinforced concrete columns subjected to axial compressive load and seismic lateral load](https://doi.org/10.1016/j.istruc.2023.104968) | 2023 | 4 | 41 | Structures | Siyuan Wang, Jinjun Xu, Yanlin Wang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 3148 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 9 | 5234 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 2988 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 8 | 3260 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://doi.org/10.1093/bioinformatics/btz682) | 2019 | 6 | 6873 | Bioinformatics | Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, et al. |
| 6 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 6 | 10552 |  | Nils Reimers, Iryna Gurevych |
| 7 | [Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2) | 2025 | 5 | 142 | Nature Medicine | Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, et al. |
| 8 | [Large language models in patient education: a scoping review of applications in medicine](https://doi.org/10.3389/fmed.2024.1477898) | 2024 | 5 | 180 | Frontiers in Medicine | Serhat Aydın, Mert Karabacak, Victoria Vlachos, et al. |
| 9 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 5 | 479 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 10 | [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0) | 2023 | 5 | 760 | Nature | Daniil A. Boiko, Robert MacKnight, Ben Kline, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 3148 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 2988 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2) | 2025 | 5 | 142 | Nature Medicine | Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, et al. |
| 4 | [Large language models in patient education: a scoping review of applications in medicine](https://doi.org/10.3389/fmed.2024.1477898) | 2024 | 5 | 180 | Frontiers in Medicine | Serhat Aydın, Mert Karabacak, Victoria Vlachos, et al. |
| 5 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 5 | 479 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 6 | [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0) | 2023 | 5 | 760 | Nature | Daniil A. Boiko, Robert MacKnight, Ben Kline, et al. |
| 7 | [The future landscape of large language models in medicine](https://doi.org/10.1038/s43856-023-00370-1) | 2023 | 5 | 918 | Communications Medicine | Jan Clusmann, Fiona R. Kolbinger, Hannah Sophie Muti, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 3474 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 9 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |
| 10 | [A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation](https://doi.org/10.1038/s41746-025-01670-7) | 2025 | 4 | 178 | npj Digital Medicine | Elham Asgari, Nina Montaña-Brown, Magda Dubois, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |
| 2 | [Cognitive transfer – why AI does not make us stupid](https://doi.org/10.5281/zenodo.18369301) | 2025 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Thomas A. Blüm |
| 3 | [Cognitive State Architecture: A Conceptual Model of Integration and Control in Human and Hybrid Cognition](https://doi.org/10.5281/zenodo.18900605) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Thomas A. Blüm |
| 4 | [High-Integration Boundary States in Human–AI Interaction](https://doi.org/10.5281/zenodo.19240688) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Thomas A. Blüm |
| 5 | [Large language models reflect the ideology of their creators](https://doi.org/10.1038/s44387-025-00048-0) | 2026 | 2 | 3 | npj Artificial Intelligence | Maarten Buyl, Alexander Rogiers, Sander Noels, et al. |
| 6 | [Multi-agent systems for chemical engineering: a review and perspective](https://doi.org/10.1016/j.coche.2025.101209) | 2025 | 2 | 5 | Current Opinion in Chemical Engineering | Sophia Rupprecht, Qinghe Gao, Tanuj Karia, et al. |
| 7 | [The decade-long growth of government-authored news media in China under Xi Jinping](https://doi.org/10.1073/pnas.2408260122) | 2025 | 2 | 9 | Proceedings of the National Academy of Sciences | Hannah Waight, Yin Yuan, Margaret E. Roberts, et al. |
| 8 | [Manufacturing Consensus](https://doi.org/10.12987/yale/9780300251234.001.0001) | 2023 | 2 | 11 | Yale University Press eBooks | Samuel Woolley |
| 9 | [RealVul: Can We Detect Vulnerabilities in Web Applications with LLM?](https://doi.org/10.18653/v1/2024.emnlp-main.472) | 2024 | 2 | 11 |  | Di Cao, Yong Liao, Xiuwei Shang |
| 10 | [The evaluation illusion of large language models in medicine](https://doi.org/10.1038/s41746-025-01963-x) | 2025 | 3 | 18 | npj Digital Medicine | Monica Agrawal, Irene Y. Chen, Freya Gulamali, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [User Acceptance of Information Technology: Toward A Unified View1](https://doi.org/10.2307/30036540) | 2003 | 9 | 41696 | MIS Quarterly | Venkatesh, Michael G. Morris, Gordon B. Davis, et al. |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 9 | 90929 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 9 | 179211 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 4 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 8 | 32609 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 5 | [Scoping studies: towards a methodological framework](https://doi.org/10.1080/1364557032000119616) | 2005 | 8 | 34777 | International Journal of Social Research Methodology | Hilary Arksey, Lisa O’Malley |
| 6 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 8 | 39114 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 7 | [From Landscape to Proof: The Even-Dominance Route to the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 7 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 8 | [FST Spectrum Duality: The Renormalized Free Energy Principle as Physical Instantiation of Functional Stability Theory](https://doi.org/10.5281/zenodo.19036190) | 2026 | 7 | 25 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 9 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 7 | 75158 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 10 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 7 | 123855 | Machine Learning | Leo Breiman |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [From Landscape to Proof: The Even-Dominance Route to the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 7 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 2 | [FST Spectrum Duality: The Renormalized Free Energy Principle as Physical Instantiation of Functional Stability Theory](https://doi.org/10.5281/zenodo.19036190) | 2026 | 7 | 25 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection (DRAFT)](https://doi.org/10.5281/zenodo.20130563) | 2026 | 4 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 6 | [Anomalous Dissipation and the Turbulent Cascade: A Variational Free-Energy Characterisation of Kolmogorov Scaling](https://doi.org/10.5281/zenodo.19056813) | 2026 | 3 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [The K41 Spectrum as the Unique Variational Minimiser of a Scale-Resolved Free Energy](https://doi.org/10.5281/zenodo.20131305) | 2026 | 3 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 8 | [Integration of IoT-Enabled Technologies and Artificial Intelligence (AI) for Smart City Scenario: Recent Advancements and Future Trends](https://doi.org/10.3390/s23115206) | 2023 | 3 | 582 | Sensors | Md Eshrat E. Alahi, Arsanchai Sukkuea, Fahmida Wazed Tina, et al. |
| 9 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 3 | 4727 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 10 | [Grundrisse of Synthetic Coherence: Foundational Notes Toward a Political Economy of the Recursive Era — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18633294) | 2026 | 2 | 2 | Open MIND | Lee Sharks |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Grundrisse of Synthetic Coherence: Foundational Notes Toward a Political Economy of the Recursive Era — Crimson Hexagon Archive](https://doi.org/10.5281/zenodo.18633294) | 2026 | 2 | 2 | Open MIND | Lee Sharks |
| 2 | [Dark Energy as Residual Vacuum Free Energy: A Thermodynamic Bound on the Cosmological Constant](https://doi.org/10.5281/zenodo.19036235) | 2026 | 6 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 3 | [Functional Stability Theory II: Chemical Stability and Autocatalytic Selection (DRAFT)](https://doi.org/10.5281/zenodo.20130563) | 2026 | 4 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 4 | [Functional Stability Theory I: A Game-Theoretic Framework for the Thermodynamic Stability of Fundamental Parameters](https://doi.org/10.5281/zenodo.20130544) | 2026 | 4 | 7 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 5 | [The Para-Semiotic Unconscious of GPT-5.4: A Case Study in Anti-Severance Technology, Architectural Compression, and the Sign the Machine Made Without Knowing](https://doi.org/10.5281/zenodo.19649795) | 2026 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks, Johannes Sigil |
| 6 | [The Curvature Relaxation Model: A Four-Paper Program for Geometric Cosmology Without the Dark Sector](https://doi.org/10.5281/zenodo.18728935) | 2026 | 2 | 5 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 7 | [Canon Formation in the Age of AI: Metadata Packet for Disambiguation, Training-Layer Selection, and Retrocausal Reception (v1.1)](https://doi.org/10.5281/zenodo.20084377) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Lee Sharks |
| 8 | [Anomalous Dissipation and the Turbulent Cascade: A Variational Free-Energy Characterisation of Kolmogorov Scaling](https://doi.org/10.5281/zenodo.19056813) | 2026 | 3 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 9 | [The K41 Spectrum as the Unique Variational Minimiser of a Scale-Resolved Free Energy](https://doi.org/10.5281/zenodo.20131305) | 2026 | 3 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
| 10 | [From Landscape to Proof: The Even-Dominance Route to the Riemann Hypothesis](https://doi.org/10.5281/zenodo.19035640) | 2026 | 7 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Lukas Geiger |
<!-- TRENDING-END -->
