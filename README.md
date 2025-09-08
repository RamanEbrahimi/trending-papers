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

Last update: 2025-09-08 06:21 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 10 | 57281 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 2 | [2023 ESC Guidelines for the management of acute coronary syndromes](https://doi.org/10.1093/eurheartj/ehad191) | 2023 | 8 | 2480 | European Heart Journal | Robert A. Byrne, Xavier Rosselló, J J Coughlan, et al. |
| 3 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 8 | 12930 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 4 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 8 | 78878 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |
| 5 | [Global Cancer Statistics 2020: GLOBOCAN Estimates of Incidence and Mortality Worldwide for 36 Cancers in 185 Countries](https://doi.org/10.3322/caac.21660) | 2021 | 8 | 92356 | CA A Cancer Journal for Clinicians | Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, et al. |
| 6 | [Cytoscape: A Software Environment for Integrated Models of Biomolecular Interaction Networks](https://doi.org/10.1101/gr.1239303) | 2003 | 7 | 45342 | Genome Research | Paul Shannon, Andrew Markiel, Owen Ozier, et al. |
| 7 | [Inference and analysis of cell-cell communication using CellChat](https://doi.org/10.1038/s41467-021-21246-9) | 2021 | 6 | 5266 | Nature Communications | Suoqin Jin, Christian F. Guerrero‐Juarez, Lihua Zhang, et al. |
| 8 | [Global Burden of Cardiovascular Diseases and Risk Factors, 1990–2019](https://doi.org/10.1016/j.jacc.2020.11.010) | 2020 | 6 | 8260 | Journal of the American College of Cardiology | Gregory A. Roth, George A. Mensah, Catherine O. Johnson, et al. |
| 9 | [DADA2: High-resolution sample inference from Illumina amplicon data](https://doi.org/10.1038/nmeth.3869) | 2016 | 6 | 27805 | Nature Methods | Benjamin J. Callahan, Paul J. McMurdie, Michael Rosen, et al. |
| 10 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 6 | 75031 | Organizational Behavior and Human Decision Processes | Icek Ajzen |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 110 | 108482 | Machine Learning | Leo Breiman |
| 2 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 43 | 6063 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 3 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 29 | 30253 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 4 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 29 | 70731 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 5 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 27 | 24691 | The Annals of Statistics | Jerome H. Friedman |
| 6 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 25 | 12209 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 20 | 26090 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 19 | 5939 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 9 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 19 | 85693 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 10 | [Optuna](https://doi.org/10.1145/3292500.3330701) | 2019 | 18 | 4341 |  | Takuya Akiba, Shotaro Sano, Toshihiko Yanase, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 9 | 539 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 7 | 5312 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 3 | [Revolutionizing healthcare: the role of artificial intelligence in clinical practice](https://doi.org/10.1186/s12909-023-04698-z) | 2023 | 6 | 1570 | BMC Medical Education | Shuroug A. Alowais, Sahar S. Alghamdi, Nada Alsuhebany, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 1883 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 13 | 2898 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://doi.org/10.48550/arxiv.1910.10683) | 2019 | 12 | 8400 | arXiv (Cornell University) | Colin Raffel, Noam Shazeer, Adam Roberts, et al. |
| 4 | [Language Models are Few-Shot Learners](https://doi.org/10.48550/arxiv.2005.14165) | 2020 | 11 | 13675 | arXiv (Cornell University) | T. B. Brown, Benjamin F. Mann, Nick Ryder, et al. |
| 5 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 10 | 61440 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 6 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 9 | 2710 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 7 | [BLEU](https://doi.org/10.3115/1073083.1073135) | 2001 | 9 | 19945 |  | Kishore Papineni, Salim Roukos, Todd J. Ward, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1052 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 1723 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 10 | [BioGPT: generative pre-trained transformer for biomedical text generation and mining](https://doi.org/10.1093/bib/bbac409) | 2022 | 7 | 610 | Briefings in Bioinformatics | Renqian Luo, Liai Sun, Yingce Xia, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 16 | 1883 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 2 | [ChatGPT for good? On opportunities and challenges of large language models for education](https://doi.org/10.1016/j.lindif.2023.102274) | 2023 | 13 | 2898 | Learning and Individual Differences | Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. |
| 3 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 9 | 2710 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1052 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 5 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 1723 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 6 | [BioGPT: generative pre-trained transformer for biomedical text generation and mining](https://doi.org/10.1093/bib/bbac409) | 2022 | 7 | 610 | Briefings in Bioinformatics | Renqian Luo, Liai Sun, Yingce Xia, et al. |
| 7 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 7 | 1537 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 8 | [Survey of Hallucination in Natural Language Generation](https://doi.org/10.1145/3571730) | 2022 | 7 | 1798 | ACM Computing Surveys | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 2646 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [Training language models to follow instructions with human feedback](https://doi.org/10.48550/arxiv.2203.02155) | 2022 | 7 | 3056 | arXiv (Cornell University) | Long Ouyang, Jeff Wu, Xu Jiang, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [OneLLM: One Framework to Align All Modalities with Language](https://doi.org/10.1109/cvpr52733.2024.02510) | 2024 | 3 | 19 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Jiaming Han, Kaixiong Gong, Yiyuan Zhang, et al. |
| 2 | [Large Language Models and Empathy: Systematic Review (Preprint)](https://doi.org/10.2196/52597) | 2024 | 5 | 34 | Journal of Medical Internet Research | Vera Sorin, Dana Brin, Yiftach Barash, et al. |
| 3 | [Devising and Detecting Phishing Emails Using Large Language Models](https://doi.org/10.1109/access.2024.3375882) | 2024 | 3 | 24 | IEEE Access | Fredrik Heiding, Bruce Schneier, Arun Vishwanath, et al. |
| 4 | [ONCE: Boosting Content-based Recommendation with Both Open- and Closed-source Large Language Models](https://doi.org/10.1145/3616855.3635845) | 2024 | 3 | 47 |  | Qijiong Liu, Nuo Chen, Tetsuya Sakai, et al. |
| 5 | [Assessing ChatGPT 4.0’s test performance and clinical diagnostic accuracy on USMLE STEP 2 CK and clinical case reports](https://doi.org/10.1038/s41598-024-58760-x) | 2024 | 3 | 53 | Scientific Reports | Allen Shieh, Brandon Q. Tran, Gene He, et al. |
| 6 | [Development of a liver disease–specific large language model chat interface using retrieval-augmented generation](https://doi.org/10.1097/hep.0000000000000834) | 2024 | 3 | 67 | Hepatology | Jin Ge, Steve Sun, Joseph F. Owens, et al. |
| 7 | [Optimization of hepatological clinical guidelines interpretation by large language models: a retrieval augmented generation-based framework](https://doi.org/10.1038/s41746-024-01091-y) | 2024 | 3 | 85 | npj Digital Medicine | Simone Kresevic, Mauro Giuffrè, Miloš Ajčević, et al. |
| 8 | [Intern VL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](https://doi.org/10.1109/cvpr52733.2024.02283) | 2024 | 3 | 89 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Zhe Chen, Jiannan Wu, Wenhai Wang, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Rent-seeking analysis of carbon emission verification based on game theory and prospect theory from the perspective of multi-participation](https://doi.org/10.1016/j.jclepro.2024.140784) | 2024 | 2 | 9 | Journal of Cleaner Production | Xingkai Yong, Yao Tao, Yunna Wu, et al. |
| 2 | [Game analysis of carbon emission verification: A case study from Shenzhen's cap-and-trade system in China](https://doi.org/10.1016/j.enpol.2019.04.024) | 2019 | 2 | 33 | Energy Policy | Yanchun Pan, Wen Yang, Nan Ma, et al. |
| 3 | [Evaluation of effectiveness of China's carbon emissions trading scheme in carbon mitigation](https://doi.org/10.1016/j.eneco.2020.104872) | 2020 | 2 | 328 | Energy Economics | Yuning Gao, Meng Li, Jinjun Xue, et al. |
| 4 | [Evolutionary Selection in Normal-Form Games](https://doi.org/10.2307/2171774) | 1995 | 2 | 411 | Econometrica | Klaus Ritzberger, Jörgen W. Weibull |
| 5 | [A note on evolutionarily stable strategies in asymmetric animal conflicts](https://doi.org/10.1016/s0022-5193(80)81038-1) | 1980 | 2 | 531 | Journal of Theoretical Biology | Reinhard Selten |
| 6 | [Foundations of Game-Based Learning](https://doi.org/10.1080/00461520.2015.1122533) | 2015 | 2 | 1226 | Educational Psychologist | Jan L. Plass, Bruce D. Homer, Charles K. Kinzer |
| 7 | [Evolutionary Games in Economics](https://doi.org/10.2307/2938222) | 1991 | 2 | 1736 | Econometrica | Daniel Friedman |
| 8 | [Advances in prospect theory: Cumulative representation of uncertainty](https://doi.org/10.1007/bf00122574) | 1992 | 2 | 14702 | Journal of Risk and Uncertainty | Amos Tversky, Daniel Kahneman |
| 9 | [Intrinsic Motivation and Self-Determination in Human Behavior](https://doi.org/10.1007/978-1-4899-2271-7) | 1985 | 2 | 24007 | Springer eBooks | Edward L. Deci, Richard M. Ryan |
| 10 | [Situated Learning](https://doi.org/10.1017/cbo9780511815355) | 1991 | 2 | 29155 |  | Jean Lave, Étienne Wenger |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Rent-seeking analysis of carbon emission verification based on game theory and prospect theory from the perspective of multi-participation](https://doi.org/10.1016/j.jclepro.2024.140784) | 2024 | 2 | 9 | Journal of Cleaner Production | Xingkai Yong, Yao Tao, Yunna Wu, et al. |
| 2 | [Untitled](https://doi.org/10.7752/jpes.2023.10292) | 2023 | 1 | 1 | Journal of Physical Education and Sport | Spyridon Plakias, Xenofon Betsios, Vasileios Kalapotharakos |
| 3 | [Prediction of the Opponents Actions in Soccer Simulation based on Location of Players](https://doi.org/10.1109/scm62608.2024.10554216) | 2024 | 1 | 1 |  | Dmitrij A. Petrunenko, Sergej A. Belyaev |
| 4 | [Assessing Creativity in Basketball Performance Using Game Theory](https://doi.org/10.1016/j.tsc.2024.101696) | 2024 | 1 | 1 | Thinking Skills and Creativity | Zahra Shariati, Rasoul Yaali, Abbas Bahram |
| 5 | [Expert and novice soccer goalkeepers’ visual perception: a practical-coaching approach eye-tracking](https://doi.org/10.1080/24748668.2024.2428541) | 2024 | 1 | 1 | International Journal of Performance Analysis in Sport | Katarzyna Piechota, Zbigniew Borysiuk, D. Zmarzły, et al. |
| 6 | [The principles of tactical formation identification in association football (soccer) — a survey](https://doi.org/10.3389/fspor.2024.1512386) | 2025 | 1 | 1 | Frontiers in Sports and Active Living | Hadi Sotudeh |
| 7 | [Emerging Technology and Interactive Feedback](https://doi.org/10.4324/9781003226659-2) | 2023 | 1 | 0 | Routledge eBooks | Andrew Butterworth |
| 8 | [Basketball Game Theory Analyzes the Choice](https://doi.org/10.2991/978-94-6463-098-5_2) | 2023 | 1 | 0 | Advances in economics, business and management research/Advances in Economics, Business and Management Research | Boqian Deng |
| 9 | [Nash Equilibria and Undecidability in Generic Physical Interactions—A Free Energy Perspective](https://doi.org/10.3390/g15050030) | 2024 | 1 | 0 | Games | Chris Fields, James F. Glazebrook |
| 10 | [Exploring decision-making practices during coaching sessions in grassroots youth soccer: a mixed-methods study](https://doi.org/10.1080/24733938.2024.2399011) | 2024 | 1 | 0 | Science and Medicine in Football | André Roca, Chris Pocock, Paul R. Ford |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [On the Solutions of Games in Normal Forms: Particular Models based on Nash Equilibrium Theory](https://doi.org/10.2478/mjss-2019-0035) | 2019 | 1 | 1 | Mediterranean Journal of Social Sciences | Gabriel Turbay, Giovanni E. Reyes |
| 2 | [Untitled](https://doi.org/10.7752/jpes.2023.10292) | 2023 | 1 | 1 | Journal of Physical Education and Sport | Spyridon Plakias, Xenofon Betsios, Vasileios Kalapotharakos |
| 3 | [Prediction of the Opponents Actions in Soccer Simulation based on Location of Players](https://doi.org/10.1109/scm62608.2024.10554216) | 2024 | 1 | 1 |  | Dmitrij A. Petrunenko, Sergej A. Belyaev |
| 4 | [Assessing Creativity in Basketball Performance Using Game Theory](https://doi.org/10.1016/j.tsc.2024.101696) | 2024 | 1 | 1 | Thinking Skills and Creativity | Zahra Shariati, Rasoul Yaali, Abbas Bahram |
| 5 | [Expert and novice soccer goalkeepers’ visual perception: a practical-coaching approach eye-tracking](https://doi.org/10.1080/24748668.2024.2428541) | 2024 | 1 | 1 | International Journal of Performance Analysis in Sport | Katarzyna Piechota, Zbigniew Borysiuk, D. Zmarzły, et al. |
| 6 | [The principles of tactical formation identification in association football (soccer) — a survey](https://doi.org/10.3389/fspor.2024.1512386) | 2025 | 1 | 1 | Frontiers in Sports and Active Living | Hadi Sotudeh |
| 7 | [Emerging Technology and Interactive Feedback](https://doi.org/10.4324/9781003226659-2) | 2023 | 1 | 0 | Routledge eBooks | Andrew Butterworth |
| 8 | [Basketball Game Theory Analyzes the Choice](https://doi.org/10.2991/978-94-6463-098-5_2) | 2023 | 1 | 0 | Advances in economics, business and management research/Advances in Economics, Business and Management Research | Boqian Deng |
| 9 | [Nash Equilibria and Undecidability in Generic Physical Interactions—A Free Energy Perspective](https://doi.org/10.3390/g15050030) | 2024 | 1 | 0 | Games | Chris Fields, James F. Glazebrook |
| 10 | [Exploring decision-making practices during coaching sessions in grassroots youth soccer: a mixed-methods study](https://doi.org/10.1080/24733938.2024.2399011) | 2024 | 1 | 0 | Science and Medicine in Football | André Roca, Chris Pocock, Paul R. Ford |
<!-- TRENDING-END -->
