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

Last update: 2025-11-24 06:23 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Expertise in Management Research: A Review and Agenda for Future Research](https://doi.org/10.5465/annals.2022.0078) | 2023 | 8 | 22 | Academy of Management Annals | Maximilian Heimstädt, Tomi Koljonen, Kasper Trolle Elmholdt |
| 2 | [For a Sociology of Expertise: The Social Origins of the Autism Epidemic](https://doi.org/10.1086/668448) | 2013 | 8 | 589 | American Journal of Sociology | Gil Eyal |
| 3 | [Translating Expertise across Work Contexts: U.S. Puppeteers Move from Stage to Screen](https://doi.org/10.1177/0003122420987199) | 2021 | 6 | 24 | American Sociological Review | Michel Anteby, Audrey Holm |
| 4 | [To Hive or to Hold? Producing Professional Authority through Scut Work](https://doi.org/10.1177/0001839214560743) | 2014 | 6 | 170 | Administrative Science Quarterly | Ruthanne Huising |
| 5 | [The System of Professions](https://doi.org/10.7208/chicago/9780226189666.001.0001) | 1988 | 6 | 6725 |  | Andrew Abbott |
| 6 | [Relational Expertise: What Machines Can't Know](https://doi.org/10.1111/joms.12915) | 2023 | 5 | 58 | Journal of Management Studies | Pauli Pakarinen, Ruthanne Huising |
| 7 | [Elements of Professional Expertise](https://doi.org/10.1177/0003122415601157) | 2015 | 5 | 101 | American Sociological Review | Rebecca L. Sandefur |
| 8 | [Estimating the Effects of Encumbrance and Walking on Mixed Reality Interaction](https://doi.org/10.1145/3706598.3713492) | 2025 | 4 | 7 |  | Tangrui Li, Eduardo Velloso, Anusha Withana, et al. |
| 9 | [Experts at Coordination: Examining the Performance, Production, and Value of Process Expertise](https://doi.org/10.1093/joc/jqz041) | 2020 | 4 | 25 | Journal of Communication | William C. Barley, Jeffrey W. Treem, Paul M. Leonardi |
| 10 | [THE PRIMACY OF TRUTH AND THE ERROR OF ZERO](https://doi.org/10.5281/zenodo.17518273) | 2025 | 4 | 46 | Zenodo (CERN European Organization for Nuclear Research) | Weekes, Randall |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 119 | 114163 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 68 | 40708 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 34 | 26188 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 27 | 6906 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Machine Learning: Algorithms, Real-World Applications and Research Directions](https://doi.org/10.1007/s42979-021-00592-x) | 2021 | 16 | 4363 | SN Computer Science | Iqbal H. Sarker |
| 6 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 16 | 14859 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 16 | 30776 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | 1986 | 15 | 28725 | Nature | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |
| 9 | [Machine learning: Trends, perspectives, and prospects](https://doi.org/10.1126/science.aaa8415) | 2015 | 14 | 8637 | Science | Michael I. Jordan, Tom M. Mitchell |
| 10 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 14 | 75169 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 9 | 1287 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 7 | 892 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 6 | 220 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 4 | [A universal graph deep learning interatomic potential for the periodic table](https://doi.org/10.1038/s43588-022-00349-3) | 2022 | 6 | 639 | Nature Computational Science | Chi Chen, Shyue Ping Ong |
| 5 | [KEGG: biological systems database as a model of the real world](https://doi.org/10.1093/nar/gkae909) | 2024 | 6 | 1074 | Nucleic Acids Research | Minoru Kanehisa, Miho Furumichi, Yoko Sato, et al. |
| 6 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 16884 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 7 | [A Comprehensive Survey on Semi-Automatic Solar-Powered Pesticide Sprayers for Farming](https://doi.org/10.55529/jeet.42.21.28) | 2024 | 5 | 117 | Journal of Energy Engineering and Thermodynamics | Altaf O. Mulani |
| 8 | [Non-invasive Anemia Detection and Prediagnosis](https://doi.org/10.1177/0976500x241276307) | 2024 | 5 | 119 | Journal of Pharmacology and Pharmacotherapeutics | Santosh Aiwale, Mahesh T. Kolte, Varsha K. Harpale, et al. |
| 9 | [Epilepsy Identification using Hybrid CoPrO-DCNN Classifier](https://doi.org/10.12785/ijcds/160157) | 2024 | 5 | 120 | International Journal of Computing and Digital Systems | Ganesh Birajadar, Altaf O. Mulani, Osamah Ibrahim Khalaf, et al. |
| 10 | [Computational and experimental analyses of pressure drop in curved tube structural sections of Coriolis mass flow metre for laminar flow region](https://doi.org/10.1080/17445302.2024.2317651) | 2024 | 5 | 121 | Ships and Offshore Structures | Vikram A. Kolhe, Suyash Y. Pawar, Scott Gohery, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 18 | 30258 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 17 | 2418 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 13 | 20253 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 2185 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 12 | 4142 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 6 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 10 | 289 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 7 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 2334 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 8 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 9 | 347 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 9 | 1677 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 9 | 9086 |  | Nils Reimers, Iryna Gurevych |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 17 | 2418 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 2185 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 10 | 289 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 4 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 2334 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 5 | [Structured information extraction from scientific text with large language models](https://doi.org/10.1038/s41467-024-45563-x) | 2024 | 9 | 347 | Nature Communications | John Dagdelen, Alexander Dunn, Sang‐Hoon Lee, et al. |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 9 | 1677 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 712 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 8 | [A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly](https://doi.org/10.1016/j.hcc.2024.100211) | 2024 | 7 | 573 | High-Confidence Computing | Yifan Yao, Jinhao Duan, Kaidi Xu, et al. |
| 9 | [The future landscape of large language models in medicine](https://doi.org/10.1038/s43856-023-00370-1) | 2023 | 7 | 712 | Communications Medicine | Jan Clusmann, Fiona R. Kolbinger, Hannah Sophie Muti, et al. |
| 10 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 2995 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Adaptive Internal Propagation (AIP): Universal Scaling of Internal Dependencies in Discrete Systems](https://doi.org/10.5281/zenodo.17666984) | 2025 | 4 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Muñoz Rodriguez, Jonatan |
| 2 | [Large Language Models in Medicine: Applications, Challenges, and Future Directions](https://doi.org/10.7150/ijms.111780) | 2025 | 4 | 16 | International Journal of Medical Sciences | Erlan Yu, Xuehong Chu, Wanwan Zhang, et al. |
| 3 | [LawBench: Benchmarking Legal Knowledge of Large Language Models](https://doi.org/10.18653/v1/2024.emnlp-main.452) | 2024 | 4 | 32 |  | Zhiwei Fei, Xiaoyu Shen, Dawei Zhu, et al. |
| 4 | [Comparative benchmarking of the DeepSeek large language model on medical tasks and clinical reasoning](https://doi.org/10.1038/s41591-025-03726-3) | 2025 | 4 | 42 | Nature Medicine | Mickaël Tordjman, Zelong Liu, Murat Yüce, et al. |
| 5 | [Applications and Concerns of ChatGPT and Other Conversational Large Language Models in Health Care: Systematic Review](https://doi.org/10.2196/22769) | 2024 | 5 | 57 | Journal of Medical Internet Research | Leyao Wang, Zhiyu Wan, Congning Ni, et al. |
| 6 | [A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation](https://doi.org/10.1038/s41746-025-01670-7) | 2025 | 4 | 48 | npj Digital Medicine | Elham Asgari, Nina Montaña-Brown, Magda Dubois, et al. |
| 7 | [CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code](https://doi.org/10.18653/v1/2023.emnlp-main.859) | 2023 | 4 | 63 |  | Shuyan Zhou, Uri Alon, Sumit Agarwal, et al. |
| 8 | [Large Language Models for Mental Health Applications: Systematic Review](https://doi.org/10.2196/57400) | 2024 | 4 | 75 | JMIR Mental Health | Zhijun Guo, Alvina G. Lai, Johan H. Thygesen, et al. |
| 9 | [Dynamic prompt-based virtual assistant framework for BIM information search](https://doi.org/10.1016/j.autcon.2023.105067) | 2023 | 4 | 85 | Automation in Construction | Junwen Zheng, Martin Fischer |
| 10 | [A multimodal approach to cross-lingual sentiment analysis with ensemble of transformer and LLM](https://doi.org/10.1038/s41598-024-60210-7) | 2024 | 4 | 97 | Scientific Reports | Md Saef Ullah Miah, Md. Mohsin Kabir, Talha Bin Sarwar, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Does Gamification Work? -- A Literature Review of Empirical Studies on Gamification](https://doi.org/10.1109/hicss.2014.377) | 2014 | 3 | 4474 |  | Juho Hamari, Jonna Koivisto, Harri Sarsa |
| 2 | [Equilibrium points in <i>n</i> -person games](https://doi.org/10.1073/pnas.36.1.48) | 1950 | 3 | 7047 | Proceedings of the National Academy of Sciences | John F. Nash |
| 3 | [Evolutionary Games in Economics](https://doi.org/10.2307/2938222) | 1991 | 2 | 1800 | Econometrica | Daniel Friedman |
| 4 | [The Logic of Animal Conflict](https://doi.org/10.1038/246015a0) | 1973 | 2 | 6040 | Nature | John Maynard Smith, George Price |
| 5 | [From game design elements to gamefulness](https://doi.org/10.1145/2181037.2181040) | 2011 | 2 | 7190 |  | Sebastian Deterding, Dan Dixon, Rilla Khaled, et al. |
| 6 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 2 | 78507 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 7 | [Source identification and health risk assessment of urban groundwater nitrate contamination in Chongqing, southwestern China](https://doi.org/10.1016/j.ejrh.2025.102792) | 2025 | 1 | 1 | Journal of Hydrology Regional Studies | Yunhui Zhang, Zhan Xie, Weiting Liu, et al. |
| 8 | [Groundwater Quality Prediction Using Proximal Hyperspectral Sensing, GIS, and Machine Learning Algorithms](https://doi.org/10.1007/s11270-025-07997-x) | 2025 | 1 | 1 | Water Air & Soil Pollution | Hemant Raheja, Arun Goel, Mahesh Pal |
| 9 | [Enhancing groundwater quality index prediction in data-scarce regions: Application of advanced artificial intelligence models in Nagaland, India](https://doi.org/10.1016/j.dynatmoce.2025.101579) | 2025 | 1 | 1 | Dynamics of Atmospheres and Oceans | Subhrajyoti Deb |
| 10 | [Practical Quantum Game Theory](https://doi.org/10.1109/coginfocom59411.2023.10397541) | 2023 | 1 | 2 |  | Mihály Szabó, Szabina Fodor |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Source identification and health risk assessment of urban groundwater nitrate contamination in Chongqing, southwestern China](https://doi.org/10.1016/j.ejrh.2025.102792) | 2025 | 1 | 1 | Journal of Hydrology Regional Studies | Yunhui Zhang, Zhan Xie, Weiting Liu, et al. |
| 2 | [Groundwater Quality Prediction Using Proximal Hyperspectral Sensing, GIS, and Machine Learning Algorithms](https://doi.org/10.1007/s11270-025-07997-x) | 2025 | 1 | 1 | Water Air & Soil Pollution | Hemant Raheja, Arun Goel, Mahesh Pal |
| 3 | [Enhancing groundwater quality index prediction in data-scarce regions: Application of advanced artificial intelligence models in Nagaland, India](https://doi.org/10.1016/j.dynatmoce.2025.101579) | 2025 | 1 | 1 | Dynamics of Atmospheres and Oceans | Subhrajyoti Deb |
| 4 | [Practical Quantum Game Theory](https://doi.org/10.1109/coginfocom59411.2023.10397541) | 2023 | 1 | 2 |  | Mihály Szabó, Szabina Fodor |
| 5 | [A Bayesian Maximum Entropy Fusion model for enhanced prediction and risk assessment of fluoride and arsenic contamination in groundwater](https://doi.org/10.1016/j.jconhyd.2025.104664) | 2025 | 1 | 2 | Journal of Contaminant Hydrology | Jiang Zhang, Changlai Xiao, Xiujuan Liang, et al. |
| 6 | [Assessment of groundwater quality and its vulnerability for safe drinking purpose](https://doi.org/10.2166/hydro.2024.122) | 2024 | 1 | 2 | Journal of Hydroinformatics | Hemant Raheja, Arun Goel, Mahesh Pal |
| 7 | [A comparison of metaheuristic optimizations with automated hyperparameter tuning methods in support vector machines algorithm for predicting soil water characteristic curve](https://doi.org/10.1016/j.enggeo.2025.108121) | 2025 | 1 | 2 | Engineering Geology | Mostafa Rastgou, Yong He, Ruitao Lou, et al. |
| 8 | [Prediction and analysis of tunnel water inrush disasters in Chinese Karst area based on Variable weight-weighted Bayesian network model](https://doi.org/10.1007/s13146-024-01031-7) | 2024 | 1 | 3 | Carbonates and Evaporites | Zengguang Xu, Fanhua Kong, Cheng Cao, et al. |
| 9 | [Groundwater quality evaluation for drinking and irrigation using analytical hierarchy process with GIS in semi critical block of Chhattisgarh, India](https://doi.org/10.1007/s12665-024-11656-5) | 2024 | 1 | 3 | Environmental Earth Sciences | Aekesh Kumar, Mahendra Prasad Tripathi, Dhiraj Khalkho, et al. |
| 10 | [GAME-THEORETICAL MODEL OF COVID-19 VACCINATION IN THE ENDEMIC EQUILIBRIUM](https://doi.org/10.1142/s021833902450013x) | 2023 | 1 | 4 | Journal of Biological Systems | R. Márquez, MARIA SEANNA CABERO MINAS, J. Santos, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Source identification and health risk assessment of urban groundwater nitrate contamination in Chongqing, southwestern China](https://doi.org/10.1016/j.ejrh.2025.102792) | 2025 | 1 | 1 | Journal of Hydrology Regional Studies | Yunhui Zhang, Zhan Xie, Weiting Liu, et al. |
| 2 | [Groundwater Quality Prediction Using Proximal Hyperspectral Sensing, GIS, and Machine Learning Algorithms](https://doi.org/10.1007/s11270-025-07997-x) | 2025 | 1 | 1 | Water Air & Soil Pollution | Hemant Raheja, Arun Goel, Mahesh Pal |
| 3 | [Enhancing groundwater quality index prediction in data-scarce regions: Application of advanced artificial intelligence models in Nagaland, India](https://doi.org/10.1016/j.dynatmoce.2025.101579) | 2025 | 1 | 1 | Dynamics of Atmospheres and Oceans | Subhrajyoti Deb |
| 4 | [Practical Quantum Game Theory](https://doi.org/10.1109/coginfocom59411.2023.10397541) | 2023 | 1 | 2 |  | Mihály Szabó, Szabina Fodor |
| 5 | [Looking Back on Decision-Making Under Conditions of Conflict](https://doi.org/10.1007/978-3-030-49629-6_31) | 2021 | 1 | 2 |  | Liping Fang, Keith W. Hipel |
| 6 | [A Bayesian Maximum Entropy Fusion model for enhanced prediction and risk assessment of fluoride and arsenic contamination in groundwater](https://doi.org/10.1016/j.jconhyd.2025.104664) | 2025 | 1 | 2 | Journal of Contaminant Hydrology | Jiang Zhang, Changlai Xiao, Xiujuan Liang, et al. |
| 7 | [Assessment of groundwater quality and its vulnerability for safe drinking purpose](https://doi.org/10.2166/hydro.2024.122) | 2024 | 1 | 2 | Journal of Hydroinformatics | Hemant Raheja, Arun Goel, Mahesh Pal |
| 8 | [A comparison of metaheuristic optimizations with automated hyperparameter tuning methods in support vector machines algorithm for predicting soil water characteristic curve](https://doi.org/10.1016/j.enggeo.2025.108121) | 2025 | 1 | 2 | Engineering Geology | Mostafa Rastgou, Yong He, Ruitao Lou, et al. |
| 9 | [From Game Theory to Drama Theory](https://doi.org/10.1007/978-3-030-49629-6_14) | 2021 | 1 | 3 |  | Jim Bryant |
| 10 | [Prediction and analysis of tunnel water inrush disasters in Chinese Karst area based on Variable weight-weighted Bayesian network model](https://doi.org/10.1007/s13146-024-01031-7) | 2024 | 1 | 3 | Carbonates and Evaporites | Zengguang Xu, Fanhua Kong, Cheng Cao, et al. |
<!-- TRENDING-END -->
