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

Last update: 2026-02-09 06:57 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Pharmacokinetic and Pharmacodynamic Properties of a Novel Inhaled Insulin](https://doi.org/10.1177/1932296816658055) | 2016 | 10 | 78 | Journal of Diabetes Science and Technology | Lutz Heinemann, R Baughman, Anders Boss, et al. |
| 2 | [Where language meets attention: How contingent interactions promote learning](https://doi.org/10.1016/j.dr.2021.100961) | 2021 | 8 | 131 | Developmental Review | Lillian R. Masek, Brianna T. M. McMillan, Sarah Paterson, et al. |
| 3 | [Improved Postprandial Glucose with Inhaled Technosphere Insulin Compared with Insulin Aspart in Patients with Type 1 Diabetes on Multiple Daily Injections: The STAT Study](https://doi.org/10.1089/dia.2018.0200) | 2018 | 7 | 65 | Diabetes Technology & Therapeutics | Halis Kaan Aktürk, Janet K. Snell‐Bergeon, Amanda Rewers, et al. |
| 4 | [Inhaled Technosphere Insulin Compared With Injected Prandial Insulin in Type 1 Diabetes: A Randomized 24-Week Trial](https://doi.org/10.2337/dc15-0075) | 2015 | 6 | 104 | Diabetes Care | Bruce W. Bode, Janet B. McGill, Daniel L. Lorber, et al. |
| 5 | [Two‐Month‐Old Infants' Sensitivity to Social Contingency in Mother–Infant and Stranger–Infant Interaction](https://doi.org/10.1207/s15327078in0903_3) | 2006 | 6 | 168 | Infancy | Ann E. Bigelow, Philippe Rochat |
| 6 | [A Social Feedback Loop for Speech Development and Its Reduction in Autism](https://doi.org/10.1177/0956797614531023) | 2014 | 6 | 387 | Psychological Science | Anne S. Warlaumont, Jeffrey A. Richards, Jill Gilkerson, et al. |
| 7 | [A 13-Week Single-Arm Evaluation of Inhaled Technosphere Insulin Plus Insulin Degludec for Adults with Type 1 Diabetes](https://doi.org/10.1089/dia.2024.0581) | 2025 | 5 | 7 | Diabetes Technology & Therapeutics | Roy W. Beck, Halis Kaan Aktürk, Halis Kaan Aktürk, et al. |
| 8 | [Time–Action Profile of Technosphere Insulin in Children with Type 1 Diabetes](https://doi.org/10.1007/s13300-023-01368-7) | 2023 | 5 | 13 | Diabetes Therapy | Michael J. Haller, Marisa Jones, Sunil Bhavsar, et al. |
| 9 | [A Randomized Trial Comparing Inhaled Insulin Plus Basal Insulin Versus Usual Care in Adults With Type 1 Diabetes](https://doi.org/10.2337/dc24-1832) | 2024 | 5 | 18 | Diabetes Care | Irl B. Hirsch, Roy W. Beck, Martin Chase Marak, et al. |
| 10 | [Galactia longifolia (Jacq.) Benth. In: Marchesi E., Mailhos A. & Bonifacino J.M. (Eds.). Flora Uruguaya: Flora Vascular del Uruguay. ISSN 3121-2050, V. 1.0.](https://doi.org/10.5281/zenodo.18277659) | 2026 | 5 | 20 | Zenodo (CERN European Organization for Nuclear Research) | Flora Uruguaya |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 125 | 118376 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 65 | 43532 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 29 | 27137 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 25 | 21811 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 21 | 77568 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 19 | 93006 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 7 | [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | 1986 | 18 | 29543 | Nature | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |
| 8 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 18 | 31603 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 9 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 16 | 7573 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 10 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 14 | 29290 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 11 | 1253 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 7 | 2246 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 3 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 13020 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 4 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 19252 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 5 | [Association between the stress hyperglycemia ratio and 28-day all-cause mortality in critically ill patients with sepsis: a retrospective cohort study and predictive model establishment based on machine learning](https://doi.org/10.1186/s12933-024-02265-4) | 2024 | 5 | 152 | Cardiovascular Diabetology | Fengjuan Yan, Xiehui Chen, Xiao‐Qing Quan, et al. |
| 6 | [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336) | 2023 | 5 | 905 | Science | Rémi Lam, Álvaro Sánchez‐González, Matthew Willson, et al. |
| 7 | [A comprehensive review on ensemble deep learning: Opportunities and challenges](https://doi.org/10.1016/j.jksuci.2023.01.014) | 2023 | 5 | 916 | Journal of King Saud University - Computer and Information Sciences | Ammar Mohammed, Rania Kora |
| 8 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 4 | 570 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 2529 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2741 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1994 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 6 | 3235 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 6 | 31052 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 5 | 378 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 7 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 5 | 522 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 8 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 5 | 2696 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 9 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 5 | 4566 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 10 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 5 | 20765 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 2529 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2741 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1994 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 6 | 3235 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 5 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 5 | 378 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 6 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 5 | 522 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 7 | [GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](https://doi.org/10.1038/s41591-024-03456-y) | 2025 | 4 | 87 | Nature Medicine | Ethan Goh, Robert J. Gallo, Eric Strong, et al. |
| 8 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 4 | 187 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 9 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 4 | 441 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 10 | [The future landscape of large language models in medicine](https://doi.org/10.1038/s43856-023-00370-1) | 2023 | 4 | 808 | Communications Medicine | Jan Clusmann, Fiona R. Kolbinger, Hannah Sophie Muti, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Hykon v4.1 — A Conversational Governance Overlay for Large Language Models](https://doi.org/10.5281/zenodo.18358206) | 2026 | 3 | 3 | Zenodo (CERN European Organization for Nuclear Research) | Kon Lionis |
| 2 | [Stigmatizing Language in Large Language Models for Alcohol and Substance Use Disorders: A Multimodel Evaluation and Prompt Engineering Approach](https://doi.org/10.1097/adm.0000000000001536) | 2025 | 2 | 2 | Journal of Addiction Medicine | Yichen Wang, Kelly Hsu, Christopher Brokus, et al. |
| 3 | [Accuracy of latest large language models in answering multiple choice questions in dentistry: A comparative study](https://doi.org/10.1371/journal.pone.0317423) | 2025 | 3 | 16 | PLoS ONE | Huy Cong Nguyen, Đang Hai, Thuy Linh Nguyen, et al. |
| 4 | [Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models](https://doi.org/10.1145/3689776) | 2024 | 2 | 11 | Proceedings of the ACM on Programming Languages | Ningke Li, Yuekang Li, Yi Liu, et al. |
| 5 | [Large Language Models in radiology: A technical and clinical perspective](https://doi.org/10.1016/j.ejrai.2025.100021) | 2025 | 2 | 13 | European Journal of Radiology Artificial Intelligence | Jean Kao, Hung‐Wen Kao |
| 6 | [A cross-sectional comparative study: ChatGPT 3.5 versus diverse levels of medical experts in the diagnosis of ENT diseases](https://doi.org/10.1007/s00405-024-08509-z) | 2024 | 2 | 14 | European Archives of Oto-Rhino-Laryngology | Mikhael Makhoul, Antoine E. Melkane, Patrick El Khoury, et al. |
| 7 | [How well do large language model-based chatbots perform in oral and maxillofacial radiology?](https://doi.org/10.1093/dmfr/twae021) | 2024 | 3 | 28 | Dentomaxillofacial Radiology | Hui Jeong, Sang‐Sun Han, Youngjae Yu, et al. |
| 8 | [ChatGPT-4 Omni’s superiority in answering multiple-choice oral radiology questions](https://doi.org/10.1186/s12903-025-05554-w) | 2025 | 3 | 28 | BMC Oral Health | Melek Taşsöker |
| 9 | [A comparison of human, GPT-3.5, and GPT-4 performance in a university-level coding course](https://doi.org/10.1038/s41598-024-73634-y) | 2024 | 2 | 28 | Scientific Reports | Will Yeadon, Alex Peach, Craig P. Testrow |
| 10 | [Do LLMs Exhibit Human-like Response Biases? A Case Study in Survey Design](https://doi.org/10.1162/tacl_a_00685) | 2024 | 3 | 46 | Transactions of the Association for Computational Linguistics | Lindia Tjuatja, Valerie Chen, Tongshuang Wu, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Adversarial Participation Without a Judge: Fail-Closed Containment for No-Meta, Observable-Only Agents](https://doi.org/10.5281/zenodo.18382670) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 2 | [The Fine-Structure Constant: A Geometric Derivation from Simplicial Spacetime (Universe Engine v13.3.1)](https://doi.org/10.5281/zenodo.18407713) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 3 | [Electromagnetic Induction and the Nature of Motion in Simplicial Spacetime (Universe Engine v13.3.3)](https://doi.org/10.5281/zenodo.18407892) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 4 | [Derivation of Lorentz Invariance from Euclidean Simplicial Geometry (Universe Engine v13.3.4)](https://doi.org/10.5281/zenodo.18408280) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 5 | [Cosmological Phenomena and the Unification of Forces in the Simplicial Universe Engine v13.3.6](https://doi.org/10.5281/zenodo.18408426) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 6 | [Gravity as Lattice Elasticity: A Geometric Derivation from the Universe Engine v13.3.5](https://doi.org/10.5281/zenodo.18408375) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 7 | [Friction-Minimal Intersubjective Contracts for No-Meta Autonomous Agents](https://doi.org/10.5281/zenodo.18308030) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 8 | [Observable-Only No-Meta Causal Autonomy Protocol (ONCAP)](https://doi.org/10.5281/zenodo.18371930) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 9 | [Floor-Specified No-Meta Autonomy](https://doi.org/10.5281/zenodo.18258262) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 10 | [The Video Game Experience as “True” Identification: A Theory of Enjoyable Alterations of Players' Self-Perception](https://doi.org/10.1111/j.1468-2885.2009.01347.x) | 2009 | 2 | 423 | Communication Theory | Klimmt Christoph, Hefner Dorothée, Vorderer Peter |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Adversarial Participation Without a Judge: Fail-Closed Containment for No-Meta, Observable-Only Agents](https://doi.org/10.5281/zenodo.18382670) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 2 | [The Fine-Structure Constant: A Geometric Derivation from Simplicial Spacetime (Universe Engine v13.3.1)](https://doi.org/10.5281/zenodo.18407713) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 3 | [Electromagnetic Induction and the Nature of Motion in Simplicial Spacetime (Universe Engine v13.3.3)](https://doi.org/10.5281/zenodo.18407892) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 4 | [Derivation of Lorentz Invariance from Euclidean Simplicial Geometry (Universe Engine v13.3.4)](https://doi.org/10.5281/zenodo.18408280) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 5 | [Cosmological Phenomena and the Unification of Forces in the Simplicial Universe Engine v13.3.6](https://doi.org/10.5281/zenodo.18408426) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 6 | [Gravity as Lattice Elasticity: A Geometric Derivation from the Universe Engine v13.3.5](https://doi.org/10.5281/zenodo.18408375) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 7 | [Friction-Minimal Intersubjective Contracts for No-Meta Autonomous Agents](https://doi.org/10.5281/zenodo.18308030) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 8 | [Observable-Only No-Meta Causal Autonomy Protocol (ONCAP)](https://doi.org/10.5281/zenodo.18371930) | 2026 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 9 | [Floor-Specified No-Meta Autonomy](https://doi.org/10.5281/zenodo.18258262) | 2026 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 10 | [Current Practices in the Development of Guaranteed Maximum Price (GMP) Contracts](https://doi.org/10.1061/9780784485286.015) | 2024 | 1 | 1 |  | Tolulope I. Ogundare, Rebecca Kassa, Omar Maali, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Adversarial Participation Without a Judge: Fail-Closed Containment for No-Meta, Observable-Only Agents](https://doi.org/10.5281/zenodo.18382670) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | K Takahashi |
| 2 | [The Fine-Structure Constant: A Geometric Derivation from Simplicial Spacetime (Universe Engine v13.3.1)](https://doi.org/10.5281/zenodo.18407713) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 3 | [Electromagnetic Induction and the Nature of Motion in Simplicial Spacetime (Universe Engine v13.3.3)](https://doi.org/10.5281/zenodo.18407892) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 4 | [Derivation of Lorentz Invariance from Euclidean Simplicial Geometry (Universe Engine v13.3.4)](https://doi.org/10.5281/zenodo.18408280) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 5 | [Cosmological Phenomena and the Unification of Forces in the Simplicial Universe Engine v13.3.6](https://doi.org/10.5281/zenodo.18408426) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 6 | [Gravity as Lattice Elasticity: A Geometric Derivation from the Universe Engine v13.3.5](https://doi.org/10.5281/zenodo.18408375) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Julian Zoria |
| 7 | [Current Practices in the Development of Guaranteed Maximum Price (GMP) Contracts](https://doi.org/10.1061/9780784485286.015) | 2024 | 1 | 1 |  | Tolulope I. Ogundare, Rebecca Kassa, Omar Maali, et al. |
| 8 | [Qualifications-Driven Procurement Selection Criteria for Design–Build and Construction Manager at Risk Firms](https://doi.org/10.1061/jsdccc.sceng-1495) | 2025 | 1 | 1 | Journal of structural design and construction practice. | Hala Sanboskani, Mounir El Asmar |
| 9 | [Risk management in guaranteed maximum price (GMP) contracts](https://doi.org/10.1108/sasbe-09-2021-0176) | 2022 | 1 | 2 | Smart and Sustainable Built Environment | Asha Dulanjalie Palihakkara, B.A.K.S. Perera |
| 10 | [Stochastic optimal pricing for retail electricity considering demand response, renewable energy sources and environmental effects](https://doi.org/10.1057/s41272-024-00492-8) | 2024 | 1 | 2 | Journal of Revenue and Pricing Management | Morteza Neishaboori, Alireza Arshadi Khamseh, Abolfazl Mirzazadeh, et al. |
<!-- TRENDING-END -->
