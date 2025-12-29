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

Last update: 2025-12-29 06:26 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [MNO and Ontological Recurrence: A Non-Representational Account of Quantum Measurement and Conscious Experience](https://doi.org/10.5281/zenodo.17913823) | 2025 | 7 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Speed, Timothy |
| 2 | [The Constructed Observer - World-Formation Beyond Representation - Why Perception Is Not Representation, but a Structural Achievement](https://doi.org/10.5281/zenodo.18006170) | 2025 | 6 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Timothy Speed |
| 3 | [On the roles of function and selection in evolving systems](https://doi.org/10.1073/pnas.2310223120) | 2023 | 6 | 92 | Proceedings of the National Academy of Sciences | Michael L. Wong, Carol E. Cleland, Daniel Arend, et al. |
| 4 | [The Causal Horizon in Causal Latency Theory: Unifying the CMB, Hubble Tension, and JWST Anomalies](https://doi.org/10.5281/zenodo.17964740) | 2025 | 4 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Sandner, Daniel |
| 5 | [Orch-OR with Recurrence: A Minimal Dynamical Condition for When Objective Reductions Yield Conscious Experience](https://doi.org/10.5281/zenodo.17942531) | 2025 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Speed, Timothy |
| 6 | [Diatom and Radiolarian Biostratigraphy in the Vicinity of the 2011 Tohoku Earthquake Source Fault in <scp>IODP</scp> Hole 343‐ <scp>C0019E</scp> of <scp>JFAST</scp>](https://doi.org/10.1111/iar.70009) | 2025 | 4 | 6 | Island Arc | Masao Iwai, Isao Motoyama, Weiren Lin, et al. |
| 7 | [Chalcone-based schiff bases: Design, synthesis, structural characterization and biological effects](https://doi.org/10.1016/j.molstruc.2025.142211) | 2025 | 4 | 6 | Journal of Molecular Structure | Halise Yalazan, Damla Koç, Fadime Aydın Köse, et al. |
| 8 | [The All–Nothing Paradox - Ontological Openness as a Condition of World-Formation - Why Closure – Not Complexity – Marks the Limit of Artificial Systems](https://doi.org/10.5281/zenodo.18000820) | 2025 | 4 | 9 | Zenodo (CERN European Organization for Nuclear Research) | Timothy Speed |
| 9 | [Evaluation of cytotoxicity, chemical composition, antioxidant potential, apoptosis relationship, molecular docking, and MM-GBSA analysis of Rumex crispus leaf extracts](https://doi.org/10.1016/j.molstruc.2024.140791) | 2024 | 4 | 10 | Journal of Molecular Structure | Burak Tüzün |
| 10 | [Molecular descriptors and in silico studies of 4-((5-(decylthio)-4-methyl-4n-1,2,4-triazol-3-yl)methyl)morpholine as a potential drug for the treatment of fungal pathologies](https://doi.org/10.1016/j.compbiolchem.2024.108206) | 2024 | 4 | 11 | Computational Biology and Chemistry | Ohloblina Myroslava, Alireza Poustforoosh, Bushuieva Inna, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 94 | 115020 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 62 | 41264 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 31 | 26394 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 24 | 7090 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 24 | 30942 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 16 | 75636 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 15 | 198843 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 8 | [Regularization and Variable Selection Via the Elastic Net](https://doi.org/10.1111/j.1467-9868.2005.00503.x) | 2005 | 12 | 19712 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Hui Zou, Trevor Hastie |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 12 | 28400 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 12 | 90535 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 10 | 12892 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 2 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 6 | 510 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 3 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 6 | 526 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 4 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 6 | 982 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 5 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 6 | 8728 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 6 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 17361 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 7 | [Untitled](https://doi.org/10.7551/mitpress/3206.001.0001) | 2022 | 5 | 19010 |  | Carl Edward Rasmussen, Christopher K. I. Williams |
| 8 | [Interpreting artificial intelligence models: a systematic review on the application of LIME and SHAP in Alzheimer’s disease detection](https://doi.org/10.1186/s40708-024-00222-1) | 2024 | 4 | 200 | Brain Informatics | Vimbi Viswan, Noushath Shaffi, Mufti Mahmud |
| 9 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 218 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 10 | [Comparative performance analysis of K-nearest neighbour (KNN) algorithm and its different variants for disease prediction](https://doi.org/10.1038/s41598-022-10358-x) | 2022 | 4 | 594 | Scientific Reports | Shahadat Uddin, Ibtisham Haque, Haohui Lu, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Advance Intelligent Video Surveillance System (AIVSS): A Future Aspect](https://doi.org/10.5772/intechopen.76444) | 2019 | 4 | 19 | IntechOpen eBooks | Mritunjay Rai, Agha Asim Husain, Tanmoy Maity, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 9 | 3647 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 9 | 30394 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 7 | 329 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 5 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 2392 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 6 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 6 | 82 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 7 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 353 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 8 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 6 | 443 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 9 | [A systematic review of large language model (LLM) evaluations in clinical medicine](https://doi.org/10.1186/s12911-025-02954-4) | 2025 | 5 | 78 | BMC Medical Informatics and Decision Making | Sina Shool, Sara Adimi, Reza Saboori Amleshi, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 5 | 1844 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 9 | 3647 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://doi.org/10.1038/s41591-024-03097-1) | 2024 | 7 | 329 | Nature Medicine | Paul Hager, Friederike Jungmann, Robbie Holland, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 2392 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 6 | 82 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 6 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 353 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 7 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 6 | 443 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 8 | [A systematic review of large language model (LLM) evaluations in clinical medicine](https://doi.org/10.1186/s12911-025-02954-4) | 2025 | 5 | 78 | BMC Medical Informatics and Decision Making | Sina Shool, Sara Adimi, Reza Saboori Amleshi, et al. |
| 9 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 5 | 1844 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 10 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 5 | 2327 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [AlphaMath Almost Zero: Process Supervision without Process](https://doi.org/10.52202/079017-0870) | 2024 | 2 | 0 |  | Chen Guoxin, Kai Fan, Chengxi Li, et al. |
| 2 | [The Clinicians’ Guide to Large Language Models: A General Perspective With a Focus on Hallucinations](https://doi.org/10.2196/59823) | 2025 | 3 | 27 | Interactive Journal of Medical Research | Dimitri Roustan, François Bastardot |
| 3 | [Open-Source Large Language Models in Radiology: A Review and Tutorial for Practical Research and Clinical Deployment](https://doi.org/10.1148/radiol.241073) | 2025 | 2 | 24 | Radiology | Cody Savage, Adway Kanhere, Vishwa S. Parekh, et al. |
| 4 | [Improving large language model applications in biomedicine with retrieval-augmented generation: a systematic review, meta-analysis, and clinical development guidelines](https://doi.org/10.1093/jamia/ocaf008) | 2025 | 4 | 49 | Journal of the American Medical Informatics Association | Siru Liu, Allison B. McCoy, Adam Wright |
| 5 | [Biomni: A General-Purpose Biomedical AI Agent](https://doi.org/10.1101/2025.05.30.656746) | 2025 | 2 | 25 | bioRxiv (Cold Spring Harbor Laboratory) | Kexin Huang, Serena Zhang, Hanchen Wang, et al. |
| 6 | [Parameter-Efficient Fine-Tuning of LLaMA for the Clinical Domain](https://doi.org/10.18653/v1/2024.clinicalnlp-1.9) | 2024 | 2 | 26 |  | Aryo Pradipta Gema, Pasquale Minervini, Luke Daines, et al. |
| 7 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 6 | 82 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 8 | [Accuracy, readability, and understandability of large language models for prostate cancer information to the public](https://doi.org/10.1038/s41391-024-00826-y) | 2024 | 3 | 45 | Prostate Cancer and Prostatic Diseases | Jacob Hershenhouse, Daniel Mokhtar, Michael Eppler, et al. |
| 9 | [A systematic review of large language model (LLM) evaluations in clinical medicine](https://doi.org/10.1186/s12911-025-02954-4) | 2025 | 5 | 78 | BMC Medical Informatics and Decision Making | Sina Shool, Sara Adimi, Reza Saboori Amleshi, et al. |
| 10 | [Work overload and diagnostic errors in radiology](https://doi.org/10.1016/j.ejrad.2023.111032) | 2023 | 2 | 34 | European Journal of Radiology | Ömer Kasalak, Haider A.A. Alnahwi, Romy Toxopeus, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolution and the Theory of Games](https://doi.org/10.1017/cbo9780511806292) | 1982 | 3 | 6826 | Cambridge University Press eBooks | John Maynard Smith |
| 2 | [How an industrial internet platform empowers the digital transformation of SMEs: theoretical mechanism and business model](https://doi.org/10.1108/jkm-09-2022-0757) | 2022 | 2 | 108 | Journal of Knowledge Management | Honglei Li, Ziyu Yang, Chunhua Jin, et al. |
| 3 | [Internet gaming disorder and psychosocial well-being: A longitudinal study of older-aged adolescents and emerging adults](https://doi.org/10.1016/j.addbeh.2020.106530) | 2020 | 2 | 137 | Addictive Behaviors | Zhaojun Teng, Halley M. Pontes, Qian Nie, et al. |
| 4 | [Global prevalence of gaming disorder: A systematic review and meta-analysis](https://doi.org/10.1177/0004867420962851) | 2020 | 2 | 688 | Australian & New Zealand Journal of Psychiatry | Matthew Stevens, Diana Dorstyn, Paul Delfabbro, et al. |
| 5 | [How entrepreneurial SMEs compete through digital platforms: The roles of digital platform capability, network capability and ambidexterity](https://doi.org/10.1016/j.jbusres.2019.03.035) | 2019 | 2 | 788 | Journal of Business Research | Javier Cenamor, Vinit Parida, Joakim Wincent |
| 6 | [Evolutionary games and spatial chaos](https://doi.org/10.1038/359826a0) | 1992 | 2 | 4339 | Nature | Martin A. Nowak, Robert M. May |
| 7 | [Dynamic optimization model of carbon emission allocation in agricultural product supply chain based on differential game theory](https://doi.org/10.5267/j.ijiec.2025.10.006) | 2025 | 1 | 1 | International Journal of Industrial Engineering Computations | Jing Chen |
| 8 | [Research on competition and cooperation in the two level multi agent supply chain of China's new energy vehicle industry based on differential game theory](https://doi.org/10.5267/j.ijiec.2025.9.004) | 2025 | 1 | 1 | International Journal of Industrial Engineering Computations | Zhuoming Wei, Jun Hu |
| 9 | [Revealing the complex dynamics of monkeypox epidemics in heterogeneous networks by the evolutionary game theory](https://doi.org/10.1038/s41598-025-13220-y) | 2025 | 1 | 1 | Scientific Reports | Mohammad Sharif Ullah, Wang Jin |
| 10 | [SPARC Big Deal Expenditures Dataset](https://doi.org/10.5281/zenodo.3361583) | 2020 | 1 | 0 | OPAL (Open@LaTrobe) (La Trobe University) | Sparc |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [How an industrial internet platform empowers the digital transformation of SMEs: theoretical mechanism and business model](https://doi.org/10.1108/jkm-09-2022-0757) | 2022 | 2 | 108 | Journal of Knowledge Management | Honglei Li, Ziyu Yang, Chunhua Jin, et al. |
| 2 | [Dynamic optimization model of carbon emission allocation in agricultural product supply chain based on differential game theory](https://doi.org/10.5267/j.ijiec.2025.10.006) | 2025 | 1 | 1 | International Journal of Industrial Engineering Computations | Jing Chen |
| 3 | [Research on competition and cooperation in the two level multi agent supply chain of China's new energy vehicle industry based on differential game theory](https://doi.org/10.5267/j.ijiec.2025.9.004) | 2025 | 1 | 1 | International Journal of Industrial Engineering Computations | Zhuoming Wei, Jun Hu |
| 4 | [Revealing the complex dynamics of monkeypox epidemics in heterogeneous networks by the evolutionary game theory](https://doi.org/10.1038/s41598-025-13220-y) | 2025 | 1 | 1 | Scientific Reports | Mohammad Sharif Ullah, Wang Jin |
| 5 | [A free toolkit to foster open access agreements](https://doi.org/10.1629/uksg.585) | 2023 | 1 | 0 | Insights the UKSG journal | Alicia Wise, Lorraine Estelle |
| 6 | [Research on Collaborative Governance of Cross-Domain Digital Innovation Ecosystems Based on Evolutionary Game Theory](https://doi.org/10.3390/systems13070558) | 2025 | 1 | 0 | Systems | Zijian Tian, Hua Zou, Shuo Yang, et al. |
| 7 | [Visualisation of Athlete Performance Based on Markov Chains and EWMs](https://doi.org/10.54097/8968mf54) | 2024 | 1 | 2 | Highlights in Science Engineering and Technology | Senlong Yu, Jianzhe Sun, Yusen Hu |
| 8 | [The 'Must Stock' Challenge in Academic Publishing: Pricing Implications of Transformative Agreements](https://doi.org/10.2139/ssrn.4818955) | 2024 | 1 | 3 | SSRN Electronic Journal | W. Benedikt Schmal |
| 9 | [The business of transformative agreements](https://doi.org/10.1016/j.acalib.2025.103020) | 2025 | 1 | 3 | The Journal of Academic Librarianship | Reece Steinberg |
| 10 | [Strategies for Negotiating and Signing Transformative Agreements in the Global South: The Colombia Consortium Experience](https://doi.org/10.1080/01930826.2023.2287945) | 2024 | 1 | 5 | Journal of Library Administration | Hernán Muñoz-Vélez, César Pallares, Andrés Ramírez, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Dynamic optimization model of carbon emission allocation in agricultural product supply chain based on differential game theory](https://doi.org/10.5267/j.ijiec.2025.10.006) | 2025 | 1 | 1 | International Journal of Industrial Engineering Computations | Jing Chen |
| 2 | [Research on competition and cooperation in the two level multi agent supply chain of China's new energy vehicle industry based on differential game theory](https://doi.org/10.5267/j.ijiec.2025.9.004) | 2025 | 1 | 1 | International Journal of Industrial Engineering Computations | Zhuoming Wei, Jun Hu |
| 3 | [Revealing the complex dynamics of monkeypox epidemics in heterogeneous networks by the evolutionary game theory](https://doi.org/10.1038/s41598-025-13220-y) | 2025 | 1 | 1 | Scientific Reports | Mohammad Sharif Ullah, Wang Jin |
| 4 | [SPARC Big Deal Expenditures Dataset](https://doi.org/10.5281/zenodo.3361583) | 2020 | 1 | 0 | OPAL (Open@LaTrobe) (La Trobe University) | Sparc |
| 5 | [A free toolkit to foster open access agreements](https://doi.org/10.1629/uksg.585) | 2023 | 1 | 0 | Insights the UKSG journal | Alicia Wise, Lorraine Estelle |
| 6 | [Research on Collaborative Governance of Cross-Domain Digital Innovation Ecosystems Based on Evolutionary Game Theory](https://doi.org/10.3390/systems13070558) | 2025 | 1 | 0 | Systems | Zijian Tian, Hua Zou, Shuo Yang, et al. |
| 7 | [Visualisation of Athlete Performance Based on Markov Chains and EWMs](https://doi.org/10.54097/8968mf54) | 2024 | 1 | 2 | Highlights in Science Engineering and Technology | Senlong Yu, Jianzhe Sun, Yusen Hu |
| 8 | [The 'Must Stock' Challenge in Academic Publishing: Pricing Implications of Transformative Agreements](https://doi.org/10.2139/ssrn.4818955) | 2024 | 1 | 3 | SSRN Electronic Journal | W. Benedikt Schmal |
| 9 | [The business of transformative agreements](https://doi.org/10.1016/j.acalib.2025.103020) | 2025 | 1 | 3 | The Journal of Academic Librarianship | Reece Steinberg |
| 10 | [Zero-Sum Two Person Games](https://doi.org/10.1007/978-0-387-30440-3_592) | 2009 | 1 | 4 | Encyclopedia of Complexity and Systems Science | T. E. S. Raghavan |
<!-- TRENDING-END -->
