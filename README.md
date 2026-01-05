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

Last update: 2026-01-05 06:30 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Biocultural Homogenization: A Wicked Problem in the Anthropocene](https://doi.org/10.1007/978-3-319-99513-7_2) | 2018 | 19 | 45 | Ecology and ethics | Ricardo Rozzi |
| 2 | [Biocultural Ethics: From Biocultural Homogenization Toward Biocultural Conservation](https://doi.org/10.1007/978-94-007-7470-4_2) | 2013 | 18 | 152 |  | Ricardo Rozzi |
| 3 | [Biocultural Ethics](https://doi.org/10.5840/enviroethics20123414) | 2012 | 14 | 118 | Environmental Ethics | Ricardo Rozzi |
| 4 | [Bridge the Channel, Enhance the Inclusivity: A Comparison Between Flagship Species-Centered and Moss-Centered Conservation in Chile and China](https://doi.org/10.1007/978-3-031-23368-5_28) | 2023 | 12 | 3 | Ecology and ethics | Danqiong Zhu |
| 5 | [Taxonomic Chauvinism, No More!](https://doi.org/10.5840/enviroethics201941325) | 2019 | 11 | 25 | Environmental Ethics | Ricardo Rozzi |
| 6 | [Ten Principles for Biocultural Conservation at the Southern Tip of the Americas: the Approach of the Omora Ethnobotanical Park](https://doi.org/10.5751/es-01709-110143) | 2006 | 10 | 189 | Ecology and Society | Ricardo Rozzi, Francisca Massardo, Christopher B. Anderson, et al. |
| 7 | [‘I’m not a complete mother’: childcare choices of migrant women in Cambodia](https://doi.org/10.1080/1369183x.2025.2594849) | 2025 | 9 | 9 | Journal of Ethnic and Migration Studies | Thida Kim, Lucy P. Jordan, Sokunnara Thlen |
| 8 | [The affective dimensions of child-raising in cross-national families in Singapore](https://doi.org/10.1080/1369183x.2025.2594854) | 2025 | 9 | 9 | Journal of Ethnic and Migration Studies | Bernice S. M. Loh, Brenda S. A. Yeoh, Shirlena Huang, et al. |
| 9 | [Reconceiving Asian parenting within intra-Asia migration](https://doi.org/10.1080/1369183x.2025.2594843) | 2025 | 9 | 9 | Journal of Ethnic and Migration Studies | Bittiandra Chand Somaiah, Exequiel Cabanda, Elaine Lynn‐Ee Ho, et al. |
| 10 | [Options within constraints: parenting experiences of college-educated Chinese stay-at-home mothers in Singapore](https://doi.org/10.1080/1369183x.2025.2594862) | 2025 | 9 | 9 | Journal of Ethnic and Migration Studies | Zheng Mu |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 112 | 115020 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 65 | 41264 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 25 | 26394 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 24 | 30942 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 17 | 7090 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 17 | 28400 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 75636 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 8 | [A tutorial on support vector regression](https://doi.org/10.1023/b:stco.0000035301.49549.88) | 2004 | 16 | 12318 | Statistics and Computing | Alex Smola, Bernhard Schölkopf |
| 9 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 15 | 14946 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 10 | [Regression Shrinkage and Selection Via the Lasso](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x) | 1996 | 15 | 49419 | Journal of the Royal Statistical Society Series B (Statistical Methodology) | Robert Tibshirani |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Effective Heart Disease Prediction Using Machine Learning Techniques](https://doi.org/10.3390/a16020088) | 2023 | 7 | 415 | Algorithms | Chintan Bhatt, P. V. Patel, Tarang Ghetia, et al. |
| 2 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 6 | 510 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 3 | [KEGG: biological systems database as a model of the real world](https://doi.org/10.1093/nar/gkae909) | 2024 | 6 | 1370 | Nucleic Acids Research | Minoru Kanehisa, Miho Furumichi, Yoko Sato, et al. |
| 4 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 12892 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 5 | [Machine learning and SHAP value interpretation for predicting comorbidity of cardiovascular disease and cancer with dietary antioxidants](https://doi.org/10.1016/j.redox.2024.103470) | 2024 | 5 | 90 | Redox Biology | Xiangjun Qi, Shujing Wang, Caishan Fang, et al. |
| 6 | [Applications of XGBoost in water resources engineering: A systematic literature review (Dec 2018–May 2023)](https://doi.org/10.1016/j.envsoft.2024.105971) | 2024 | 5 | 188 | Environmental Modelling & Software | Majid Niazkar, Andrea Menapace, Bruno Brentan, et al. |
| 7 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 5 | 1146 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 8 | [2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Association](https://doi.org/10.1161/cir.0000000000001209) | 2024 | 5 | 1841 | Circulation | Seth S. Martin, Aaron W. Aday, Zaid Almarzooq, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Machine learning and SHAP value interpretation for predicting comorbidity of cardiovascular disease and cancer with dietary antioxidants](https://doi.org/10.1016/j.redox.2024.103470) | 2024 | 5 | 90 | Redox Biology | Xiangjun Qi, Shujing Wang, Caishan Fang, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 14 | 20359 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 13 | 2392 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 11 | 30394 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 3647 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 2327 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 9 | 4223 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 8 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 9 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 8 | 9199 |  | Nils Reimers, Iryna Gurevych |
| 10 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 7 | 762 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 3647 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 2327 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 8 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 5 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 7 | 762 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 6 | [A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges](https://doi.org/10.1109/access.2024.3365742) | 2024 | 6 | 444 | IEEE Access | Mohaimenul Azam Khan Raiaan, Md. Saddam Hossain Mukta, Kaniz Fatema, et al. |
| 7 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 6 | 534 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 8 | [ChatGPT and large language models in academia: opportunities and challenges](https://doi.org/10.1186/s13040-023-00339-9) | 2023 | 5 | 444 | BioData Mining | Jesse G. Meyer, Ryan J. Urbanowicz, Patrick Martin, et al. |
| 9 | [Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy](https://doi.org/10.1016/j.ijinfomgt.2023.102642) | 2023 | 5 | 2968 | International Journal of Information Management | Yogesh K. Dwivedi, Nir Kshetri, Laurie Hughes, et al. |
| 10 | [A Survey on RAG with LLMs](https://doi.org/10.1016/j.procs.2024.09.178) | 2024 | 4 | 71 | Procedia Computer Science | Muhammad Arslan, Hussam Ghanem, Saba Munawar, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Diagnostic Performance of Large Language Models in Multimodal Analysis of Radiolucent Jaw Lesions](https://doi.org/10.1016/j.identj.2025.103910) | 2025 | 3 | 1 | International Dental Journal | K T Kim, Bong-Chul Kim |
| 2 | [Generative Artificial Intelligence: A New Engine for Advancing Environmental Science and Engineering](https://doi.org/10.1021/acs.est.4c07216) | 2024 | 3 | 16 | Environmental Science & Technology | Yipeng Wu, Ming Xu, Shuming Liu |
| 3 | [LLM-Aided Museum Guide: Personalized Tours Based on User Preferences](https://doi.org/10.1007/978-3-031-71710-9_18) | 2024 | 2 | 18 | Lecture notes in computer science | Iva Vasic, Hans-Georg Fill, Ramona Quattrini, et al. |
| 4 | [A Fast, Performant, Secure Distributed Training Framework For LLM](https://doi.org/10.1109/icassp48485.2024.10446717) | 2024 | 2 | 19 |  | Wei Huang, Yinggui Wang, Anda Cheng, et al. |
| 5 | [Using ChatGPT and Persuasive Technology for Personalized Recommendation Messages in Hotel Upselling](https://doi.org/10.3390/info14090504) | 2023 | 2 | 21 | Information | Manolis Remountakis, Konstantinos Kotis, Babis Kourtzis, et al. |
| 6 | [On Protecting the Data Privacy of Large Language Models (LLMs): A Survey](https://doi.org/10.1109/icmc60390.2024.00008) | 2024 | 2 | 35 |  | Biwei Yan, Kun Li, Minghui Xu, et al. |
| 7 | [A Survey on RAG with LLMs](https://doi.org/10.1016/j.procs.2024.09.178) | 2024 | 4 | 71 | Procedia Computer Science | Muhammad Arslan, Hussam Ghanem, Saba Munawar, et al. |
| 8 | [LLM-based agentic systems in medicine and healthcare](https://doi.org/10.1038/s42256-024-00944-1) | 2024 | 4 | 72 | Nature Machine Intelligence | Jianing Qiu, Kyle Lam, Guohao Li, et al. |
| 9 | [Accuracy of ChatGPT, Google Bard, and Microsoft Bing for Simplifying Radiology Reports](https://doi.org/10.1148/radiol.232561) | 2023 | 4 | 78 | Radiology | Kanhai Amin, Melissa Davis, Rushabh Doshi, et al. |
| 10 | [Implementing large language models in healthcare while balancing control, collaboration, costs and security](https://doi.org/10.1038/s41746-025-01476-7) | 2025 | 2 | 46 | npj Digital Medicine | Fabio Dennstädt, Janna Hastings, Paul Martin Putora, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Data-driven distributionally robust scheduling of community integrated energy systems with uncertain renewable generations considering integrated demand response](https://doi.org/10.1016/j.apenergy.2023.120749) | 2023 | 2 | 214 | Applied Energy | Yang Li, Meng Han, Mohammad Shahidehpour, et al. |
| 2 | [The Logic of Animal Conflict](https://doi.org/10.1038/246015a0) | 1973 | 2 | 6050 | Nature | John Maynard Smith, George Price |
| 3 | [Resilience and Stability of Ecological Systems](https://doi.org/10.1146/annurev.es.04.110173.000245) | 1973 | 2 | 16805 | Annual Review of Ecology and Systematics | C. S. Holling |
| 4 | [The "What" and "Why" of Goal Pursuits: Human Needs and the Self-Determination of Behavior](https://doi.org/10.1207/s15327965pli1104_01) | 2000 | 2 | 29272 | Psychological Inquiry | Edward L. Deci, Richard M. Ryan |
| 5 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 2 | 41264 |  | Tianqi Chen, Carlos Guestrin |
| 6 | [Improved Methods of Task Assignment and Resource Allocation With Preemption in Edge Computing Systems](https://doi.org/10.1109/tpds.2025.3583966) | 2025 | 1 | 1 | IEEE Transactions on Parallel and Distributed Systems | Adrian C. Rublein, Fidan Mehmeti, Mark Mahon, et al. |
| 7 | [Advanced Robust Heading Control for Unmanned Surface Vessels Using Hybrid Metaheuristic-Optimized Variable Universe Fuzzy PID with Enhanced Smith Predictor](https://doi.org/10.3390/biomimetics10090611) | 2025 | 1 | 1 | Biomimetics | Siyuan Zhan, Qiang Liu, Zhao Zhao, et al. |
| 8 | [Quantum-Inspired Statistical Frameworks: Enhancing Traditional Methods with Quantum Principles](https://doi.org/10.3390/encyclopedia5020048) | 2025 | 1 | 1 | Encyclopedia | Theodoros Kyriazos, Mary Poga |
| 9 | [A Quantum-Inspired Predator–Prey Algorithm for Real-Parameter Optimization](https://doi.org/10.3390/a17010033) | 2024 | 1 | 1 | Algorithms | Azal Ahmad Khan, Salman Hussain, Rohitash Chandra |
| 10 | [Optimal Tracking Control of Second-Order Multiagent Systems With Input Delay via Data-Driven Forward Reward <i>Q</i>-Learning Framework](https://doi.org/10.1109/tsmc.2024.3513561) | 2024 | 1 | 1 | IEEE Transactions on Systems Man and Cybernetics Systems | Kai Rao, Huaicheng Yan, Qiwei Liu, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Data-driven distributionally robust scheduling of community integrated energy systems with uncertain renewable generations considering integrated demand response](https://doi.org/10.1016/j.apenergy.2023.120749) | 2023 | 2 | 214 | Applied Energy | Yang Li, Meng Han, Mohammad Shahidehpour, et al. |
| 2 | [Improved Methods of Task Assignment and Resource Allocation With Preemption in Edge Computing Systems](https://doi.org/10.1109/tpds.2025.3583966) | 2025 | 1 | 1 | IEEE Transactions on Parallel and Distributed Systems | Adrian C. Rublein, Fidan Mehmeti, Mark Mahon, et al. |
| 3 | [Advanced Robust Heading Control for Unmanned Surface Vessels Using Hybrid Metaheuristic-Optimized Variable Universe Fuzzy PID with Enhanced Smith Predictor](https://doi.org/10.3390/biomimetics10090611) | 2025 | 1 | 1 | Biomimetics | Siyuan Zhan, Qiang Liu, Zhao Zhao, et al. |
| 4 | [Quantum-Inspired Statistical Frameworks: Enhancing Traditional Methods with Quantum Principles](https://doi.org/10.3390/encyclopedia5020048) | 2025 | 1 | 1 | Encyclopedia | Theodoros Kyriazos, Mary Poga |
| 5 | [A Quantum-Inspired Predator–Prey Algorithm for Real-Parameter Optimization](https://doi.org/10.3390/a17010033) | 2024 | 1 | 1 | Algorithms | Azal Ahmad Khan, Salman Hussain, Rohitash Chandra |
| 6 | [Optimal Tracking Control of Second-Order Multiagent Systems With Input Delay via Data-Driven Forward Reward <i>Q</i>-Learning Framework](https://doi.org/10.1109/tsmc.2024.3513561) | 2024 | 1 | 1 | IEEE Transactions on Systems Man and Cybernetics Systems | Kai Rao, Huaicheng Yan, Qiwei Liu, et al. |
| 7 | [Effects of employee stock ownership plans on firm performance – evidence from listed commercial banks of Vietnam](https://doi.org/10.21511/bbs.18(2).2023.17) | 2023 | 1 | 1 | Banks and Bank Systems | Phuong Lan Le, Hoa Nguyen |
| 8 | [Employee stock ownership plans and within-firm income inequality: evidence from China](https://doi.org/10.1108/cms-12-2022-0479) | 2023 | 1 | 1 | Chinese Management Studies | Peng Ning, Lixiao Geng, Liangding Jia |
| 9 | [Research on Heading Adaptive Control for Unmanned Surface Vehicles](https://doi.org/10.1109/ainit61980.2024.10581734) | 2024 | 1 | 0 |  | Qian Xiang, Jinghua Tie, Yong Tang, et al. |
| 10 | [Research on Collaborative Governance of Cross-Domain Digital Innovation Ecosystems Based on Evolutionary Game Theory](https://doi.org/10.3390/systems13070558) | 2025 | 1 | 0 | Systems | Zijian Tian, Hua Zou, Shuo Yang, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Improved Methods of Task Assignment and Resource Allocation With Preemption in Edge Computing Systems](https://doi.org/10.1109/tpds.2025.3583966) | 2025 | 1 | 1 | IEEE Transactions on Parallel and Distributed Systems | Adrian C. Rublein, Fidan Mehmeti, Mark Mahon, et al. |
| 2 | [Advanced Robust Heading Control for Unmanned Surface Vessels Using Hybrid Metaheuristic-Optimized Variable Universe Fuzzy PID with Enhanced Smith Predictor](https://doi.org/10.3390/biomimetics10090611) | 2025 | 1 | 1 | Biomimetics | Siyuan Zhan, Qiang Liu, Zhao Zhao, et al. |
| 3 | [Quantum-Inspired Statistical Frameworks: Enhancing Traditional Methods with Quantum Principles](https://doi.org/10.3390/encyclopedia5020048) | 2025 | 1 | 1 | Encyclopedia | Theodoros Kyriazos, Mary Poga |
| 4 | [A Quantum-Inspired Predator–Prey Algorithm for Real-Parameter Optimization](https://doi.org/10.3390/a17010033) | 2024 | 1 | 1 | Algorithms | Azal Ahmad Khan, Salman Hussain, Rohitash Chandra |
| 5 | [Optimal Tracking Control of Second-Order Multiagent Systems With Input Delay via Data-Driven Forward Reward <i>Q</i>-Learning Framework](https://doi.org/10.1109/tsmc.2024.3513561) | 2024 | 1 | 1 | IEEE Transactions on Systems Man and Cybernetics Systems | Kai Rao, Huaicheng Yan, Qiwei Liu, et al. |
| 6 | [Effects of employee stock ownership plans on firm performance – evidence from listed commercial banks of Vietnam](https://doi.org/10.21511/bbs.18(2).2023.17) | 2023 | 1 | 1 | Banks and Bank Systems | Phuong Lan Le, Hoa Nguyen |
| 7 | [Research on the Impact of Employee Stock Ownership Plan on Enterprise Innovation](https://doi.org/10.4236/ojacct.2021.104012) | 2021 | 1 | 1 | Open Journal of Accounting | Qiuyue Wang |
| 8 | [Employee stock ownership plans and within-firm income inequality: evidence from China](https://doi.org/10.1108/cms-12-2022-0479) | 2023 | 1 | 1 | Chinese Management Studies | Peng Ning, Lixiao Geng, Liangding Jia |
| 9 | [Research on Heading Adaptive Control for Unmanned Surface Vehicles](https://doi.org/10.1109/ainit61980.2024.10581734) | 2024 | 1 | 0 |  | Qian Xiang, Jinghua Tie, Yong Tang, et al. |
| 10 | [Research on Collaborative Governance of Cross-Domain Digital Innovation Ecosystems Based on Evolutionary Game Theory](https://doi.org/10.3390/systems13070558) | 2025 | 1 | 0 | Systems | Zijian Tian, Hua Zou, Shuo Yang, et al. |
<!-- TRENDING-END -->
