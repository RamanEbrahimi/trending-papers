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

Last update: 2025-10-20 06:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Ethnic Groups and Boundaries: The Social Organization of Culture Difference](https://doi.org/10.2307/588416) | 1970 | 19 | 3868 | British Journal of Sociology | Maurice Freedman, Fredrik Barth |
| 2 | [What Shall We Do With the Drunken Sailor? a Critical Re-Examination of Genesis 9.20-27](https://doi.org/10.1177/030908929502006803) | 1995 | 18 | 1 | Journal for the Study of the Old Testament | Marc Vervenne |
| 3 | [A Critical and Exegetical Commentary on the Book of Genesis: With a New Translation](https://openalex.org/W1972325180) | 2001 | 18 | 3 |  | James Murphy, Jeffrey Thompson |
| 4 | [Paradise Lost Again: Violence and Obedience in the Flood Narrative](https://doi.org/10.1177/030908929401906201) | 1994 | 18 | 3 | Journal for the Study of the Old Testament | Robert W. E. Forrest |
| 5 | [PARONOMASIA IN THE OLD TESTAMENT](https://doi.org/10.1093/jss/9.2.282) | 1964 | 18 | 6 | Journal of Semitic Studies | A. Guillaume |
| 6 | [The Savage Text](https://doi.org/10.1002/9781444302691) | 2008 | 18 | 9 |  | Adrian Thatcher |
| 7 | [Response: The Curse of Ham and David H. Aaron](https://doi.org/10.1093/jaarel/lxv.1.183) | 1997 | 18 | 17 | Journal of the American Academy of Religion | S. L. McKenzie |
| 8 | [A Process Theological Interpretation of the Primeval History in Genesis 2–11](https://doi.org/10.1017/s0360966900009701) | 2002 | 18 | 0 | Horizons | Robert Gnuse |
| 9 | [Biblical Curses and the Displacement of Tradition](https://openalex.org/W2279098326) | 2011 | 18 | 0 |  | Brian Britt |
| 10 | [Notes, Critical and Practical on the Book of Genesis: Designed as a General Help to Biblical Reading and Instruction](https://openalex.org/W1545017549) | 2005 | 18 | 19 |  | George Bush |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 123 | 110356 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 33 | 25185 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 24 | 6847 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 23 | 6181 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 23 | 71737 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 22 | 26523 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 22 | 30572 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 22 | 86461 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 21 | 12523 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 10 | [Machine Learning: Algorithms, Real-World Applications and Research Directions](https://doi.org/10.1007/s42979-021-00592-x) | 2021 | 18 | 3718 | SN Computer Science | Iqbal H. Sarker |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 13 | 631 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Artificial Intelligence and Machine Learning in Clinical Medicine, 2023](https://doi.org/10.1056/nejmra2302038) | 2023 | 7 | 813 | New England Journal of Medicine | Charlotte Haug, Jeffrey M. Drazen |
| 3 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 7 | 14710 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 4 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 6 | 1141 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 5 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 132 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 6 | [A Review of Feature Selection Methods for Machine Learning-Based Disease Risk Prediction](https://doi.org/10.3389/fbinf.2022.927312) | 2022 | 5 | 522 | Frontiers in Bioinformatics | Nicholas Pudjihartono, Tayaza Fadason, Andreas W. Kempa-Liehr, et al. |
| 7 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 5 | 1474 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 16 | 13893 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Proceedings of the ACM on Human-Computer Interaction](https://openalex.org/W3040472729) | 2018 | 15 | 902 |  | Karrie Karahalios, Andrés Monroy‐Hernández, Airi Lampinen, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 15 | 1825 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1150 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 5 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 12 | 2742 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 6 | [Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems](https://doi.org/10.1145/3706598) | 2025 | 10 | 419 |  | Unknown |
| 7 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 9 | 2454 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 8 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 9 | 3645 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 9 | [Proceedings of the 13th International Conference on Neural Information Processing Systems](https://openalex.org/W2914304175) | 2000 | 8 | 2119 |  | Todd K. Leen, Thomas G. Dietterich, Volker Tresp |
| 10 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 8 | 2810 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 15 | 1825 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1150 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 3 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 12 | 2742 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 4 | [Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems](https://doi.org/10.1145/3706598) | 2025 | 10 | 419 |  | Unknown |
| 5 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 9 | 2454 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 6 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 8 | 2810 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 7 | [Training language models to follow instructions with human feedback](https://doi.org/10.48550/arxiv.2203.02155) | 2022 | 8 | 3107 | arXiv (Cornell University) | Long Ouyang, Jeff Wu, Xu Jiang, et al. |
| 8 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 1911 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 433 | ACM transactions on office information systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [The future landscape of large language models in medicine](https://doi.org/10.1038/s43856-023-00370-1) | 2023 | 5 | 586 | Communications Medicine | Jan Clusmann, Fiona R. Kolbinger, Hannah Sophie Muti, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Jailbreaking Black Box Large Language Models in Twenty Queries](https://doi.org/10.1109/satml64287.2025.00010) | 2025 | 3 | 5 |  | Patrick Chao, Alexander Robey, Edgar Dobriban, et al. |
| 2 | [Tender: Accelerating Large Language Models via Tensor Decomposition and Runtime Requantization](https://doi.org/10.1109/isca59077.2024.00080) | 2024 | 3 | 6 |  | Jungi Lee, Wonbeom Lee, Jaewoong Sim |
| 3 | [ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs](https://doi.org/10.18653/v1/2024.acl-long.809) | 2024 | 3 | 12 |  | Fengqing Jiang, Zhangchen Xu, Luyao Niu, et al. |
| 4 | [A Systematic Review of Testing and Evaluation of Healthcare Applications of Large Language Models (LLMs)](https://doi.org/10.1101/2024.04.15.24305869) | 2024 | 3 | 19 | medRxiv (Cold Spring Harbor Laboratory) | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 5 | [A Comparative Study of Responses to Retina Questions from Either Experts, Expert-Edited Large Language Models, or Expert-Edited Large Language Models Alone](https://doi.org/10.1016/j.xops.2024.100485) | 2024 | 3 | 26 | Ophthalmology Science | Prashant D. Tailor, Lauren A. Dalvin, John J. Chen, et al. |
| 6 | [Rehearsal: Simulating Conflict to Teach Conflict Resolution](https://doi.org/10.1145/3613904.3642159) | 2024 | 3 | 29 |  | Omar Shaikh, Valentino Chai, Michele J. Gelfand, et al. |
| 7 | [Healthcare AI Treatment Decision Support: Design Principles to Enhance Clinician Adoption and Trust](https://doi.org/10.1145/3544548.3581251) | 2023 | 3 | 36 |  | Eleanor R. Burgess, Ivana Jankovic, Melissa Austin, et al. |
| 8 | [Large language models in medical and healthcare fields: applications, advances, and challenges](https://doi.org/10.1007/s10462-024-10921-0) | 2024 | 4 | 58 | Artificial Intelligence Review | Dandan Wang, Shiqing Zhang |
| 9 | [OliVe: Accelerating Large Language Models via Hardware-friendly Outlier-Victim Pair Quantization](https://doi.org/10.1145/3579371.3589038) | 2023 | 3 | 45 |  | Cong Guo, Jiaming Tang, Weiming Hu, et al. |
| 10 | [The application of ChatGPT in healthcare progress notes: A commentary from a clinical and research perspective](https://doi.org/10.1002/ctm2.1324) | 2023 | 3 | 47 | Clinical and Translational Medicine | Josh Nguyen, Christopher A. Pepping |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Integrating Game Theory and AI in Management Training: A Revolutionary Approach to Enhancing Leadership and Managerial Decision-Making Skills](https://doi.org/10.4236/tel.2024.143047) | 2024 | 2 | 1 | Theoretical Economics Letters | Marko Kesti |
| 2 | [The impact of government subsidy on photovoltaic enterprises independent innovation based on the evolutionary game theory](https://doi.org/10.1016/j.energy.2023.129385) | 2023 | 2 | 32 | Energy | Xi Zhang, Qingyuan Zhu, Xingchen Li, et al. |
| 3 | [A definition for gamification: anchoring gamification in the service marketing literature](https://doi.org/10.1007/s12525-015-0212-z) | 2016 | 2 | 928 | Electronic Markets | Kai Huotari, Juho Hamari |
| 4 | [Prospect Theory: An Analysis of Decision Under Risk](https://doi.org/10.1142/9789814417358_0006) | 2013 | 2 | 1645 | World Scientific handbook in financial economic series | Daniel Kahneman, Amos Tversky |
| 5 | [The Bargaining Problem](https://doi.org/10.2307/1907266) | 1950 | 2 | 7839 | Econometrica | John F. Nash |
| 6 | [Statistical power analyses using G*Power 3.1: Tests for correlation and regression analyses](https://doi.org/10.3758/brm.41.4.1149) | 2009 | 2 | 30904 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Axel Buchner, et al. |
| 7 | [Prospect Theory: An Analysis of Decision under Risk](https://doi.org/10.2307/1914185) | 1979 | 2 | 43953 | Econometrica | Daniel Kahneman, Amos Tversky |
| 8 | [Vekâlet Teorisinde Fırsatçılık Kavramı ve Oyun Teorisi Arasındaki İlişki](https://doi.org/10.33712/mana.962926) | 2021 | 1 | 1 | Uluslararası Yönetim Akademisi Dergisi | Buket ARSLAN, Elif ÇETİN |
| 9 | [Oyun Teorisi Perspektifinden Çatışma Yönetim Stratejilerinin Karşılıklı Etkileşimi ve Denetçilere Yönelik Bir Uygulama](https://doi.org/10.21076/vizyoner.1071129) | 2023 | 1 | 1 | Süleyman Demirel Üniversitesi Vizyoner Dergisi | Gürbüz AYDIN, Hakan Karabacak |
| 10 | [Improved Backward Scenario Reduction Method for Generation Planning Considering Extreme Scenarios](https://doi.org/10.1109/ei259745.2023.10512627) | 2023 | 1 | 1 | 2021 IEEE 5th Conference on Energy Internet and Energy System Integration (EI2) | Yigong Xie, Ziyu Huo, Chen Wu, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Integrating Game Theory and AI in Management Training: A Revolutionary Approach to Enhancing Leadership and Managerial Decision-Making Skills](https://doi.org/10.4236/tel.2024.143047) | 2024 | 2 | 1 | Theoretical Economics Letters | Marko Kesti |
| 2 | [The impact of government subsidy on photovoltaic enterprises independent innovation based on the evolutionary game theory](https://doi.org/10.1016/j.energy.2023.129385) | 2023 | 2 | 32 | Energy | Xi Zhang, Qingyuan Zhu, Xingchen Li, et al. |
| 3 | [Oyun Teorisi Perspektifinden Çatışma Yönetim Stratejilerinin Karşılıklı Etkileşimi ve Denetçilere Yönelik Bir Uygulama](https://doi.org/10.21076/vizyoner.1071129) | 2023 | 1 | 1 | Süleyman Demirel Üniversitesi Vizyoner Dergisi | Gürbüz AYDIN, Hakan Karabacak |
| 4 | [Improved Backward Scenario Reduction Method for Generation Planning Considering Extreme Scenarios](https://doi.org/10.1109/ei259745.2023.10512627) | 2023 | 1 | 1 | 2021 IEEE 5th Conference on Energy Internet and Energy System Integration (EI2) | Yigong Xie, Ziyu Huo, Chen Wu, et al. |
| 5 | [Recent advances in the extraction of critical metals from spent lithium-ion batteries: Challenges and solutions- a review](https://doi.org/10.1016/j.seppur.2025.134070) | 2025 | 1 | 1 | Separation and Purification Technology | Xinlong Li, Xiangnan Zhu, Xi-guang Li, et al. |
| 6 | [Stochastic optimization of thermal energy storage for multi-energy systems with hydrogen and renewable integration](https://doi.org/10.1016/j.est.2025.117830) | 2025 | 1 | 1 | Journal of Energy Storage | Lalji Kumar, Uttam Kumar Khedlekar |
| 7 | [The Study of Long-Term Trading Revenue Distribution Models in Wind-Photovoltaic-Thermal Complementary Systems Based on the Improved Shapley Value Method](https://doi.org/10.32604/ee.2025.062154) | 2025 | 1 | 0 | Energy Engineering | Dongfeng Yang, Ruirui Zhang, Chuang Liu, et al. |
| 8 | [Interpretable prediction of coagulant dosage in drinking water treatment plant based on automated machine learning and SHAP method](https://doi.org/10.1016/j.jwpe.2025.107925) | 2025 | 1 | 0 | Journal of Water Process Engineering | Liyan Feng, Ying Zhang, Xiaoting Wei, et al. |
| 9 | [Sensitivity analysis of renewable energy coupled hydrogen system to government reward and punishment policies based on multi-agent Nash equilibrium](https://doi.org/10.1016/j.ijhydene.2025.06.152) | 2025 | 1 | 0 | International Journal of Hydrogen Energy | Kai Kang, Yunlong Zhang, Shuai Cheng, et al. |
| 10 | [Capacity optimization strategy for energy storage system to ensure power supply](https://doi.org/10.1093/ijlct/ctad039) | 2023 | 1 | 2 | International Journal of Low-Carbon Technologies | Huimin Fu, Ming Shi, Miaomiao Feng |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Integrating Game Theory and AI in Management Training: A Revolutionary Approach to Enhancing Leadership and Managerial Decision-Making Skills](https://doi.org/10.4236/tel.2024.143047) | 2024 | 2 | 1 | Theoretical Economics Letters | Marko Kesti |
| 2 | [Vekâlet Teorisinde Fırsatçılık Kavramı ve Oyun Teorisi Arasındaki İlişki](https://doi.org/10.33712/mana.962926) | 2021 | 1 | 1 | Uluslararası Yönetim Akademisi Dergisi | Buket ARSLAN, Elif ÇETİN |
| 3 | [Oyun Teorisi Perspektifinden Çatışma Yönetim Stratejilerinin Karşılıklı Etkileşimi ve Denetçilere Yönelik Bir Uygulama](https://doi.org/10.21076/vizyoner.1071129) | 2023 | 1 | 1 | Süleyman Demirel Üniversitesi Vizyoner Dergisi | Gürbüz AYDIN, Hakan Karabacak |
| 4 | [Improved Backward Scenario Reduction Method for Generation Planning Considering Extreme Scenarios](https://doi.org/10.1109/ei259745.2023.10512627) | 2023 | 1 | 1 | 2021 IEEE 5th Conference on Energy Internet and Energy System Integration (EI2) | Yigong Xie, Ziyu Huo, Chen Wu, et al. |
| 5 | [Recent advances in the extraction of critical metals from spent lithium-ion batteries: Challenges and solutions- a review](https://doi.org/10.1016/j.seppur.2025.134070) | 2025 | 1 | 1 | Separation and Purification Technology | Xinlong Li, Xiangnan Zhu, Xi-guang Li, et al. |
| 6 | [Stochastic optimization of thermal energy storage for multi-energy systems with hydrogen and renewable integration](https://doi.org/10.1016/j.est.2025.117830) | 2025 | 1 | 1 | Journal of Energy Storage | Lalji Kumar, Uttam Kumar Khedlekar |
| 7 | [Game Theory in Management](https://doi.org/10.4324/9781315583778) | 2016 | 1 | 0 | Routledge eBooks | Michael Hatfield |
| 8 | [The Study of Long-Term Trading Revenue Distribution Models in Wind-Photovoltaic-Thermal Complementary Systems Based on the Improved Shapley Value Method](https://doi.org/10.32604/ee.2025.062154) | 2025 | 1 | 0 | Energy Engineering | Dongfeng Yang, Ruirui Zhang, Chuang Liu, et al. |
| 9 | [Interpretable prediction of coagulant dosage in drinking water treatment plant based on automated machine learning and SHAP method](https://doi.org/10.1016/j.jwpe.2025.107925) | 2025 | 1 | 0 | Journal of Water Process Engineering | Liyan Feng, Ying Zhang, Xiaoting Wei, et al. |
| 10 | [Sensitivity analysis of renewable energy coupled hydrogen system to government reward and punishment policies based on multi-agent Nash equilibrium](https://doi.org/10.1016/j.ijhydene.2025.06.152) | 2025 | 1 | 0 | International Journal of Hydrogen Energy | Kai Kang, Yunlong Zhang, Shuai Cheng, et al. |
<!-- TRENDING-END -->
