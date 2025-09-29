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

Last update: 2025-09-29 06:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://doi.org/10.1007/978-3-319-24574-4_28) | 2015 | 19 | 74220 | Lecture notes in computer science | Olaf Ronneberger, Philipp Fischer, Thomas Brox |
| 2 | [nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation](https://doi.org/10.1038/s41592-020-01008-z) | 2020 | 10 | 5848 | Nature Methods | Fabian Isensee, Paul F. Jaeger, Simon Köhl, et al. |
| 3 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 9 | 149978 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 4 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 9 | 194890 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 5 | [MIMIC-CXR, a de-identified publicly available database of chest radiographs with free-text reports](https://doi.org/10.1038/s41597-019-0322-0) | 2019 | 8 | 1153 | Scientific Data | Alistair E. W. Johnson, Tom Pollard, Seth J. Berkowitz, et al. |
| 6 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 79780 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 7 | [Greek laughter and the problem of the absurd](https://doi.org/10.1017/cbo9780511483004.009) | 2008 | 7 | 5 | Cambridge University Press eBooks | Stephen Halliwell |
| 8 | [VERBAL INSULTING IN ANCIENT GREEK CULTURE](https://doi.org/10.1556/aant.40.2000.1-4.7) | 2000 | 7 | 5 | Acta Antiqua Academiae Scientiarum Hungaricae | Jan Ν. Bremmer |
| 9 | [Ancient Critics of Greek Sport](https://doi.org/10.1002/9781118609965.ch21) | 2013 | 7 | 7 |  | Zinon Papakonstantinou |
| 10 | [IMPLIED VENGEANCE IN THE SIMILE OF GRIEVING VULTURES (<i>ODYSSEY</i> 16.216–19)](https://doi.org/10.1017/s0009838806000012) | 2006 | 7 | 7 | The Classical Quarterly | Naomi Rood |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 96 | 109434 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 24 | 24946 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 22 | 30354 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 4 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 21 | 12330 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 5 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 20 | 6484 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 20 | 71274 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 19 | 6071 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [limma powers differential expression analyses for RNA-sequencing and microarray studies](https://doi.org/10.1093/nar/gkv007) | 2015 | 18 | 34270 | Nucleic Acids Research | Matthew E. Ritchie, Belinda Phipson, Di Wu, et al. |
| 9 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 18 | 194890 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 10 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 16 | 13759 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 16 | 13759 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Machine Learning Implementation in Membrane Bioreactor Systems: Progress, Challenges, and Future Perspectives: A Review](https://doi.org/10.3390/environments10070127) | 2023 | 7 | 21 | Environments | Zacharias Frontistis, Grigoris Lykogiannis, Anastasios Sarmpanis |
| 3 | [Revolutionizing healthcare: the role of artificial intelligence in clinical practice](https://doi.org/10.1186/s12909-023-04698-z) | 2023 | 7 | 1629 | BMC Medical Education | Shuroug A. Alowais, Sahar S. Alghamdi, Nada Alsuhebany, et al. |
| 4 | [Understanding and Designing a High-Performance Ultrafiltration Membrane Using Machine Learning](https://doi.org/10.1021/acs.est.2c05404) | 2023 | 6 | 60 | Environmental Science & Technology | Haiping Gao, Shifa Zhong, Raghav Dangayach, et al. |
| 5 | [Investigation of performance metrics in regression analysis and machine learning-based prediction models](https://doi.org/10.23967/eccomas.2022.155) | 2022 | 5 | 129 | 8th European Congress on Computational Methods in Applied Sciences and Engineering | V. Plevris, G. Solorzano, N. Bakas, et al. |
| 6 | [PubChem 2025 update](https://doi.org/10.1093/nar/gkae1059) | 2024 | 5 | 210 | Nucleic Acids Research | Sunghwan Kim, Jie Chen, Tiejun Cheng, et al. |
| 7 | [Ensemble deep learning: A review](https://doi.org/10.1016/j.engappai.2022.105151) | 2022 | 5 | 1477 | Engineering Applications of Artificial Intelligence | M. A. Ganaie, Minghui Hu, A. K. Malik, et al. |
| 8 | [Software update: The <scp>ORCA</scp> program system—Version 5.0](https://doi.org/10.1002/wcms.1606) | 2022 | 5 | 2991 | Wiley Interdisciplinary Reviews Computational Molecular Science | Frank Neese |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Multiscale computational modeling of organic compounds separation using microporous membranes](https://doi.org/10.5004/dwt.2019.23502) | 2019 | 5 | 1 | Desalination and Water Treatment | Mashallah Rezakazemi, Saeed Shirazian |
| 2 | [Machine Learning Implementation in Membrane Bioreactor Systems: Progress, Challenges, and Future Perspectives: A Review](https://doi.org/10.3390/environments10070127) | 2023 | 7 | 21 | Environments | Zacharias Frontistis, Grigoris Lykogiannis, Anastasios Sarmpanis |
| 3 | [Understanding and Designing a High-Performance Ultrafiltration Membrane Using Machine Learning](https://doi.org/10.1021/acs.est.2c05404) | 2023 | 6 | 60 | Environmental Science & Technology | Haiping Gao, Shifa Zhong, Raghav Dangayach, et al. |
| 4 | [Sustainable MXenes-based membranes for highly energy-efficient separations](https://doi.org/10.1016/j.rser.2021.110878) | 2021 | 5 | 61 | Renewable and Sustainable Energy Reviews | Mashallah Rezakazemi, Ahmad Arabi Shamsabadi, Haiqing Lin, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 20 | 13751 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 9 | 1853 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1086 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 8 | 2749 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 5 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://doi.org/10.48550/arxiv.1910.10683) | 2019 | 8 | 8474 | arXiv (Cornell University) | Colin Raffel, Noam Shazeer, Adam Roberts, et al. |
| 6 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 8 | 20022 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 7 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 8 | 61725 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 8 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 1541 | arXiv (Cornell University) | OpenAI |
| 9 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 1764 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 10 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 1921 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 9 | 1853 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 2 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1086 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 3 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 8 | 2749 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 1541 | arXiv (Cornell University) | OpenAI |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 1764 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 1921 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [A Review on Large Language Models: Architectures, Applications, Taxonomies, Open Issues and Challenges](https://doi.org/10.1109/access.2024.3365742) | 2024 | 5 | 253 | IEEE Access | Mohaimenul Azam Khan Raiaan, Md. Saddam Hossain Mukta, Kaniz Fatema, et al. |
| 8 | [Lost in the Middle: How Language Models Use Long Contexts](https://doi.org/10.1162/tacl_a_00638) | 2024 | 5 | 333 | Transactions of the Association for Computational Linguistics | Nelson F. Liu, Kevin Lin, John Hewitt, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 5 | 389 | ACM transactions on office information systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing](https://doi.org/10.1145/3613904.3642016) | 2024 | 4 | 61 |  | Ian Arawjo, Chelse Swoopes, Priyan Vaithilingam, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Humans or LLMs as the Judge? A Study on Judgement Bias](https://doi.org/10.18653/v1/2024.emnlp-main.474) | 2024 | 3 | 9 | Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing | Guiming Hardy Chen, Shunian Chen, Ziche Liu, et al. |
| 2 | [Retrieval augmented generation for 10 large language models and its generalizability in assessing medical fitness](https://doi.org/10.1038/s41746-025-01519-z) | 2025 | 3 | 17 | npj Digital Medicine | Yu He Ke, Liyuan Jin, Kabilan Elangovan, et al. |
| 3 | [EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria](https://doi.org/10.1145/3613904.3642216) | 2024 | 3 | 26 |  | Tae Soo Kim, Yoonjoo Lee, Jamin Shin, et al. |
| 4 | [A Comprehensive Overview of Large Language Models](https://doi.org/10.1145/3744746) | 2025 | 3 | 40 | ACM Transactions on Intelligent Systems and Technology | Humza Naveed, Asad Ullah Khan, Shi Qiu, et al. |
| 5 | [ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing](https://doi.org/10.1145/3613904.3642016) | 2024 | 4 | 61 |  | Ian Arawjo, Chelse Swoopes, Priyan Vaithilingam, et al. |
| 6 | [LLaVA-MR: Large Language-and-Vision Assistant for Video Moment Retrieval](https://doi.org/10.32388/vlxb6m) | 2024 | 3 | 46 |  | Jianping Li |
| 7 | [Assessing ChatGPT 4.0’s test performance and clinical diagnostic accuracy on USMLE STEP 2 CK and clinical case reports](https://doi.org/10.1038/s41598-024-58760-x) | 2024 | 3 | 57 | Scientific Reports | Allen Shieh, Brandon Q. Tran, Gene He, et al. |
| 8 | [Prediction during language comprehension: what is next?](https://doi.org/10.1016/j.tics.2023.08.003) | 2023 | 3 | 63 | Trends in Cognitive Sciences | Rachel Ryskin, Mante S. Nieuwland |
| 9 | [MEDITRON-70B: Scaling Medical Pretraining for Large Language Models](https://doi.org/10.48550/arxiv.2311.16079) | 2023 | 3 | 67 | arXiv (Cornell University) | Zeming Chen, A. Cano, Angelika Romanou, et al. |
| 10 | [Large language models and their impact in ophthalmology](https://doi.org/10.1016/s2589-7500(23)00201-7) | 2023 | 3 | 84 | The Lancet Digital Health | Bjorn Kaijun Betzler, Haichao Chen, Ching‐Yu Cheng, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The coevolution mechanism of stakeholder strategies in the recycled resources industry innovation ecosystem: the view of evolutionary game theory](https://doi.org/10.1016/j.techfore.2022.121627) | 2022 | 2 | 64 | Technological Forecasting and Social Change | Xinyu Hao, Guangfu Liu, Xiaoling Zhang, et al. |
| 2 | [Global prevalence of gaming disorder: A systematic review and meta-analysis](https://doi.org/10.1177/0004867420962851) | 2020 | 2 | 612 | Australian & New Zealand Journal of Psychiatry | Matthew Stevens, Diana Dorstyn, Paul Delfabbro, et al. |
| 3 | [Game theory meets network security and privacy](https://doi.org/10.1145/2480741.2480742) | 2013 | 2 | 786 | ACM Computing Surveys | Mohammad Hossein Manshaei, Quanyan Zhu, Tansu Alpcan, et al. |
| 4 | [Towards a theory of ecosystems](https://doi.org/10.1002/smj.2904) | 2018 | 2 | 2497 | Strategic Management Journal | Michael G. Jacobides, Carmelo Cennamo, Annabelle Gawer |
| 5 | [Power failure: why small sample size undermines the reliability of neuroscience](https://doi.org/10.1038/nrn3475) | 2013 | 2 | 7227 | Nature reviews. Neuroscience | Katherine S. Button, John P. A. Ioannidis, Claire Mokrysz, et al. |
| 6 | [Intrinsic Motivation and Self-Determination in Human Behavior](https://doi.org/10.1007/978-1-4899-2271-7) | 1985 | 2 | 24108 | Springer eBooks | Edward L. Deci, Richard M. Ryan |
| 7 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 2 | 58131 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 8 | [A Game Theory Approach to Preserve Privacy in Hospital Management System](https://doi.org/10.1109/icirca.2018.8597182) | 2018 | 1 | 1 | 2018 International Conference on Inventive Research in Computing Applications (ICIRCA) | D G Arpitha |
| 9 | [Privacy-Preserving Publishing of Individual-Level Pandemic Data Based on a Game Theoretic Model](https://doi.org/10.1109/bibm55620.2022.9995513) | 2022 | 1 | 1 | 2021 IEEE International Conference on Bioinformatics and Biomedicine (BIBM) | Abinitha Gourabathina, Zhiyu Wan, J Thomas Brown, et al. |
| 10 | [An Efficient and Secure Data Audit Scheme for Cloud-Based EHRs with Recoverable and Batch Auditing](https://doi.org/10.32604/cmc.2025.062910) | 2025 | 1 | 1 | Computers, materials & continua/Computers, materials & continua (Print) | Yuanhang Zhang, Xu An Wang, Weiwei Jiang, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The coevolution mechanism of stakeholder strategies in the recycled resources industry innovation ecosystem: the view of evolutionary game theory](https://doi.org/10.1016/j.techfore.2022.121627) | 2022 | 2 | 64 | Technological Forecasting and Social Change | Xinyu Hao, Guangfu Liu, Xiaoling Zhang, et al. |
| 2 | [Privacy-Preserving Publishing of Individual-Level Pandemic Data Based on a Game Theoretic Model](https://doi.org/10.1109/bibm55620.2022.9995513) | 2022 | 1 | 1 | 2021 IEEE International Conference on Bioinformatics and Biomedicine (BIBM) | Abinitha Gourabathina, Zhiyu Wan, J Thomas Brown, et al. |
| 3 | [An Efficient and Secure Data Audit Scheme for Cloud-Based EHRs with Recoverable and Batch Auditing](https://doi.org/10.32604/cmc.2025.062910) | 2025 | 1 | 1 | Computers, materials & continua/Computers, materials & continua (Print) | Yuanhang Zhang, Xu An Wang, Weiwei Jiang, et al. |
| 4 | [A Game-Theoretic Approach to Privacy-Utility Tradeoff in Sharing Genomic
  Summary Statistics](https://doi.org/10.48550/arxiv.2406.01811) | 2024 | 1 | 0 | arXiv (Cornell University) | Tao Zhang, Rajagopal Venkatesaramani, Rajat K. De, et al. |
| 5 | [The Role of Multi-Factor Authentication and Encryption in Securing Data Access of Cloud Resources in a Multitenant Environment](https://doi.org/10.2139/ssrn.5267886) | 2025 | 1 | 0 | SSRN Electronic Journal | Hardial Singh |
| 6 | [A game theoretic approach to balance privacy risks and familial benefits](https://doi.org/10.1038/s41598-023-33177-0) | 2023 | 1 | 2 | Scientific Reports | Jia Guo, Ellen Wright Clayton, Murat Kantarcıoǧlu, et al. |
| 7 | [PanDa Game: Optimized Privacy-Preserving Publishing of Individual-Level Pandemic Data Based on a Game Theoretic Model](https://doi.org/10.1109/tnb.2023.3284092) | 2023 | 1 | 2 | IEEE Transactions on NanoBioscience | Abinitha Gourabathina, Zhiyu Wan, J Thomas Brown, et al. |
| 8 | [Achieving sustainable medical tourism: unpacking privacy concerns through a tripartite game theoretic lens](https://doi.org/10.3389/fpubh.2024.1347231) | 2024 | 1 | 2 | Frontiers in Public Health | Ran Wang, Songtao Geng |
| 9 | [Cybersecurity Threats in Healthcare IT: Challenges, Risks, and Mitigation Strategies](https://doi.org/10.60087/jaigs.v6i1.268) | 2024 | 1 | 3 | Deleted Journal | Md Jawadur Rahim, Muhammad Abdur Rahim, Ahlina Afroz, et al. |
| 10 | [Fuzzy ensemble-based federated learning for EEG-based emotion recognition in Internet of Medical Things](https://doi.org/10.1016/j.jii.2025.100789) | 2025 | 1 | 4 | Journal of Industrial Information Integration | Weiwei Jiang, Yang Zhang, Haoyu Han, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Game Theory Approach to Preserve Privacy in Hospital Management System](https://doi.org/10.1109/icirca.2018.8597182) | 2018 | 1 | 1 | 2018 International Conference on Inventive Research in Computing Applications (ICIRCA) | D G Arpitha |
| 2 | [Privacy-Preserving Publishing of Individual-Level Pandemic Data Based on a Game Theoretic Model](https://doi.org/10.1109/bibm55620.2022.9995513) | 2022 | 1 | 1 | 2021 IEEE International Conference on Bioinformatics and Biomedicine (BIBM) | Abinitha Gourabathina, Zhiyu Wan, J Thomas Brown, et al. |
| 3 | [An Efficient and Secure Data Audit Scheme for Cloud-Based EHRs with Recoverable and Batch Auditing](https://doi.org/10.32604/cmc.2025.062910) | 2025 | 1 | 1 | Computers, materials & continua/Computers, materials & continua (Print) | Yuanhang Zhang, Xu An Wang, Weiwei Jiang, et al. |
| 4 | [A Personalization-Privacy Paradox in Usage of Mobile Health Services: A Game Theoretic Perspective](https://openalex.org/W2887949638) | 2018 | 1 | 0 | WHICEB | Fanbo Meng, Xitong Guo, Kee‐hung Lai, et al. |
| 5 | [A Game-Theoretic Approach to Privacy-Utility Tradeoff in Sharing Genomic
  Summary Statistics](https://doi.org/10.48550/arxiv.2406.01811) | 2024 | 1 | 0 | arXiv (Cornell University) | Tao Zhang, Rajagopal Venkatesaramani, Rajat K. De, et al. |
| 6 | [The Role of Multi-Factor Authentication and Encryption in Securing Data Access of Cloud Resources in a Multitenant Environment](https://doi.org/10.2139/ssrn.5267886) | 2025 | 1 | 0 | SSRN Electronic Journal | Hardial Singh |
| 7 | [Socio-Cultural Interpretations to the Diffusion and Use of Broadband Services in a Korean Digital Society](https://doi.org/10.4018/978-1-87828-991-9.ch075) | 2009 | 1 | 0 | Human computer interaction. | Dal Jin Yong |
| 8 | [A game theoretic approach to balance privacy risks and familial benefits](https://doi.org/10.1038/s41598-023-33177-0) | 2023 | 1 | 2 | Scientific Reports | Jia Guo, Ellen Wright Clayton, Murat Kantarcıoǧlu, et al. |
| 9 | [PanDa Game: Optimized Privacy-Preserving Publishing of Individual-Level Pandemic Data Based on a Game Theoretic Model](https://doi.org/10.1109/tnb.2023.3284092) | 2023 | 1 | 2 | IEEE Transactions on NanoBioscience | Abinitha Gourabathina, Zhiyu Wan, J Thomas Brown, et al. |
| 10 | [Achieving sustainable medical tourism: unpacking privacy concerns through a tripartite game theoretic lens](https://doi.org/10.3389/fpubh.2024.1347231) | 2024 | 1 | 2 | Frontiers in Public Health | Ran Wang, Songtao Geng |
<!-- TRENDING-END -->
