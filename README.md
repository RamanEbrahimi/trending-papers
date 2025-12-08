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

Last update: 2025-12-08 06:25 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [What returnee bilinguals may teach us about language attrition, language stabilization, and individualvariation](https://doi.org/10.1075/lab.25021.flo) | 2025 | 11 | 14 | Linguistic Approaches to Bilingualism | Cristina Flores, Neal Snape |
| 2 | [LFIS–01: Derivation of the Cadence Law of Motion (S14) from Cadence Geometry](https://doi.org/10.5281/zenodo.17809556) | 2025 | 10 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Beaupain, MIchael |
| 3 | [LFIS–02: Cadence Triangle & Cadence Star Geometry — Derivational Form](https://doi.org/10.5281/zenodo.17809760) | 2025 | 9 | 20 | Zenodo (CERN European Organization for Nuclear Research) | Beaupain, MIchael John |
| 4 | [Screening for Lung Cancer](https://doi.org/10.1001/jama.2021.1117) | 2021 | 9 | 1504 | JAMA | Alex H. Krist, Karina W. Davidson, Carol M. Mangione, et al. |
| 5 | [Reduced Lung-Cancer Mortality with Low-Dose Computed Tomographic Screening](https://doi.org/10.1056/nejmoa1102873) | 2011 | 9 | 10477 | New England Journal of Medicine | The National Lung Screening Trial Research Team |
| 6 | [LFIS–03: Cadence Ledger, Drift Cancellation, and Sink Structure — Derivational Form](https://doi.org/10.5281/zenodo.17809852) | 2025 | 8 | 18 | Zenodo (CERN European Organization for Nuclear Research) | Beaupain, MIchael John |
| 7 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 7 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 8 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 7 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 9 | [LFIS–04: Cadence Frame Matching and Continuity Conditions — Derivational Form](https://doi.org/10.5281/zenodo.17812879) | 2025 | 7 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Beaupain, MIchael John |
| 10 | [LFIS–04: Cadence Frame Matching and Continuity Conditions — Derivational Form](https://doi.org/10.5281/zenodo.17813137) | 2025 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Beaupain, MIchael |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 133 | 115020 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 67 | 41264 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 32 | 26394 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 31 | 28400 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 5 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 22 | 75636 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 6 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 20 | 7051 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 7 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 19 | 21175 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 8 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 19 | 30942 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 9 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 16 | 961 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 10 | [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | 1986 | 15 | 28888 | Nature | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 16 | 961 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 9 | 218 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 3 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 7 | 2012 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 4 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 6 | 250 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 5 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 6 | 17361 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 6 | [Scope of machine learning in materials research—A review](https://doi.org/10.1016/j.apsadv.2023.100523) | 2023 | 5 | 140 | Applied Surface Science Advances | Md Hosne Mobarak, Mariam Akter Mimona, Md. Aminul Islam, et al. |
| 7 | [A Comprehensive Review on Machine Learning in Healthcare Industry: Classification, Restrictions, Opportunities and Challenges](https://doi.org/10.3390/s23094178) | 2023 | 5 | 240 | Sensors | Qi An, Saifur Rahman, Jingwen Zhou, et al. |
| 8 | [A novel approach to explain the black-box nature of machine learning in compressive strength predictions of concrete using Shapley additive explanations (SHAP)](https://doi.org/10.1016/j.cscm.2022.e01059) | 2022 | 5 | 399 | Case Studies in Construction Materials | I.U. Ekanayake, D.P.P. Meddage, Upaka Rathnayake |
| 9 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 5 | 1082 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 10 | [Root-mean-square error (RMSE) or mean absolute error (MAE): when to use them or not](https://doi.org/10.5194/gmd-15-5481-2022) | 2022 | 5 | 1295 | Geoscientific model development | Timothy Hodson |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Semantic segmentation of high-resolution satellite images using deep learning](https://doi.org/10.1007/s12145-021-00674-7) | 2021 | 7 | 19 | Earth Science Informatics | Kuldeep Chaurasia, Ritesh Nandy, Omkar Pawar, et al. |
| 2 | [Dilated-ResUnet: A novel deep learning architecture for building extraction from medium resolution multi-spectral satellite imagery](https://doi.org/10.1016/j.eswa.2021.115530) | 2021 | 6 | 57 | Expert Systems with Applications | Mayank Dixit, Kuldeep Chaurasia, Vipul Kumar Mishra |
| 3 | [Quantification of carbon sequestration by urban forest using Landsat 8 OLI and machine learning algorithms in Jodhpur, India](https://doi.org/10.1016/j.ufug.2021.127445) | 2021 | 5 | 49 | Urban forestry & urban greening | Swati Uniyal, Saurabh Purohit, Kuldeep Chaurasia, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2248 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 13 | 3647 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1741 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 12 | 20359 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 2489 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4223 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 7 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 11 | 30394 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 8 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 10 | 319 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 9 | 3108 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 14 | 2248 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 13 | 3647 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 12 | 1741 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 11 | 2489 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 10 | 319 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 9 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 9 | 3108 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 8 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 8 | 440 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 9 | [Large Multi-Modal Model Cartographic Map Comprehension for Textual Locality Georeferencing](https://doi.org/10.4230/lipics.giscience.2025.12) | 2025 | 8 | 2084 | Leibniz-Zentrum für Informatik (Schloss Dagstuhl) | OpenAI |
| 10 | [Durably reducing conspiracy beliefs through dialogues with AI](https://doi.org/10.1126/science.adq1814) | 2024 | 7 | 161 | Science | Thomas H. Costello, Gordon Pennycook, David G. Rand |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Scaling language model size yields diminishing returns for single-message political persuasion](https://doi.org/10.1073/pnas.2413443122) | 2025 | 4 | 9 | Proceedings of the National Academy of Sciences | Kobi Hackenburg, Ben M Tappin, Paul Röttger, et al. |
| 2 | [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://doi.org/10.18653/v1/2025.naacl-long.182) | 2025 | 4 | 9 |  | Hanjie Chen, Zhouxiang Fang, Yash Singla, et al. |
| 3 | [AI Can Be Cognitively Biased: An Exploratory Study on Threshold Priming in LLM-Based Batch Relevance Assessment](https://doi.org/10.1145/3673791.3698420) | 2024 | 3 | 7 |  | Nuo Chen, Jiqun Liu, Xiaoyu Dong, et al. |
| 4 | [MedExQA: Medical Question Answering Benchmark with Multiple Explanations](https://doi.org/10.18653/v1/2024.bionlp-1.14) | 2024 | 3 | 10 |  | Yunsoo Kim, Jinge Wu, Yusuf Abdulle, et al. |
| 5 | [MedBench: A Comprehensive, Standardized, and Reliable Benchmarking System for Evaluating Chinese Medical Large Language Models](https://doi.org/10.26599/bdma.2024.9020044) | 2024 | 4 | 15 | Big Data Mining and Analytics | Mianxin Liu, Weiguo Hu, Jinru Ding, et al. |
| 6 | [On the conversational persuasiveness of GPT-4](https://doi.org/10.1038/s41562-025-02194-6) | 2025 | 4 | 18 | Nature Human Behaviour | Francesco Salvi, Manoel Horta Ribeiro, Riccardo Gallotti, et al. |
| 7 | [Application of large language models in medicine](https://doi.org/10.1038/s44222-025-00279-5) | 2025 | 3 | 23 | Nature Reviews Bioengineering | Fenglin Liu, Hongjian Zhou, 博司 熊谷, et al. |
| 8 | [Impact of large language model (ChatGPT) in healthcare: an umbrella review and evidence synthesis](https://doi.org/10.1186/s12929-025-01131-z) | 2025 | 3 | 27 | Journal of Biomedical Science | Usman Iqbal, Afifa Tanweer, Annisa Ristya Rahmanti, et al. |
| 9 | [Practically Adopting Human Activity Recognition](https://doi.org/10.1145/3570361.3613299) | 2023 | 3 | 40 |  | Huatao Xu, Pengfei Zhou, Rui Tan, et al. |
| 10 | [HEAD-QA: A Healthcare Dataset for Complex Reasoning](https://doi.org/10.18653/v1/p19-1092) | 2019 | 3 | 41 |  | David Vilares, Carlos Gómez‐Rodríguez |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 6 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 2 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 6 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 3 | [Cinematic Clarity is Business Strategy™: A Financial and Neuro-Scientific Proof of the Trust Dividend](https://doi.org/10.5281/zenodo.17814452) | 2025 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 4 | [Architect not Strategist™: A Structural Analysis of the 'Principal-Agent Problem' in the High-Stakes Advisory Market](https://doi.org/10.5281/zenodo.17801032) | 2025 | 6 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 5 | [The Architecture of Conviction™: A Doctrinal Synthesis on Solving Asymmetrical Information in the High-Stakes Advisory Market](https://doi.org/10.5281/zenodo.17815175) | 2025 | 4 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 6 | [An attack-agnostic defense method against adversarial attacks on speaker verification by fusing downsampling and upsampling of speech signals](https://doi.org/10.1016/j.ins.2024.120618) | 2024 | 2 | 1 | Information Sciences | Yihao Li, Xiongwei Zhang, Meng Sun, et al. |
| 7 | [Enhancing cross-domain transferability of black-box adversarial attacks on speaker recognition systems using linearized backpropagation](https://doi.org/10.1007/s10044-024-01269-w) | 2024 | 2 | 1 | Pattern Analysis and Applications | Umang Patel, Shruti Bhilare, Avik Hati |
| 8 | [Pseudo-Siamese Network based Timbre-reserved Black-box Adversarial Attack in Speaker Identification](https://doi.org/10.48550/arxiv.2305.19020) | 2023 | 2 | 1 | arXiv (Cornell University) | Qing Wang, Jixun Yao, Ziqian Wang, et al. |
| 9 | [Parrot-Trained Adversarial Examples: Pushing the Practicality of Black-Box Audio Attacks against Speaker Recognition Models](https://doi.org/10.48550/arxiv.2311.07780) | 2023 | 2 | 2 | arXiv (Cornell University) | Rui Duan, Zhe Qu, Lei Ding, et al. |
| 10 | [Transferable universal adversarial perturbations against speaker recognition systems](https://doi.org/10.1007/s11280-024-01274-3) | 2024 | 2 | 2 | World Wide Web | Xiaochen Liu, Hao Tan, Junjian Zhang, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 6 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 2 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 6 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 3 | [Cinematic Clarity is Business Strategy™: A Financial and Neuro-Scientific Proof of the Trust Dividend](https://doi.org/10.5281/zenodo.17814452) | 2025 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 4 | [Architect not Strategist™: A Structural Analysis of the 'Principal-Agent Problem' in the High-Stakes Advisory Market](https://doi.org/10.5281/zenodo.17801032) | 2025 | 6 | 14 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 5 | [The Architecture of Conviction™: A Doctrinal Synthesis on Solving Asymmetrical Information in the High-Stakes Advisory Market](https://doi.org/10.5281/zenodo.17815175) | 2025 | 4 | 10 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 6 | [An attack-agnostic defense method against adversarial attacks on speaker verification by fusing downsampling and upsampling of speech signals](https://doi.org/10.1016/j.ins.2024.120618) | 2024 | 2 | 1 | Information Sciences | Yihao Li, Xiongwei Zhang, Meng Sun, et al. |
| 7 | [Enhancing cross-domain transferability of black-box adversarial attacks on speaker recognition systems using linearized backpropagation](https://doi.org/10.1007/s10044-024-01269-w) | 2024 | 2 | 1 | Pattern Analysis and Applications | Umang Patel, Shruti Bhilare, Avik Hati |
| 8 | [Pseudo-Siamese Network based Timbre-reserved Black-box Adversarial Attack in Speaker Identification](https://doi.org/10.48550/arxiv.2305.19020) | 2023 | 2 | 1 | arXiv (Cornell University) | Qing Wang, Jixun Yao, Ziqian Wang, et al. |
| 9 | [Parrot-Trained Adversarial Examples: Pushing the Practicality of Black-Box Audio Attacks against Speaker Recognition Models](https://doi.org/10.48550/arxiv.2311.07780) | 2023 | 2 | 2 | arXiv (Cornell University) | Rui Duan, Zhe Qu, Lei Ding, et al. |
| 10 | [Transferable universal adversarial perturbations against speaker recognition systems](https://doi.org/10.1007/s11280-024-01274-3) | 2024 | 2 | 2 | World Wide Web | Xiaochen Liu, Hao Tan, Junjian Zhang, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [An attack-agnostic defense method against adversarial attacks on speaker verification by fusing downsampling and upsampling of speech signals](https://doi.org/10.1016/j.ins.2024.120618) | 2024 | 2 | 1 | Information Sciences | Yihao Li, Xiongwei Zhang, Meng Sun, et al. |
| 2 | [Enhancing cross-domain transferability of black-box adversarial attacks on speaker recognition systems using linearized backpropagation](https://doi.org/10.1007/s10044-024-01269-w) | 2024 | 2 | 1 | Pattern Analysis and Applications | Umang Patel, Shruti Bhilare, Avik Hati |
| 3 | [Pseudo-Siamese Network based Timbre-reserved Black-box Adversarial Attack in Speaker Identification](https://doi.org/10.48550/arxiv.2305.19020) | 2023 | 2 | 1 | arXiv (Cornell University) | Qing Wang, Jixun Yao, Ziqian Wang, et al. |
| 4 | [The Clarity Tax™: Quantifying the Cost of Confusion in Executive Strategy](https://doi.org/10.5281/zenodo.17600790) | 2025 | 6 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 5 | [The Strategic Void™: Diagnosing the Invisible Gap Between Vision and Execution](https://doi.org/10.5281/zenodo.17606968) | 2025 | 6 | 0 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
| 6 | [Parrot-Trained Adversarial Examples: Pushing the Practicality of Black-Box Audio Attacks against Speaker Recognition Models](https://doi.org/10.48550/arxiv.2311.07780) | 2023 | 2 | 2 | arXiv (Cornell University) | Rui Duan, Zhe Qu, Lei Ding, et al. |
| 7 | [Transferable universal adversarial perturbations against speaker recognition systems](https://doi.org/10.1007/s11280-024-01274-3) | 2024 | 2 | 2 | World Wide Web | Xiaochen Liu, Hao Tan, Junjian Zhang, et al. |
| 8 | [Rethinking multi‐spatial information for transferable adversarial attacks on speaker recognition systems](https://doi.org/10.1049/cit2.12295) | 2024 | 2 | 3 | CAAI Transactions on Intelligence Technology | J. Zhang, Hao Tan, Le Wang, et al. |
| 9 | [AdvTTS: Adversarial Text-to-Speech Synthesis Attack on Speaker Identification Systems](https://doi.org/10.1109/icassp48485.2024.10447190) | 2024 | 2 | 3 |  | Chu-Xiao Zuo, Zhi-Jun Jia, Wu-Jun Li |
| 10 | [Cinematic Clarity is Business Strategy™: A Financial and Neuro-Scientific Proof of the Trust Dividend](https://doi.org/10.5281/zenodo.17814452) | 2025 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Idoniwako, Muhammad |
<!-- TRENDING-END -->
