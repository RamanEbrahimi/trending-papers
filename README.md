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

Last update: 2025-09-22 06:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 10 | 13289 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 9 | 149978 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 9 | 191181 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 4 | [The go-between: Jan Eliasson and the styles of mediation](https://doi.org/10.5860/choice.48-6559) | 2011 | 7 | 63 | Choice Reviews Online | Peter Wallensteen, Isak Svensson |
| 5 | [The State: Past, Present, Future](https://openalex.org/W2297699385) | 2015 | 7 | 567 |  | Bob Jessop |
| 6 | [Efficient iterative schemes for<i>ab initio</i>total-energy calculations using a plane-wave basis set](https://doi.org/10.1103/physrevb.54.11169) | 1996 | 7 | 108451 | Physical review. B, Condensed matter | Georg Kresse, J. Furthmüller |
| 7 | [To End a Civil War: Norway's Peace Engagement in Sri Lanka](https://doi.org/10.17585/ip.v74.513) | 2016 | 6 | 26 | Internasjonal politikk | Ada Nissen |
| 8 | [Manipulating social tensions: Collibration as an alternative mode of government intervention](https://openalex.org/W1482146059) | 1993 | 6 | 47 | RePEc: Research Papers in Economics | Andrew Dunsire |
| 9 | [The Peace Brokers](https://doi.org/10.1515/9780691242903) | 1982 | 6 | 151 | Princeton University Press eBooks | Saadia Touval |
| 10 | [World Medical Association Declaration of Helsinki](https://doi.org/10.1001/jama.2013.281053) | 2013 | 6 | 23857 | JAMA | Unknown |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 58 | 109180 | Machine Learning | Leo Breiman |
| 2 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 21 | 30354 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 3 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 20 | 71125 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 4 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 19 | 6370 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 5 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 19 | 26229 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 6 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 16 | 24874 | The Annals of Statistics | Jerome H. Friedman |
| 7 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 13 | 19600 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 8 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 10 | 92698 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |
| 9 | [LightGBM: A Highly Efficient Gradient Boosting Decision Tree](https://openalex.org/W2768348081) | 2017 | 9 | 6749 |  | Guolin Ke, Qi Meng, Thomas Finley, et al. |
| 10 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 9 | 34250 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 8 | 13289 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 7 | 5523 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 3 | [Feature selection strategies: a comparative analysis of SHAP-value and importance-based methods](https://doi.org/10.1186/s40537-024-00905-w) | 2024 | 5 | 131 | Journal Of Big Data | Huanjing Wang, Qianxin Liang, John Hancock, et al. |
| 4 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 105 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 5 | [Optimizing renewable energy systems through artificial intelligence: Review and future prospects](https://doi.org/10.1177/0958305x241256293) | 2024 | 4 | 129 | Energy & Environment | Kingsley Ukoba, Kehinde O. Olatunji, Eyitayo Adeoye, et al. |
| 6 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 4 | 160 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 7 | [De novo design of protein structure and function with RFdiffusion](https://doi.org/10.1038/s41586-023-06415-8) | 2023 | 3 | 991 | Nature | Joseph L. Watson, David Juergens, Nathaniel R. Bennett, et al. |
| 8 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 3 | 2690 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 8 | 61725 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 2 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1070 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 5 | 1921 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://doi.org/10.48550/arxiv.2005.11401) | 2020 | 5 | 1935 | arXiv (Cornell University) | Patrick Lewis, Ethan Perez, Aleksandara Piktus, et al. |
| 5 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 2932 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 6 | [LLaMA: Open and Efficient Foundation Language Models](https://doi.org/10.48550/arxiv.2302.13971) | 2023 | 4 | 3014 | arXiv (Cornell University) | Hugo Touvron, Thibaut Lavril, Gautier Izacard, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 4 | 3510 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://doi.org/10.18653/v1/2020.acl-main.703) | 2020 | 4 | 6751 |  | Mike Lewis, Yinhan Liu, Naman Goyal, et al. |
| 9 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 4 | 7969 |  | Nils Reimers, Iryna Gurevych |
| 10 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://doi.org/10.48550/arxiv.1910.10683) | 2019 | 4 | 8449 | arXiv (Cornell University) | Colin Raffel, Noam Shazeer, Adam Roberts, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1070 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 5 | 1921 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 2932 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 4 | [LLaMA: Open and Efficient Foundation Language Models](https://doi.org/10.48550/arxiv.2302.13971) | 2023 | 4 | 3014 | arXiv (Cornell University) | Hugo Touvron, Thibaut Lavril, Gautier Izacard, et al. |
| 5 | [GeoGPT: An assistant for understanding and processing geospatial tasks](https://doi.org/10.1016/j.jag.2024.103976) | 2024 | 3 | 45 | International Journal of Applied Earth Observation and Geoinformation | Yifan Zhang, Wei Cheng, Zhengting He, et al. |
| 6 | [InfographicVQA](https://doi.org/10.1109/wacv51458.2022.00264) | 2022 | 3 | 53 | 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) | Minesh Mathew, Viraj Bagal, Rubèn Tito, et al. |
| 7 | [Software Testing With Large Language Models: Survey, Landscape, and Vision](https://doi.org/10.1109/tse.2024.3368208) | 2024 | 3 | 144 | IEEE Transactions on Software Engineering | Junjie Wang, Yuchao Huang, Chunyang Chen, et al. |
| 8 | [OCR-Free Document Understanding Transformer](https://doi.org/10.1007/978-3-031-19815-1_29) | 2022 | 3 | 154 | Lecture notes in computer science | Geewook Kim, Teakgyu Hong, Moonbin Yim, et al. |
| 9 | [Leveraging Large Language Models for Decision Support in Personalized Oncology](https://doi.org/10.1001/jamanetworkopen.2023.43689) | 2023 | 3 | 164 | JAMA Network Open | Manuela Benary, Xing David Wang, Max Schmidt, et al. |
| 10 | [Bias and Fairness in Large Language Models: A Survey](https://doi.org/10.1162/coli_a_00524) | 2024 | 3 | 174 | Computational Linguistics | Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Generative AI Apps with LangChain and Python](https://doi.org/10.1007/979-8-8688-0882-1) | 2024 | 2 | 1 | Apress eBooks | R. Patel Jay |
| 2 | [DocLayLLM: An Efficient Multi-modal Extension of Large Language Models for Text-rich Document Understanding](https://doi.org/10.1109/cvpr52734.2025.00382) | 2025 | 2 | 1 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Wenhui Liao, Jiapeng Wang, Hongliang Li, et al. |
| 3 | [GeoAgent: To Empower LLMs using Geospatial Tools for Address Standardization](https://doi.org/10.18653/v1/2024.findings-acl.362) | 2024 | 2 | 2 | Findings of the Association for Computational Linguistics: ACL 2022 | Chao-Long Huang, Shisong Chen, Zhixu Li, et al. |
| 4 | [Deidentifying Medical Documents with Local, Privacy-Preserving Large Language Models: The LLM-Anonymizer](https://doi.org/10.1056/aidbp2400537) | 2025 | 2 | 2 | NEJM AI | Isabella C. Wiest, Marie-Elisabeth Leßmann, F M Wolf, et al. |
| 5 | [Quantized Transformer Language Model Implementations on Edge Devices](https://doi.org/10.1109/icmla58977.2023.00104) | 2023 | 2 | 5 |  | Mohammad Wali Ur Rahman, Murad Mehrab Abrar, Hunter Gibbons Copening, et al. |
| 6 | [Security Requirements Classification into Groups Using NLP Transformers](https://doi.org/10.1109/rew53955.2021.9714713) | 2021 | 2 | 7 |  | Vasily Varenov, Aydar Gabdrahmanov |
| 7 | [Performance of ChatGPT and Bard on the medical licensing examinations varies across different cultures: a comparison study](https://doi.org/10.1186/s12909-024-06309-x) | 2024 | 2 | 8 | BMC Medical Education | Yikai Chen, Xiujie Huang, Fangjie Yang, et al. |
| 8 | [InstructDoc: A Dataset for Zero-Shot Generalization of Visual Document Understanding with Instructions](https://doi.org/10.1609/aaai.v38i17.29874) | 2024 | 2 | 9 | Proceedings of the AAAI Conference on Artificial Intelligence | Ryota Tanaka, Taichi Iki, Kyosuke Nishida, et al. |
| 9 | [Performance of Large Language Models on the Korean Dental Licensing Examination: A Comparative Study](https://doi.org/10.1016/j.identj.2024.09.002) | 2024 | 2 | 9 | International Dental Journal | Woojun Kim, Bong-Chul Kim, Han-Gyeol Yeom |
| 10 | [Scientists flock to DeepSeek: how they’re using the blockbuster AI model](https://doi.org/10.1038/d41586-025-00275-0) | 2025 | 2 | 13 | Nature | Elizabeth Gibney |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Multi-UAV path planning for multiple emergency payloads delivery in natural disaster scenarios](https://doi.org/10.1016/j.jnlest.2025.100303) | 2025 | 1 | 1 | Journal of Electronic Science and Technology | Zarina Kutpanova, Mustafa Raad Kadhim, Xu Zheng, et al. |
| 2 | [Collaborative Coverage Path Planning for UAV Swarm for Multi-region Post-Disaster Assessment](https://doi.org/10.1016/j.vehcom.2025.100915) | 2025 | 1 | 1 | Vehicular Communications | Yonghua Xiong, Yan Zhou, Jinhua She, et al. |
| 3 | [Adaptive multi-UAV cooperative path planning based on novel rotation artificial potential fields](https://doi.org/10.1016/j.knosys.2025.113429) | 2025 | 1 | 1 | Knowledge-Based Systems | Huidong Liu, Xianlei Long, Yong Li, et al. |
| 4 | [Performance enhancement of UAV-enabled MEC systems through intelligent task offloading and resource allocation](https://doi.org/10.1016/j.comnet.2025.111280) | 2025 | 1 | 1 | Computer Networks | Mohsen Darchini-Tabrizi, Amirali Pakdaman-Donyavi, Reza Entezari‐Maleki, et al. |
| 5 | [UAV-Supported Communication: Current and Prospective Solutions](https://doi.org/10.1016/j.vehcom.2025.100923) | 2025 | 1 | 1 | Vehicular Communications | Moayad Aloqaily, Ouns Bouachir, Ismaeel Al Ridhawi |
| 6 | [Deep learning-enhanced safety system for real-time in-situ blade damage monitoring in UAV using triboelectric sensor](https://doi.org/10.1016/j.nanoen.2025.111063) | 2025 | 1 | 1 | Nano Energy | Zhipeng Pan, Kuankuan Wang, Yixin Liu, et al. |
| 7 | [The development of distributed cooperative localization algorithms for multi-UAV systems in the past decade](https://doi.org/10.1016/j.measurement.2025.118040) | 2025 | 1 | 1 | Measurement | Zhaoyu Zhang, Nan Li, Gongmin Yan, et al. |
| 8 | [Flight path planning of UAV-driven refinement inspection for construction sites based on 3D reconstruction](https://doi.org/10.1016/j.autcon.2025.106360) | 2025 | 1 | 1 | Automation in Construction | Jian Liu, Wen Yi, Penglu Chen, et al. |
| 9 | [Security and privacy consideration for the deployment of electronic health records: a qualitative study covering Greece and Oman](https://doi.org/10.1080/19393555.2021.2003914) | 2021 | 1 | 1 | Information Security Journal A Global Perspective | Ourania Koutzampasopoulou Xanthidou, Dimitrios Xanthidis, Christos Manolas, et al. |
| 10 | [Delay-prioritized and Reliable Task Scheduling with Long-term Load Balancing in Computing Power Networks](https://doi.org/10.1109/tsc.2024.3495500) | 2024 | 1 | 1 | IEEE Transactions on Services Computing | Renchao Xie, Feng Li, Qinqin Tang, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Multi-UAV path planning for multiple emergency payloads delivery in natural disaster scenarios](https://doi.org/10.1016/j.jnlest.2025.100303) | 2025 | 1 | 1 | Journal of Electronic Science and Technology | Zarina Kutpanova, Mustafa Raad Kadhim, Xu Zheng, et al. |
| 2 | [Collaborative Coverage Path Planning for UAV Swarm for Multi-region Post-Disaster Assessment](https://doi.org/10.1016/j.vehcom.2025.100915) | 2025 | 1 | 1 | Vehicular Communications | Yonghua Xiong, Yan Zhou, Jinhua She, et al. |
| 3 | [Adaptive multi-UAV cooperative path planning based on novel rotation artificial potential fields](https://doi.org/10.1016/j.knosys.2025.113429) | 2025 | 1 | 1 | Knowledge-Based Systems | Huidong Liu, Xianlei Long, Yong Li, et al. |
| 4 | [Performance enhancement of UAV-enabled MEC systems through intelligent task offloading and resource allocation](https://doi.org/10.1016/j.comnet.2025.111280) | 2025 | 1 | 1 | Computer Networks | Mohsen Darchini-Tabrizi, Amirali Pakdaman-Donyavi, Reza Entezari‐Maleki, et al. |
| 5 | [UAV-Supported Communication: Current and Prospective Solutions](https://doi.org/10.1016/j.vehcom.2025.100923) | 2025 | 1 | 1 | Vehicular Communications | Moayad Aloqaily, Ouns Bouachir, Ismaeel Al Ridhawi |
| 6 | [Deep learning-enhanced safety system for real-time in-situ blade damage monitoring in UAV using triboelectric sensor](https://doi.org/10.1016/j.nanoen.2025.111063) | 2025 | 1 | 1 | Nano Energy | Zhipeng Pan, Kuankuan Wang, Yixin Liu, et al. |
| 7 | [The development of distributed cooperative localization algorithms for multi-UAV systems in the past decade](https://doi.org/10.1016/j.measurement.2025.118040) | 2025 | 1 | 1 | Measurement | Zhaoyu Zhang, Nan Li, Gongmin Yan, et al. |
| 8 | [Flight path planning of UAV-driven refinement inspection for construction sites based on 3D reconstruction](https://doi.org/10.1016/j.autcon.2025.106360) | 2025 | 1 | 1 | Automation in Construction | Jian Liu, Wen Yi, Penglu Chen, et al. |
| 9 | [Delay-prioritized and Reliable Task Scheduling with Long-term Load Balancing in Computing Power Networks](https://doi.org/10.1109/tsc.2024.3495500) | 2024 | 1 | 1 | IEEE Transactions on Services Computing | Renchao Xie, Feng Li, Qinqin Tang, et al. |
| 10 | [THE ROLE OF SMART CITY APPLICATIONS IN MIGRATION MANAGEMENT: OPEN DATA AND GEOGRAPHICAL INFORMATION SYSTEMS](https://doi.org/10.53092/duiibfd.1129085) | 2022 | 1 | 0 | Dicle Üniversitesi İktisadi ve İdari Bilimler Fakültesi Dergisi | Yakup Bulut, Muhammed Miraç ASLAN |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Multi-UAV path planning for multiple emergency payloads delivery in natural disaster scenarios](https://doi.org/10.1016/j.jnlest.2025.100303) | 2025 | 1 | 1 | Journal of Electronic Science and Technology | Zarina Kutpanova, Mustafa Raad Kadhim, Xu Zheng, et al. |
| 2 | [Collaborative Coverage Path Planning for UAV Swarm for Multi-region Post-Disaster Assessment](https://doi.org/10.1016/j.vehcom.2025.100915) | 2025 | 1 | 1 | Vehicular Communications | Yonghua Xiong, Yan Zhou, Jinhua She, et al. |
| 3 | [Adaptive multi-UAV cooperative path planning based on novel rotation artificial potential fields](https://doi.org/10.1016/j.knosys.2025.113429) | 2025 | 1 | 1 | Knowledge-Based Systems | Huidong Liu, Xianlei Long, Yong Li, et al. |
| 4 | [Performance enhancement of UAV-enabled MEC systems through intelligent task offloading and resource allocation](https://doi.org/10.1016/j.comnet.2025.111280) | 2025 | 1 | 1 | Computer Networks | Mohsen Darchini-Tabrizi, Amirali Pakdaman-Donyavi, Reza Entezari‐Maleki, et al. |
| 5 | [UAV-Supported Communication: Current and Prospective Solutions](https://doi.org/10.1016/j.vehcom.2025.100923) | 2025 | 1 | 1 | Vehicular Communications | Moayad Aloqaily, Ouns Bouachir, Ismaeel Al Ridhawi |
| 6 | [Deep learning-enhanced safety system for real-time in-situ blade damage monitoring in UAV using triboelectric sensor](https://doi.org/10.1016/j.nanoen.2025.111063) | 2025 | 1 | 1 | Nano Energy | Zhipeng Pan, Kuankuan Wang, Yixin Liu, et al. |
| 7 | [The development of distributed cooperative localization algorithms for multi-UAV systems in the past decade](https://doi.org/10.1016/j.measurement.2025.118040) | 2025 | 1 | 1 | Measurement | Zhaoyu Zhang, Nan Li, Gongmin Yan, et al. |
| 8 | [Flight path planning of UAV-driven refinement inspection for construction sites based on 3D reconstruction](https://doi.org/10.1016/j.autcon.2025.106360) | 2025 | 1 | 1 | Automation in Construction | Jian Liu, Wen Yi, Penglu Chen, et al. |
| 9 | [Security and privacy consideration for the deployment of electronic health records: a qualitative study covering Greece and Oman](https://doi.org/10.1080/19393555.2021.2003914) | 2021 | 1 | 1 | Information Security Journal A Global Perspective | Ourania Koutzampasopoulou Xanthidou, Dimitrios Xanthidis, Christos Manolas, et al. |
| 10 | [Delay-prioritized and Reliable Task Scheduling with Long-term Load Balancing in Computing Power Networks](https://doi.org/10.1109/tsc.2024.3495500) | 2024 | 1 | 1 | IEEE Transactions on Services Computing | Renchao Xie, Feng Li, Qinqin Tang, et al. |
<!-- TRENDING-END -->
