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

Last update: 2025-08-18 06:24 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 20 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 19 | 55181 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 11 | 147595 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 4 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 10 | 91039 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |
| 5 | [Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR and the 2−ΔΔCT Method](https://doi.org/10.1006/meth.2001.1262) | 2001 | 10 | 164306 | Methods | Kenneth J. Livak, Thomas D. Schmittgen |
| 6 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 9 | 33158 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |
| 7 | [The PHQ-9](https://doi.org/10.1046/j.1525-1497.2001.016009606.x) | 2001 | 9 | 37659 | Journal of General Internal Medicine | Kurt Kroenke, Robert L. Spitzer, Janet B. W. Williams |
| 8 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 9 | 107723 | Machine Learning | Leo Breiman |
| 9 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 7 | 4708 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 10 | [The REDCap consortium: Building an international community of software platform partners](https://doi.org/10.1016/j.jbi.2019.103208) | 2019 | 7 | 17946 | Journal of Biomedical Informatics | Paul A. Harris, Robert J. Taylor, Brenda L. Minor, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 68 | 107723 | Machine Learning | Leo Breiman |
| 2 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 17 | 5561 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 16 | 24495 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 14 | 70108 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 5 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 12 | 11926 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 6 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 12 | 192837 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 7 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 9 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 8 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 9 | 30050 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 9 | [limma powers differential expression analyses for RNA-sequencing and microarray studies](https://doi.org/10.1093/nar/gkv007) | 2015 | 9 | 33734 | Nucleic Acids Research | Matthew E. Ritchie, Belinda Phipson, Di Wu, et al. |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 9 | 85022 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 9 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Identification and validation of an explainable prediction model of acute kidney injury with prognostic implications in critically ill children: a prospective multicenter cohort study](https://doi.org/10.1016/j.eclinm.2023.102409) | 2024 | 5 | 90 | EClinicalMedicine | Junlong Hu, Jing Xu, Min Li, et al. |
| 3 | [Applications of Artificial Neural Networks and Machine Learning in Civil Engineering](https://doi.org/10.1007/978-3-031-66051-1) | 2024 | 5 | 153 | Studies in computational intelligence | A. Kaveh |
| 4 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 4 | 342 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Identification and validation of an explainable prediction model of acute kidney injury with prognostic implications in critically ill children: a prospective multicenter cohort study](https://doi.org/10.1016/j.eclinm.2023.102409) | 2024 | 5 | 90 | EClinicalMedicine | Junlong Hu, Jing Xu, Min Li, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 11 | 13449 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 1667 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Explainability for Large Language Models: A Survey](https://doi.org/10.1145/3639372) | 2024 | 6 | 232 | ACM Transactions on Intelligent Systems and Technology | Haiyan Zhao, Hanjie Chen, Fan Yang, et al. |
| 4 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 4 | 89 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 5 | [Challenges and barriers of using large language models (LLM) such as ChatGPT for diagnostic medicine with a focus on digital pathology – a recent scoping review](https://doi.org/10.1186/s13000-024-01464-7) | 2024 | 4 | 112 | Diagnostic Pathology | Ehsan Ullah, Anil V. Parwani, Mirza Mansoor Baig, et al. |
| 6 | [A Survey on Multimodal Large Language Models](https://doi.org/10.1093/nsr/nwae403) | 2024 | 4 | 143 | National Science Review | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 7 | [Bias and Fairness in Large Language Models: A Survey](https://doi.org/10.1162/coli_a_00524) | 2024 | 4 | 153 | Computational Linguistics | Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, et al. |
| 8 | [A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly](https://doi.org/10.1016/j.hcc.2024.100211) | 2024 | 4 | 308 | High-Confidence Computing | Yifan Yao, Jinhao Duan, Kaidi Xu, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 4 | 992 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 4 | 1478 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 9 | 1667 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Explainability for Large Language Models: A Survey](https://doi.org/10.1145/3639372) | 2024 | 6 | 232 | ACM Transactions on Intelligent Systems and Technology | Haiyan Zhao, Hanjie Chen, Fan Yang, et al. |
| 3 | [Testing and Evaluation of Health Care Applications of Large Language Models](https://doi.org/10.1001/jama.2024.21700) | 2024 | 4 | 89 | JAMA | Suhana Bedi, Yutong Liu, Lucy Orr-Ewing, et al. |
| 4 | [Challenges and barriers of using large language models (LLM) such as ChatGPT for diagnostic medicine with a focus on digital pathology – a recent scoping review](https://doi.org/10.1186/s13000-024-01464-7) | 2024 | 4 | 112 | Diagnostic Pathology | Ehsan Ullah, Anil V. Parwani, Mirza Mansoor Baig, et al. |
| 5 | [A Survey on Multimodal Large Language Models](https://doi.org/10.1093/nsr/nwae403) | 2024 | 4 | 143 | National Science Review | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 6 | [Bias and Fairness in Large Language Models: A Survey](https://doi.org/10.1162/coli_a_00524) | 2024 | 4 | 153 | Computational Linguistics | Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, et al. |
| 7 | [A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly](https://doi.org/10.1016/j.hcc.2024.100211) | 2024 | 4 | 308 | High-Confidence Computing | Yifan Yao, Jinhao Duan, Kaidi Xu, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 4 | 992 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 4 | 1478 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 10 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 4 | 2567 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Ensuring Transparency and Fairness in AI DecisionMaking Processes Influenced by large language Models](https://doi.org/10.1109/csnt60213.2024.10545998) | 2024 | 2 | 1 | 2022 IEEE 11th International Conference on Communication Systems and Network Technologies (CSNT) | Dheeraj Singh, K. I. Pavan Kumar, Ginni Nijhawan, et al. |
| 2 | [On the reliability of Large Language Models to misinformed and demographically informed prompts](https://doi.org/10.1002/aaai.12208) | 2025 | 2 | 0 | AI Magazine | Toluwani Aremu, Oluwakemi Akinwehinmi, Chukwuemeka Nwagu, et al. |
| 3 | [ChatGPT in Education: A Review of Ethical Challenges and Approaches to Enhancing Transparency and Privacy](https://doi.org/10.1016/j.procs.2025.02.077) | 2025 | 2 | 4 | Procedia Computer Science | Ibomoiye Domor Mienye, Theo G. Swart |
| 4 | [Findings of the Association for Computational Linguistics: NAACL 2025](https://doi.org/10.18653/v1/2025.findings-naacl) | 2025 | 2 | 14 | Findings of the Association for Computational Linguistics: NAACL 2022 | Unknown |
| 5 | [Sentiment analysis of the United States public support of nuclear power on social media using large language models](https://doi.org/10.1016/j.rser.2024.114570) | 2024 | 2 | 15 | Renewable and Sustainable Energy Reviews | O. Hwang Kwon, Katie Vu, Naman Bhargava, et al. |
| 6 | [Implementing large language models in healthcare while balancing control, collaboration, costs and security](https://doi.org/10.1038/s41746-025-01476-7) | 2025 | 2 | 15 | npj Digital Medicine | Fabio Dennstädt, Janna Hastings, Paul Martin Putora, et al. |
| 7 | [Large Language Model–Based Responses to Patients’ In-Basket Messages](https://doi.org/10.1001/jamanetworkopen.2024.22399) | 2024 | 2 | 32 | JAMA Network Open | William Small, Batia M. Wiesenfeld, Beatrix Brandfield-Harvey, et al. |
| 8 | [Evaluating the Application of Large Language Models in Clinical Research Contexts](https://doi.org/10.1001/jamanetworkopen.2023.35924) | 2023 | 2 | 37 | JAMA Network Open | Roy H. Perlis, Stephan D. Fihn |
| 9 | [LLaMA-Reviewer: Advancing Code Review Automation with Large Language Models through Parameter-Efficient Fine-Tuning](https://doi.org/10.1109/issre59848.2023.00026) | 2023 | 2 | 38 |  | Junyi Lu, Lei Yu, LI Xiao-jia, et al. |
| 10 | [Security and Privacy Challenges of Large Language Models: A Survey](https://doi.org/10.1145/3712001) | 2025 | 2 | 44 | ACM Computing Surveys | Badhan Chandra Das, M. Hadi Amini, Yanzhao Wu |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Logic of Animal Conflict](https://doi.org/10.1038/246015a0) | 1973 | 2 | 5993 | Nature | John Maynard Smith, George Price |
| 2 | [Evolution and the Theory of Games](https://doi.org/10.1017/cbo9780511806292) | 1982 | 2 | 6711 |  | John Maynard Smith |
| 3 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 2 | 11926 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 4 | [Emergence of Scaling in Random Networks](https://doi.org/10.1126/science.286.5439.509) | 1999 | 2 | 35196 | Science | Albert‐László Barabási, Réka Albert |
| 5 | [A tournament theory of congressional committee leadership](https://doi.org/10.1007/s11127-024-01184-y) | 2024 | 1 | 1 | Public Choice | Christian Fong, Joshua McCrain |
| 6 | [Tullock contest alliances with proportional prize-sharing agreements: private collective action mechanisms?](https://doi.org/10.1007/s11127-024-01219-4) | 2024 | 1 | 1 | Public Choice | James W. Boudreau, Shane Sanders |
| 7 | [Income and the (eventual) rise of democracy](https://doi.org/10.1007/s11127-025-01268-3) | 2025 | 1 | 1 | Public Choice | Darío Debowicz, Alex Dickson, Ian A. MacKenzie, et al. |
| 8 | [Automated Detection of Intracranial Hemorrhage using Convolutional Neural Networks](https://doi.org/10.1109/ieeeconf61558.2024.10585483) | 2024 | 1 | 1 |  | Pritam Chakraborty, Anjan Bandyopadhyay, Mukul Misra, et al. |
| 9 | [Effort comparisons for a class of four-player tournaments](https://doi.org/10.1007/s00355-021-01381-4) | 2022 | 1 | 2 | Social Choice and Welfare | Deren Çağlayan, Emin Karagözoğlu, Kerim Keskin, et al. |
| 10 | [Bargaining in the shadow of conflict: resource division and War’s Inefficiency Puzzle in the commons](https://doi.org/10.1007/s11127-023-01074-9) | 2023 | 1 | 2 | Public Choice | Jeremy Kettering, Shane Sanders |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A tournament theory of congressional committee leadership](https://doi.org/10.1007/s11127-024-01184-y) | 2024 | 1 | 1 | Public Choice | Christian Fong, Joshua McCrain |
| 2 | [Tullock contest alliances with proportional prize-sharing agreements: private collective action mechanisms?](https://doi.org/10.1007/s11127-024-01219-4) | 2024 | 1 | 1 | Public Choice | James W. Boudreau, Shane Sanders |
| 3 | [Income and the (eventual) rise of democracy](https://doi.org/10.1007/s11127-025-01268-3) | 2025 | 1 | 1 | Public Choice | Darío Debowicz, Alex Dickson, Ian A. MacKenzie, et al. |
| 4 | [Automated Detection of Intracranial Hemorrhage using Convolutional Neural Networks](https://doi.org/10.1109/ieeeconf61558.2024.10585483) | 2024 | 1 | 1 |  | Pritam Chakraborty, Anjan Bandyopadhyay, Mukul Misra, et al. |
| 5 | [Effort comparisons for a class of four-player tournaments](https://doi.org/10.1007/s00355-021-01381-4) | 2022 | 1 | 2 | Social Choice and Welfare | Deren Çağlayan, Emin Karagözoğlu, Kerim Keskin, et al. |
| 6 | [Bargaining in the shadow of conflict: resource division and War’s Inefficiency Puzzle in the commons](https://doi.org/10.1007/s11127-023-01074-9) | 2023 | 1 | 2 | Public Choice | Jeremy Kettering, Shane Sanders |
| 7 | [Intelligent Stroke Disease Prediction Model Using Deep Learning Approaches](https://doi.org/10.1155/2024/4523388) | 2024 | 1 | 2 | Stroke Research and Treatment | Chunhua Gao, H. J. Wang |
| 8 | [Predicting stroke occurrences: a stacked machine learning approach with feature selection and data preprocessing](https://doi.org/10.1186/s12859-024-05866-8) | 2024 | 1 | 6 | BMC Bioinformatics | Pritam Chakraborty, Anjan Bandyopadhyay, Preeti Ranjan Sahu, et al. |
| 9 | [Simulated Quantum Mechanics-Based Joint Learning Network for Stroke Lesion Segmentation and TICI Grading](https://doi.org/10.1109/jbhi.2023.3270861) | 2023 | 1 | 11 | IEEE Journal of Biomedical and Health Informatics | Liangliang Liu, Chang Jing, Gongbo Liang, et al. |
| 10 | [Predicting the Internal Knee Abduction Impulse During Walking Using Deep Learning](https://doi.org/10.3389/fbioe.2022.877347) | 2022 | 1 | 12 | Frontiers in Bioengineering and Biotechnology | Issam Boukhennoufa, Zainab Altai, Xiaojun Zhai, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A tournament theory of congressional committee leadership](https://doi.org/10.1007/s11127-024-01184-y) | 2024 | 1 | 1 | Public Choice | Christian Fong, Joshua McCrain |
| 2 | [Tullock contest alliances with proportional prize-sharing agreements: private collective action mechanisms?](https://doi.org/10.1007/s11127-024-01219-4) | 2024 | 1 | 1 | Public Choice | James W. Boudreau, Shane Sanders |
| 3 | [Income and the (eventual) rise of democracy](https://doi.org/10.1007/s11127-025-01268-3) | 2025 | 1 | 1 | Public Choice | Darío Debowicz, Alex Dickson, Ian A. MacKenzie, et al. |
| 4 | [Automated Detection of Intracranial Hemorrhage using Convolutional Neural Networks](https://doi.org/10.1109/ieeeconf61558.2024.10585483) | 2024 | 1 | 1 |  | Pritam Chakraborty, Anjan Bandyopadhyay, Mukul Misra, et al. |
| 5 | [Effort comparisons for a class of four-player tournaments](https://doi.org/10.1007/s00355-021-01381-4) | 2022 | 1 | 2 | Social Choice and Welfare | Deren Çağlayan, Emin Karagözoğlu, Kerim Keskin, et al. |
| 6 | [Bargaining in the shadow of conflict: resource division and War’s Inefficiency Puzzle in the commons](https://doi.org/10.1007/s11127-023-01074-9) | 2023 | 1 | 2 | Public Choice | Jeremy Kettering, Shane Sanders |
| 7 | [Intelligent Stroke Disease Prediction Model Using Deep Learning Approaches](https://doi.org/10.1155/2024/4523388) | 2024 | 1 | 2 | Stroke Research and Treatment | Chunhua Gao, H. J. Wang |
| 8 | [“The ball is round, the game lasts 90 minutes, everything else is pure theory”](https://doi.org/10.1177/1527002520939614) | 2020 | 1 | 4 | Journal of Sports Economics | Peter‐J. Jost |
| 9 | [A Clustered Routing Algorithm Based on Depth and Energy for Three-Dimensional Underwater Sensor Networks](https://openalex.org/W2377660645) | 2015 | 1 | 4 | Deleted Journal | Yin Zhang⋆ |
| 10 | [A Novel Matching Framework For One-Sided Markets In Fog Computing](https://openalex.org/W3112576362) | 2020 | 1 | 5 | International Journal of Computing and Digital Systems | Prarena Shroff, Anjan Bandyopadhyay |
<!-- TRENDING-END -->
