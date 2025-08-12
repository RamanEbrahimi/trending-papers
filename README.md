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

Last update: 2025-08-12 21:33 UTC

<!-- TRENDING-START -->
### Journal Articles

Journal Articles — window last 90 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Deleted Work](https://openalex.org/W4285719527) | 1955 | 18 | 0 |  | Unknown |
| 2 | [Matplotlib: A 2D Graphics Environment](https://doi.org/10.1109/mcse.2007.55) | 2007 | 17 | 32141 | Computing in Science & Engineering | John D. Hunter |
| 3 | [Astropy: A community Python package for astronomy](https://doi.org/10.1051/0004-6361/201322068) | 2013 | 15 | 11526 | Astronomy and Astrophysics | Thomas Robitaille, Erik Tollerud, P. Greenfield, et al. |
| 4 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 14 | 33158 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |
| 5 | [<i>Planck</i>2018 results](https://doi.org/10.1051/0004-6361/201833910) | 2020 | 13 | 10734 | Astronomy and Astrophysics | N. Aghanim, Y. Akrami, M. Ashdown, et al. |
| 6 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 12 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 7 | [Design and Optimization of Graphene-Gold Metasurface THz Biosensor Using Au-SiO2 Material with Machine Learning for Multi-Analyte Detection](https://doi.org/10.1007/s11468-025-02954-0) | 2025 | 11 | 13 | Plasmonics | Jacob Wekalao, Habib Kraiem, Sana Ben Khalifa, et al. |
| 8 | [Ultra-Sensitive Graphene-Metal Hybrid Metasurface for Non-Invasive Glucose Detection with Convolutional Neural Network Integration](https://doi.org/10.1007/s11468-025-02989-3) | 2025 | 11 | 16 | Plasmonics | R. Mahalakshmi, Jacob Wekalao, M. Ramkumar Raja, et al. |
| 9 | [Array programming with NumPy](https://doi.org/10.1038/s41586-020-2649-2) | 2020 | 11 | 18323 | Nature | C. R. Harris, K. Jarrod Millman, Stéfan van der Walt, et al. |
| 10 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 11 | 78301 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |

### Proceedings Articles

Proceedings Articles — window last 90 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Deleted Work](https://openalex.org/W4285719527) | 1955 | 18 | 0 |  | Unknown |
| 2 | [Matplotlib: A 2D Graphics Environment](https://doi.org/10.1109/mcse.2007.55) | 2007 | 17 | 32141 | Computing in Science & Engineering | John D. Hunter |
| 3 | [Astropy: A community Python package for astronomy](https://doi.org/10.1051/0004-6361/201322068) | 2013 | 15 | 11526 | Astronomy and Astrophysics | Thomas Robitaille, Erik Tollerud, P. Greenfield, et al. |
| 4 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 14 | 33158 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |
| 5 | [<i>Planck</i>2018 results](https://doi.org/10.1051/0004-6361/201833910) | 2020 | 13 | 10734 | Astronomy and Astrophysics | N. Aghanim, Y. Akrami, M. Ashdown, et al. |
| 6 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 12 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 7 | [Design and Optimization of Graphene-Gold Metasurface THz Biosensor Using Au-SiO2 Material with Machine Learning for Multi-Analyte Detection](https://doi.org/10.1007/s11468-025-02954-0) | 2025 | 11 | 13 | Plasmonics | Jacob Wekalao, Habib Kraiem, Sana Ben Khalifa, et al. |
| 8 | [Ultra-Sensitive Graphene-Metal Hybrid Metasurface for Non-Invasive Glucose Detection with Convolutional Neural Network Integration](https://doi.org/10.1007/s11468-025-02989-3) | 2025 | 11 | 16 | Plasmonics | R. Mahalakshmi, Jacob Wekalao, M. Ramkumar Raja, et al. |
| 9 | [Array programming with NumPy](https://doi.org/10.1038/s41586-020-2649-2) | 2020 | 11 | 18323 | Nature | C. R. Harris, K. Jarrod Millman, Stéfan van der Walt, et al. |
| 10 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 11 | 78301 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |

### Overall (All Types)

Overall (all types) — window last 90 days; topic: All topics. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Deleted Work](https://openalex.org/W4285719527) | 1955 | 18 | 0 |  | Unknown |
| 2 | [Matplotlib: A 2D Graphics Environment](https://doi.org/10.1109/mcse.2007.55) | 2007 | 17 | 32141 | Computing in Science & Engineering | John D. Hunter |
| 3 | [Astropy: A community Python package for astronomy](https://doi.org/10.1051/0004-6361/201322068) | 2013 | 15 | 11526 | Astronomy and Astrophysics | Thomas Robitaille, Erik Tollerud, P. Greenfield, et al. |
| 4 | [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2) | 2021 | 14 | 33158 | Nature | John Jumper, K Taki, Alexander Pritzel, et al. |
| 5 | [<i>Planck</i>2018 results](https://doi.org/10.1051/0004-6361/201833910) | 2020 | 13 | 10734 | Astronomy and Astrophysics | N. Aghanim, Y. Akrami, M. Ashdown, et al. |
| 6 | [Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries](https://doi.org/10.3322/caac.21834) | 2024 | 12 | 11626 | CA A Cancer Journal for Clinicians | Freddie Bray, Mathieu Laversanne, Hyuna Sung, et al. |
| 7 | [Design and Optimization of Graphene-Gold Metasurface THz Biosensor Using Au-SiO2 Material with Machine Learning for Multi-Analyte Detection](https://doi.org/10.1007/s11468-025-02954-0) | 2025 | 11 | 13 | Plasmonics | Jacob Wekalao, Habib Kraiem, Sana Ben Khalifa, et al. |
| 8 | [Ultra-Sensitive Graphene-Metal Hybrid Metasurface for Non-Invasive Glucose Detection with Convolutional Neural Network Integration](https://doi.org/10.1007/s11468-025-02989-3) | 2025 | 11 | 16 | Plasmonics | R. Mahalakshmi, Jacob Wekalao, M. Ramkumar Raja, et al. |
| 9 | [Array programming with NumPy](https://doi.org/10.1038/s41586-020-2649-2) | 2020 | 11 | 18323 | Nature | C. R. Harris, K. Jarrod Millman, Stéfan van der Walt, et al. |
| 10 | [Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2](https://doi.org/10.1186/s13059-014-0550-8) | 2014 | 11 | 78301 | Genome biology | Michael I. Love, Wolfgang Huber, Simon Anders |

### Topic: games on networks

Topic: games on networks — window last 90 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Five Rules for the Evolution of Cooperation](https://doi.org/10.1126/science.1133755) | 2006 | 5 | 5504 | Science | Martin A. Nowak |
| 2 | [Evolutionary dynamics of higher-order interactions in social networks](https://doi.org/10.1038/s41562-020-01024-1) | 2021 | 4 | 408 | Nature Human Behaviour | Unai Alvarez-Rodriguez, Federico Battiston, Guilherme Ferraz de Arruda, et al. |
| 3 | [Spatial structure often inhibits the evolution of cooperation in the snowdrift game](https://doi.org/10.1038/nature02360) | 2004 | 4 | 1513 | Nature | Christoph Hauert, Michael Doebeli |
| 4 | [Scale-Free Networks Provide a Unifying Framework for the Emergence of Cooperation](https://doi.org/10.1103/physrevlett.95.098104) | 2005 | 4 | 1706 | Physical Review Letters | Francisco C. Santos, Jorge M. Pacheco |
| 5 | [Evolutionary games and spatial chaos](https://doi.org/10.1038/359826a0) | 1992 | 4 | 4265 | Nature | Martin A. Nowak, Robert M. May |
| 6 | [Evolutionary Games and Population Dynamics](https://doi.org/10.1017/cbo9781139173179) | 1998 | 4 | 5487 |  | Josef Hofbauer, Karl Sigmund |
| 7 | [Evolutionary dynamics of any multiplayer game on regular graphs](https://doi.org/10.1038/s41467-024-49505-5) | 2024 | 3 | 22 | Nature Communications | Chaoqian Wang, Matjaž Perc, Attila Szolnoki |
| 8 | [Application of Artificial Intelligence in Basketball Sport](https://doi.org/10.12775/jehs.2021.11.07.005) | 2021 | 3 | 104 | Journal of Education Health and Sport | Li Bin, Xinyang Xu |
| 9 | [Inequality, communication, and the avoidance of disastrous climate change in a public goods game](https://doi.org/10.1073/pnas.1102493108) | 2011 | 3 | 470 | Proceedings of the National Academy of Sciences | Alessandro Tavoni, Astrid Dannenberg, Giorgos Kallis, et al. |
| 10 | [Evolutionary games on multilayer networks: a colloquium](https://doi.org/10.1140/epjb/e2015-60270-7) | 2015 | 3 | 741 | The European Physical Journal B | Zhen Wang, Lin Wang, Attila Szolnoki, et al. |

### Topic: network science in finance

Topic: network science in finance — window last 90 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [bibliometrix : An R-tool for comprehensive science mapping analysis](https://doi.org/10.1016/j.joi.2017.08.007) | 2017 | 6 | 10236 | Journal of Informetrics | Massimo Aria, Corrado Cuccurullo |
| 2 | [How to conduct a bibliometric analysis: An overview and guidelines](https://doi.org/10.1016/j.jbusres.2021.04.070) | 2021 | 5 | 7997 | Journal of Business Research | Naveen Donthu, Satish Kumar, Debmalya Mukherjee, et al. |
| 3 | [The Evolution of Fintech: A New Post-Crisis Paradigm?](https://doi.org/10.2139/ssrn.2676553) | 2015 | 3 | 1159 | SSRN Electronic Journal | Douglas W. Arner, Jànos Barberis, Ross P. Buckley |
| 4 | [On the Fintech Revolution: Interpreting the Forces of Innovation, Disruption, and Transformation in Financial Services](https://doi.org/10.1080/07421222.2018.1440766) | 2018 | 3 | 1457 | Journal of Management Information Systems | Peter Gomber, Robert J. Kauffman, Chris Parker, et al. |
| 5 | [What do we know about <scp>ESG</scp> and risk? A systematic and bibliometric review](https://doi.org/10.1002/csr.2624) | 2023 | 2 | 28 | Corporate Social Responsibility and Environmental Management | Maria Elena De Giuli, Daniele Grechi, Alessandra Tanda |
| 6 | [Fintech](https://doi.org/10.1007/s12599-017-0464-6) | 2017 | 2 | 475 | Business & Information Systems Engineering | Thomas Puschmann |
| 7 | [How Valuable Is FinTech Innovation?](https://doi.org/10.1093/rfs/hhy130) | 2018 | 2 | 588 | Review of Financial Studies | Mark A. Chen, Qinxi Wu, Baozhong Yang |
| 8 | [The emergence of the global fintech market: economic and technological determinants](https://doi.org/10.1007/s11187-018-9991-x) | 2018 | 2 | 599 | Small Business Economics | Christian Haddad, Lars Hornuf |
| 9 | [Fintech and banking: What do we know?](https://doi.org/10.1016/j.jfi.2019.100833) | 2019 | 2 | 845 | Journal of Financial Intermediation | Anjan V. Thakor |
| 10 | [Fintech, regulatory arbitrage, and the rise of shadow banks](https://doi.org/10.1016/j.jfineco.2018.03.011) | 2018 | 2 | 1201 | Journal of Financial Economics | Greg Buchak, Gregor Matvos, Tomasz Piskorski, et al. |

### Topic: influence maximization

Topic: influence maximization — window last 90 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 14 | 146606 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 2 | [Maximizing the spread of influence through a social network](https://doi.org/10.1145/956750.956769) | 2003 | 11 | 6835 |  | David Kempe, Jon Kleinberg, Éva Tardos |
| 3 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 11 | 25300 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 4 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 10 | 74679 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 5 | [When to use and how to report the results of PLS-SEM](https://doi.org/10.1108/ebr-11-2018-0203) | 2018 | 9 | 17086 | European Business Review | Joseph F. Hair, Jeffrey J. Risher, Marko Sarstedt, et al. |
| 6 | [Fitting Linear Mixed-Effects Models Using<b>lme4</b>](https://doi.org/10.18637/jss.v067.i01) | 2015 | 9 | 72632 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |
| 7 | [Mining the network value of customers](https://doi.org/10.1145/502512.502525) | 2001 | 8 | 2835 |  | Pedro Domingos, Matt Richardson |
| 8 | [User Acceptance of Information Technology: Toward a Unified View](https://doi.org/10.2307/30036540) | 2003 | 7 | 36816 | MIS Quarterly | Venkatesh, Jeremy Morris, Davis, et al. |
| 9 | [Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008) | 1989 | 7 | 56606 | MIS Quarterly | Fred D. Davis |
| 10 | [Common method biases in behavioral research: A critical review of the literature and recommended remedies.](https://doi.org/10.1037/0021-9010.88.5.879) | 2003 | 7 | 66576 | Journal of Applied Psychology | Philip M. Podsakoff, Scott MacKenzie, Jeong Yeon Lee, et al. |

### Topic: graph neural networks

Topic: graph neural networks — window last 90 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Graph Neural Network Model](https://doi.org/10.1109/tnn.2008.2005605) | 2008 | 77 | 7593 | IEEE Transactions on Neural Networks | Franco Scarselli, M. Gori, Ah Chung Tsoi, et al. |
| 2 | [Graph neural networks: A review of methods and applications](https://doi.org/10.1016/j.aiopen.2021.01.001) | 2020 | 59 | 4030 | AI Open | Jie Zhou, Ganqu Cui, Shengding Hu, et al. |
| 3 | [Graph Attention Networks](https://doi.org/10.48550/arxiv.1710.10903) | 2017 | 58 | 8001 | arXiv (Cornell University) | Petar Veličković, Guillem Cucurull, Arantxa Casanova, et al. |
| 4 | [Semi-Supervised Classification with Graph Convolutional Networks](https://doi.org/10.48550/arxiv.1609.02907) | 2016 | 52 | 15453 | arXiv (Cornell University) | Thomas Kipf, Max Welling |
| 5 | [Inductive Representation Learning on Large Graphs](https://doi.org/10.48550/arxiv.1706.02216) | 2017 | 47 | 5285 | arXiv (Cornell University) | William L. Hamilton, Rex Ying, Jure Leskovec |
| 6 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 36 | 84553 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 7 | [Attention Is All You Need](https://doi.org/10.48550/arxiv.1706.03762) | 2017 | 34 | 60078 | arXiv (Cornell University) | Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. |
| 8 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 33 | 192837 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |
| 9 | [Advances in Neural Information Processing Systems 19](https://doi.org/10.7551/mitpress/7503.001.0001) | 2007 | 32 | 14539 | The MIT Press eBooks | Unknown |
| 10 | [Graph neural networks for materials science and chemistry](https://doi.org/10.1038/s43246-022-00315-6) | 2022 | 25 | 431 | Communications Materials | Patrick Reiser, Marlen Neubert, André Eberhard, et al. |

### Topic: machine learning

Topic: machine learning — window last 90 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 102 | 107723 | Machine Learning | Leo Breiman |
| 2 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 31 | 24495 | The Annals of Statistics | Jerome H. Friedman |
| 3 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 31 | 70108 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 4 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 30 | 5561 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 5 | [Support-vector networks](https://doi.org/10.1007/bf00994018) | 1995 | 25 | 37997 | Machine Learning | Corinna Cortes, Vladimir Vapnik |
| 6 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 24 | 84553 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 7 | [Machine Learning: Algorithms, Real-World Applications and Research Directions](https://doi.org/10.1007/s42979-021-00592-x) | 2021 | 23 | 3470 | SN Computer Science | Iqbal H. Sarker |
| 8 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 21 | 5839 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 9 | [Machine learning: Trends, perspectives, and prospects](https://doi.org/10.1126/science.aaa8415) | 2015 | 20 | 7755 | Science | Michael I. Jordan, Tom M. Mitchell |
| 10 | ["Why Should I Trust You?"](https://doi.org/10.1145/2939672.2939778) | 2016 | 19 | 12158 |  | Marco Túlio Ribeiro, Sameer Singh, Carlos Guestrin |
<!-- TRENDING-END -->
