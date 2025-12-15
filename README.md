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

Last update: 2025-12-15 06:26 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Diversity and Ecosystem Services of Trichoptera](https://doi.org/10.3390/insects10050125) | 2019 | 6 | 176 | Insects | John C. Morse, Paul B. Frandsen, Wolfram Graf, et al. |
| 2 | [The Conscious Field Energy Plus (CFE⁺) Framework v2.0 — Unified Metrics of Consciousness and the Civilization–Kardashev Scale](https://doi.org/10.5281/zenodo.17668588) | 2025 | 5 | 28 | Zenodo (CERN European Organization for Nuclear Research) | Lee, Jinho |
| 3 | [Catalog of the Neotropical Trichoptera (Caddisflies)](https://doi.org/10.3897/zookeys.654.9516) | 2017 | 5 | 157 | ZooKeys | Ralph W. Holzenthal, Adolfo R. Calor |
| 4 | [Racialization and belonging in higher education: Counternarratives of Turkish Belgian students from a community cultural wealth perspective.](https://doi.org/10.1037/dhe0000563) | 2024 | 4 | 2 | Journal of Diversity in Higher Education | F. Zehra Çolak |
| 5 | [Plastens skjulte kjemikalier: hvordan plastforurensning truer hormonsystemet til dyr og mennesker](https://doi.org/10.18261/naturen.149.5.9) | 2025 | 4 | 4 | Naturen | Odd André Karlsen, Anders Goksøyr |
| 6 | [Healthcare providers' perceived learning needs and barriers to providing care for chronic multisymptom illness and environmental exposure concerns](https://doi.org/10.1016/j.lfs.2021.119757) | 2021 | 4 | 4 | Life Sciences | Lisa M. McAndrew, Linda A. Khatib, Nicole Sullivan, et al. |
| 7 | [Consciousness Civilization Framework (CCF) v1.0](https://doi.org/10.5281/zenodo.17720525) | 2025 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Lee Jin-Ho |
| 8 | [“Because the country, it seems though, has turned their back on me”: Experiences of institutional betrayal among veterans living with Gulf War Illness](https://doi.org/10.1016/j.socscimed.2021.114211) | 2021 | 4 | 27 | Social Science & Medicine | Katharine Bloeser, Kelly K. McCarron, Vanessa L. Merker, et al. |
| 9 | [‘Same old story, just a different policy’: race and policy making in higher education in the UK](https://doi.org/10.1080/13613324.2020.1718082) | 2020 | 4 | 146 | Race Ethnicity and Education | Kalwant Bhopal, Clare Pitkin |
| 10 | [Larvae of the North American Caddisfly Genera (Trichoptera)](https://doi.org/10.3138/9781442623606) | 1996 | 4 | 622 | University of Toronto Press eBooks | Glenn B. Wiggins |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 120 | 115020 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 70 | 41264 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 27 | 26394 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 22 | 30942 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 5 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 22 | 90535 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 18 | 75636 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 17 | 198843 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 8 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 16 | 28400 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 9 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 15 | 21175 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 10 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 14 | 7090 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 8 | 1318 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 2 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 8 | 8728 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 3 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 218 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 4 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 7 | 982 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 5 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 6 | 510 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 6 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 6 | 2040 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 7 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 12892 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 8 | [A comprehensive review on ensemble deep learning: Opportunities and challenges](https://doi.org/10.1016/j.jksuci.2023.01.014) | 2023 | 5 | 820 | Journal of King Saud University - Computer and Information Sciences | Ammar Mohammed, Rania Kora |
| 9 | [Scaling deep learning for materials discovery](https://doi.org/10.1038/s41586-023-06735-9) | 2023 | 5 | 846 | Nature | Amil Merchant, Simon Batzner, Samuel S. Schoenholz, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Semantic segmentation of high-resolution satellite images using deep learning](https://doi.org/10.1007/s12145-021-00674-7) | 2021 | 7 | 19 | Earth Science Informatics | Kuldeep Chaurasia, Ritesh Nandy, Omkar Pawar, et al. |
| 2 | [Dilated-ResUnet: A novel deep learning architecture for building extraction from medium resolution multi-spectral satellite imagery](https://doi.org/10.1016/j.eswa.2021.115530) | 2021 | 6 | 57 | Expert Systems with Applications | Mayank Dixit, Kuldeep Chaurasia, Vipul Kumar Mishra |
| 3 | [Quantification of carbon sequestration by urban forest using Landsat 8 OLI and machine learning algorithms in Jodhpur, India](https://doi.org/10.1016/j.ufug.2021.127445) | 2021 | 5 | 49 | Urban forestry & urban greening | Swati Uniyal, Saurabh Purohit, Kuldeep Chaurasia, et al. |
| 4 | [Two Dimensions of Opacity and the Deep Learning Predicament](https://doi.org/10.1007/s11023-021-09569-4) | 2021 | 5 | 86 | Minds and Machines | Florian J. Boge |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 15 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 2248 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4223 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 10 | 30394 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 8 | 365 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 7 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1741 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 8 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 8 | 3108 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 9 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 8 | 20359 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 10 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 8 | 74977 | Biometrics | J. Richard Landis, Gary G. Koch |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 15 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 11 | 2248 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 8 | 365 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 5 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1741 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 6 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 8 | 3108 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 7 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 7 | 221 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 8 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 6 | 137 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 9 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 6 | 305 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 10 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 319 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Leveraging Large Language Models for Improved Patient Access and Self-Management: Assessor-Blinded Comparison Between Expert- and AI-Generated Content](https://doi.org/10.2196/55847) | 2024 | 3 | 17 | Journal of Medical Internet Research | Xiaolei Lv, Xiaomeng Zhang, Yuan Li, et al. |
| 2 | [Large Language Models in Medicine: Applications, Challenges, and Future Directions](https://doi.org/10.7150/ijms.111780) | 2025 | 3 | 21 | International Journal of Medical Sciences | Erlan Yu, Xuehong Chu, Wanwan Zhang, et al. |
| 3 | [Evaluating and addressing demographic disparities in medical large language models: a systematic review](https://doi.org/10.1186/s12939-025-02419-0) | 2025 | 3 | 28 | International Journal for Equity in Health | Mahmud Omar, Vera Sorin, Reem Agbareia, et al. |
| 4 | [Clinical decision support for bipolar depression using large language models](https://doi.org/10.1038/s41386-024-01841-2) | 2024 | 4 | 40 | Neuropsychopharmacology | Roy H. Perlis, Joseph F. Goldberg, Michael J. Ostacher, et al. |
| 5 | [“Doctor ChatGPT, Can You Help Me?” The Patient’s Perspective: Cross-Sectional Study](https://doi.org/10.2196/58831) | 2024 | 3 | 37 | Journal of Medical Internet Research | Jonas Armbruster, Florian Bussmann, Catharina Rothhaas, et al. |
| 6 | [Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2) | 2025 | 4 | 53 | Nature Medicine | Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, et al. |
| 7 | [Sociodemographic biases in medical decision making by large language models](https://doi.org/10.1038/s41591-025-03626-6) | 2025 | 3 | 42 | Nature Medicine | Mahmud Omar, Shelly Soffer, Reem Agbareia, et al. |
| 8 | [Benchmarking large language models for biomedical natural language processing applications and recommendations](https://doi.org/10.1038/s41467-025-56989-2) | 2025 | 3 | 47 | Nature Communications | Qingyu Chen, Yan Hu, Xueqing Peng, et al. |
| 9 | [Harnessing artificial intelligence in bariatric surgery: comparative analysis of ChatGPT-4, Bing, and Bard in generating clinician-level bariatric surgery recommendations](https://doi.org/10.1016/j.soard.2024.03.011) | 2024 | 3 | 47 | Surgery for Obesity and Related Diseases | Yung Lee, Thomas H. Shin, Léa Tessier, et al. |
| 10 | [Comparative Analysis of Multimodal Large Language Model Performance on Clinical Vignette Questions](https://doi.org/10.1001/jama.2023.27861) | 2024 | 3 | 51 | JAMA | Tianyu Han, Lisa C. Adams, Keno K. Bressem, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Architect as Principal: Why the Cinematic Strategist is the Inevitable Successor to the Game of Scale Consultant](https://doi.org/10.5281/zenodo.17822338) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 2 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 3 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 4 | [Cinematic Strategy as a New Field of Study: A Capstone Synthesis of the Doctrinal, Economic, and Scientific Foundations of a Game of Stakes Practice](https://doi.org/10.5281/zenodo.17822495) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 5 | [The Doctrine of Strategic Counsel: A Foundational Thesis on the Rejection of the Consultant (Agent) Model and the Ascension to Peer (Principal) Status](https://doi.org/10.5281/zenodo.17818520) | 2025 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 6 | [The Effectiveness of Gamification in Changing Health-related Behaviors: A Systematic Review and Meta-analysis](https://doi.org/10.2174/0118749445234806240206094335) | 2024 | 2 | 6 | The Open Public Health Journal | Bashar I. Alzghoul |
| 7 | [The Anti-Sales Doctrine: A Structural Rebuttal to the Principal-Agent Problem in High-Stakes Conversion](https://doi.org/10.5281/zenodo.17817355) | 2025 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 8 | [The Strategist's Crucible: A Superior Model for Forging Talent](https://doi.org/10.5281/zenodo.17816022) | 2025 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 9 | [The Architecture of Conviction™: A Doctrinal Synthesis on Solving Asymmetrical Information in the High-Stakes Advisory Market](https://doi.org/10.5281/zenodo.17815175) | 2025 | 2 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 10 | [Cinematic Clarity is Business Strategy™: A Financial and Neuro-Scientific Proof of the Trust Dividend](https://doi.org/10.5281/zenodo.17814452) | 2025 | 2 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Architect as Principal: Why the Cinematic Strategist is the Inevitable Successor to the Game of Scale Consultant](https://doi.org/10.5281/zenodo.17822338) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 2 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 3 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 4 | [Cinematic Strategy as a New Field of Study: A Capstone Synthesis of the Doctrinal, Economic, and Scientific Foundations of a Game of Stakes Practice](https://doi.org/10.5281/zenodo.17822495) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 5 | [The Doctrine of Strategic Counsel: A Foundational Thesis on the Rejection of the Consultant (Agent) Model and the Ascension to Peer (Principal) Status](https://doi.org/10.5281/zenodo.17818520) | 2025 | 2 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 6 | [The Effectiveness of Gamification in Changing Health-related Behaviors: A Systematic Review and Meta-analysis](https://doi.org/10.2174/0118749445234806240206094335) | 2024 | 2 | 6 | The Open Public Health Journal | Bashar I. Alzghoul |
| 7 | [The Anti-Sales Doctrine: A Structural Rebuttal to the Principal-Agent Problem in High-Stakes Conversion](https://doi.org/10.5281/zenodo.17817355) | 2025 | 2 | 6 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 8 | [The Strategist's Crucible: A Superior Model for Forging Talent](https://doi.org/10.5281/zenodo.17816022) | 2025 | 2 | 8 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 9 | [The Architecture of Conviction™: A Doctrinal Synthesis on Solving Asymmetrical Information in the High-Stakes Advisory Market](https://doi.org/10.5281/zenodo.17815175) | 2025 | 2 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 10 | [Cinematic Clarity is Business Strategy™: A Financial and Neuro-Scientific Proof of the Trust Dividend](https://doi.org/10.5281/zenodo.17814452) | 2025 | 2 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Architect as Principal: Why the Cinematic Strategist is the Inevitable Successor to the Game of Scale Consultant](https://doi.org/10.5281/zenodo.17822338) | 2025 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 2 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 3 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 4 | [Cinematic Strategy as a New Field of Study: A Capstone Synthesis of the Doctrinal, Economic, and Scientific Foundations of a Game of Stakes Practice](https://doi.org/10.5281/zenodo.17822495) | 2025 | 2 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 5 | [A Deep Policy Dynamic Programming Based Intelligent Data Routing Scheme for IoT-Enabled Wireless Sensor Networks](https://doi.org/10.1109/tsusc.2024.3462512) | 2024 | 1 | 1 | IEEE Transactions on Sustainable Computing | Archana Ojha, Sahil Manikchand Chaudhari, Prasenjit Chanak |
| 6 | [Theorico-Game Approach for Interaction of Corporate Center and Divisions in Companies](https://doi.org/10.21686/2413-2829-2025-3-223-230) | 2025 | 1 | 0 | Vestnik of the Plekhanov Russian University of Economics | A. A. Kulikov |
| 7 | [IMPLEMENTATION OF THE PRINCIPLES OF THE SPIRAL DYNAMICS MODEL IN THE MANAGEMENT OF THE "GROUP OF COMPANIES" (ON THE EXAMPLE OF SILTEK GROUP)](https://doi.org/10.34925/eip.2023.150.1.247) | 2023 | 1 | 0 | Экономика и предпринимательство | Ю.Г. ЛЕСНЫХ |
| 8 | [SMART CONTRACTS AS INNOVATIVE CONTRACTING PRACTICES IN THE DIGITAL ECONOMY](https://doi.org/10.31249/rsm/2021.02.16) | 2021 | 1 | 0 | Russia and the Contemporary World | Е.А. Мосакова |
| 9 | [METHODOLOGY AND MAIN STAGES OF THE APPLICATION OF COOPERATIVE GAMES IN ECONOMIC RESEARCH](https://doi.org/10.55421/2499992x_2022_4_29) | 2022 | 1 | 0 | Managing Sustainable Development | Felix F. Yurlov, Anna Plekhanova, Sergey Yashin |
| 10 | [Discrete models of economic efficiency of an oil and gas industry enterprise](https://doi.org/10.25726/r7391-9520-1979-a) | 2023 | 1 | 0 | Management of Education | Р.Х. Байрамгазиев, Ф.Ф. Газизов, А.Р. Гарипов, et al. |
<!-- TRENDING-END -->
