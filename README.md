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

Last update: 2026-03-16 07:08 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Why Strong Governance Still Drifts: How Institutions Quietly Lose Alignment](https://doi.org/10.5281/zenodo.18471068) | 2026 | 12 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 2 | [The Field Protocol: Measuring Translation Coherence in Institutional Systems](https://doi.org/10.5281/zenodo.18657810) | 2026 | 12 | 45 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 3 | [The Sovereign Spine: How Institutions Stay True to Their Intent Over Time](https://doi.org/10.5281/zenodo.18646691) | 2026 | 12 | 47 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 4 | [Prologue – The Green Dashboard Trap: How Institutions Lose Sight of Their Intent](https://doi.org/10.5281/zenodo.18641907) | 2026 | 11 | 43 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 5 | [The Sovereign Spine: A New Theory of Institutional Coherence and Agency](https://doi.org/10.5281/zenodo.18649453) | 2026 | 11 | 43 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 6 | [AI-Augmented Impact Frames: A Closed-Loop Architecture for Purpose-Aligned Decisions](https://doi.org/10.5281/zenodo.18668799) | 2026 | 11 | 43 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 7 | [How Decision Systems Learn What Matters: Building Purpose-Aligned Governance](https://doi.org/10.5281/zenodo.17964280) | 2026 | 11 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 8 | [Designing the Meaning Infrastructure: Governing Interpretation in AI-Driven Institutions](https://doi.org/10.5281/zenodo.18494690) | 2026 | 11 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 9 | [Making Meaning Measurable: How to See Coherence in Decision Systems](https://doi.org/10.5281/zenodo.18486778) | 2026 | 11 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Robin Edgard Ulrik Mertens |
| 10 | [Bootstrap Foundations: The Geometric Origin of Dimensionless Constants](https://doi.org/10.5281/zenodo.18085101) | 2026 | 9 | 40 | Zenodo (CERN European Organization for Nuclear Research) | Clifford Keeble |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 84 | 120453 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 65 | 44904 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 19 | 27618 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 16 | 22231 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 16 | 31956 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 15 | 7907 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 7 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 15 | 78757 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 8 | [Machine learning: Trends, perspectives, and prospects](https://doi.org/10.1126/science.aaa8415) | 2015 | 13 | 9187 | Science | Michael I. Jordan, Tom M. Mitchell |
| 9 | [A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting](https://doi.org/10.1006/jcss.1997.1504) | 1997 | 12 | 19917 | Journal of Computer and System Sciences | Yoav Freund, Robert E. Schapire |
| 10 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 12 | 29851 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 11 | 1459 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 8 | 13104 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 3 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 5 | 20225 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 4 | [Random Forest Algorithm Overview](https://doi.org/10.58496/bjml/2024/007) | 2024 | 4 | 407 | Babylonian Journal of Machine Learning | Hasan Ahmed Salman, Ali Kalakech, Amani Steiti |
| 5 | [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6) | 2025 | 4 | 416 | Nature | Noah Hollmann, Samuel Müller, Lennart Purucker, et al. |
| 6 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 4 | 1422 | Cognitive Computation | Vikas Hassija, Vinay Chamola, A. Mahapatra, et al. |
| 7 | [Cancer statistics, 2023](https://doi.org/10.3322/caac.21763) | 2023 | 4 | 16219 | CA A Cancer Journal for Clinicians | Rebecca L. Siegel, Kimberly D. Miller, Nikita Sandeep Wagle, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 21 | 2711 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 11 | 2905 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 3 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4800 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 4 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 10 | 837 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 5 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2916 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 6 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 4253 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 7 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 8 | 564 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 8 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1109 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 9 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 2159 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 10 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 8 | 76965 | Biometrics | J. Richard Landis, Gary G. Koch |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 21 | 2711 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 10 | 837 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2916 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 10 | 4253 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 5 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 8 | 564 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 6 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 8 | 1109 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 7 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 2159 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 8 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 7 | 41 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 9 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 7 | 525 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 10 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 3324 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [I Was Blind but Now I See: Implementing Vision-Enabled Dialogue in Social Robots](https://doi.org/10.1109/hri61500.2025.10973830) | 2025 | 3 | 7 |  | Giulio Antonio Abbo, Tony Belpaeme |
| 2 | [Evaluating Urban Visual Attractiveness Perception Using Multimodal Large Language Model and Street View Images](https://doi.org/10.3390/buildings15162970) | 2025 | 3 | 10 | Buildings | Qiaogen Zhou, Jiaxin Zhang, Zehong Zhu |
| 3 | [Assessing the accuracy of the GPT-4 model in multidisciplinary tumor board decision prediction](https://doi.org/10.1007/s12094-025-03905-1) | 2025 | 3 | 11 | Clinical & Translational Oncology | Efe Cem Erdat, Merih Yalçıner, Mehmet Berk Örüncü, et al. |
| 4 | [Utility of Artificial Intelligence for Decision Making in Thoracic Multidisciplinary Tumor Boards](https://doi.org/10.3390/jcm14020399) | 2025 | 3 | 14 | Journal of Clinical Medicine | Jon Zabaleta, Borja Aguinagalde, Iker López, et al. |
| 5 | [ChatGPT's Gastrointestinal Tumor Board Tango: A limping dance partner?](https://doi.org/10.1016/j.ejca.2024.114100) | 2024 | 4 | 23 | European Journal of Cancer | Ughur Aghamaliyev, Javad Karimbayli, Clemens Gießen-Jung, et al. |
| 6 | [QLoRA: Efficient Finetuning of Quantized LLMs](https://doi.org/10.52202/075280-0441) | 2023 | 7 | 41 |  | Tim Dettmers, Ari J. Holtzman, Artidoro Pagnoni, et al. |
| 7 | [LLM-generated messages can persuade humans on policy issues](https://doi.org/10.1038/s41467-025-61345-5) | 2025 | 3 | 23 | Nature Communications | Hui Bai, Jan G. Voelkel, Shane Muldowney, et al. |
| 8 | [Limitations of the LLM-as-a-Judge Approach for Evaluating LLM Outputs in Expert Knowledge Tasks](https://doi.org/10.1145/3708359.3712091) | 2025 | 4 | 37 |  | Annalisa Szymanski, Noah Ziems, Heather A. Eicher‐Miller, et al. |
| 9 | [Large Language Model Prompting Techniques for Advancement in Clinical Medicine](https://doi.org/10.3390/jcm13175101) | 2024 | 5 | 55 | Journal of Clinical Medicine | Krish Shah, Andrew Xu, Yatharth Sharma, et al. |
| 10 | [Generative Expressive Robot Behaviors using Large Language Models](https://doi.org/10.1145/3610977.3634999) | 2024 | 4 | 47 |  | Karthik Mahadevan, Jonathan Chien, Noah Brown, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 35 | 85343 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 34 | 173056 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 14 | 44904 |  | Tianqi Chen, Carlos Guestrin |
| 4 | [Naturalistic inquiry](https://doi.org/10.1016/0147-1767(85)90062-8) | 1985 | 12 | 32394 | International Journal of Intercultural Relations | Yvonna S. Lincoln, Egon G. Guba, Joseph J. Pilotta |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 9 | 7907 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [Reflecting on reflexive thematic analysis](https://doi.org/10.1080/2159676x.2019.1628806) | 2019 | 8 | 15341 | Qualitative Research in Sport Exercise and Health | Virginia Braun, Victoria Clarke |
| 7 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 8 | 37186 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 8 | [G*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences](https://doi.org/10.3758/bf03193146) | 2007 | 8 | 61640 | Behavior Research Methods | Franz Faul, Edgar Erdfelder, Albert-Georg Lang, et al. |
| 9 | [Fitting Linear Mixed-Effects Models Using <b>lme4</b>](https://doi.org/10.18637/jss.v067.i01) | 2015 | 8 | 82135 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |
| 10 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 8 | 120453 | Machine Learning | Leo Breiman |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 5 | 13104 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee, Ribot, Pauline, et al. |
| 2 | [Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy](https://doi.org/10.1016/j.ijinfomgt.2023.102642) | 2023 | 4 | 3309 | International Journal of Information Management | Yogesh K. Dwivedi, Nir Kshetri, Laurie Hughes, et al. |
| 3 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 4 | 4253 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
<!-- TRENDING-END -->
