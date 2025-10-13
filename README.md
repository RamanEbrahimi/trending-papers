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

Last update: 2025-10-13 06:22 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 9 | 14067 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 9 | 59079 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 6 | 93500 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |
| 4 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 6 | 151621 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 5 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 6 | 195501 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 6 | [Deleted Work](https://openalex.org/W4285719527) | 1955 | 5 | 0 |  | Unknown |
| 7 | [The science of the total environment](https://doi.org/10.1016/0143-1471(82)90047-2) | 1982 | 5 | 3172 | Environmental Pollution Series A Ecological and Biological | K.M. |
| 8 | [The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement](https://doi.org/10.1371/journal.pmed.1001885) | 2015 | 5 | 4153 | PLoS Medicine | Eric I. Benchimol, Liam Smeeth, Astrid Guttmann, et al. |
| 9 | [Photoperoxidation in isolated chloroplasts](https://doi.org/10.1016/0003-9861(68)90654-1) | 1968 | 5 | 10272 | Archives of Biochemistry and Biophysics | Robert L. Heath, Lester Packer |
| 10 | [Sarcopenia: revised European consensus on definition and diagnosis](https://doi.org/10.1093/ageing/afy169) | 2018 | 5 | 11296 | Age and Ageing | Alfonso J. Cruz‐Jentoft, Gülistan Bahat, Jürgen M. Bauer, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 106 | 110040 | Machine Learning | Leo Breiman |
| 2 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 23 | 6734 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 3 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 21 | 71583 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 20 | 25121 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 20 | 86461 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 18 | 26451 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 17 | 12523 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 8 | [Building Predictive Models in<i>R</i>Using the<b>caret</b>Package](https://doi.org/10.18637/jss.v028.i05) | 2008 | 16 | 7670 | Journal of Statistical Software | Max Kühn |
| 9 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 16 | 30572 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 10 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 16 | 192329 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 10 | 14067 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [From patterns to patients: Advances in clinical machine learning for cancer diagnosis, prognosis, and treatment](https://doi.org/10.1016/j.cell.2023.01.035) | 2023 | 7 | 346 | Cell | Kyle Swanson, Eric Q. Wu, Angela Zhang, et al. |
| 3 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 7 | 389 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 4 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 5 | 118 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 5 | [Machine Learning for Electrocatalyst and Photocatalyst Design and Discovery](https://doi.org/10.1021/acs.chemrev.2c00061) | 2022 | 5 | 349 | Chemical Reviews | Haoxin Mai, Tu C. Le, Dehong Chen, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 13 | 13893 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 10 | 1825 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 1988 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 8 | 8076 |  | Nils Reimers, Iryna Gurevych |
| 5 | [Advances in Neural Information Processing Systems 19](https://doi.org/10.7551/mitpress/7503.001.0001) | 2007 | 7 | 15643 | The MIT Press eBooks | Unknown |
| 6 | [ChatGPT Utility in Healthcare Education, Research, and Practice: Systematic Review on the Promising Perspectives and Valid Concerns](https://doi.org/10.3390/healthcare11060887) | 2023 | 6 | 2113 | Healthcare | Malik Sallam |
| 7 | [High-performance medicine: the convergence of human and artificial intelligence](https://doi.org/10.1038/s41591-018-0300-7) | 2018 | 6 | 5704 | Nature Medicine | Eric J. Topol |
| 8 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://doi.org/10.48550/arxiv.1910.10683) | 2019 | 6 | 8508 | arXiv (Cornell University) | Colin Raffel, Noam Shazeer, Adam Roberts, et al. |
| 9 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 5 | 406 | ACM transactions on office information systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 10 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 5 | 1150 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 10 | 1825 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 1988 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [ChatGPT Utility in Healthcare Education, Research, and Practice: Systematic Review on the Promising Perspectives and Valid Concerns](https://doi.org/10.3390/healthcare11060887) | 2023 | 6 | 2113 | Healthcare | Malik Sallam |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 5 | 406 | ACM transactions on office information systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 5 | 1150 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 6 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 5 | 2810 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 7 | [Training language models to follow instructions with human feedback](https://doi.org/10.48550/arxiv.2203.02155) | 2022 | 5 | 3107 | arXiv (Cornell University) | Long Ouyang, Jeff Wu, Xu Jiang, et al. |
| 8 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 4 | 195 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 9 | [Augmenting large language models with chemistry tools](https://doi.org/10.1038/s42256-024-00832-8) | 2024 | 4 | 252 | Nature Machine Intelligence | Andres M. Bran, Sam Cox, Oliver Schilter, et al. |
| 10 | [Assessing the potential of GPT-4 to perpetuate racial and gender biases in health care: a model evaluation study](https://doi.org/10.1016/s2589-7500(23)00225-x) | 2023 | 4 | 279 | The Lancet Digital Health | Travis Zack, Eric Lehman, Mirac Süzgün, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Automated Metrics for Medical Multi-Document Summarization Disagree with Human Evaluations](https://doi.org/10.18653/v1/2023.acl-long.549) | 2023 | 2 | 7 |  | Lucy Lu Wang, Yulia Otmakhova, Jay DeYoung, et al. |
| 2 | [It’s Time to Bench the Medical Exam Benchmark](https://doi.org/10.1056/aie2401235) | 2025 | 3 | 11 | NEJM AI | Inioluwa Deborah Raji, Roxana Daneshjou, Emily Alsentzer |
| 3 | [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](https://doi.org/10.1145/3689736) | 2024 | 3 | 12 | Proceedings of the ACM on Programming Languages | Chenyuan Yang, Yinlin Deng, Runyu Lu, et al. |
| 4 | [SciAgents: Automating Scientific Discovery Through Bioinspired Multi‐Agent Intelligent Graph Reasoning](https://doi.org/10.1002/adma.202413523) | 2024 | 3 | 15 | Advanced Materials | Alireza Ghafarollahi, Markus J. Buehler |
| 5 | [Benchmark evaluation of DeepSeek large language models in clinical decision-making](https://doi.org/10.1038/s41591-025-03727-2) | 2025 | 3 | 19 | Nature Medicine | Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, et al. |
| 6 | [The Scientific Knowledge of Bard and ChatGPT in Endocrinology, Diabetes, and Diabetes Technology: Multiple-Choice Questions Examination-Based Performance](https://doi.org/10.1177/19322968231203987) | 2023 | 3 | 32 | Journal of Diabetes Science and Technology | Sultan Ayoub Meo, Thamir Al-khlaiwi, Abdulelah Adnan Abukhalaf, et al. |
| 7 | [Large Language Models Empowered Autonomous Edge AI for Connected Intelligence](https://doi.org/10.1109/mcom.001.2300550) | 2024 | 3 | 33 | IEEE Communications Magazine | Yifei Shen, Jiawei Shao, Xinjie Zhang, et al. |
| 8 | [Quality of Large Language Model Responses to Radiation Oncology Patient Care Questions](https://doi.org/10.1001/jamanetworkopen.2024.4630) | 2024 | 3 | 50 | JAMA Network Open | Amulya Yalamanchili, Bishwambhar Sengupta, Joshua Song, et al. |
| 9 | [Generative artificial intelligence in primary care: an online survey of UK general practitioners](https://doi.org/10.1136/bmjhci-2024-101102) | 2024 | 3 | 56 | BMJ Health & Care Informatics | Charlotte Blease, Cosima Locher, Jens Gaab, et al. |
| 10 | [Large Language Model guided Protocol Fuzzing](https://doi.org/10.14722/ndss.2024.24556) | 2024 | 2 | 66 |  | Ruijie Meng, Мартин Мирчев, Marcel Böhme, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The future of theoretical evolutionary game theory](https://doi.org/10.1098/rstb.2021.0508) | 2023 | 2 | 80 | Philosophical Transactions of the Royal Society B Biological Sciences | Arne Traulsen, Nikoleta E. Glynatsi |
| 2 | [Game theory: analysis of conflict](https://doi.org/10.5860/choice.29-2753) | 1992 | 2 | 3512 | Choice Reviews Online | Roger B. Myerson |
| 3 | [The Logic of Animal Conflict](https://doi.org/10.1038/246015a0) | 1973 | 2 | 6026 | Nature | John Maynard Smith, George Price |
| 4 | [Evolution and the Theory of Games](https://doi.org/10.1017/cbo9780511806292) | 1982 | 2 | 6767 |  | John Maynard Smith |
| 5 | [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being.](https://doi.org/10.1037/0003-066x.55.1.68) | 2000 | 2 | 30722 | American Psychologist | Richard M. Ryan, Edward L. Deci |
| 6 | [Prospect Theory: An Analysis of Decision under Risk](https://doi.org/10.2307/1914185) | 1979 | 2 | 43834 | Econometrica | Daniel Kahneman, Amos Tversky |
| 7 | [The Determinants of Dividend Payout Ratios of Nigerian Non-Financial Firms](https://openalex.org/W3114250680) | 2020 | 1 | 0 | SSRN Electronic Journal | Oluseun Paseda |
| 8 | [A SURVEY OF AUCTION THEORY AND AUCTION FORMATS](https://openalex.org/W3166722873) | 2021 | 1 | 0 |  | Oluseun Paseda |
| 9 | [Earnings Announcement and Stock Prices of Quoted Deposit Money Banks in Nigeria in the Era of COVID-19 Pandemic](https://doi.org/10.1353/jda.2023.a908650) | 2023 | 1 | 0 | The Journal of developing areas | Idowu Bosede Fasola, Oluseun Paseda |
| 10 | [Social Priorities, Institutional Quality, and Investment](https://doi.org/10.2139/ssrn.4762358) | 2024 | 1 | 0 | SSRN Electronic Journal | Amar Gande, Kose John, Guanmin Liao, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The future of theoretical evolutionary game theory](https://doi.org/10.1098/rstb.2021.0508) | 2023 | 2 | 80 | Philosophical Transactions of the Royal Society B Biological Sciences | Arne Traulsen, Nikoleta E. Glynatsi |
| 2 | [Earnings Announcement and Stock Prices of Quoted Deposit Money Banks in Nigeria in the Era of COVID-19 Pandemic](https://doi.org/10.1353/jda.2023.a908650) | 2023 | 1 | 0 | The Journal of developing areas | Idowu Bosede Fasola, Oluseun Paseda |
| 3 | [Social Priorities, Institutional Quality, and Investment](https://doi.org/10.2139/ssrn.4762358) | 2024 | 1 | 0 | SSRN Electronic Journal | Amar Gande, Kose John, Guanmin Liao, et al. |
| 4 | [Banking Resolution and Its Key Concepts and Tools](https://doi.org/10.1007/978-3-031-52311-3_5) | 2024 | 1 | 0 | Contributions to finance and accounting | Nordine Abidi, Bruno Buchetti, Samuele Crosetti, et al. |
| 5 | [A game theoretic analysis of geothermal development consensus building in Japan](https://doi.org/10.1016/j.egyr.2024.12.004) | 2024 | 1 | 0 | Energy Reports | Kotaro Shinozaki, Jun Nishijima, Tatsuya Wakeyama |
| 6 | [PRIVATIZING DEPOSIT INSURANCE](https://doi.org/10.2139/ssrn.5054917) | 2025 | 1 | 0 | SSRN Electronic Journal | Christina Parajon Skinner |
| 7 | [Game Theory Applications in Modern Business Strategy: Optimizing Competitive Decision-Making in Uncertain Markets](https://doi.org/10.2139/ssrn.5141929) | 2025 | 1 | 0 | SSRN Electronic Journal | Sonny Marmon |
| 8 | [Game Theory with Applications in Operations Management](https://doi.org/10.1007/978-981-99-4833-8) | 2024 | 1 | 2 | Springer texts in business and economics | R. K. Amit |
| 9 | [Determinates of investor opinion gap around IPOs: A machine learning approach](https://doi.org/10.1016/j.iswa.2024.200420) | 2024 | 1 | 2 | Intelligent Systems with Applications | Ali Albada, Muataz Salam Al-Daweri, Rabie Α. Ramadan, et al. |
| 10 | [Optimal financing strategies for low‐carbon supply chains: A Stackelberg game perspective](https://doi.org/10.1002/mde.4394) | 2024 | 1 | 4 | Managerial and Decision Economics | Lei Wang, Lin Zhang, Xiaoli Zhang |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Determinants of Dividend Payout Ratios of Nigerian Non-Financial Firms](https://openalex.org/W3114250680) | 2020 | 1 | 0 | SSRN Electronic Journal | Oluseun Paseda |
| 2 | [A SURVEY OF AUCTION THEORY AND AUCTION FORMATS](https://openalex.org/W3166722873) | 2021 | 1 | 0 |  | Oluseun Paseda |
| 3 | [Earnings Announcement and Stock Prices of Quoted Deposit Money Banks in Nigeria in the Era of COVID-19 Pandemic](https://doi.org/10.1353/jda.2023.a908650) | 2023 | 1 | 0 | The Journal of developing areas | Idowu Bosede Fasola, Oluseun Paseda |
| 4 | [Social Priorities, Institutional Quality, and Investment](https://doi.org/10.2139/ssrn.4762358) | 2024 | 1 | 0 | SSRN Electronic Journal | Amar Gande, Kose John, Guanmin Liao, et al. |
| 5 | [Banking Resolution and Its Key Concepts and Tools](https://doi.org/10.1007/978-3-031-52311-3_5) | 2024 | 1 | 0 | Contributions to finance and accounting | Nordine Abidi, Bruno Buchetti, Samuele Crosetti, et al. |
| 6 | [A game theoretic analysis of geothermal development consensus building in Japan](https://doi.org/10.1016/j.egyr.2024.12.004) | 2024 | 1 | 0 | Energy Reports | Kotaro Shinozaki, Jun Nishijima, Tatsuya Wakeyama |
| 7 | [PRIVATIZING DEPOSIT INSURANCE](https://doi.org/10.2139/ssrn.5054917) | 2025 | 1 | 0 | SSRN Electronic Journal | Christina Parajon Skinner |
| 8 | [Game Theory Applications in Modern Business Strategy: Optimizing Competitive Decision-Making in Uncertain Markets](https://doi.org/10.2139/ssrn.5141929) | 2025 | 1 | 0 | SSRN Electronic Journal | Sonny Marmon |
| 9 | [Game Theory with Applications in Operations Management](https://doi.org/10.1007/978-981-99-4833-8) | 2024 | 1 | 2 | Springer texts in business and economics | R. K. Amit |
| 10 | [Determinates of investor opinion gap around IPOs: A machine learning approach](https://doi.org/10.1016/j.iswa.2024.200420) | 2024 | 1 | 2 | Intelligent Systems with Applications | Ali Albada, Muataz Salam Al-Daweri, Rabie Α. Ramadan, et al. |
<!-- TRENDING-END -->
