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

Last update: 2025-08-25 06:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 14 | 12310 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 12 | 33590 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |
| 3 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 12 | 56244 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 4 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 10 | 148106 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 5 | [G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences](https://doi.org/10.3758/bf03193146) | 2007 | 9 | 55376 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Albert-Georg Lang, et al. |
| 6 | [IQ-TREE: A Fast and Effective Stochastic Algorithm for Estimating Maximum-Likelihood Phylogenies](https://doi.org/10.1093/molbev/msu300) | 2014 | 8 | 22095 | Molecular Biology and Evolution | Lam-Tung Nguyen, Heiko A. Schmidt, Arndt von Haeseler, et al. |
| 7 | [Consolidated criteria for reporting qualitative research (COREQ): a 32-item checklist for interviews and focus groups](https://doi.org/10.1093/intqhc/mzm042) | 2007 | 8 | 30891 | International Journal for Quality in Health Care | Allison Tong, Peter Sainsbury, Jonathan C. Craig |
| 8 | [NIH Image to ImageJ: 25 years of image analysis](https://doi.org/10.1038/nmeth.2089) | 2012 | 8 | 57761 | Nature Methods | Caroline A Schneider, Wayne Rasband, Kevin W. Eliceiri |
| 9 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 8 | 189685 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 10 | [CHARMM36m: an improved force field for folded and intrinsically disordered proteins](https://doi.org/10.1038/nmeth.4067) | 2016 | 7 | 5989 | Nature Methods | Jing Huang, Sarah Rauscher, Grzegorz Nawrocki, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 91 | 108061 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 35 | 24576 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 25 | 12038 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 4 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 22 | 85265 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 5 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 21 | 30117 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 20 | 5902 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 7 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 17 | 70541 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 8 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 16 | 189685 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 9 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 15 | 14160 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |
| 10 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 14 | 5884 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 8 | 1066 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 75 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 5 | 676 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 7 | 75 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 14 | 13535 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 1833 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 9 | 7838 |  | Nils Reimers, Iryna Gurevych |
| 4 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 8 | 60957 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 1690 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 7 | 2622 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 7 | [BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://doi.org/10.1093/bioinformatics/btz682) | 2019 | 6 | 5458 | Bioinformatics | Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, et al. |
| 8 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 5 | 96 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 9 | [A Survey of Large Language Models](https://doi.org/10.48550/arxiv.2303.18223) | 2023 | 5 | 1164 | arXiv (Cornell University) | Wayne Xin Zhao, Kun Zhou, Junyi Li, et al. |
| 10 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 5 | 1727 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 12 | 1833 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 1690 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 7 | 2622 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 5 | 96 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 5 | [A Survey of Large Language Models](https://doi.org/10.48550/arxiv.2303.18223) | 2023 | 5 | 1164 | arXiv (Cornell University) | Wayne Xin Zhao, Kun Zhou, Junyi Li, et al. |
| 6 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 5 | 1727 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 7 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 5 | 2794 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 8 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via
  Reinforcement Learning](https://doi.org/10.48550/arxiv.2501.12948) | 2025 | 4 | 148 | arXiv (Cornell University) | DeepSeek-AI, Daya Guo, Dejian Yang, et al. |
| 9 | [Detecting hallucinations in large language models using semantic entropy](https://doi.org/10.1038/s41586-024-07421-0) | 2024 | 4 | 159 | Nature | Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, et al. |
| 10 | [Chatbots and Large Language Models in Radiology: A Practical Primer for Clinical and Research Applications](https://doi.org/10.1148/radiol.232756) | 2024 | 4 | 163 | Radiology | Rajesh Bhayana |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Retrieval augmented generation for large language models in healthcare: A systematic review](https://doi.org/10.1371/journal.pdig.0000877) | 2025 | 3 | 1 | PLOS Digital Health | Lameck Mbangula Amugongo, Pietro Mascheroni, Steven E. Brooks, et al. |
| 2 | [Evaluating large language model workflows in clinical decision support for triage and referral and diagnosis](https://doi.org/10.1038/s41746-025-01684-1) | 2025 | 3 | 6 | npj Digital Medicine | Farieda Gaber, Maqsood Shaik, Fabio Allega, et al. |
| 3 | [A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation](https://doi.org/10.1038/s41746-025-01670-7) | 2025 | 3 | 7 | npj Digital Medicine | Elham Asgari, Nina Montaña-Brown, Magda Dubois, et al. |
| 4 | [Medical Hallucination in Foundation Models and Their Impact on Healthcare](https://doi.org/10.1101/2025.02.28.25323115) | 2025 | 3 | 9 | medRxiv (Cold Spring Harbor Laboratory) | Yubin Kim, Hyewon Jeong, Shan Chen, et al. |
| 5 | [ChatGPT becomes an Oncologist: the performance of Artificial Intelligence in the American Society of Clinical Oncology Evaluation Program (Preprint)](https://doi.org/10.2196/50442) | 2023 | 2 | 6 | JMIR AI | Roupen Odabashian, Donald Bastin, Georden Jones, et al. |
| 6 | [Implementing large language models in healthcare while balancing control, collaboration, costs and security](https://doi.org/10.1038/s41746-025-01476-7) | 2025 | 3 | 15 | npj Digital Medicine | Fabio Dennstädt, Janna Hastings, Paul Martin Putora, et al. |
| 7 | [Fully Autonomous Programming with Large Language Models](https://doi.org/10.1145/3583131.3590481) | 2023 | 3 | 24 | Proceedings of the Genetic and Evolutionary Computation Conference | Vadim Liventsev, Anastasiia Grishina, Aki Härmä, et al. |
| 8 | [Quality of Answers of Generative Large Language Models Versus Peer Users for Interpreting Laboratory Test Results for Lay Patients: Evaluation Study](https://doi.org/10.2196/56655) | 2024 | 2 | 17 | Journal of Medical Internet Research | Zhe He, Balu Bhasuran, Qiao Jin, et al. |
| 9 | [DeepSeek in Healthcare: Revealing Opportunities and Steering Challenges of a New Open-Source Artificial Intelligence Frontier](https://doi.org/10.7759/cureus.79221) | 2025 | 2 | 21 | Cureus | Abdulrahman Temsah, Khalid Alhasan, Ibraheem Altamimi, et al. |
| 10 | [DRG-LLaMA : tuning LLaMA model to predict diagnosis-related group for hospitalized patients](https://doi.org/10.1038/s41746-023-00989-3) | 2024 | 3 | 49 | npj Digital Medicine | Hanyin Wang, Chufan Gao, Christopher Dantona, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary stable strategies and game dynamics](https://doi.org/10.1016/0025-5564(78)90077-9) | 1978 | 3 | 3329 | Mathematical Biosciences | Peter Taylor, Leo Jonker |
| 2 | [The future of theoretical evolutionary game theory](https://doi.org/10.1098/rstb.2021.0508) | 2023 | 2 | 71 | Philosophical Transactions of the Royal Society B Biological Sciences | Arne Traulsen, Nikoleta E. Glynatsi |
| 3 | [Equilibrium points in <i>n</i> -person games](https://doi.org/10.1073/pnas.36.1.48) | 1950 | 2 | 7042 | Proceedings of the National Academy of Sciences | John F. Nash |
| 4 | [An optimized environment-adaptive computation offloading strategy for real-time cross-camera task in edge computing networks](https://doi.org/10.1007/s11042-023-16102-5) | 2023 | 1 | 1 | Multimedia Tools and Applications | Peng Yang, Siming Jiang, Meng Yi, et al. |
| 5 | [Online resolution adaptation and resource allocation for edge-assisted video analytics](https://doi.org/10.1016/j.comnet.2024.110342) | 2024 | 1 | 1 | Computer Networks | Yue Li, Yanjun Li, Yuzhe Chen, et al. |
| 6 | [Edge-Cloud Collaborative Streaming Video Analytics with Multi-agent Deep Reinforcement Learning](https://doi.org/10.1109/mnet.2024.3398724) | 2024 | 1 | 1 | IEEE Network | Bin Qian, Yubo Xuan, Di Wu, et al. |
| 7 | [HiVAT: Improving QoE for Hybrid Video Streaming Service With Adaptive Transcoding](https://doi.org/10.1109/tmc.2024.3399398) | 2024 | 1 | 1 | IEEE Transactions on Mobile Computing | Yuanwei Zhu, Yakun Huang, Xiuquan Qiao, et al. |
| 8 | [Collaborative Video Streaming With Super-Resolution in Multi-User MEC Networks](https://doi.org/10.1109/tmc.2024.3461685) | 2024 | 1 | 1 | IEEE Transactions on Mobile Computing | Xiaobo Zhou, Jiaxin Zeng, Shuxin Ge, et al. |
| 9 | [Unveiling the masks: Deception and reputation in spatial prisoner’s dilemma game](https://doi.org/10.1016/j.chaos.2024.115234) | 2024 | 1 | 1 | Chaos Solitons & Fractals | Kai Xie, Yaojun Liu, Tingjin Liu |
| 10 | [Threshold incentive mechanisms for the sustainable management of public resources](https://doi.org/10.1063/5.0233220) | 2024 | 1 | 1 | Chaos An Interdisciplinary Journal of Nonlinear Science | Lichen Wang, Shijia Hua, Yuyuan Liu, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The future of theoretical evolutionary game theory](https://doi.org/10.1098/rstb.2021.0508) | 2023 | 2 | 71 | Philosophical Transactions of the Royal Society B Biological Sciences | Arne Traulsen, Nikoleta E. Glynatsi |
| 2 | [An optimized environment-adaptive computation offloading strategy for real-time cross-camera task in edge computing networks](https://doi.org/10.1007/s11042-023-16102-5) | 2023 | 1 | 1 | Multimedia Tools and Applications | Peng Yang, Siming Jiang, Meng Yi, et al. |
| 3 | [Online resolution adaptation and resource allocation for edge-assisted video analytics](https://doi.org/10.1016/j.comnet.2024.110342) | 2024 | 1 | 1 | Computer Networks | Yue Li, Yanjun Li, Yuzhe Chen, et al. |
| 4 | [Edge-Cloud Collaborative Streaming Video Analytics with Multi-agent Deep Reinforcement Learning](https://doi.org/10.1109/mnet.2024.3398724) | 2024 | 1 | 1 | IEEE Network | Bin Qian, Yubo Xuan, Di Wu, et al. |
| 5 | [HiVAT: Improving QoE for Hybrid Video Streaming Service With Adaptive Transcoding](https://doi.org/10.1109/tmc.2024.3399398) | 2024 | 1 | 1 | IEEE Transactions on Mobile Computing | Yuanwei Zhu, Yakun Huang, Xiuquan Qiao, et al. |
| 6 | [Collaborative Video Streaming With Super-Resolution in Multi-User MEC Networks](https://doi.org/10.1109/tmc.2024.3461685) | 2024 | 1 | 1 | IEEE Transactions on Mobile Computing | Xiaobo Zhou, Jiaxin Zeng, Shuxin Ge, et al. |
| 7 | [Unveiling the masks: Deception and reputation in spatial prisoner’s dilemma game](https://doi.org/10.1016/j.chaos.2024.115234) | 2024 | 1 | 1 | Chaos Solitons & Fractals | Kai Xie, Yaojun Liu, Tingjin Liu |
| 8 | [Threshold incentive mechanisms for the sustainable management of public resources](https://doi.org/10.1063/5.0233220) | 2024 | 1 | 1 | Chaos An Interdisciplinary Journal of Nonlinear Science | Lichen Wang, Shijia Hua, Yuyuan Liu, et al. |
| 9 | [An adaptive exploration mechanism for Q-learning in spatial public goods games](https://doi.org/10.1016/j.chaos.2024.115705) | 2024 | 1 | 1 | Chaos Solitons & Fractals | Shaofei Shen, Xuejun Zhang, Ao‐Bo Xu, et al. |
| 10 | [TSBG: A Two-stage Stackelberg Game Algorithm for QoE-awareness Video Streaming Transmission](https://doi.org/10.1109/tmc.2024.3412860) | 2024 | 1 | 0 | IEEE Transactions on Mobile Computing | Xiang Shu-zhen, Huigui Rong, Jianguo Chen, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [An optimized environment-adaptive computation offloading strategy for real-time cross-camera task in edge computing networks](https://doi.org/10.1007/s11042-023-16102-5) | 2023 | 1 | 1 | Multimedia Tools and Applications | Peng Yang, Siming Jiang, Meng Yi, et al. |
| 2 | [Online resolution adaptation and resource allocation for edge-assisted video analytics](https://doi.org/10.1016/j.comnet.2024.110342) | 2024 | 1 | 1 | Computer Networks | Yue Li, Yanjun Li, Yuzhe Chen, et al. |
| 3 | [Edge-Cloud Collaborative Streaming Video Analytics with Multi-agent Deep Reinforcement Learning](https://doi.org/10.1109/mnet.2024.3398724) | 2024 | 1 | 1 | IEEE Network | Bin Qian, Yubo Xuan, Di Wu, et al. |
| 4 | [HiVAT: Improving QoE for Hybrid Video Streaming Service With Adaptive Transcoding](https://doi.org/10.1109/tmc.2024.3399398) | 2024 | 1 | 1 | IEEE Transactions on Mobile Computing | Yuanwei Zhu, Yakun Huang, Xiuquan Qiao, et al. |
| 5 | [Collaborative Video Streaming With Super-Resolution in Multi-User MEC Networks](https://doi.org/10.1109/tmc.2024.3461685) | 2024 | 1 | 1 | IEEE Transactions on Mobile Computing | Xiaobo Zhou, Jiaxin Zeng, Shuxin Ge, et al. |
| 6 | [Unveiling the masks: Deception and reputation in spatial prisoner’s dilemma game](https://doi.org/10.1016/j.chaos.2024.115234) | 2024 | 1 | 1 | Chaos Solitons & Fractals | Kai Xie, Yaojun Liu, Tingjin Liu |
| 7 | [Threshold incentive mechanisms for the sustainable management of public resources](https://doi.org/10.1063/5.0233220) | 2024 | 1 | 1 | Chaos An Interdisciplinary Journal of Nonlinear Science | Lichen Wang, Shijia Hua, Yuyuan Liu, et al. |
| 8 | [An adaptive exploration mechanism for Q-learning in spatial public goods games](https://doi.org/10.1016/j.chaos.2024.115705) | 2024 | 1 | 1 | Chaos Solitons & Fractals | Shaofei Shen, Xuejun Zhang, Ao‐Bo Xu, et al. |
| 9 | [TSBG: A Two-stage Stackelberg Game Algorithm for QoE-awareness Video Streaming Transmission](https://doi.org/10.1109/tmc.2024.3412860) | 2024 | 1 | 0 | IEEE Transactions on Mobile Computing | Xiang Shu-zhen, Huigui Rong, Jianguo Chen, et al. |
| 10 | [Cooperation resonance based on link strategy reinforcement learning and conformity](https://doi.org/10.1063/5.0239335) | 2024 | 1 | 0 | Chaos An Interdisciplinary Journal of Nonlinear Science | Bo Gao, Pengfei Zuo, Xiangfeng Dai, et al. |
<!-- TRENDING-END -->
