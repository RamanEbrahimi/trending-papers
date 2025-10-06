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

Last update: 2025-10-06 06:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 14 | 151012 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 13 | 58608 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 3 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 9 | 67647 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 4 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 9 | 93500 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |
| 5 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 8 | 95213 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 6 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 8 | 194890 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 7 | [Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR and the 2−ΔΔCT Method](https://doi.org/10.1006/meth.2001.1262) | 2001 | 7 | 165704 | Methods | Kenneth J. Livak, Thomas D. Schmittgen |
| 8 | [Investigation of the freely available easy-to-use software ‘EZR’ for medical statistics](https://doi.org/10.1038/bmt.2012.244) | 2012 | 6 | 16313 | Bone Marrow Transplantation | Yoshinobu Kanda |
| 9 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 6 | 71274 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 10 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 6 | 86265 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 123 | 109434 | Machine Learning | Leo Breiman |
| 2 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 35 | 6484 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 32 | 24946 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 30 | 71274 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 5 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 27 | 30502 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 26 | 86265 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 7 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 21 | 12466 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 8 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 20 | 26314 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 9 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 19 | 6071 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 10 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 17 | 191559 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 14 | 14067 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 2 | [Machine Learning Implementation in Membrane Bioreactor Systems: Progress, Challenges, and Future Perspectives: A Review](https://doi.org/10.3390/environments10070127) | 2023 | 7 | 28 | Environments | Zacharias Frontistis, Grigoris Lykogiannis, Anastasios Sarmpanis |
| 3 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 7 | 1436 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 4 | [Understanding and Designing a High-Performance Ultrafiltration Membrane Using Machine Learning](https://doi.org/10.1021/acs.est.2c05404) | 2023 | 6 | 60 | Environmental Science & Technology | Haiping Gao, Shifa Zhong, Raghav Dangayach, et al. |
| 5 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 6 | 115 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 6 | [Extracting spatial effects from machine learning model using local interpretation method: An example of SHAP and XGBoost](https://doi.org/10.1016/j.compenvurbsys.2022.101845) | 2022 | 6 | 556 | Computers Environment and Urban Systems | Ziqi Li |
| 7 | [Root-mean-square error (RMSE) or mean absolute error (MAE): when to use them or not](https://doi.org/10.5194/gmd-15-5481-2022) | 2022 | 6 | 987 | Geoscientific model development | Timothy Hodson |
| 8 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 6 | 2777 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Multiscale computational modeling of organic compounds separation using microporous membranes](https://doi.org/10.5004/dwt.2019.23502) | 2019 | 5 | 7 | Desalination and Water Treatment | Mashallah Rezakazemi, Saeed Shirazian |
| 2 | [Machine Learning Implementation in Membrane Bioreactor Systems: Progress, Challenges, and Future Perspectives: A Review](https://doi.org/10.3390/environments10070127) | 2023 | 7 | 28 | Environments | Zacharias Frontistis, Grigoris Lykogiannis, Anastasios Sarmpanis |
| 3 | [Understanding and Designing a High-Performance Ultrafiltration Membrane Using Machine Learning](https://doi.org/10.1021/acs.est.2c05404) | 2023 | 6 | 60 | Environmental Science & Technology | Haiping Gao, Shifa Zhong, Raghav Dangayach, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 13 | 13858 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 1868 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 10 | 2793 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://doi.org/10.1093/bioinformatics/btz682) | 2019 | 10 | 5610 | Bioinformatics | Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, et al. |
| 5 | [Preface for LLMs4OL 2024: The 1st Large Language Models for Ontology Learning Challenge at the 23rd ISWC](https://doi.org/10.52825/ocp.v4i.2472) | 2024 | 9 | 0 | Open Conference Proceedings | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 6 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 1964 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 7 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 9 | 61944 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 8 | [LLMs4OL: Large Language Models for Ontology Learning](https://doi.org/10.1007/978-3-031-47240-4_22) | 2023 | 7 | 53 | Lecture notes in computer science | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1138 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://doi.org/10.18653/v1/2021.acl-long.353) | 2021 | 7 | 1726 |  | Xiang Lisa Li, Percy Liang |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 10 | 1868 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 2 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 10 | 2793 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 3 | [Preface for LLMs4OL 2024: The 1st Large Language Models for Ontology Learning Challenge at the 23rd ISWC](https://doi.org/10.52825/ocp.v4i.2472) | 2024 | 9 | 0 | Open Conference Proceedings | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 9 | 1964 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [LLMs4OL: Large Language Models for Ontology Learning](https://doi.org/10.1007/978-3-031-47240-4_22) | 2023 | 7 | 53 | Lecture notes in computer science | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 6 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1138 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 7 | [LLMs4OL 2024 Overview: The 1st Large Language Models for Ontology Learning Challenge](https://doi.org/10.52825/ocp.v4i.2473) | 2024 | 6 | 0 | Open Conference Proceedings | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 8 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 6 | 1787 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 9 | [A survey on large language model (LLM) security and privacy: The Good, The Bad, and The Ugly](https://doi.org/10.1016/j.hcc.2024.100211) | 2024 | 5 | 362 | High-Confidence Computing | Yifan Yao, Jinhao Duan, Kaidi Xu, et al. |
| 10 | [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://doi.org/10.1109/tkde.2024.3352100) | 2024 | 5 | 449 | IEEE Transactions on Knowledge and Data Engineering | Shirui Pan, Linhao Luo, Yufei Wang, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Preface for LLMs4OL 2024: The 1st Large Language Models for Ontology Learning Challenge at the 23rd ISWC](https://doi.org/10.52825/ocp.v4i.2472) | 2024 | 9 | 0 | Open Conference Proceedings | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 2 | [LLMs4OL 2024 Overview: The 1st Large Language Models for Ontology Learning Challenge](https://doi.org/10.52825/ocp.v4i.2473) | 2024 | 6 | 0 | Open Conference Proceedings | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 3 | [silp_nlp at LLMs4OL 2024 Tasks A, B, and C: Ontology Learning through Prompts with LLMs](https://doi.org/10.52825/ocp.v4i.2485) | 2024 | 4 | 0 | Open Conference Proceedings | Pankaj Kumar Goyal, Sumit Singh, Uma Shanker Tiwary |
| 4 | [LLMs4OL 2024 Datasets: Toward Ontology Learning with Large Language Models](https://doi.org/10.52825/ocp.v4i.2480) | 2024 | 3 | 0 | Open Conference Proceedings | Hamed Babaei Giglou, Jennifer D’Souza, Sameer Sadruddin, et al. |
| 5 | [SKH-NLP at LLMs4OL 2024 Task B: Taxonomy Discovery in Ontologies Using BERT and LLaMA 3](https://doi.org/10.52825/ocp.v4i.2483) | 2024 | 3 | 0 | Open Conference Proceedings | Seyed Mohammad Hossein Hashemi, Mostafa Karimi Manesh, Mehrnoush Shamsfard |
| 6 | [Humans or LLMs as the Judge? A Study on Judgement Bias](https://doi.org/10.18653/v1/2024.emnlp-main.474) | 2024 | 3 | 12 | Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing | Guiming Hardy Chen, Shunian Chen, Ziche Liu, et al. |
| 7 | [Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages](https://doi.org/10.1177/08944393241286471) | 2024 | 3 | 13 | Social Science Computer Review | Petter Törnberg |
| 8 | [Large language models outperform mental and medical health care professionals in identifying obsessive-compulsive disorder](https://doi.org/10.1038/s41746-024-01181-x) | 2024 | 3 | 21 | npj Digital Medicine | Jiyeong Kim, Kimberly Glazier Leonte, Michael L. Chen, et al. |
| 9 | [LLMs4OL: Large Language Models for Ontology Learning](https://doi.org/10.1007/978-3-031-47240-4_22) | 2023 | 7 | 53 | Lecture notes in computer science | Hamed Babaei Giglou, Jennifer D’Souza, Sören Auer |
| 10 | [From GPT to DeepSeek: Significant gaps remains in realizing AI in healthcare](https://doi.org/10.1016/j.jbi.2025.104791) | 2025 | 3 | 36 | Journal of Biomedical Informatics | Yifan Peng, Bradley Malin, Justin F. Rousseau, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A conceptual framework on the role of magnetic cues in songbird migration ecology](https://doi.org/10.1111/brv.13082) | 2024 | 2 | 2 | Biological reviews/Biological reviews of the Cambridge Philosophical Society | Thiemo Karwinkel, Annika Peter, Richard A. Holland, et al. |
| 2 | [Cumulative route improvements spontaneously emerge in artificial navigators even in the absence of sophisticated communication or thought](https://doi.org/10.1371/journal.pbio.3002644) | 2024 | 2 | 0 | PLoS Biology | Edwin S. Dalmaijer |
| 3 | [Timing decisions as the next frontier for collective intelligence](https://doi.org/10.1016/j.tree.2024.06.003) | 2024 | 2 | 5 | Trends in Ecology & Evolution | Albert B. Kao, Shoubhik Chandan Banerjee, Fritz A. Francisco, et al. |
| 4 | [Collective learning in route navigation](https://doi.org/10.4161/cib.26521) | 2013 | 2 | 7 | Communicative & Integrative Biology | Andrea Flack, Dora Biro |
| 5 | [Empirical test of the many-wrongs hypothesis reveals weighted averaging of individual routes in pigeon flocks](https://doi.org/10.1016/j.isci.2022.105076) | 2022 | 2 | 8 | iScience | Takao Sasaki, Naoki Masuda, Richard P. Mann, et al. |
| 6 | [Experience reduces route selection for conspecifics by the collectively migrating white stork](https://doi.org/10.1016/j.cub.2024.03.052) | 2024 | 2 | 9 | Current Biology | Hester Brønnvik, Elham Nourani, Wolfgang Fiedler, et al. |
| 7 | [Disentangling influence over group speed and direction reveals multiple patterns of influence in moving meerkat groups](https://doi.org/10.1038/s41598-022-17259-z) | 2022 | 2 | 12 | Scientific Reports | Baptiste Averly, Vivek H. Sridhar, Vlad Demartsev, et al. |
| 8 | [Naïve individuals promote collective exploration in homing pigeons](https://doi.org/10.7554/elife.68653) | 2021 | 2 | 13 | eLife | Gabriele Valentini, Theodore P. Pavlic, Sara Imari Walker, et al. |
| 9 | [Chimpanzees use social information to acquire a skill they fail to innovate](https://doi.org/10.1038/s41562-024-01836-5) | 2024 | 2 | 14 | Nature Human Behaviour | Edwin J. C. van Leeuwen, Sarah E. DeTroy, Daniel B. M. Haun, et al. |
| 10 | [Multidimensional social influence drives leadership and composition-dependent success in octopus–fish hunting groups](https://doi.org/10.1038/s41559-024-02525-2) | 2024 | 2 | 14 | Nature Ecology & Evolution | Eduardo Sampaio, Vivek H. Sridhar, Fritz A. Francisco, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A conceptual framework on the role of magnetic cues in songbird migration ecology](https://doi.org/10.1111/brv.13082) | 2024 | 2 | 2 | Biological reviews/Biological reviews of the Cambridge Philosophical Society | Thiemo Karwinkel, Annika Peter, Richard A. Holland, et al. |
| 2 | [Cumulative route improvements spontaneously emerge in artificial navigators even in the absence of sophisticated communication or thought](https://doi.org/10.1371/journal.pbio.3002644) | 2024 | 2 | 0 | PLoS Biology | Edwin S. Dalmaijer |
| 3 | [Timing decisions as the next frontier for collective intelligence](https://doi.org/10.1016/j.tree.2024.06.003) | 2024 | 2 | 5 | Trends in Ecology & Evolution | Albert B. Kao, Shoubhik Chandan Banerjee, Fritz A. Francisco, et al. |
| 4 | [Empirical test of the many-wrongs hypothesis reveals weighted averaging of individual routes in pigeon flocks](https://doi.org/10.1016/j.isci.2022.105076) | 2022 | 2 | 8 | iScience | Takao Sasaki, Naoki Masuda, Richard P. Mann, et al. |
| 5 | [Experience reduces route selection for conspecifics by the collectively migrating white stork](https://doi.org/10.1016/j.cub.2024.03.052) | 2024 | 2 | 9 | Current Biology | Hester Brønnvik, Elham Nourani, Wolfgang Fiedler, et al. |
| 6 | [Disentangling influence over group speed and direction reveals multiple patterns of influence in moving meerkat groups](https://doi.org/10.1038/s41598-022-17259-z) | 2022 | 2 | 12 | Scientific Reports | Baptiste Averly, Vivek H. Sridhar, Vlad Demartsev, et al. |
| 7 | [Chimpanzees use social information to acquire a skill they fail to innovate](https://doi.org/10.1038/s41562-024-01836-5) | 2024 | 2 | 14 | Nature Human Behaviour | Edwin J. C. van Leeuwen, Sarah E. DeTroy, Daniel B. M. Haun, et al. |
| 8 | [Multidimensional social influence drives leadership and composition-dependent success in octopus–fish hunting groups](https://doi.org/10.1038/s41559-024-02525-2) | 2024 | 2 | 14 | Nature Ecology & Evolution | Eduardo Sampaio, Vivek H. Sridhar, Fritz A. Francisco, et al. |
| 9 | [Animal navigation: how animals use environmental factors to find their way](https://doi.org/10.1140/epjs/s11734-022-00610-w) | 2022 | 2 | 37 | The European Physical Journal Special Topics | Roswitha Wiltschko, Wolfgang Wiltschko |
| 10 | [Virtual Reality in Education: A Review of Learning Theories, Approaches and Methodologies for the Last Decade](https://doi.org/10.3390/electronics12132832) | 2023 | 2 | 283 | Electronics | Andreas Marougkas, Christos Troussas, Akrivi Krouska, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A conceptual framework on the role of magnetic cues in songbird migration ecology](https://doi.org/10.1111/brv.13082) | 2024 | 2 | 2 | Biological reviews/Biological reviews of the Cambridge Philosophical Society | Thiemo Karwinkel, Annika Peter, Richard A. Holland, et al. |
| 2 | [Cumulative route improvements spontaneously emerge in artificial navigators even in the absence of sophisticated communication or thought](https://doi.org/10.1371/journal.pbio.3002644) | 2024 | 2 | 0 | PLoS Biology | Edwin S. Dalmaijer |
| 3 | [A cooperative strategy based on Nash bargaining solution under spectral mask constraint in cooperative relay networks](https://doi.org/10.1109/iccsn.2011.6013683) | 2011 | 1 | 1 |  | Brima Fallah, Huang Ben-xiong, Weihua Yin |
| 4 | [Installation, operation and maintenance considerations for electrical equipment in hazardous location](https://doi.org/10.1109/esw.2010.6164452) | 2010 | 1 | 0 |  | Marty Cole, Tim Driscoll, Ken Martin |
| 5 | [Research on Lahu’s traditional sports culture from the perspective of cultural ecology](https://doi.org/10.1051/shsconf/20162401008) | 2016 | 1 | 0 | SHS Web of Conferences | Youfeng Wang |
| 6 | [Timing decisions as the next frontier for collective intelligence](https://doi.org/10.1016/j.tree.2024.06.003) | 2024 | 2 | 5 | Trends in Ecology & Evolution | Albert B. Kao, Shoubhik Chandan Banerjee, Fritz A. Francisco, et al. |
| 7 | [Collective learning in route navigation](https://doi.org/10.4161/cib.26521) | 2013 | 2 | 7 | Communicative & Integrative Biology | Andrea Flack, Dora Biro |
| 8 | [Empirical test of the many-wrongs hypothesis reveals weighted averaging of individual routes in pigeon flocks](https://doi.org/10.1016/j.isci.2022.105076) | 2022 | 2 | 8 | iScience | Takao Sasaki, Naoki Masuda, Richard P. Mann, et al. |
| 9 | [Experience reduces route selection for conspecifics by the collectively migrating white stork](https://doi.org/10.1016/j.cub.2024.03.052) | 2024 | 2 | 9 | Current Biology | Hester Brønnvik, Elham Nourani, Wolfgang Fiedler, et al. |
| 10 | [Disentangling influence over group speed and direction reveals multiple patterns of influence in moving meerkat groups](https://doi.org/10.1038/s41598-022-17259-z) | 2022 | 2 | 12 | Scientific Reports | Baptiste Averly, Vivek H. Sridhar, Vlad Demartsev, et al. |
<!-- TRENDING-END -->
