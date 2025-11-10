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

Last update: 2025-11-10 06:23 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Purpose in Life as a System that Creates and Sustains Health and Well-Being: An Integrative, Testable Theory](https://doi.org/10.1037/a0017152) | 2009 | 10 | 878 | Review of General Psychology | Patrick E. McKnight, Todd B. Kashdan |
| 2 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 90027 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 3 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 7 | 73882 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 4 | [Viewing Purpose Through an Eriksonian Lens](https://doi.org/10.1080/15283488.2012.632394) | 2012 | 6 | 92 | Identity | Patrick L. Hill, Anthony L. Burrow |
| 5 | [Purpose as a form of identity capital for positive youth adjustment.](https://doi.org/10.1037/a0023818) | 2011 | 6 | 219 | Developmental Psychology | Anthony L. Burrow, Patrick L. Hill |
| 6 | [Profiles of a Developmental Asset: Youth Purpose as a Context for Hope and Well-Being](https://doi.org/10.1007/s10964-009-9481-1) | 2009 | 6 | 226 | Journal of Youth and Adolescence | Anthony L. Burrow, Amanda C. O’Dell, Patrick L. Hill |
| 7 | [The Power of the Archive and its Limits](https://doi.org/10.1007/978-94-010-0570-8_2) | 2002 | 6 | 498 |  | Achille Mbembé |
| 8 | [Happiness is everything, or is it? Explorations on the meaning of psychological well-being.](https://doi.org/10.1037/0022-3514.57.6.1069) | 1989 | 6 | 12626 | Journal of Personality and Social Psychology | Carol D. Ryff |
| 9 | [STAR: ultrafast universal RNA-seq aligner](https://doi.org/10.1093/bioinformatics/bts635) | 2012 | 6 | 50701 | Bioinformatics | Alexander Dobin, Carrie Davis, Felix Schlesinger, et al. |
| 10 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 6 | 159853 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 90 | 113526 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 80 | 40230 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 29 | 74807 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 4 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 25 | 26032 | The Annals of Statistics | Jerome H. Friedman |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 20 | 6827 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 19 | 89439 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 17 | 27973 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 14 | 20888 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 9 | ["Why Should I Trust You?"](https://doi.org/10.1145/2939672.2939778) | 2016 | 13 | 13014 |  | Marco Túlio Ribeiro, Sameer Singh, Carlos Guestrin |
| 10 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 13 | 30651 | Machine Learning | Corinna Cortes, Vladimir Vapnik |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 10 | 12829 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 2 | [MizAR 60 for Mizar 50](https://doi.org/10.4230/lipics.itp.2023.19) | 2023 | 7 | 69414 | Leibniz-Zentrum für Informatik (Schloss Dagstuhl) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 3 | [Ethical and Bias Considerations in Artificial Intelligence/Machine Learning](https://doi.org/10.1016/j.modpat.2024.100686) | 2024 | 5 | 167 | Modern Pathology | Matthew G. Hanna, Liron Pantanowitz, Brian Jackson, et al. |
| 4 | [Machine learning for the prediction of acute kidney injury in patients with sepsis](https://doi.org/10.1186/s12967-022-03364-0) | 2022 | 5 | 266 | Journal of Translational Medicine | Suru Yue, Shasha Li, Xueying Huang, et al. |
| 5 | [A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME](https://doi.org/10.1002/aisy.202400304) | 2024 | 5 | 281 | Advanced Intelligent Systems | Ahmed Salih, Zahra Raisi‐Estabragh, Ilaria Boscolo Galazzo, et al. |
| 6 | [Small data machine learning in materials science](https://doi.org/10.1038/s41524-023-01000-z) | 2023 | 5 | 470 | npj Computational Materials | Pengcheng Xu, Xiaobo Ji, Minjie Li, et al. |
| 7 | [Extracting spatial effects from machine learning model using local interpretation method: An example of SHAP and XGBoost](https://doi.org/10.1016/j.compenvurbsys.2022.101845) | 2022 | 5 | 683 | Computers Environment and Urban Systems | Ziqi Li |
| 8 | [Evaluation metrics and statistical tests for machine learning](https://doi.org/10.1038/s41598-024-56706-x) | 2024 | 4 | 585 | Scientific Reports | Oona Rainio, Jarmo Teuho, Riku Klén |
| 9 | [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336) | 2023 | 4 | 752 | Science | Rémi Lam, Álvaro Sánchez‐González, Matthew Willson, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 10 | 1624 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2361 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 2131 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 7 | 407 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 5 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 2030 | Leibniz-Zentrum für Informatik (Schloss Dagstuhl) | OpenAI |
| 6 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 6 | 3023 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 7 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 6 | 4062 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 8 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 2960 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 9 | [AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models](https://doi.org/10.18653/v1/2024.findings-naacl.149) | 2024 | 4 | 92 |  | Wanjun Zhong, Ruixiang Cui, Yiduo Guo, et al. |
| 10 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 4 | 530 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 10 | 1624 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2361 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 2131 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 4 | [Adapted large language models can outperform medical experts in clinical text summarization](https://doi.org/10.1038/s41591-024-02855-5) | 2024 | 7 | 407 | Nature Medicine | Dave Van Veen, Cara Van Uden, Louis Blankemeier, et al. |
| 5 | [GPT-4 Technical Report](https://doi.org/10.48550/arxiv.2303.08774) | 2023 | 7 | 2030 | Leibniz-Zentrum für Informatik (Schloss Dagstuhl) | OpenAI |
| 6 | [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://doi.org/10.1145/3560815) | 2022 | 6 | 3023 | ACM Computing Surveys | Pengfei Liu, Weizhe Yuan, Jinlan Fu, et al. |
| 7 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 5 | 2960 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 8 | [AGIEval: A Human-Centric Benchmark for Evaluating Foundation Models](https://doi.org/10.18653/v1/2024.findings-naacl.149) | 2024 | 4 | 92 |  | Wanjun Zhong, Ruixiang Cui, Yiduo Guo, et al. |
| 9 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 4 | 530 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 10 | [Evolutionary-scale prediction of atomic-level protein structure with a language model](https://doi.org/10.1126/science.ade2574) | 2023 | 4 | 3448 | Science | Zeming Lin, Halil Akin, Roshan Rao, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Authors’ Response to Peer Reviews of “Assessing the Limitations of Large Language Models in Clinical Practice Guideline–Concordant Treatment Decision-Making on Real-World Data: Retrospective Study”](https://doi.org/10.2196/84173) | 2025 | 3 | 3 | JMIRx Med | Tobias Roeschl, Marie Hoffmann, Djawid Hashemi, et al. |
| 2 | [Case to Vignette: A Framework to Elevate Narrative by Embracing Vignette-Based Learning in Medicine](https://doi.org/10.1007/s11606-025-09531-5) | 2025 | 2 | 2 | Journal of General Internal Medicine | Shannon K. Martin, Mary Ann Kirkconnell Hall, Ethan Molitch-Hou, et al. |
| 3 | [Scenario-Driven Evaluation of Autonomous Agents: Integrating Large Language Model for UAV Mission Reliability](https://doi.org/10.3390/drones9030213) | 2025 | 2 | 8 | Drones | Anıl Sezgin |
| 4 | [How do large language models answer breast cancer quiz questions? A comparative study of GPT-3.5, GPT-4 and Google Gemini](https://doi.org/10.1007/s11547-024-01872-1) | 2024 | 2 | 11 | La radiologia medica | Giovanni Irmici, Andrea Cozzi, Gianmarco Della Pepa, et al. |
| 5 | [ChatGPT's Gastrointestinal Tumor Board Tango: A limping dance partner?](https://doi.org/10.1016/j.ejca.2024.114100) | 2024 | 3 | 18 | European Journal of Cancer | Ughur Aghamaliyev, Javad Karimbayli, Clemens Gießen-Jung, et al. |
| 6 | [ChatGPT-4o can serve as the second rater for data extraction in systematic reviews](https://doi.org/10.1371/journal.pone.0313401) | 2025 | 3 | 20 | PLoS ONE | M. Jensen, Mathias Brix Danielsen, Johannes Riis, et al. |
| 7 | [ProKnow: Process knowledge for safety constrained and explainable question generation for mental health diagnostic assistance](https://doi.org/10.3389/fdata.2022.1056728) | 2023 | 2 | 17 | Frontiers in Big Data | Kaushik Roy, Manas Gaur, Misagh Soltani, et al. |
| 8 | [Llama 3 Challenges Proprietary State-of-the-Art Large Language Models in Radiology Board–style Examination Questions](https://doi.org/10.1148/radiol.241191) | 2024 | 2 | 23 | Radiology | Lisa C. Adams, Daniel Truhn, Felix Busch, et al. |
| 9 | [TheoremQA: A Theorem-driven Question Answering Dataset](https://doi.org/10.18653/v1/2023.emnlp-main.489) | 2023 | 2 | 26 |  | Wenhu Chen, Ming Yin, Max Ku, et al. |
| 10 | [Performance of two large language models for data extraction in evidence synthesis](https://doi.org/10.1002/jrsm.1732) | 2024 | 3 | 40 | Research Synthesis Methods | Amanda Konet, Ian B. Thomas, Gerald Gartlehner, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary game and LGPSO for attack-defense confrontation analysis in WSN from macro perspective](https://doi.org/10.1016/j.eswa.2024.125815) | 2024 | 2 | 3 | Expert Systems with Applications | Ning Liu, Shangkun Liu, Wei-Min Zheng |
| 2 | [Mobile advergames in tourism marketing](https://doi.org/10.1177/1356766710380882) | 2010 | 2 | 52 | Journal Of Vacation Marketing | Evrim Çeltek |
| 3 | [How do the electricity market and carbon market interact and achieve integrated development?--A bibliometric-based review](https://doi.org/10.1016/j.energy.2022.126308) | 2022 | 2 | 58 | Energy | Yan Li, Tiantian Feng, Liu Lili, et al. |
| 4 | [Gamification for Crowdsourcing Marketing Practices: Applications and Benefits in Tourism](https://doi.org/10.1007/978-3-319-18341-1_11) | 2015 | 2 | 71 |  | Μαριάννα Σιγάλα |
| 5 | [Can gamification improve the virtual reality tourism experience? Analyzing the mediating role of tourism fatigue](https://doi.org/10.1016/j.tourman.2022.104715) | 2023 | 2 | 95 | Tourism Management | Zhenda Wei, Jingru Zhang, Xiaoting Huang, et al. |
| 6 | [Gamification in tourism and hospitality research in the era of digital platforms: a systematic literature review](https://doi.org/10.1108/jstp-05-2020-0094) | 2021 | 2 | 105 | Journal of Service Theory and Practice | Maria Giovina Pasca, Maria Francesca Renzi, Laura Di Pietro, et al. |
| 7 | [The application and impact of gamification funware on trip planning and experiences: the case of TripAdvisor’s funware](https://doi.org/10.1007/s12525-014-0179-1) | 2015 | 2 | 163 | Electronic Markets | Μαριάννα Σιγάλα |
| 8 | [Meeting the needs of the Millennials and Generation Z: gamification in tourism through geocaching](https://doi.org/10.1108/jtf-12-2017-0060) | 2018 | 2 | 163 | Journal of Tourism Futures | Heather Skinner, David Sarpong, Gareth White |
| 9 | [Serious games and the gamification of tourism](https://doi.org/10.1016/j.tourman.2016.11.020) | 2016 | 2 | 478 | Tourism Management | Feifei Xu, Dimitrios Buhalis, Jessika Weber |
| 10 | [Gamification in theory and action: A survey](https://doi.org/10.1016/j.ijhcs.2014.09.006) | 2014 | 2 | 2251 | International Journal of Human-Computer Studies | Katie Seaborn, Deborah I. Fels |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary game and LGPSO for attack-defense confrontation analysis in WSN from macro perspective](https://doi.org/10.1016/j.eswa.2024.125815) | 2024 | 2 | 3 | Expert Systems with Applications | Ning Liu, Shangkun Liu, Wei-Min Zheng |
| 2 | [How do the electricity market and carbon market interact and achieve integrated development?--A bibliometric-based review](https://doi.org/10.1016/j.energy.2022.126308) | 2022 | 2 | 58 | Energy | Yan Li, Tiantian Feng, Liu Lili, et al. |
| 3 | [Can gamification improve the virtual reality tourism experience? Analyzing the mediating role of tourism fatigue](https://doi.org/10.1016/j.tourman.2022.104715) | 2023 | 2 | 95 | Tourism Management | Zhenda Wei, Jingru Zhang, Xiaoting Huang, et al. |
| 4 | [Game Theory](https://doi.org/10.1007/978-3-031-37574-3) | 2023 | 1 | 2 |  | Ana Espínola‐Arredondo, Félix Muñoz-García |
| 5 | [An Analytical Approach to Bimonotone Linear Inequalities and Sublattice Structures](https://doi.org/10.58496/bjm/2025/003) | 2025 | 1 | 2 | Babylonian Journal of Mathematics | Nematollah Kadkhoda, Mostafa Abotaleb |
| 6 | [Explainable Artificial Intelligence with Integrated Gradients for the Detection of Adversarial Attacks on Text Classifiers](https://doi.org/10.3390/asi8010017) | 2025 | 1 | 2 | Applied System Innovation | Harsha Moraliyage, Geemini Kulawardana, Daswin De Silva, et al. |
| 7 | [GCPNet: Gradient-aware channel pruning network with bilateral coupled sampling strategy](https://doi.org/10.1016/j.eswa.2024.126104) | 2024 | 1 | 2 | Expert Systems with Applications | Ziyang Zhang, Chuqing Cao, Fangjun Zheng, et al. |
| 8 | [EVONChain: a bi-tiered public blockchain network architecture](https://doi.org/10.1007/s12083-023-01562-1) | 2023 | 1 | 3 | Peer-to-Peer Networking and Applications | Yihan Kong, Jing Li, Ting Xiong, et al. |
| 9 | [Machine Learning Basics: A Comprehensive Guide. A Review](https://doi.org/10.58496/bjml/2023/006) | 2023 | 1 | 3 | Babylonian Journal of Machine Learning | Alok Singh Chauhan, H. Mary Henrietta |
| 10 | [Explainable AI: Methods, Challenges, and Future Directions](https://doi.org/10.58496/adsa/2025/001) | 2025 | 1 | 3 | Applied Data Science and Analysis | Ahmed Hussein Ali, Marwan Ali Shnan |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary game and LGPSO for attack-defense confrontation analysis in WSN from macro perspective](https://doi.org/10.1016/j.eswa.2024.125815) | 2024 | 2 | 3 | Expert Systems with Applications | Ning Liu, Shangkun Liu, Wei-Min Zheng |
| 2 | [Game Theory](https://doi.org/10.1007/978-3-031-37574-3) | 2023 | 1 | 2 |  | Ana Espínola‐Arredondo, Félix Muñoz-García |
| 3 | [An Analytical Approach to Bimonotone Linear Inequalities and Sublattice Structures](https://doi.org/10.58496/bjm/2025/003) | 2025 | 1 | 2 | Babylonian Journal of Mathematics | Nematollah Kadkhoda, Mostafa Abotaleb |
| 4 | [Explainable Artificial Intelligence with Integrated Gradients for the Detection of Adversarial Attacks on Text Classifiers](https://doi.org/10.3390/asi8010017) | 2025 | 1 | 2 | Applied System Innovation | Harsha Moraliyage, Geemini Kulawardana, Daswin De Silva, et al. |
| 5 | [GCPNet: Gradient-aware channel pruning network with bilateral coupled sampling strategy](https://doi.org/10.1016/j.eswa.2024.126104) | 2024 | 1 | 2 | Expert Systems with Applications | Ziyang Zhang, Chuqing Cao, Fangjun Zheng, et al. |
| 6 | [EVONChain: a bi-tiered public blockchain network architecture](https://doi.org/10.1007/s12083-023-01562-1) | 2023 | 1 | 3 | Peer-to-Peer Networking and Applications | Yihan Kong, Jing Li, Ting Xiong, et al. |
| 7 | [Machine Learning Basics: A Comprehensive Guide. A Review](https://doi.org/10.58496/bjml/2023/006) | 2023 | 1 | 3 | Babylonian Journal of Machine Learning | Alok Singh Chauhan, H. Mary Henrietta |
| 8 | [Explainable AI: Methods, Challenges, and Future Directions](https://doi.org/10.58496/adsa/2025/001) | 2025 | 1 | 3 | Applied Data Science and Analysis | Ahmed Hussein Ali, Marwan Ali Shnan |
| 9 | [Optimizing Decision Tree Classifiers for Healthcare Predictions: A Comparative Analysis of Model Depth, Pruning, and Performance](https://doi.org/10.58496/mjaih/2025/013) | 2025 | 1 | 3 | Mesopotamian Journal of Artificial Intelligence in Healthcare | Hussein Alkattan, Alhumaima Ali Subhi, Mohammed Shakir Mohmood, et al. |
| 10 | [Improved Banzhaf Value Based on Participant’s Triangular Fuzzy Number-Weighted Excess Contributions and Its Application in Manufacturing Supply Chain Coalitions](https://doi.org/10.3390/sym16121593) | 2024 | 1 | 3 | Symmetry | Jia-Cai Liu, Shiying Liu, Rongji Lai, et al. |
<!-- TRENDING-END -->
