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

Last update: 2026-03-02 06:49 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Why Strong Governance Still Drifts: How Institutions Quietly Lose Alignment](https://doi.org/10.5281/zenodo.18471068) | 2026 | 11 | 27 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 2 | [The Field Protocol: Measuring Translation Coherence in Institutional Systems](https://doi.org/10.5281/zenodo.18657810) | 2026 | 11 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 3 | [The Sovereign Spine: How Institutions Stay True to Their Intent Over Time](https://doi.org/10.5281/zenodo.18646691) | 2026 | 11 | 29 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 4 | [European riverine and coastal wetlands under pressure: biodiversity and climate change](https://doi.org/10.3897/natureconservation.62.163636) | 2026 | 10 | 11 | Nature Conservation | Ute Susanne Kaden, Sophia Schmid, Michael Vieweg, et al. |
| 5 | [Prologue – The Green Dashboard Trap: How Institutions Lose Sight of Their Intent](https://doi.org/10.5281/zenodo.18641907) | 2026 | 10 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 6 | [The Sovereign Spine: A New Theory of Institutional Coherence and Agency](https://doi.org/10.5281/zenodo.18649453) | 2026 | 10 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 7 | [AI-Augmented Impact Frames: A Closed-Loop Architecture for Purpose-Aligned Decisions](https://doi.org/10.5281/zenodo.18668799) | 2026 | 10 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 8 | [How Decision Systems Learn What Matters: Building Purpose-Aligned Governance](https://doi.org/10.5281/zenodo.17964280) | 2026 | 10 | 27 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 9 | [Designing the Meaning Infrastructure: Governing Interpretation in AI-Driven Institutions](https://doi.org/10.5281/zenodo.18494690) | 2026 | 10 | 27 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 10 | [Making Meaning Measurable: How to See Coherence in Decision Systems](https://doi.org/10.5281/zenodo.18486778) | 2026 | 10 | 27 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 99 | 119505 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 62 | 44368 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 28 | 27390 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 21 | 7754 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 18 | 29634 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 18 | 31810 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 7 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 16 | 15478 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 8 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 16 | 50389 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |
| 9 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 15 | 22038 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 10 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 14 | 204092 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 11 | 13070 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 10 | 373 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 10 | 1373 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 4 | [An Introduction to Statistical Learning](https://doi.org/10.1007/978-3-031-38747-0) | 2023 | 5 | 1732 | Springer texts in statistics | Gareth James, Daniela Witten, Trevor Hastie, et al. |
| 5 | [Using machine learning to predict the long-term performance of fibre-reinforced polymer structures: A state-of-the-art review](https://doi.org/10.1016/j.conbuildmat.2023.133692) | 2023 | 4 | 49 | Construction and Building Materials | Chiara Machello, Milad Bazli, Ali Rajabipour, et al. |
| 6 | [Harmonizing physical and deep learning modeling: A computationally efficient and interpretable approach for property prediction](https://doi.org/10.1016/j.scriptamat.2024.116350) | 2024 | 4 | 130 | Scripta Materialia | Da Ren, Chenchong Wang, Xiaolu Wei, et al. |
| 7 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 4 | 2333 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using machine learning to predict the long-term performance of fibre-reinforced polymer structures: A state-of-the-art review](https://doi.org/10.1016/j.conbuildmat.2023.133692) | 2023 | 4 | 49 | Construction and Building Materials | Chiara Machello, Milad Bazli, Ali Rajabipour, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 15 | 2817 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2638 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 2854 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 10 | 9893 |  | Nils Reimers, Iryna Gurevych |
| 5 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3286 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 6 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 9 | 76396 | Biometrics | J. Richard Landis, Gary G. Koch |
| 7 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 8 | 20925 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 8 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 8 | 31276 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 9 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 7 | 1139 |  | Joon Sung Park, Joseph O’Brien, Carrie J. Cai, et al. |
| 10 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 7 | 4158 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2638 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 2854 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3286 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [Generative Agents: Interactive Simulacra of Human Behavior](https://doi.org/10.1145/3586183.3606763) | 2023 | 7 | 1139 |  | Joon Sung Park, Joseph O’Brien, Carrie J. Cai, et al. |
| 5 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 7 | 4158 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 6 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 487 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 7 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 6 | 2035 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 6 | 2106 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0) | 2024 | 5 | 444 | Nature | Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, et al. |
| 10 | [The imperative for regulatory oversight of large language models (or generative AI) in healthcare](https://doi.org/10.1038/s41746-023-00873-0) | 2023 | 5 | 822 | npj Digital Medicine | Bertalan Meskó, Eric J. Topol |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Leveraging Large Language Models to Generate Multiple-Choice Questions for Ophthalmology Education](https://doi.org/10.1001/jamaophthalmol.2025.3622) | 2025 | 3 | 5 | JAMA Ophthalmology | Shahrzad Gholami, Daniel B. Mummert, Beth Wilson, et al. |
| 2 | [Diagnostic performance of ChatGPT-4.0 in histopathological description analysis of oral and maxillofacial lesions: a comparative study with pathologists](https://doi.org/10.1016/j.oooo.2024.11.087) | 2024 | 3 | 13 | Oral Surgery Oral Medicine Oral Pathology and Oral Radiology | Maria Cuevas‐Nunez, Valentina Ignacia Alvarez Silberberg, María Arregui, et al. |
| 3 | [A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://doi.org/10.18653/v1/2025.findings-acl.539) | 2025 | 3 | 16 |  | Wenxuan Wang, Z. Ma, Zheng Wang, et al. |
| 4 | [Efficient fine-tuning of large language models for automated building energy modeling in complex cases](https://doi.org/10.1016/j.autcon.2025.106223) | 2025 | 3 | 17 | Automation in Construction | Gang Jiang, Jianli Chen |
| 5 | [Assessing the use of the novel tool Claude 3 in comparison to ChatGPT 4.0 as an artificial intelligence tool in the diagnosis and therapy of primary head and neck cancer cases](https://doi.org/10.1007/s00405-024-08828-1) | 2024 | 4 | 40 | European Archives of Oto-Rhino-Laryngology | Benedikt Schmidl, Tobias Hütten, Steffi Pigorsch, et al. |
| 6 | [Transforming dental diagnostics with artificial intelligence: advanced integration of ChatGPT and large language models for patient care](https://doi.org/10.3389/fdmed.2024.1456208) | 2025 | 3 | 32 | Frontiers in Dental Medicine | Masoumeh Farhadi Nia, Mohsen Ahmadi, Elyas Irankhah |
| 7 | [Instruction-Following Evaluation for Large Language Models](https://doi.org/10.48550/arxiv.2311.07911) | 2023 | 2 | 26 | arXiv (Cornell University) | Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, et al. |
| 8 | [Large language models for disease diagnosis: a scoping review](https://doi.org/10.1038/s44387-025-00011-z) | 2025 | 3 | 49 | npj Artificial Intelligence | Shuang Zhou, Zidu Xu, Mian Zhang, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Prediction-Regulation Dual-Drive Game Theory (Positive Game) and Reverse Game: Theoretical Proof and Multi-Round Verification of Inevitable Human Victory Within Human-Machine Frameworks](https://doi.org/10.5281/zenodo.18339379) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 2 | [Trait Locking Science_ A New Interdisciplinary Subject for Rigid Control of Core Traits in Dynamic Systems](https://doi.org/10.5281/zenodo.18337462) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 3 | [Game Theory and Robust Predictive Control for Peer-to-Peer Energy Management: A Pathway to a Low-Carbon Economy](https://doi.org/10.3390/su17051780) | 2025 | 2 | 8 | Sustainability | Felix M. Gonzalez, Paúl Arévalo, Luis Ramírez |
| 4 | [Review of Cooperative Game Theory applications in power system expansion planning](https://doi.org/10.1016/j.rser.2021.111056) | 2021 | 2 | 86 | Renewable and Sustainable Energy Reviews | Andrey Churkin, Janusz Białek, David Pozo, et al. |
| 5 | [Effectiveness of digital educational game and game design in STEM learning: a meta-analytic review](https://doi.org/10.1186/s40594-023-00424-9) | 2023 | 2 | 88 | International Journal of STEM Education | Yang Gui, Zhihui Cai, Yajiao Yang, et al. |
| 6 | [Social interactions in the metaverse: Framework, initial evidence, and research roadmap](https://doi.org/10.1007/s11747-022-00908-0) | 2022 | 2 | 363 | Journal of the Academy of Marketing Science | Thorsten Hennig‐Thurau, Dorothea Nilusha Aliman, Alina Marie Herting, et al. |
| 7 | [A note on evolutionarily stable strategies in asymmetric animal conflicts](https://doi.org/10.1016/s0022-5193(80)81038-1) | 1980 | 2 | 549 | Journal of Theoretical Biology | Reinhard Selten |
| 8 | [Meta-analysis of action video game impact on perceptual, attentional, and cognitive skills.](https://doi.org/10.1037/bul0000130) | 2017 | 2 | 751 | Psychological Bulletin | Benoît Bediou, Deanne Adams, Richard E. Mayer, et al. |
| 9 | [Artificial intelligence in the construction industry: A review of present status, opportunities and future challenges](https://doi.org/10.1016/j.jobe.2021.103299) | 2021 | 2 | 829 | Journal of Building Engineering | Sofiat Abioye, Lukumon O. Oyedele, Lukman Akanbi, et al. |
| 10 | [A Systematic Review of Social Presence: Definition, Antecedents, and Implications](https://doi.org/10.3389/frobt.2018.00114) | 2018 | 2 | 891 | Frontiers in Robotics and AI | Catherine S. Oh, Jeremy N. Bailenson, Greg Welch |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Prediction-Regulation Dual-Drive Game Theory (Positive Game) and Reverse Game: Theoretical Proof and Multi-Round Verification of Inevitable Human Victory Within Human-Machine Frameworks](https://doi.org/10.5281/zenodo.18339379) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 2 | [Trait Locking Science_ A New Interdisciplinary Subject for Rigid Control of Core Traits in Dynamic Systems](https://doi.org/10.5281/zenodo.18337462) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 3 | [Game Theory and Robust Predictive Control for Peer-to-Peer Energy Management: A Pathway to a Low-Carbon Economy](https://doi.org/10.3390/su17051780) | 2025 | 2 | 8 | Sustainability | Felix M. Gonzalez, Paúl Arévalo, Luis Ramírez |
| 4 | [Effectiveness of digital educational game and game design in STEM learning: a meta-analytic review](https://doi.org/10.1186/s40594-023-00424-9) | 2023 | 2 | 88 | International Journal of STEM Education | Yang Gui, Zhihui Cai, Yajiao Yang, et al. |
| 5 | [The Impact of Odd-Even Policy on Distance and Time in Private Sector](https://doi.org/10.14513/actatechjaur.00716) | 2024 | 1 | 1 | Acta Technica Jaurinensis | Agung Chandra |
| 6 | [Game Theory-Based Approach for Massive Route Planning in Dynamic Road Networks](https://doi.org/10.1109/tce.2024.3449285) | 2024 | 1 | 1 | IEEE Transactions on Consumer Electronics | Detian Zhang, Yunjun Zhou, Jin Wang |
| 7 | [Medium- and Long-Term Impacts of Transit on Congestion: Jakarta’s Experience](https://doi.org/10.32866/001c.120125) | 2024 | 1 | 2 | Findings | Alyas Widita |
| 8 | [Dynamic Evolutionary Game on Travel Mode Choices Among Buses, Ride-Sharing Vehicles, and Driving Alone in Shared Bus Lane Scenarios](https://doi.org/10.3390/su17052101) | 2025 | 1 | 4 | Sustainability | Yunqiang Xue, Guangqing Bao, Caifeng Tan, et al. |
| 9 | [Building Stock and Emission Models for Jakarta](https://doi.org/10.1016/j.rcns.2024.10.002) | 2024 | 1 | 7 | Resilient Cities and Structures | Hanif Hanif, Ahmed Z. Khan, Muhammad Idrus Alhamid, et al. |
| 10 | [Impact of Traffic Volume on the Pollution Cost, Value of Time, and Travel Time Cost in Jakarta City Centre Area](https://doi.org/10.13189/cea.2023.110830) | 2023 | 1 | 8 | Civil Engineering and Architecture | Asep Yayat Nurhidayat, Hera Widyastuti, Sutikno Sutikno, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Prediction-Regulation Dual-Drive Game Theory (Positive Game) and Reverse Game: Theoretical Proof and Multi-Round Verification of Inevitable Human Victory Within Human-Machine Frameworks](https://doi.org/10.5281/zenodo.18339379) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 2 | [Trait Locking Science_ A New Interdisciplinary Subject for Rigid Control of Core Traits in Dynamic Systems](https://doi.org/10.5281/zenodo.18337462) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Relike Zhou |
| 3 | [The Impact of Odd-Even Policy on Distance and Time in Private Sector](https://doi.org/10.14513/actatechjaur.00716) | 2024 | 1 | 1 | Acta Technica Jaurinensis | Agung Chandra |
| 4 | [Game Theory-Based Approach for Massive Route Planning in Dynamic Road Networks](https://doi.org/10.1109/tce.2024.3449285) | 2024 | 1 | 1 | IEEE Transactions on Consumer Electronics | Detian Zhang, Yunjun Zhou, Jin Wang |
| 5 | [Medium- and Long-Term Impacts of Transit on Congestion: Jakarta’s Experience](https://doi.org/10.32866/001c.120125) | 2024 | 1 | 2 | Findings | Alyas Widita |
| 6 | [Game Theory and Robust Predictive Control for Peer-to-Peer Energy Management: A Pathway to a Low-Carbon Economy](https://doi.org/10.3390/su17051780) | 2025 | 2 | 8 | Sustainability | Felix M. Gonzalez, Paúl Arévalo, Luis Ramírez |
| 7 | [Dynamic Evolutionary Game on Travel Mode Choices Among Buses, Ride-Sharing Vehicles, and Driving Alone in Shared Bus Lane Scenarios](https://doi.org/10.3390/su17052101) | 2025 | 1 | 4 | Sustainability | Yunqiang Xue, Guangqing Bao, Caifeng Tan, et al. |
| 8 | [Building Stock and Emission Models for Jakarta](https://doi.org/10.1016/j.rcns.2024.10.002) | 2024 | 1 | 7 | Resilient Cities and Structures | Hanif Hanif, Ahmed Z. Khan, Muhammad Idrus Alhamid, et al. |
| 9 | [Impact of Traffic Volume on the Pollution Cost, Value of Time, and Travel Time Cost in Jakarta City Centre Area](https://doi.org/10.13189/cea.2023.110830) | 2023 | 1 | 8 | Civil Engineering and Architecture | Asep Yayat Nurhidayat, Hera Widyastuti, Sutikno Sutikno, et al. |
| 10 | [A Study of Taxi Service Mode Choice Based on Evolutionary Game Theory](https://doi.org/10.1155/2019/8607942) | 2019 | 1 | 14 | Journal of Advanced Transportation | Zhu Bai, Mingxia Huang, Shuai Bian, et al. |
<!-- TRENDING-END -->
