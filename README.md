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

Last update: 2026-08-10 07:17 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [morphe-metrics: A Stateless Python Library for Morphogenetic Computing Evaluation](https://doi.org/10.5281/zenodo.20107083) | 2026 | 37 | 139 | Open MIND | Venkatesh Swaminathan |
| 2 | [Nociceptive Metaplasticity and Graceful Decay in Spiking Neural Networks: Towards Survival-Driven Continual Learning](https://doi.org/10.5281/zenodo.19151562) | 2026 | 35 | 129 | Open MIND | Venkatesh Swaminathan |
| 3 | [Maya-CL: Nociceptive Metaplasticity and Vairagya-Governed Heterosynaptic Decay for Continual Learning in Spiking Neural Networks](https://doi.org/10.5281/zenodo.19201768) | 2026 | 35 | 129 | Open MIND | Swaminathan, Venkatesh |
| 4 | [Maya-Manas: Oscillatory Thalamo-Cortical Gating for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19363005) | 2026 | 35 | 130 | Open MIND | Venkatesh Swaminathan |
| 5 | [Maya-Śūnyatā: Karma-Weighted Synaptic Pruning for Class-Incremental Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19397010) | 2026 | 35 | 130 | Open MIND | Venkatesh Swaminathan |
| 6 | [Maya-Prana: Metabolic Plasticity Budget for Continual Learning in Affective Spiking Neural Networks](https://doi.org/10.5281/zenodo.19451173) | 2026 | 35 | 130 | Open MIND | Venkatesh Swaminathan |
| 7 | [maya-metrics: A Stateless Python Library for Affective Neuromorphic Evaluation in Continual Learning SNNs](https://doi.org/10.5281/zenodo.19553204) | 2026 | 35 | 130 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 8 | [Maya-LLM-Defence: Sovereign Military LLM with Affective SNN Safety Substrate](https://doi.org/10.5281/zenodo.19708800) | 2026 | 35 | 130 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |
| 9 | [cl-metrics: A Stateless Python Library for Continual Learning Evaluation with SNN Energy-Aware Extensions](https://doi.org/10.5281/zenodo.19389017) | 2026 | 35 | 131 | Open MIND | Venkatesh Swaminathan |
| 10 | [Maya-OS: An Affective Spiking Neural Network as a Conversational Operating System Arbitration Layer](https://doi.org/10.5281/zenodo.19160122) | 2026 | 34 | 128 | Zenodo (CERN European Organization for Nuclear Research) | Venkatesh Swaminathan |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 138 | 129101 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 82 | 50622 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 48 | 29652 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 30 | 9528 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 23 | 23965 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 20 | 31862 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 7 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 20 | 33539 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 8 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 17 | 99840 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 9 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 15 | 2710 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 10 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 15 | 9513 | Nature Machine Intelligence | Cynthia Rudin |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 15 | 2710 | BMJ | Professor Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 9 | 761 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 3 | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | 8 | 785 | Patterns | Sayash Kapoor, Arvind Narayanan |
| 4 | [PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods](https://doi.org/10.1136/bmj-2024-082505) | 2025 | 6 | 529 | BMJ | Karel G.M. Moons, Johanna AAG Damen, T. K. Kaul, et al. |
| 5 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 6 | 687 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 6 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 6 | 776 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 7 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 5 | 653 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 8 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 4 | 5234 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Chain-Of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.52202/068431-1800) | 2022 | 23 | 1221 |  | Jason Wei, Xuezhi Wang, Dale Schuurmans, et al. |
| 2 | [Training Language Models to Follow Instructions with Human Feedback](https://doi.org/10.52202/068431-2011) | 2022 | 21 | 675 |  | Long Ouyang, Jeffrey Wu, Xu Jiang, et al. |
| 3 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 20 | 3923 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 4 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3567 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 5 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 14 | 33118 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 6 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 13 | 768 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 7 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://doi.org/10.18653/v1/d19-1410) | 2019 | 13 | 11373 |  | Nils Reimers, Iryna Gurevych |
| 8 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 12 | 457 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 9 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 12 | 516 |  | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 10 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 12 | 607 |  | Haotian Liu, Chunyuan Li, Qingyang Wu, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 14 | 3567 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 13 | 768 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 3 | [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | 12 | 457 |  | Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al. |
| 4 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 12 | 516 |  | Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, et al. |
| 5 | [Visual Instruction Tuning](https://doi.org/10.52202/075280-1516) | 2023 | 12 | 607 |  | Haotian Liu, Chunyuan Li, Qingyang Wu, et al. |
| 6 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 3479 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 7 | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://doi.org/10.52202/075280-2997) | 2023 | 8 | 207 |  | Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, et al. |
| 8 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://doi.org/10.52202/075280-2338) | 2023 | 8 | 214 |  | Rafael Rafailov, Archit Sharma, Eric Mitchell, et al. |
| 9 | [The TRIPOD-LLM reporting guideline for studies using large language models](https://doi.org/10.1038/s41591-024-03425-5) | 2025 | 8 | 424 | Nature Medicine | Jack Gallifant, Majid Afshar, Saleem Ameen, et al. |
| 10 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 8 | 824 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [HybridFlow: A Flexible and Efficient RLHF Framework](https://doi.org/10.1145/3689031.3696075) | 2025 | 6 | 39 |  | Guangming Sheng, Chi Zhang, Zilingfeng Ye, et al. |
| 2 | [One Fits All: Power General Time Series Analysis by Pretrained LM](https://doi.org/10.52202/075280-1877) | 2023 | 5 | 82 |  | Tian Zhou, Peisong Niu, Xue Wang, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 28 | 188549 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 25 | 129101 | Machine Learning | Leo Breiman |
| 3 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 17 | 50622 |  | Tianqi Chen, Carlos Guestrin |
| 4 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 17 | 78469 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |
| 5 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 16 | 100349 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 6 | [Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives](https://doi.org/10.1080/10705519909540118) | 1999 | 15 | 106962 | Structural Equation Modeling A Multidisciplinary Journal | Li‐tze Hu, Peter M. Bentler |
| 7 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 14 | 86168 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 8 | [Naturalistic inquiry](https://doi.org/10.1016/0147-1767(85)90062-8) | 1985 | 10 | 35212 | International Journal of Intercultural Relations | Yvonna S. Lincoln, Egon G. Guba, Joseph J. Pilotta |
| 9 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 10 | 65893 | MIS Quarterly | Fred D. Davis |
| 10 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 10 | 69589 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
<!-- TRENDING-END -->
