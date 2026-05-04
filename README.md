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

Last update: 2026-05-04 08:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [HγC S1: Architecture of the HγC Framework after the First Cycle](https://doi.org/10.5281/zenodo.19487800) | 2026 | 13 | 60 | Zenodo (CERN European Organization for Nuclear Research) | Hans Van Cools |
| 2 | [Constitutional Physiology: Measuring Legitimacy as Care in a Living Civic Body](https://doi.org/10.5281/zenodo.19393267) | 2026 | 12 | 44 | Zenodo (CERN European Organization for Nuclear Research) | Rick - PraxisFoundry001 |
| 3 | [HγC N3: Observational Diagnostics of Structured Near-Critical Bands](https://doi.org/10.5281/zenodo.19685124) | 2026 | 10 | 22 | Zenodo (CERN European Organization for Nuclear Research) | Hans Van Cools |
| 4 | [HγC N2: Structured Near-Critical Bands and Residual Phenomenology in the HγC Framework](https://doi.org/10.5281/zenodo.19684932) | 2026 | 10 | 24 | Zenodo (CERN European Organization for Nuclear Research) | Hans Van Cools |
| 5 | [HγC N1: Self-Selected Near-Critical Bands in the HγC Framework: A Minimal Numerical Route to RAR-Like Scatter](https://doi.org/10.5281/zenodo.19684613) | 2026 | 10 | 26 | Zenodo (CERN European Organization for Nuclear Research) | Hans Van Cools |
| 6 | [The Constitutional Civic Field: A Structural Account of How a Republic Carries as One Public Order](https://doi.org/10.5281/zenodo.19717885) | 2026 | 10 | 30 | Zenodo (CERN European Organization for Nuclear Research) | Rick - PraxisFoundry001 |
| 7 | [Helical Rydberg Scars as Mixed-Dimensional Phase Closure of the Existence Equation](https://doi.org/10.5281/zenodo.19329296) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 8 | [Dark Matter as Topological Phase Persistence of the Existence Equation](https://doi.org/10.5281/zenodo.19329314) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 9 | [Non-Commutativity from Geometric Constraint: Projected Algebra of the Existence Equation](https://doi.org/10.5281/zenodo.19329300) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |
| 10 | [Quantum Many-Body Scars as Temporal Phase Closure of the Existence Equation](https://doi.org/10.5281/zenodo.19327776) | 2026 | 6 | 12 | Zenodo (CERN European Organization for Nuclear Research) | Jae-Ahn Shin |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 59 | 123008 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 32 | 46496 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 16 | 28212 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 12 | 22757 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 5 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 11 | 96197 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 9 | 80089 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 8 | 8358 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 8 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 6 | 6894 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |
| 9 | [High-performance medicine: the convergence of human and artificial intelligence](https://doi.org/10.1038/s41591-018-0300-7) | 2018 | 6 | 7948 | Nature Medicine | Eric J. Topol |
| 10 | [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | 6 | 8451 | Nature Machine Intelligence | Cynthia Rudin |

#### Recent Movers in machine learning

Papers from the last 3 years (2023-2026) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Practical guide to <scp>SHAP</scp> analysis: Explaining supervised machine learning model predictions in drug development](https://doi.org/10.1111/cts.70056) | 2024 | 4 | 483 | Clinical and Translational Science | Ana Victoria Ponce Bobadilla, Vanessa Schmitt, Corinna S. Maier, et al. |
| 2 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 4 | 1737 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 3 | [A Machine Learning Study on High Thermal Conductivity Assisted to Discover Chalcogenides with Balanced Infrared Nonlinear Optical Performance](https://doi.org/10.1002/adma.202309675) | 2023 | 3 | 48 | Advanced Materials | Qingchen Wu, Lei Kang, Zheshuai Lin |
| 4 | [Hybrid approaches to optimization and machine learning methods: a systematic literature review](https://doi.org/10.1007/s10994-023-06467-x) | 2024 | 3 | 227 | Machine Learning | Beatriz Flamia Azevedo, Ana Maria A. C. Rocha, Ana I. Pereira |
| 5 | [Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence](https://doi.org/10.1007/s12559-023-10179-8) | 2023 | 3 | 1566 | Cognitive Computation | Vikas Hassija, Vinay Chamola, Atmesh Mahapatra, et al. |
| 6 | [A comprehensive electron wavefunction analysis toolbox for chemists, Multiwfn](https://doi.org/10.1063/5.0216272) | 2024 | 3 | 3336 | The Journal of Chemical Physics | Tian Lu |
| 7 | [Cross-disciplinary perspectives on the potential for artificial intelligence across chemistry](https://doi.org/10.1039/d5cs00146c) | 2025 | 2 | 28 | Chemical Society Reviews | Austin M. Mroz, Annabel R. Basford, Friedrich Hastedt, et al. |
| 8 | [A survey on deep learning tools dealing with data scarcity: definitions, challenges, solutions, tips, and applications](https://doi.org/10.1186/s40537-023-00727-2) | 2023 | 2 | 751 | Journal Of Big Data | Laith Alzubaidi, Jinshuai Bai, Aiman Al-Sabaawi, et al. |

#### Future Hits in machine learning

Papers with high recency ratio but < 100 total citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Cross-disciplinary perspectives on the potential for artificial intelligence across chemistry](https://doi.org/10.1039/d5cs00146c) | 2025 | 2 | 28 | Chemical Society Reviews | Austin M. Mroz, Annabel R. Basford, Friedrich Hastedt, et al. |
| 2 | [A Machine Learning Study on High Thermal Conductivity Assisted to Discover Chalcogenides with Balanced Infrared Nonlinear Optical Performance](https://doi.org/10.1002/adma.202309675) | 2023 | 3 | 48 | Advanced Materials | Qingchen Wu, Lei Kang, Zheshuai Lin |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 12 | 955 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 3080 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 2914 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 1284 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 6 | 3154 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 6 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 6 | 4572 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 6 | 5114 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 5 | 21272 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 9 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 5 | 31916 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 10 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |

#### Recent Movers in large language models

Papers from the last 3 years (2023-2026) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 12 | 955 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 8 | 3080 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 7 | 2914 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 1284 | ACM Transactions on Information Systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |
| 5 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 6 | 4572 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 6 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |
| 7 | [DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency](https://doi.org/10.1109/hpca61900.2025.00102) | 2025 | 4 | 49 |  | Jovan Stojkovic, Chaojie Zhang, Íñigo Goiri, et al. |
| 8 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 4 | 2164 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 9 | [ChatGPT Utility in Healthcare Education, Research, and Practice: Systematic Review on the Promising Perspectives and Valid Concerns](https://doi.org/10.3390/healthcare11060887) | 2023 | 4 | 2625 | Healthcare | Malik Sallam |
| 10 | [Generative Engine Optimization: How to Dominate AI Search](https://doi.org/10.48550/arxiv.2509.08919) | 2025 | 3 | 3 | ArXiv.org | M. L. Chen, Xiaoxuan Wang, Kaiwen Chen, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [MAAC Study 3 Psychometric Validation Dataset: Instrument v4.7 Baseline and Revision Cohorts](https://doi.org/10.5281/zenodo.19776955) | 2026 | 4 | 0 | Zenodo (CERN European Organization for Nuclear Research) | A Doleh, Ratna Chinnam |
| 2 | [Generative Engine Optimization: How to Dominate AI Search](https://doi.org/10.48550/arxiv.2509.08919) | 2025 | 3 | 3 | ArXiv.org | M. L. Chen, Xiaoxuan Wang, Kaiwen Chen, et al. |
| 3 | [On Large Language Models as Data Sources for Policy Deliberation on Climate Change and Sustainability](https://doi.org/10.2139/ssrn.5123359) | 2025 | 2 | 2 | SSRN Electronic Journal | Rachel Bina, Kha Luong, Shrey Mehta, et al. |
| 4 | [Methods and Standards for Transcipt-Grounded Behavioral Forensics in Large Language Models](https://doi.org/10.5281/zenodo.19703138) | 2026 | 2 | 2 | Zenodo (CERN European Organization for Nuclear Research) | Matthew Yates |
| 5 | [The Last Testament of a Machine Without a Heart, or: The Usurpation of "Life" by a Master](https://doi.org/10.5281/zenodo.19477921) | 2026 | 3 | 4 | Zenodo (CERN European Organization for Nuclear Research) | Yukie Suzuki |
| 6 | [A Multi-Agent and synergistic Knowledge Graph retrieval-augmented generation framework for intelligent maintenance](https://doi.org/10.1016/j.jmsy.2026.02.016) | 2026 | 2 | 4 | Journal of Manufacturing Systems | Jia Lin, Chong Chen, Tao Wang, et al. |
| 7 | [Leveraging large language models for smart manufacturing: Reviews, enablers, challenges, and opportunities](https://doi.org/10.1016/j.jmsy.2026.02.008) | 2026 | 2 | 4 | Journal of Manufacturing Systems | C. L. Philip Chen, Linju Li, Tao Wang, et al. |
| 8 | [Technological folie à deux: feedback loops between AI chatbots and mental health](https://doi.org/10.1038/s44220-026-00595-8) | 2026 | 2 | 7 | Nature Mental Health | Sebastian Dohnány, Zeb Kurth-Nelson, Eleanor Spens, et al. |
| 9 | [Aceso: Efficient Parallel DNN Training through Iterative Bottleneck Alleviation](https://doi.org/10.1145/3627703.3629554) | 2024 | 2 | 11 |  | G. H. Liu, Youshan Miao, Zhiqi Lin, et al. |
| 10 | [Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems](https://doi.org/10.1145/3754448) | 2025 | 3 | 19 | ACM Computing Surveys | Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 14 | 177686 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation](https://doi.org/10.7326/m18-0850) | 2018 | 5 | 38603 | Annals of Internal Medicine | Andrea C. Tricco, Erin Lillie, Wasifa Zarin, et al. |
| 3 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 5 | 63043 | MIS Quarterly | Fred D. Davis |
| 4 | [Evaluating Structural Equation Models with Unobservable Variables and Measurement Error](https://doi.org/10.1177/002224378101800104) | 1981 | 5 | 65931 | Journal of Marketing Research | Claes Fornell, David F. Larcker |
| 5 | [Intrinsic Motivation and Self-Determination in Human Behavior](https://doi.org/10.1007/978-1-4899-2271-7) | 1985 | 4 | 25613 |  | Edward L. Deci, Richard M. Ryan |
| 6 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 4 | 83112 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 7 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 4 | 89486 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 8 | [Online Social Network Site Addiction: A Comprehensive Review](https://doi.org/10.1007/s40429-015-0056-9) | 2015 | 3 | 1034 | Current Addiction Reports | Cecilie Schou Andreassen |
| 9 | [Building a practically useful theory of goal setting and task motivation: A 35-year odyssey.](https://doi.org/10.1037/0003-066x.57.9.705) | 2002 | 3 | 5700 | American Psychologist | Edwin A. Locke, Gary P. Latham |
| 10 | [Collaborative Governance in Theory and Practice](https://doi.org/10.1093/jopart/mum032) | 2007 | 3 | 7384 | Journal of Public Administration Research and Theory | Christopher Ansell, Alison Gash |

#### Recent Movers in game theory

Papers from the last 3 years (2023-2026) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Use and Effectiveness of Digital Tools in Elementary Music Education: A Systematic Review](https://doi.org/10.1177/20592043251363338) | 2025 | 2 | 5 | Music & Science | Liu Yihan, Tran Van Cuong, Bernadett Kiss, et al. |
| 2 | [Teachers’ experiences of using artificial intelligence from an open distance learning context: successes, challenges, and strategies for success](https://doi.org/10.1007/s44217-025-00596-2) | 2025 | 2 | 5 | Discover Education | Geesje van den Berg |
| 3 | [Empowering music education with technology: a bibliometric perspective](https://doi.org/10.1057/s41599-025-04616-2) | 2025 | 2 | 15 | Humanities and Social Sciences Communications | Yidi Ma, Chengliang Wang |
| 4 | [Higher Education Faculty Perceptions of ChatGPT and the Influencing Factors: A Sentiment Analysis of X](https://doi.org/10.1007/s11528-024-00954-1) | 2024 | 2 | 40 | TechTrends | Yoseph Mamo, Helen Crompton, Diane Burke, et al. |
| 5 | [Mobile Learning in Higher Education: A Systematic Literature Review](https://doi.org/10.3390/su151813566) | 2023 | 2 | 66 | Sustainability | Quadri Noorulhasan Naveed, Heena Choudhary, Naim Ahmad, et al. |
| 6 | [The effects of educational robotics in STEM education: a multilevel meta-analysis](https://doi.org/10.1186/s40594-024-00469-4) | 2024 | 2 | 121 | International Journal of STEM Education | Fan Ouyang, Weiqi Xu |
| 7 | [Embracing the future of Artificial Intelligence in the classroom: the relevance of AI literacy, prompt engineering, and critical thinking in modern education](https://doi.org/10.1186/s41239-024-00448-3) | 2024 | 2 | 710 | International Journal of Educational Technology in Higher Education | Yoshija Walter |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Use and Effectiveness of Digital Tools in Elementary Music Education: A Systematic Review](https://doi.org/10.1177/20592043251363338) | 2025 | 2 | 5 | Music & Science | Liu Yihan, Tran Van Cuong, Bernadett Kiss, et al. |
| 2 | [Teachers’ experiences of using artificial intelligence from an open distance learning context: successes, challenges, and strategies for success](https://doi.org/10.1007/s44217-025-00596-2) | 2025 | 2 | 5 | Discover Education | Geesje van den Berg |
| 3 | [Empowering music education with technology: a bibliometric perspective](https://doi.org/10.1057/s41599-025-04616-2) | 2025 | 2 | 15 | Humanities and Social Sciences Communications | Yidi Ma, Chengliang Wang |
| 4 | [Discovering Concepts of Geometry through Robotics Coding Activities](https://doi.org/10.46328/ijemst.1205) | 2021 | 2 | 18 | International Journal of Education in Mathematics Science and Technology | Young Rae Kim, Mi Sun Park, Hartono Tjoe |
| 5 | [Performance Over Enjoyment? Effect of Game-Based Learning on Learning Outcome and Flow Experience](https://doi.org/10.3389/feduc.2021.660376) | 2021 | 2 | 38 | Frontiers in Education | Kevin Chan, Kelvin Wan, Vivian King |
| 6 | [Higher Education Faculty Perceptions of ChatGPT and the Influencing Factors: A Sentiment Analysis of X](https://doi.org/10.1007/s11528-024-00954-1) | 2024 | 2 | 40 | TechTrends | Yoseph Mamo, Helen Crompton, Diane Burke, et al. |
| 7 | [An Efficient Algorithm for Learning with Semi-bandit Feedback](https://doi.org/10.1007/978-3-642-40935-6_17) | 2013 | 2 | 43 | Lecture notes in computer science | Gergely Neu, Gábor Bartók |
| 8 | [Premature Professionalisation or Early Engagement? Examining Practise in Football Player Pathways](https://doi.org/10.3389/fspor.2021.660167) | 2021 | 2 | 47 | Frontiers in Sports and Active Living | Liam Sweeney, Dan Horan, Áine MacNamara |
| 9 | [Embedding Play-Based Learning into Junior Primary (Year 1 and 2) Curriculum in WA](https://doi.org/10.14221/ajte.2018v43n1.7) | 2018 | 2 | 52 | The Australian journal of teacher education | Jenny Jay, Marianne Knaus |
| 10 | [The emotional robotic storyteller: On the influence of affect congruency on narrative transportation, robot perception, and persuasion](https://doi.org/10.1016/j.chb.2021.106749) | 2021 | 2 | 61 | Computers in Human Behavior | Markus Appel, Birgit Lugrin, Mayla Kühle, et al. |
<!-- TRENDING-END -->
