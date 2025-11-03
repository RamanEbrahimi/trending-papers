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

Last update: 2025-11-03 06:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Archivación digital de memorias colectivas en la diaspora chilena-estadounidense Recordándose al Chile de Pinochet en línea](https://doi.org/10.46530/virtualis.v13i25.410) | 2022 | 11 | 2 | Virtualis | Maxim Karagodin |
| 2 | [Individual, yet collective voices: polyphonic poetic memories in contemporary Ukrainian literature](https://doi.org/10.1080/00085006.2019.1708532) | 2020 | 11 | 3 | Canadian Slavonic Papers | Alessandro Achilli |
| 3 | [The Story of Carora: The Origins of El Sistema](https://doi.org/10.1177/0255761415617926) | 2015 | 11 | 9 | International Journal of Music Education | Alexandra Carlson |
| 4 | [Transitional Justice ‘From Within’: Police, Forensic and Legal Actors Searching for Chile’s Disappeared](https://doi.org/10.1093/jhuman/huy003) | 2018 | 11 | 9 | Journal of Human Rights Practice | Cath Collins |
| 5 | [Ethical review and qualitative research competence: Guidance for reviewers and applicants](https://doi.org/10.1177/1747016116677636) | 2016 | 11 | 12 | Research Ethics | Julie Mooney‐Somers, Anna Olsen |
| 6 | [‘They were drinking, singing, and shooting’: Singing and the Holocaust in the USSR](https://doi.org/10.21039/85) | 2021 | 11 | 12 | Journal of Perpetrator Research | Alexandra Birch |
| 7 | [Refugees, Refuge and Human Displacement](https://doi.org/10.2307/j.ctv32r02x2) | 2022 | 11 | 12 |  | Unknown |
| 8 | [Thinking about Music from Latin America](https://doi.org/10.5040/9781978735903) | 2018 | 11 | 12 | Lexington Books | Juan Pablo González |
| 9 | [Militant Song Movement in Latin America](https://doi.org/10.5040/9781978737129) | 2014 | 11 | 12 |  | Unknown |
| 10 | [Knowing the Suffering of Others](https://doi.org/10.2307/jj.30297235) | 2014 | 11 | 12 |  | Unknown |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 113 | 110978 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 45 | 25350 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 30 | 7078 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 4 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 27 | 12749 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 25 | 72044 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 23 | 19899 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 23 | 26660 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 21 | 6277 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 9 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 21 | 30746 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 21 | 86998 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 12 | 15024 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 7 | 1171 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Improved Baselines with Visual Instruction Tuning](https://doi.org/10.1109/cvpr52733.2024.02484) | 2024 | 16 | 436 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Haotian Liu, Chunyuan Li, Yuheng Li, et al. |
| 2 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 15 | 2855 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 3 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 15 | 14029 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 4 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1198 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 1878 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [LoRA: Low-Rank Adaptation of Large Language Models](https://doi.org/10.48550/arxiv.2106.09685) | 2021 | 12 | 1979 | arXiv (Cornell University) | J. Edward Hu, Yelong Shen, Phillip Wallis, et al. |
| 7 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 2043 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 8 | [Proceedings of the 32nd ACM International Conference on Multimedia](https://doi.org/10.1145/3664647) | 2024 | 11 | 539 |  | Qihe Pan, Zhen Zhao, Zicheng Wang, et al. |
| 9 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://doi.org/10.48550/arxiv.2005.11401) | 2020 | 10 | 2036 | arXiv (Cornell University) | Patrick Lewis, Ethan Perez, Aleksandara Piktus, et al. |
| 10 | [Advances in Neural Information Processing Systems 19](https://doi.org/10.7551/mitpress/7503.001.0001) | 2007 | 10 | 16031 | The MIT Press eBooks | Unknown |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Improved Baselines with Visual Instruction Tuning](https://doi.org/10.1109/cvpr52733.2024.02484) | 2024 | 16 | 436 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Haotian Liu, Chunyuan Li, Yuheng Li, et al. |
| 2 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 15 | 2855 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1198 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 1878 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 2043 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [Proceedings of the 32nd ACM International Conference on Multimedia](https://doi.org/10.1145/3664647) | 2024 | 11 | 539 |  | Qihe Pan, Zhen Zhao, Zicheng Wang, et al. |
| 7 | [Proceedings of the 31st ACM International Conference on Multimedia](https://doi.org/10.1145/3581783) | 2023 | 9 | 565 |  | Alejandro Jaimes, Nicu Sebe, Nozha Boujemaa, et al. |
| 8 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 8 | 1932 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 9 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 8 | 3094 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 10 | [OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://doi.org/10.1109/cvpr52733.2024.01274) | 2024 | 7 | 25 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Qidong Huang, Xiaoyi Dong, Pan Zhang, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding](https://doi.org/10.18653/v1/2024.findings-acl.937) | 2024 | 4 | 10 | Findings of the Association for Computational Linguistics: ACL 2022 | Xintong Wang, Jingheng Pan, Ding Liang, et al. |
| 2 | [Woodpecker: hallucination correction for multimodal large language models](https://doi.org/10.1007/s11432-024-4251-x) | 2024 | 4 | 13 | Science China Information Sciences | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 3 | [OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://doi.org/10.1109/cvpr52733.2024.01274) | 2024 | 7 | 25 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Qidong Huang, Xiaoyi Dong, Pan Zhang, et al. |
| 4 | [Development and evaluation of a large language model of ophthalmology in Chinese](https://doi.org/10.1136/bjo-2023-324526) | 2024 | 3 | 12 | British Journal of Ophthalmology | Ce Zheng, Hongfei Ye, Jinming Guo, et al. |
| 5 | [Q-Instruct: Improving Low-Level Visual Abilities for Multi-Modality Foundation Models](https://doi.org/10.1109/cvpr52733.2024.02408) | 2024 | 4 | 19 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Haoning Wu, Zicheng Zhang, Erli Zhang, et al. |
| 6 | [Evaluation of the accuracy and readability of ChatGPT-4 and Google Gemini in providing information on retinal detachment: a multicenter expert comparative study](https://doi.org/10.1186/s40942-024-00579-9) | 2024 | 3 | 16 | International Journal of Retina and Vitreous | Piotr Strzalkowski, Alicja Strzalkowska, Jay Chhablani, et al. |
| 7 | [A Survey of Multimodel Large Language Models](https://doi.org/10.1145/3672758.3672824) | 2024 | 4 | 29 |  | Zijing Liang, Yanjie Xu, Yifan Hong, et al. |
| 8 | [Qwen2.5-VL Technical Report](https://doi.org/10.48550/arxiv.2502.13923) | 2025 | 4 | 30 | arXiv (Cornell University) | Shuai Bai, Keqin Chen, Xuejing Liu, et al. |
| 9 | [The ethics of ChatGPT in medicine and healthcare: a systematic review on Large Language Models (LLMs)](https://doi.org/10.1038/s41746-024-01157-x) | 2024 | 3 | 50 | npj Digital Medicine | Joschka Haltaufderheide, Robert Ranisch |
| 10 | [Companion Proceedings of the ACM on Web Conference 2025](https://doi.org/10.1145/3701716) | 2025 | 4 | 68 |  | Unknown |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Educational Impact of a Comprehensive Serious Game within the University Setting: Improving Learning and Fostering Motivation](https://doi.org/10.1016/j.heliyon.2024.e35608) | 2024 | 2 | 5 | Heliyon | Lorena Rodríguez-Calzada, Maximiliano Paredes Velasco, Jaime Urquiza‐Fuentes |
| 2 | [Revealing the theoretical basis of gamification: A systematic review and analysis of theory in research on gamification, serious games and game-based learning](https://doi.org/10.1016/j.chb.2021.106963) | 2021 | 2 | 669 | Computers in Human Behavior | Jeanine Krath, Linda Schürmann, Harald F. O. von Korflesch |
| 3 | [On economic applications of evolutionary game theory](https://doi.org/10.1007/s001910050054) | 1998 | 2 | 809 | Journal of Evolutionary Economics | Daniel Friedman |
| 4 | [Evolutionary Games in Economics](https://doi.org/10.2307/2938222) | 1991 | 2 | 1769 | Econometrica | Daniel Friedman |
| 5 | [Purposive sampling: complex or simple? Research case examples](https://doi.org/10.1177/1744987120927206) | 2020 | 2 | 2296 | Journal of research in nursing | Steve Campbell, Melanie Greenwood, Sarah Prior, et al. |
| 6 | [The general problem of the stability of motion](https://doi.org/10.1080/00207179208934253) | 1992 | 2 | 2386 | International Journal of Control | A. M. Lyapunov |
| 7 | [Sentiment analysis algorithms and applications: A survey](https://doi.org/10.1016/j.asej.2014.04.011) | 2014 | 2 | 2931 | Ain Shams Engineering Journal | Walaa Medhat, Ahmed H. Yousef, Hoda Korashy |
| 8 | [The Motivational Pull of Video Games: A Self-Determination Theory Approach](https://doi.org/10.1007/s11031-006-9051-8) | 2006 | 2 | 3048 | Motivation and Emotion | Richard M. Ryan, C. Scott Rigby, Andrew K Przybylski |
| 9 | [Intrinsic and extrinsic motivation from a self-determination theory perspective: Definitions, theory, practices, and future directions](https://doi.org/10.1016/j.cedpsych.2020.101860) | 2020 | 2 | 3751 | Contemporary Educational Psychology | Richard M. Ryan, Edward L. Deci |
| 10 | [Game Theory](https://doi.org/10.1007/978-3-031-37574-3) | 2023 | 1 | 1 | Springer eBooks | Ana Espínola‐Arredondo, Félix Muñoz-García |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Educational Impact of a Comprehensive Serious Game within the University Setting: Improving Learning and Fostering Motivation](https://doi.org/10.1016/j.heliyon.2024.e35608) | 2024 | 2 | 5 | Heliyon | Lorena Rodríguez-Calzada, Maximiliano Paredes Velasco, Jaime Urquiza‐Fuentes |
| 2 | [Game Theory](https://doi.org/10.1007/978-3-031-37574-3) | 2023 | 1 | 1 | Springer eBooks | Ana Espínola‐Arredondo, Félix Muñoz-García |
| 3 | [Energy and throughput aware adequate routing for wireless sensor networks using integrated game theory method](https://doi.org/10.1038/s41598-024-71902-5) | 2024 | 1 | 1 | Scientific Reports | Vivek Kumar. M, O Saraniya |
| 4 | [GTD‐CER: Game‐Theoretic Dynamic Clustering for Enhanced Efficiency and Reliability in Wireless Sensor Networks](https://doi.org/10.1002/dac.6101) | 2025 | 1 | 0 | International Journal of Communication Systems | M. Vargheese, R. S. Sankarasubramanian, B. Vijayalakshmi, et al. |
| 5 | [Self-healing and energy-efficient cluster-based routing for sustainable wireless sensor networks](https://doi.org/10.3389/frcmn.2025.1602928) | 2025 | 1 | 0 | Frontiers in Communications and Networks | M. Gayathri, Vanapalli Veera Snigdha |
| 6 | [A conditional probabilistic deep learning approach for anomaly detection in structures under varying environmental conditions](https://doi.org/10.1016/j.ymssp.2025.113005) | 2025 | 1 | 2 | Mechanical Systems and Signal Processing | Yi-Kai Zhu, Hua‐Ping Wan, YingYing Ye, et al. |
| 7 | [The Dynamics of Rewards and Penalties: Governmental Impact on Green Packaging Adoption in Logistics](https://doi.org/10.3390/su16114835) | 2024 | 1 | 3 | Sustainability | Xingyi Yang, Xiaopei Dai, Bin Hou |
| 8 | [A BIM-GIS Integrated Database to Support Planned Maintenance Activities of Historical Built Heritage](https://doi.org/10.1007/978-3-030-94426-1_14) | 2022 | 1 | 5 | Communications in computer and information science | Elisabetta Colucci, Emmanuele Iacono, Francesca Matrone, et al. |
| 9 | [Designing Online Workshops for Teacher Trainees: Heritage Mapping with Web GIS Story Maps](https://doi.org/10.48088/ejg.c.mar.14.3.068.078) | 2023 | 1 | 5 | European Journal of Geography | Carlos Martínez Hernández, Radosław Piskorski, Arie Stoffelen |
| 10 | [Promoting Sponge City Construction through Rainwater Trading: An Evolutionary Game Theory-Based Analysis](https://doi.org/10.3390/w15040771) | 2023 | 1 | 6 | Water | Chun­yan Shi, Xinyue Miao, Tongyu Xu, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Game Theory](https://doi.org/10.1007/978-3-031-37574-3) | 2023 | 1 | 1 | Springer eBooks | Ana Espínola‐Arredondo, Félix Muñoz-García |
| 2 | [Voluntary Environmental Regulations and Firm Innovation in China](https://doi.org/10.20448/journal.501.2020.72.171.177) | 2020 | 1 | 1 | Asian Journal of Economics and Empirical Research | Shaojie Zhang |
| 3 | [Energy and throughput aware adequate routing for wireless sensor networks using integrated game theory method](https://doi.org/10.1038/s41598-024-71902-5) | 2024 | 1 | 1 | Scientific Reports | Vivek Kumar. M, O Saraniya |
| 4 | [GTD‐CER: Game‐Theoretic Dynamic Clustering for Enhanced Efficiency and Reliability in Wireless Sensor Networks](https://doi.org/10.1002/dac.6101) | 2025 | 1 | 0 | International Journal of Communication Systems | M. Vargheese, R. S. Sankarasubramanian, B. Vijayalakshmi, et al. |
| 5 | [Self-healing and energy-efficient cluster-based routing for sustainable wireless sensor networks](https://doi.org/10.3389/frcmn.2025.1602928) | 2025 | 1 | 0 | Frontiers in Communications and Networks | M. Gayathri, Vanapalli Veera Snigdha |
| 6 | [Does Environmental Regulation Indirectly Induce Upstream Innovation? New Evidence from India](https://doi.org/10.2139/ssrn.2664131) | 2015 | 1 | 2 | SSRN Electronic Journal | Pavel Chakraborty, Chirantan Chatterjee |
| 7 | [A conditional probabilistic deep learning approach for anomaly detection in structures under varying environmental conditions](https://doi.org/10.1016/j.ymssp.2025.113005) | 2025 | 1 | 2 | Mechanical Systems and Signal Processing | Yi-Kai Zhu, Hua‐Ping Wan, YingYing Ye, et al. |
| 8 | [The Educational Impact of a Comprehensive Serious Game within the University Setting: Improving Learning and Fostering Motivation](https://doi.org/10.1016/j.heliyon.2024.e35608) | 2024 | 2 | 5 | Heliyon | Lorena Rodríguez-Calzada, Maximiliano Paredes Velasco, Jaime Urquiza‐Fuentes |
| 9 | [The Dynamics of Rewards and Penalties: Governmental Impact on Green Packaging Adoption in Logistics](https://doi.org/10.3390/su16114835) | 2024 | 1 | 3 | Sustainability | Xingyi Yang, Xiaopei Dai, Bin Hou |
| 10 | [Field measurement of wind pressure on a large-scale spatial structure and comparison with wind tunnel test results](https://doi.org/10.1007/s13349-021-00477-w) | 2021 | 1 | 4 | Journal of Civil Structural Health Monitoring | Yaozhi Luo, Xuan Liu, Hua‐Ping Wan, et al. |
<!-- TRENDING-END -->
