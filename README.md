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

Last update: 2025-10-27 06:23 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 10 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Institutionalizing Central Bank Cooperation](https://doi.org/10.1017/9781009367578.006) | 2023 | 23 | 2 | Cambridge University Press eBooks | Piet Clement |
| 2 | [The Bank for International Settlements at Work.](https://doi.org/10.2307/2224296) | 1933 | 23 | 10 | The Economic Journal | W. A. Elkin, Eleanor Lansing Dulles |
| 3 | [The financial history of the Bank for International Settlements](https://openalex.org/W1440109248) | 2013 | 23 | 14 | Routledge eBooks | 和彦 矢後 |
| 4 | [Using COVID-19 as opportunity: the role of the AIIB’s leadership in its strategic adaptation to the pandemic](https://doi.org/10.1080/09512748.2023.2178486) | 2023 | 23 | 16 | The Pacific Review | Giuseppe Zaccaria |
| 5 | [The Multilateral Development Banks Volume 1: The African Development Bank](https://doi.org/10.1093/oxfordjournals.afraf.a007835) | 1997 | 23 | 20 | African Affairs | Victor Murinde |
| 6 | [The multilateral development banks. Volume 2: The Asian Development Bank.](https://openalex.org/W347699255) | 1995 | 23 | 21 |  | Nihal Kappagoda |
| 7 | [Inter-American Development Bank](https://doi.org/10.1163/1570-6664_iyb_sim_org_2006) | 2014 | 23 | 24 | International Year Book and Statesmen's Who's Who | Hugo Ñopo |
| 8 | [AFRICAN DEVELOPMENT BANK](https://doi.org/10.1111/j.1467-6346.2025.12150.x) | 2025 | 23 | 24 | Africa Research Bulletin Economic Financial and Technical Series | Unknown |
| 9 | [The Creative Role of the Lawyer – Example: The Office of the World Bank's General Counsel](https://openalex.org/W759853343) | 1999 | 23 | 24 |  | Ibrahim F.I. Shihata |
| 10 | [International Labor Conference: Twenty-Sixth Session](https://doi.org/10.2307/2192792) | 1944 | 23 | 25 | American Journal of International Law | Smith Simpson |

### Topic: machine learning

Topic: machine learning — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 120 | 110356 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 42 | 25185 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Untitled](https://doi.org/10.1023/a:1022627411411) | 1995 | 29 | 30699 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 4 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 27 | 6847 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 5 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 24 | 19808 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 23 | 71737 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 22 | 86817 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 8 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 20 | 195788 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 9 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 19 | 12683 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 10 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 18 | 6181 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |

#### Recent Movers in machine learning

Papers from the last 3 years (2022-2025) with most recent citations in **machine learning**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials](https://doi.org/10.1038/s41467-022-29939-5) | 2022 | 8 | 1141 | Nature Communications | Simon Batzner, Albert Musaelian, Lixin Sun, et al. |
| 2 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 8 | 15024 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 3 | [Enhancing K-nearest neighbor algorithm: a comprehensive review and performance analysis of modifications](https://doi.org/10.1186/s40537-024-00973-y) | 2024 | 6 | 142 | Journal Of Big Data | Rajib Kumar Halder, Mohammed Nasir Uddin, Md. Ashraf Uddin, et al. |
| 4 | [K-means clustering algorithms: A comprehensive review, variants analysis, and advances in the era of big data](https://doi.org/10.1016/j.ins.2022.11.139) | 2022 | 5 | 1253 | Information Sciences | Abiodun M. Ikotun, Absalom E. Ezugwu, Laith Abualigah, et al. |
| 5 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 5 | 6045 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |

### Topic: large language models

Topic: large language models — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Improved Baselines with Visual Instruction Tuning](https://doi.org/10.1109/cvpr52733.2024.02484) | 2024 | 15 | 385 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Haotian Liu, Chunyuan Li, Yuheng Li, et al. |
| 2 | [Advances in Neural Information Processing Systems 19](https://doi.org/10.7551/mitpress/7503.001.0001) | 2007 | 12 | 16031 | The MIT Press eBooks | Unknown |
| 3 | [Proceedings of the 32nd ACM International Conference on Multimedia](https://doi.org/10.1145/3664647) | 2024 | 11 | 278 |  | Qihe Pan, Zhen Zhao, Zicheng Wang, et al. |
| 4 | [Proceedings of the 13th International Conference on Neural Information Processing Systems](https://openalex.org/W2914304175) | 2000 | 11 | 2183 |  | Todd K. Leen, Thomas G. Dietterich, Volker Tresp |
| 5 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 10 | 2855 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 6 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 10 | 195788 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 7 | [Proceedings of the 31st ACM International Conference on Multimedia](https://doi.org/10.1145/3581783) | 2023 | 9 | 565 |  | Alejandro Jaimes, Nicu Sebe, Nozha Boujemaa, et al. |
| 8 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 8 | 338 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 9 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 1878 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 10 | [LoRA: Low-Rank Adaptation of Large Language Models](https://doi.org/10.48550/arxiv.2106.09685) | 2021 | 8 | 1979 | arXiv (Cornell University) | J. Edward Hu, Yelong Shen, Phillip Wallis, et al. |

#### Recent Movers in large language models

Papers from the last 3 years (2022-2025) with most recent citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Improved Baselines with Visual Instruction Tuning](https://doi.org/10.1109/cvpr52733.2024.02484) | 2024 | 15 | 385 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Haotian Liu, Chunyuan Li, Yuheng Li, et al. |
| 2 | [Proceedings of the 32nd ACM International Conference on Multimedia](https://doi.org/10.1145/3664647) | 2024 | 11 | 278 |  | Qihe Pan, Zhen Zhao, Zicheng Wang, et al. |
| 3 | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://doi.org/10.48550/arxiv.2201.11903) | 2022 | 10 | 2855 | arXiv (Cornell University) | Jason Lee, Xuezhi Wang, Dale Schuurmans, et al. |
| 4 | [Proceedings of the 31st ACM International Conference on Multimedia](https://doi.org/10.1145/3581783) | 2023 | 9 | 565 |  | Alejandro Jaimes, Nicu Sebe, Nozha Boujemaa, et al. |
| 5 | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | 2023 | 8 | 338 |  | Woosuk Kwon, Z. Li, Siyuan Zhuang, et al. |
| 6 | [Large language models encode clinical knowledge](https://doi.org/10.1038/s41586-023-06291-2) | 2023 | 8 | 1878 | Nature | Karan Singhal, Shekoofeh Azizi, Tao Tu, et al. |
| 7 | [OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://doi.org/10.1109/cvpr52733.2024.01274) | 2024 | 7 | 16 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Qidong Huang, Xiaoyi Dong, Pan Zhang, et al. |
| 8 | [A Survey on Evaluation of Large Language Models](https://doi.org/10.1145/3641289) | 2024 | 7 | 1198 | ACM Transactions on Intelligent Systems and Technology | Yupeng Chang, Xu Wang, Jindong Wang, et al. |
| 9 | [Large language models in medicine](https://doi.org/10.1038/s41591-023-02448-8) | 2023 | 7 | 2023 | Nature Medicine | Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. |
| 10 | [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://doi.org/10.1145/3703155) | 2024 | 6 | 450 | ACM transactions on office information systems | Lei Huang, Weijiang Yu, Weitao Ma, et al. |

#### Future Hits in large language models

Papers with high recency ratio but < 100 total citations in **large language models**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Emotion-LLaMA: Multimodal Emotion Recognition and Reasoning with
  Instruction Tuning](https://doi.org/10.48550/arxiv.2406.11161) | 2024 | 4 | 3 | arXiv (Cornell University) | Zebang Cheng, Zhi-Qi Cheng, Jun-Yan He, et al. |
| 2 | [Tender: Accelerating Large Language Models via Tensor Decomposition and Runtime Requantization](https://doi.org/10.1109/isca59077.2024.00080) | 2024 | 3 | 6 |  | Jungi Lee, Wonbeom Lee, Jaewoong Sim |
| 3 | [OPERA: Alleviating Hallucination in Multi-Modal Large Language Models via Over-Trust Penalty and Retrospection-Allocation](https://doi.org/10.1109/cvpr52733.2024.01274) | 2024 | 7 | 16 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Qidong Huang, Xiaoyi Dong, Pan Zhang, et al. |
| 4 | [Mitigating Hallucinations in Large Vision-Language Models with Instruction Contrastive Decoding](https://doi.org/10.18653/v1/2024.findings-acl.937) | 2024 | 4 | 10 | Findings of the Association for Computational Linguistics: ACL 2022 | Xintong Wang, Jingheng Pan, Ding Liang, et al. |
| 5 | [Woodpecker: hallucination correction for multimodal large language models](https://doi.org/10.1007/s11432-024-4251-x) | 2024 | 4 | 12 | Science China Information Sciences | Shukang Yin, Chaoyou Fu, Sirui Zhao, et al. |
| 6 | [A Survey of Multimodel Large Language Models](https://doi.org/10.1145/3672758.3672824) | 2024 | 4 | 18 |  | Zijing Liang, Yanjie Xu, Yifan Hong, et al. |
| 7 | [Q-Instruct: Improving Low-Level Visual Abilities for Multi-Modality Foundation Models](https://doi.org/10.1109/cvpr52733.2024.02408) | 2024 | 4 | 19 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Haoning Wu, Zicheng Zhang, Erli Zhang, et al. |
| 8 | [Harnessing Large Language Models to Collect and Analyze Metal–Organic Framework Property Data Set](https://doi.org/10.1021/jacs.4c11085) | 2025 | 4 | 21 | Journal of the American Chemical Society | Yeonghun Kang, Wonseok Lee, Taeun Bae, et al. |
| 9 | [Hallusionbench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models](https://doi.org/10.1109/cvpr52733.2024.01363) | 2024 | 3 | 18 | 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | Tianrui Guan, Fuxiao Liu, Xiyang Wu, et al. |
| 10 | [Qwen2.5-VL Technical Report](https://doi.org/10.48550/arxiv.2502.13923) | 2025 | 3 | 21 | arXiv (Cornell University) | Shuai Bai, Keqin Chen, Xuejing Liu, et al. |

### Topic: game theory

Topic: game theory — window last 10 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Evolutionary Games in Economics](https://doi.org/10.2307/2938222) | 1991 | 4 | 1758 | Econometrica | Daniel Friedman |
| 2 | [Impact of Gamification on Motivation and Academic Performance: A Systematic Review](https://doi.org/10.3390/educsci14060639) | 2024 | 2 | 46 | Education Sciences | Lorena Jaramillo-Mediavilla, Andrea Basantes-Andrade, Marcos Cabezas González, et al. |
| 3 | [Evolutionary game theory](https://doi.org/10.1016/s0898-1221(96)90123-6) | 1996 | 2 | 287 | Computers & Mathematics with Applications | Gerhard Jäger, Gerhard Jaeger |
| 4 | [A meta-analysis of the cognitive and motivational effects of serious games.](https://doi.org/10.1037/a0031311) | 2013 | 2 | 1576 | Journal of Educational Psychology | Pieter Wouters, Christof van Nimwegen, Herre van Oostendorp, et al. |
| 5 | [What video games have to teach us about learning and literacy](https://doi.org/10.1145/950566.950595) | 2003 | 2 | 5119 | Computers in entertainment | James Paul Gee |
| 6 | [Bank lending policies and green transition](https://doi.org/10.1016/j.strueco.2025.04.006) | 2025 | 1 | 1 | Structural Change and Economic Dynamics | Edgar J. Sánchez Carrera, Germana Giombini, Giorgio Calcagnini |
| 7 | [Lateral Solutions to Mathematical Problems](https://doi.org/10.1201/9781003341468) | 2023 | 1 | 0 |  | Desmond MacHale |
| 8 | [Optimization of electric concrete transport vehicle configuration for long-distance tunnel construction considering driving range: a case study](https://doi.org/10.17531/ein/207181) | 2025 | 1 | 0 | Eksploatacja i Niezawodnosc - Maintenance and Reliability | Xiaoxu Yang, Wenbin Guo, Shuo Yang |
| 9 | [Transitioning to zero emission construction: A comparative study of diesel and electric loaders and trucks in Norwegian tunnel construction](https://doi.org/10.1016/j.tust.2025.106847) | 2025 | 1 | 0 | Tunnelling and Underground Space Technology | Asmat Ullah Khan, Lizhen Huang, Amund Bruland |
| 10 | [Effect of green finance on the green transformation of China’s building sector: A system dynamics assessment for targeted financing instruments and policies](https://doi.org/10.1016/j.energy.2025.137845) | 2025 | 1 | 0 | Energy | Pei Liu, Borong Lin, Hao Zhou, et al. |

#### Recent Movers in game theory

Papers from the last 3 years (2022-2025) with most recent citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Impact of Gamification on Motivation and Academic Performance: A Systematic Review](https://doi.org/10.3390/educsci14060639) | 2024 | 2 | 46 | Education Sciences | Lorena Jaramillo-Mediavilla, Andrea Basantes-Andrade, Marcos Cabezas González, et al. |
| 2 | [Bank lending policies and green transition](https://doi.org/10.1016/j.strueco.2025.04.006) | 2025 | 1 | 1 | Structural Change and Economic Dynamics | Edgar J. Sánchez Carrera, Germana Giombini, Giorgio Calcagnini |
| 3 | [Lateral Solutions to Mathematical Problems](https://doi.org/10.1201/9781003341468) | 2023 | 1 | 0 |  | Desmond MacHale |
| 4 | [Optimization of electric concrete transport vehicle configuration for long-distance tunnel construction considering driving range: a case study](https://doi.org/10.17531/ein/207181) | 2025 | 1 | 0 | Eksploatacja i Niezawodnosc - Maintenance and Reliability | Xiaoxu Yang, Wenbin Guo, Shuo Yang |
| 5 | [Transitioning to zero emission construction: A comparative study of diesel and electric loaders and trucks in Norwegian tunnel construction](https://doi.org/10.1016/j.tust.2025.106847) | 2025 | 1 | 0 | Tunnelling and Underground Space Technology | Asmat Ullah Khan, Lizhen Huang, Amund Bruland |
| 6 | [Effect of green finance on the green transformation of China’s building sector: A system dynamics assessment for targeted financing instruments and policies](https://doi.org/10.1016/j.energy.2025.137845) | 2025 | 1 | 0 | Energy | Pei Liu, Borong Lin, Hao Zhou, et al. |
| 7 | [Game-Theoretic Modeling of Hybrid Defense Strategies Against DRDoS Traffic in 5G Networks](https://doi.org/10.1109/icc51166.2024.10622381) | 2024 | 1 | 0 | ICC 2022 - IEEE International Conference on Communications | Chaojie Guo, Shen Wang, Xin Rong, et al. |
| 8 | [Application and configuration analysis of electric muck transfer equipment in plateau railway tunnel: a case study in southwest China](https://doi.org/10.1038/s41598-024-57628-4) | 2024 | 1 | 3 | Scientific Reports | Xiaoxu Yang, Yuming Liu, Kai Liu, et al. |
| 9 | [AI_Adaptive_POW: An AI assisted Proof Of Work (POW) framework for DDoS defense](https://doi.org/10.1016/j.simpa.2022.100335) | 2022 | 1 | 3 | Software Impacts | Trisha Chakraborty, Shaswata Mitra, Sudip Mittal, et al. |
| 10 | [CAPoW: Context-Aware AI-Assisted Proof of Work Based DDoS Defense](https://doi.org/10.5220/0012069000003555) | 2023 | 1 | 3 |  | Trisha Chakraborty, Shaswata Mitra, Sudip Mittal |

#### Future Hits in game theory

Papers with high recency ratio but < 100 total citations in **game theory**. Window last 10 days. Sampled up to 2000 recent works.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Bank lending policies and green transition](https://doi.org/10.1016/j.strueco.2025.04.006) | 2025 | 1 | 1 | Structural Change and Economic Dynamics | Edgar J. Sánchez Carrera, Germana Giombini, Giorgio Calcagnini |
| 2 | [Lateral Solutions to Mathematical Problems](https://doi.org/10.1201/9781003341468) | 2023 | 1 | 0 |  | Desmond MacHale |
| 3 | [Optimization of electric concrete transport vehicle configuration for long-distance tunnel construction considering driving range: a case study](https://doi.org/10.17531/ein/207181) | 2025 | 1 | 0 | Eksploatacja i Niezawodnosc - Maintenance and Reliability | Xiaoxu Yang, Wenbin Guo, Shuo Yang |
| 4 | [Transitioning to zero emission construction: A comparative study of diesel and electric loaders and trucks in Norwegian tunnel construction](https://doi.org/10.1016/j.tust.2025.106847) | 2025 | 1 | 0 | Tunnelling and Underground Space Technology | Asmat Ullah Khan, Lizhen Huang, Amund Bruland |
| 5 | [Effect of green finance on the green transformation of China’s building sector: A system dynamics assessment for targeted financing instruments and policies](https://doi.org/10.1016/j.energy.2025.137845) | 2025 | 1 | 0 | Energy | Pei Liu, Borong Lin, Hao Zhou, et al. |
| 6 | [Game-Theoretic Modeling of Hybrid Defense Strategies Against DRDoS Traffic in 5G Networks](https://doi.org/10.1109/icc51166.2024.10622381) | 2024 | 1 | 0 | ICC 2022 - IEEE International Conference on Communications | Chaojie Guo, Shen Wang, Xin Rong, et al. |
| 7 | [On a Game Theoretic Approach to Detect the Low-Rate Denial of Service Attacks](https://doi.org/10.1109/iccomm.2018.8484775) | 2018 | 1 | 2 | 2018 International Conference on Communications (COMM) | Paul Cotae, Rashed Rabie |
| 8 | [Application and configuration analysis of electric muck transfer equipment in plateau railway tunnel: a case study in southwest China](https://doi.org/10.1038/s41598-024-57628-4) | 2024 | 1 | 3 | Scientific Reports | Xiaoxu Yang, Yuming Liu, Kai Liu, et al. |
| 9 | [AI_Adaptive_POW: An AI assisted Proof Of Work (POW) framework for DDoS defense](https://doi.org/10.1016/j.simpa.2022.100335) | 2022 | 1 | 3 | Software Impacts | Trisha Chakraborty, Shaswata Mitra, Sudip Mittal, et al. |
| 10 | [CAPoW: Context-Aware AI-Assisted Proof of Work Based DDoS Defense](https://doi.org/10.5220/0012069000003555) | 2023 | 1 | 3 |  | Trisha Chakraborty, Shaswata Mitra, Sudip Mittal |
<!-- TRENDING-END -->
