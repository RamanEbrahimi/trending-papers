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

Last update: 2025-12-22 06:26 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Catch and Non-catch-related Determinants of Where Anglers Fish: A Review of Three Decades of Site Choice Research in Recreational Fisheries](https://doi.org/10.1080/23308249.2019.1583166) | 2019 | 13 | 112 | Reviews in Fisheries Science & Aquaculture | Len M. Hunt, Ed Camp, Brett T. van Poorten, et al. |
| 2 | [Understanding and Managing Freshwater Recreational Fisheries as Complex Adaptive Social-Ecological Systems](https://doi.org/10.1080/23308249.2016.1209160) | 2016 | 11 | 217 | Reviews in Fisheries Science & Aquaculture | Robert Arlinghaus, Josep Alós, Ben Beardmore, et al. |
| 3 | [Illustrating the critical role of human dimensions research for understanding and managing recreational fisheries within a social‐ecological system framework](https://doi.org/10.1111/j.1365-2400.2012.00870.x) | 2013 | 10 | 233 | Fisheries Management and Ecology | Len M. Hunt, Stephen G. Sutton, Robert Arlinghaus |
| 4 | [Managing Climate Change Refugia for Climate Adaptation](https://doi.org/10.1371/journal.pone.0159909) | 2016 | 10 | 499 | PLoS ONE | Toni Lyn Morelli, Christopher Daly, Solomon Z. Dobrowski, et al. |
| 5 | [Digital Data Mining](https://doi.org/10.1007/978-3-031-99739-6_15) | 2025 | 9 | 10 | Fish & fisheries series/Fish and fisheries series (Print) | Paul Venturelli, Christian Skov, Asta Audzijonytė, et al. |
| 6 | [Managing climate-change refugia to prevent extinctions](https://doi.org/10.1016/j.tree.2024.05.002) | 2024 | 9 | 33 | Trends in Ecology & Evolution | Gunnar Keppel, Diana Stralberg, Toni Lyn Morelli, et al. |
| 7 | [Quantitative and Qualitative Content Analysis of Text and Images](https://doi.org/10.1007/978-3-031-99739-6_17) | 2025 | 8 | 8 | Fish & fisheries series/Fish and fisheries series (Print) | Sophia Kochalski, Fanny Barz, Pablo Pita, et al. |
| 8 | [Measurement Instruments](https://doi.org/10.1007/978-3-031-99739-6_12) | 2025 | 8 | 8 | Fish & fisheries series/Fish and fisheries series (Print) | Gerard T. Kyle, Adam C. Landon, Daniel G. Pilgreen, et al. |
| 9 | [Resource Economics for Understanding Recreational Fishers and Fisheries](https://doi.org/10.1007/978-3-031-99739-6_5) | 2025 | 8 | 8 | Fish & fisheries series/Fish and fisheries series (Print) | Richard T. Melstrom, Brenna Jungers, Xiang Bi, et al. |
| 10 | [Understanding and Managing Social–Ecological Feedbacks in Spatially Structured Recreational Fisheries: The Overlooked Behavioral Dimension](https://doi.org/10.1080/03632415.2016.1207632) | 2016 | 8 | 76 | Fisheries | Hillary G. M. Ward, Micheal S. Allen, Edward V. Camp, et al. |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Random Forests](https://doi.org/10.1023/a:1010933404324) | 2001 | 105 | 115020 | Machine Learning | Leo Breiman |
| 2 | [XGBoost](https://doi.org/10.1145/2939672.2939785) | 2016 | 73 | 41264 |  | Tianqi Chen, Carlos Guestrin |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 30 | 26394 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 24 | 7090 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 5 | [Support-Vector Networks](https://doi.org/10.1023/a:1022627411411) | 1995 | 23 | 30942 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 21 | 198843 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 7 | [Efficient iterative schemes for<i>ab initio</i>total-energy calculations using a plane-wave basis set](https://doi.org/10.1103/physrevb.54.11169) | 1996 | 16 | 113005 | Physical review. B, Condensed matter | Georg Kresse, J. Furthmüller |
| 8 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 15 | 21175 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 9 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 14 | 28400 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 10 | [Nearest neighbor pattern classification](https://doi.org/10.1109/tit.1967.1053964) | 1967 | 13 | 14946 | IEEE Transactions on Information Theory | Thomas M. Cover, Peter E. Hart |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods](https://doi.org/10.1136/bmj-2023-078378) | 2024 | 8 | 982 | BMJ | Gary S. Collins, Karel G.M. Moons, Paula Dhiman, et al. |
| 2 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 7 | 17361 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 3 | [GPUMD: A package for constructing accurate machine-learned potentials and performing highly efficient atomistic simulations](https://doi.org/10.1063/5.0106617) | 2022 | 6 | 297 | The Journal of Chemical Physics | Zheyong Fan, Yanzhou Wang, Penghua Ying, et al. |
| 4 | [An improved random forest based on the classification accuracy and correlation measurement of decision trees](https://doi.org/10.1016/j.eswa.2023.121549) | 2023 | 6 | 340 | Expert Systems with Applications | Zhigang Sun, Guotao Wang, Pengfei Li, et al. |
| 5 | [CHGNet as a pretrained universal neural network potential for charge-informed atomistic modelling](https://doi.org/10.1038/s42256-023-00716-3) | 2023 | 6 | 510 | Nature Machine Intelligence | Bowen Deng, Peichen Zhong, KyuJung Jun, et al. |
| 6 | [MIMIC-IV, a freely accessible electronic health record dataset](https://doi.org/10.1038/s41597-022-01899-x) | 2023 | 6 | 2040 | Scientific Data | Alistair E. W. Johnson, Lucas Bulgarelli, Lu Shen, et al. |
| 7 | [On a Method to Measure Supervised Multiclass Model’s Interpretability: Application to Degradation Diagnosis (Short Paper)](https://doi.org/10.4230/oasics.dx.2024.27) | 2024 | 6 | 12892 | Dagstuhl Research Online Publication Server | Scott Lundberg, Su‐In Lee |
| 8 | [Association between the stress hyperglycemia ratio and 28-day all-cause mortality in critically ill patients with sepsis: a retrospective cohort study and predictive model establishment based on machine learning](https://doi.org/10.1186/s12933-024-02265-4) | 2024 | 5 | 126 | Cardiovascular Diabetology | Fengjuan Yan, Xiehui Chen, Xiao‐Qing Quan, et al. |
| 9 | [A Survey of Ensemble Learning: Concepts, Algorithms, Applications, and Prospects](https://doi.org/10.1109/access.2022.3207287) | 2022 | 5 | 876 | IEEE Access | Ibomoiye Domor Mienye, Yanxia Sun |
| 10 | [The STRING database in 2023: protein–protein association networks and functional enrichment analyses for any sequenced genome of interest](https://doi.org/10.1093/nar/gkac1000) | 2022 | 5 | 6702 | Nucleic Acids Research | Damian Szklarczyk, Rebecca Kirsch, Mikaela Koutrouli, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 2248 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | 2021 | 11 | 4223 |  | Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, et al. |
| 3 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 4 | [The Measurement of Observer Agreement for Categorical Data](https://doi.org/10.2307/2529310) | 1977 | 10 | 74977 | Biometrics | J. Richard Landis, Gary G. Koch |
| 5 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1741 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 6 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 8 | 1844 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 7 | [Untitled](https://doi.org/10.18653/v1/n19-1423) | 2019 | 8 | 30394 |  | Jacob Devlin, Ming‐Wei Chang, Kenton Lee, et al. |
| 8 | [Benefits, Limits, and Risks of GPT-4 as an AI Chatbot for Medicine](https://doi.org/10.1056/nejmsr2214184) | 2023 | 7 | 1379 | New England Journal of Medicine | Peter Lee, Sébastien Bubeck, Joseph Petro |
| 9 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 10 | [A new readability yardstick.](https://doi.org/10.1037/h0057532) | 1948 | 7 | 4937 | Journal of Applied Psychology | Rudolph Flesch |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 12 | 2248 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 2 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 10 | 2502 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 3 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 8 | 1741 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 4 | [Comparing Physician and Artificial Intelligence Chatbot Responses to Patient Questions Posted to a Public Social Media Forum](https://doi.org/10.1001/jamainternmed.2023.1838) | 2023 | 8 | 1844 | JAMA Internal Medicine | John W. Ayers, Adam Poliak, Mark Dredze, et al. |
| 5 | [Benefits, Limits, and Risks of GPT-4 as an AI Chatbot for Medicine](https://doi.org/10.1056/nejmsr2214184) | 2023 | 7 | 1379 | New England Journal of Medicine | Peter Lee, Sébastien Bubeck, Joseph Petro |
| 6 | [Performance of ChatGPT on USMLE: Potential for AI-assisted medical education using large language models](https://doi.org/10.1371/journal.pdig.0000198) | 2023 | 7 | 3039 | PLOS Digital Health | Tiffany H. Kung, Morgan Cheatham, Arielle Medenilla, et al. |
| 7 | [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://doi.org/10.1038/s41586-025-09422-z) | 2025 | 6 | 82 | Nature | Daya Guo, Dejian Yang, Haowei Zhang, et al. |
| 8 | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | 6 | 319 | Nature Medicine | K. K. Singhal, Tao Tu, Juraj Gottweis, et al. |
| 9 | [Large Language Model Influence on Diagnostic Reasoning](https://doi.org/10.1001/jamanetworkopen.2024.40969) | 2024 | 6 | 324 | JAMA Network Open | Ethan Goh, Robert Gallo, Jason Hom, et al. |
| 10 | [Large Multi-Modal Model Cartographic Map Comprehension for Textual Locality Georeferencing](https://doi.org/10.4230/lipics.giscience.2025.12) | 2025 | 6 | 2094 | Leibniz-Zentrum für Informatik (Schloss Dagstuhl) | OpenAI |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Towards an AI co-scientist](https://doi.org/10.48550/arxiv.2502.18864) | 2025 | 3 | 2 | arXiv (Cornell University) | Juraj Gottweis, Wei‐Hung Weng, Alexander Daryin, et al. |
| 2 | [The effect of medical explanations from large language models on diagnostic decisions in radiology](https://doi.org/10.1101/2025.03.04.25323357) | 2025 | 3 | 3 | bioRxiv (Cold Spring Harbor Laboratory) | Philipp Spitzer, Dirk Hendriks, Jan Rudolph, et al. |
| 3 | [Dental Trauma Evo – Development of an Artificial Intelligence-powered Chatbot to Support Professional Management of Dental Trauma](https://doi.org/10.1016/j.joen.2025.05.012) | 2025 | 3 | 4 | Journal of Endodontics | Diulia Pereira Bubna, Pedro Felipe de Jesus Freitas, Aline Xavier Ferraz, et al. |
| 4 | [How People Use ChatGPT](https://doi.org/10.3386/w34255) | 2025 | 3 | 8 |  | Aaron Chatterji, Thomas Cunningham, David Deming, et al. |
| 5 | [Evidence-Based Analysis of AI Chatbots in Oncology Patient Education: Implications for Trust, Perceived Realness, and Misinformation Management](https://doi.org/10.1007/s13187-025-02592-4) | 2025 | 3 | 10 | Journal of Cancer Education | Aaron Lawson McLean, Vagelis Hristidis |
| 6 | [Evaluating the clinical benefits of LLMs](https://doi.org/10.1038/s41591-024-03181-6) | 2024 | 3 | 14 | Nature Medicine | Suhana Bedi, Sneha S. Jain, Nigam H. Shah |
| 7 | [A framework for evaluating the chemical knowledge and reasoning abilities of large language models against the expertise of chemists](https://doi.org/10.1038/s41557-025-01815-x) | 2025 | 3 | 19 | Nature Chemistry | A.H. Mirza, Nawaf Alampara, Sreekanth Kunchapu, et al. |
| 8 | [The Illusion of Thinking](https://doi.org/10.70777/si.v2i6.15919) | 2025 | 3 | 22 | SuperIntelligence - Robotics - Safety & Alignment | Parshin Shojaee, Iman Mirzadeh, Keivan Alizadeh, et al. |
| 9 | [DeepSeek versus ChatGPT: Multimodal artificial intelligence revolutionizing scientific discovery. From language editing to autonomous content generation—Redefining innovation in research and practice](https://doi.org/10.1002/ksa.12628) | 2025 | 4 | 32 | Knee Surgery Sports Traumatology Arthroscopy | Mahmut Enes Kayaalp, Robert Prill, Erdem Aras Sezgin, et al. |
| 10 | [Can AI tell good stories? Narrative transportation and persuasion with ChatGPT](https://doi.org/10.1093/joc/jqae029) | 2024 | 3 | 29 | Journal of Communication | Haoran Chu, Sixiao Liu |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Video Game Influences on Aggression, Cognition, and Attention](https://doi.org/10.1007/978-3-319-95495-0) | 2018 | 2 | 39 |  | Christopher J. Ferguson |
| 2 | [Applications of evolutionary game theory in urban road transport network: A state of the art review](https://doi.org/10.1016/j.scs.2023.104791) | 2023 | 2 | 64 | Sustainable Cities and Society | Furkan Ahmad, Zubair Shah, Luluwah Al‐Fagih |
| 3 | [A Comprehensive Review of Cable Monitoring Techniques for Nuclear Power Plants](https://doi.org/10.3390/en18092333) | 2025 | 1 | 1 | Energies | Allan Ghaforian, Patrick Duggan, Lixuan Lu |
| 4 | [The Use of Comparative Multi-Criteria Analysis Methods to Evaluate Criteria Weighting in Assessments of Onshore Wind Farm Projects](https://doi.org/10.3390/en18040771) | 2025 | 1 | 1 | Energies | Dimitra Vagiona |
| 5 | [Selection model for domains across time: application to labour force survey by economic activities](https://doi.org/10.1007/s11749-020-00712-4) | 2020 | 1 | 0 | Test | María José Lombardía, Esther López‐Vizcaíno, Cristina Rueda |
| 6 | [Condition-Based Maintenance in Complex Degradation Systems: A Review of Modeling Evolution, Multi-Component Systems, and Maintenance Strategies](https://doi.org/10.3390/machines13080714) | 2025 | 1 | 0 | Machines | Hui Cao, Jie Yu, Fuhai Duan |
| 7 | [Analysis of internal defects in power cables based on temperature field simulation](https://doi.org/10.54254/2977-3903/10/2024112) | 2024 | 1 | 0 | Advances in Engineering Innovation | Zhe Li |
| 8 | [A Review of Partial Discharge Electrical Localization Techniques in Power Cables: Practical Approaches and Circuit Models](https://doi.org/10.3390/en18102583) | 2025 | 1 | 2 | Energies | Mohammad Alqtish, Alessio Di Fatta, Giuseppe Rizzo, et al. |
| 9 | [Evaluating Water Resource Management in the Transboundary Rio Grande/Bravo using Cooperative Game Theory](https://doi.org/10.1061/41114(371)227) | 2010 | 1 | 3 |  | Rebecca Teasley, Daene C. McKinney |
| 10 | [Transformer Fault Diagnosis and Location Method Based on Fault Tree Analysis](https://doi.org/10.12694/scpe.v25i5.3182) | 2024 | 1 | 3 | Scalable Computing Practice and Experience | Zhiwu Wu, Tianfu Huang, Chunguang Wang, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Applications of evolutionary game theory in urban road transport network: A state of the art review](https://doi.org/10.1016/j.scs.2023.104791) | 2023 | 2 | 64 | Sustainable Cities and Society | Furkan Ahmad, Zubair Shah, Luluwah Al‐Fagih |
| 2 | [A Comprehensive Review of Cable Monitoring Techniques for Nuclear Power Plants](https://doi.org/10.3390/en18092333) | 2025 | 1 | 1 | Energies | Allan Ghaforian, Patrick Duggan, Lixuan Lu |
| 3 | [The Use of Comparative Multi-Criteria Analysis Methods to Evaluate Criteria Weighting in Assessments of Onshore Wind Farm Projects](https://doi.org/10.3390/en18040771) | 2025 | 1 | 1 | Energies | Dimitra Vagiona |
| 4 | [Condition-Based Maintenance in Complex Degradation Systems: A Review of Modeling Evolution, Multi-Component Systems, and Maintenance Strategies](https://doi.org/10.3390/machines13080714) | 2025 | 1 | 0 | Machines | Hui Cao, Jie Yu, Fuhai Duan |
| 5 | [Analysis of internal defects in power cables based on temperature field simulation](https://doi.org/10.54254/2977-3903/10/2024112) | 2024 | 1 | 0 | Advances in Engineering Innovation | Zhe Li |
| 6 | [A Review of Partial Discharge Electrical Localization Techniques in Power Cables: Practical Approaches and Circuit Models](https://doi.org/10.3390/en18102583) | 2025 | 1 | 2 | Energies | Mohammad Alqtish, Alessio Di Fatta, Giuseppe Rizzo, et al. |
| 7 | [Transformer Fault Diagnosis and Location Method Based on Fault Tree Analysis](https://doi.org/10.12694/scpe.v25i5.3182) | 2024 | 1 | 3 | Scalable Computing Practice and Experience | Zhiwu Wu, Tianfu Huang, Chunguang Wang, et al. |
| 8 | [Partial Discharge Signal Pattern Recognition of Composite Insulation Defects in Cross-Linked Polyethylene Cables](https://doi.org/10.3390/s24113460) | 2024 | 1 | 3 | Sensors | Chunxu Qin, Xiaokai Zhu, Pengfei Zhu, et al. |
| 9 | [Risk Assessment Model for Converter Transformers Based on Entropy-Weight Analytic Hierarchy Process](https://doi.org/10.3390/en18071757) | 2025 | 1 | 3 | Energies | Guochao Qian, Weiju Dai, Dexu Zou, et al. |
| 10 | [Analysis of excessive sheath currents in multiple cable circuits bonded to the same grounding grid](https://doi.org/10.1049/hve2.12503) | 2024 | 1 | 4 | High Voltage | Gen Li, Zhou Wenjun, Chengke Zhou, et al. |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [A Comprehensive Review of Cable Monitoring Techniques for Nuclear Power Plants](https://doi.org/10.3390/en18092333) | 2025 | 1 | 1 | Energies | Allan Ghaforian, Patrick Duggan, Lixuan Lu |
| 2 | [The Use of Comparative Multi-Criteria Analysis Methods to Evaluate Criteria Weighting in Assessments of Onshore Wind Farm Projects](https://doi.org/10.3390/en18040771) | 2025 | 1 | 1 | Energies | Dimitra Vagiona |
| 3 | [Selection model for domains across time: application to labour force survey by economic activities](https://doi.org/10.1007/s11749-020-00712-4) | 2020 | 1 | 0 | Test | María José Lombardía, Esther López‐Vizcaíno, Cristina Rueda |
| 4 | [Condition-Based Maintenance in Complex Degradation Systems: A Review of Modeling Evolution, Multi-Component Systems, and Maintenance Strategies](https://doi.org/10.3390/machines13080714) | 2025 | 1 | 0 | Machines | Hui Cao, Jie Yu, Fuhai Duan |
| 5 | [Analysis of internal defects in power cables based on temperature field simulation](https://doi.org/10.54254/2977-3903/10/2024112) | 2024 | 1 | 0 | Advances in Engineering Innovation | Zhe Li |
| 6 | [A Review of Partial Discharge Electrical Localization Techniques in Power Cables: Practical Approaches and Circuit Models](https://doi.org/10.3390/en18102583) | 2025 | 1 | 2 | Energies | Mohammad Alqtish, Alessio Di Fatta, Giuseppe Rizzo, et al. |
| 7 | [Evaluating Water Resource Management in the Transboundary Rio Grande/Bravo using Cooperative Game Theory](https://doi.org/10.1061/41114(371)227) | 2010 | 1 | 3 |  | Rebecca Teasley, Daene C. McKinney |
| 8 | [Transformer Fault Diagnosis and Location Method Based on Fault Tree Analysis](https://doi.org/10.12694/scpe.v25i5.3182) | 2024 | 1 | 3 | Scalable Computing Practice and Experience | Zhiwu Wu, Tianfu Huang, Chunguang Wang, et al. |
| 9 | [Partial Discharge Signal Pattern Recognition of Composite Insulation Defects in Cross-Linked Polyethylene Cables](https://doi.org/10.3390/s24113460) | 2024 | 1 | 3 | Sensors | Chunxu Qin, Xiaokai Zhu, Pengfei Zhu, et al. |
| 10 | [Risk Assessment Model for Converter Transformers Based on Entropy-Weight Analytic Hierarchy Process](https://doi.org/10.3390/en18071757) | 2025 | 1 | 3 | Energies | Guochao Qian, Weiju Dai, Dexu Zou, et al. |
<!-- TRENDING-END -->
