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

### Preprint sources (bioRxiv, arXiv)

In addition to overall and topic sections, the script can include sections where the pool of recent citing works is restricted to specific sources:

- bioRxiv
- arXiv

These sections show which papers are most frequently referenced by preprints from that source in the last N days. Control via `config.yaml`:

```yaml
include_biorxiv: true
include_arxiv: true
preprint_top_k: 10
```

No extra dependencies are needed; filtering is performed via OpenAlex `primary_location` host venue names.

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

Last update: 2025-08-13 23:48 UTC

Last update: 2025-08-12 22:37 UTC

<!-- TRENDING-START -->
### Overall (All Types)

Overall (all types) — window last 30 days; topic: pangenome. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Prokka: rapid prokaryotic genome annotation](https://doi.org/10.1093/bioinformatics/btu153) | 2014 | 7 | 15706 | Bioinformatics | Torsten Seemann |
| 2 | [Proksee: in-depth characterization and visualization of bacterial genomes](https://doi.org/10.1093/nar/gkad326) | 2023 | 5 | 898 | Nucleic Acids Research | Jason R. Grant, Eric Enns, Eric Marinier, et al. |
| 3 | [IQ-TREE 2: New Models and Efficient Methods for Phylogenetic Inference in the Genomic Era](https://doi.org/10.1093/molbev/msaa015) | 2020 | 5 | 11000 | Molecular Biology and Evolution | Bùi Quang Minh, Heiko A. Schmidt, Olga Chernomor, et al. |
| 4 | [eggNOG-mapper v2: Functional Annotation, Orthology Assignments, and Domain Prediction at the Metagenomic Scale](https://doi.org/10.1093/molbev/msab293) | 2021 | 4 | 2674 | Molecular Biology and Evolution | Carlos P. Cantalapiedra, Ana Hernández-Plaza, Ivica Letunić, et al. |
| 5 | [Haplotype-resolved de novo assembly using phased assembly graphs with hifiasm](https://doi.org/10.1038/s41592-020-01056-5) | 2021 | 4 | 3698 | Nature Methods | Haoyu Cheng, Gregory T. Concepcion, Xiaowen Feng, et al. |
| 6 | [Roary: rapid large-scale prokaryote pan genome analysis](https://doi.org/10.1093/bioinformatics/btv421) | 2015 | 4 | 4797 | Bioinformatics | Andrew J. Page, Carla Cummins, Martin Hunt, et al. |
| 7 | [OrthoFinder: phylogenetic orthology inference for comparative genomics](https://doi.org/10.1186/s13059-019-1832-y) | 2019 | 4 | 5556 | Genome biology | David Emms, Steven Kelly |
| 8 | [Prodigal: prokaryotic gene recognition and translation initiation site identification](https://doi.org/10.1186/1471-2105-11-119) | 2010 | 4 | 10458 | BMC Bioinformatics | Doug Hyatt, Gwo-Liang Chen, Philip LoCascio, et al. |
| 9 | [BUSCO: assessing genome assembly and annotation completeness with single-copy orthologs](https://doi.org/10.1093/bioinformatics/btv351) | 2015 | 4 | 11944 | Bioinformatics | Felipe A. Simão, Robert M. Waterhouse, Panagiotis Ioannidis, et al. |
| 10 | [Minimap2: pairwise alignment for nucleotide sequences](https://doi.org/10.1093/bioinformatics/bty191) | 2018 | 4 | 11945 | Bioinformatics | Heng Li |

### Topic: games on networks

Topic: games on networks — window last 30 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Strategy evolution on dynamic networks](https://doi.org/10.1038/s43588-023-00509-z) | 2023 | 2 | 45 | Nature Computational Science | Qi Su, Alex McAvoy, Joshua B. Plotkin |
| 2 | [Mathematical foundations of moral preferences](https://doi.org/10.1098/rsif.2020.0880) | 2021 | 2 | 261 | Journal of The Royal Society Interface | Valerio Capraro, Matjaž Perc |
| 3 | [Evolutionary dynamics of higher-order interactions in social networks](https://doi.org/10.1038/s41562-020-01024-1) | 2021 | 2 | 408 | Nature Human Behaviour | Unai Alvarez-Rodriguez, Federico Battiston, Guilherme Ferraz de Arruda, et al. |
| 4 | [Evolutionary dynamics on any population structure](https://doi.org/10.1038/nature21723) | 2017 | 2 | 460 | Nature | Benjamin Allen, Gábor Lippner, Yu-Ting Chen, et al. |
| 5 | [Inequality, communication, and the avoidance of disastrous climate change in a public goods game](https://doi.org/10.1073/pnas.1102493108) | 2011 | 2 | 470 | Proceedings of the National Academy of Sciences | Alessandro Tavoni, Astrid Dannenberg, Giorgos Kallis, et al. |
| 6 | [The relationship between addictive use of social media, narcissism, and self-esteem: Findings from a large national survey](https://doi.org/10.1016/j.addbeh.2016.03.006) | 2016 | 2 | 1151 | Addictive Behaviors | Cecilie Schou Andreassen, Ståle Pallesen, Mark D. Griffiths |
| 7 | [Emergence of cooperation and evolutionary stability in finite populations](https://doi.org/10.1038/nature02414) | 2004 | 2 | 1369 | Nature | Martin A. Nowak, Akira Sasaki, Christine Taylor, et al. |
| 8 | [Scale-Free Networks Provide a Unifying Framework for the Emergence of Cooperation](https://doi.org/10.1103/physrevlett.95.098104) | 2005 | 2 | 1706 | Physical Review Letters | Francisco C. Santos, Jorge M. Pacheco |
| 9 | [Evolutionary games and spatial chaos](https://doi.org/10.1038/359826a0) | 1992 | 2 | 4265 | Nature | Martin A. Nowak, Robert M. May |
| 10 | [Evolutionary Games and Population Dynamics](https://doi.org/10.1017/cbo9781139173179) | 1998 | 2 | 5487 |  | Josef Hofbauer, Karl Sigmund |

### Topic: network science in finance

Topic: network science in finance — window last 30 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Exploring the research development trajectory and trends of green finance](https://doi.org/10.1016/j.apmrv.2024.10.001) | 2024 | 1 | 1 | Asia Pacific Management Review | Pi‐Cheng Tung, Yu-Hsuan Chiu, Chen-Hao Huang |
| 2 | [The relationship between artificial intelligence, geopolitical risk, and green growth: Exploring the moderating role of green finance and energy technology](https://doi.org/10.1016/j.techfore.2025.124135) | 2025 | 1 | 1 | Technological Forecasting and Social Change | Xiyue Yang, Hui Chen, Bofeng Li, et al. |
| 3 | [Understanding the Resistance to Use Metaverse Shopping Platforms in Sarawak, Malaysia: An Investigation by Using Innovation Resistance Theory](https://doi.org/10.21002/seam.v18i2.1697) | 2024 | 1 | 1 | The South East Asian Journal of Management | Chee-Hua Chin, Evelyn Cai-Ni Chiew, Karment Tiong |
| 4 | [Measuring factors affecting consumer attitudes toward metaverse adoption: Islamic banking services setting](https://doi.org/10.21511/bbs.19(4).2024.16) | 2024 | 1 | 1 | Banks and Bank Systems | Hasan Alhanatleh, Amineh Khaddam, Amro Alzghoul |
| 5 | [Examining the impact of trust on customer intention to use metaverse payments: A next-gen transactions strategic outlook](https://doi.org/10.22495/cbsrv6i1art16) | 2025 | 1 | 1 | Corporate and Business Strategy Review | Tri-Quan Dang, Đặng Thị Việt Đức, Lan Anh Tran, et al. |
| 6 | [Employing Blockchain, NFTs, and Digital Certificates for Unparalleled Authenticity and Data Protection of Source Code](https://doi.org/10.20944/preprints202502.1048.v1) | 2025 | 1 | 1 |  | Leonardo Juan Ramírez López, Genesis Gabriela Morillo Ledezma |
| 7 | [Technological Innovation in Banking: Opportunities and Challenges of MetaVerse in Banking Business Model](https://doi.org/10.59324/ejmeb.2025.2(2).07) | 2025 | 1 | 1 | European journal of management, economics and business. | Shaila Kedla, Rohit J. Nair, Nazmoon Nahar Asha |
| 8 | [Could e-commerce activities drive to climate change mitigation? Novel evidence from panel quantile regression model](https://doi.org/10.3846/jbem.2025.23604) | 2025 | 1 | 1 | Journal of Business Economics and Management | Nicoleta Mihaela Doran, Alina Georgiana Manta, Gabriela Badareu, et al. |
| 9 | [The Impact of Bank Fintech on Corporate Short-Term Debt for Long-Term Use—Based on the Perspective of Financial Risk](https://doi.org/10.3390/ijfs13020068) | 2025 | 1 | 1 | International Journal of Financial Studies | Wu Wenyu, Xiaoyan Lin |
| 10 | [Decoding Digital Synergies: How Mechatronic Systems and Artificial Intelligence Shape Banking Performance Through Quantile-Driven Method of Moments](https://doi.org/10.3390/app15105282) | 2025 | 1 | 1 | Applied Sciences | Liviu Florin Manta, Alina Georgiana Manta, Claudia Gherțescu |

### Topic: influence maximization

Topic: influence maximization — window last 30 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The theory of planned behavior](https://doi.org/10.1016/0749-5978(91)90020-t) | 1991 | 5 | 74679 | Organizational Behavior and Human Decision Processes | Icek Ajzen |
| 2 | [Using thematic analysis in psychology](https://doi.org/10.1191/1478088706qp063oa) | 2006 | 5 | 147595 | Qualitative Research in Psychology | Virginia Braun, Victoria Clarke |
| 3 | [Scalable influence maximization for prevalent viral marketing in large-scale social networks](https://doi.org/10.1145/1835804.1835934) | 2010 | 4 | 1713 |  | Wei Chen, Chi Wang, Yajun Wang |
| 4 | [When to use and how to report the results of PLS-SEM](https://doi.org/10.1108/ebr-11-2018-0203) | 2018 | 4 | 17086 | European Business Review | Joseph F. Hair, Jeffrey J. Risher, Marko Sarstedt, et al. |
| 5 | [A new criterion for assessing discriminant validity in variance-based structural equation modeling](https://doi.org/10.1007/s11747-014-0403-8) | 2014 | 4 | 25300 | Journal of the Academy of Marketing Science | Jörg Henseler, Christian M. Ringle, Marko Sarstedt |
| 6 | [User Acceptance of Information Technology: Toward a Unified View](https://doi.org/10.2307/30036540) | 2003 | 4 | 36816 | MIS Quarterly | Venkatesh, Jeremy Morris, Davis, et al. |
| 7 | [CELF++](https://doi.org/10.1145/1963192.1963217) | 2011 | 3 | 810 |  | Amit Goyal, Wei Lu, Laks V. S. Lakshmanan |
| 8 | [Mining the network value of customers](https://doi.org/10.1145/502512.502525) | 2001 | 3 | 2835 |  | Pedro Domingos, Matt Richardson |
| 9 | [Maximizing the spread of influence through a social network](https://doi.org/10.1145/956750.956769) | 2003 | 3 | 6835 |  | David Kempe, Jon Kleinberg, Éva Tardos |
| 10 | [Fitting Linear Mixed-Effects Models Using<b>lme4</b>](https://doi.org/10.18637/jss.v067.i01) | 2015 | 3 | 72632 | Journal of Statistical Software | Douglas M. Bates, Martin Mächler, Benjamin M. Bolker, et al. |

### Topic: graph neural networks

Topic: graph neural networks — window last 30 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [The Graph Neural Network Model](https://doi.org/10.1109/tnn.2008.2005605) | 2008 | 20 | 7593 | IEEE Transactions on Neural Networks | Franco Scarselli, M. Gori, Ah Chung Tsoi, et al. |
| 2 | [Inductive Representation Learning on Large Graphs](https://doi.org/10.48550/arxiv.1706.02216) | 2017 | 14 | 5285 | arXiv (Cornell University) | William L. Hamilton, Rex Ying, Jure Leskovec |
| 3 | [Semi-Supervised Classification with Graph Convolutional Networks](https://doi.org/10.48550/arxiv.1609.02907) | 2016 | 14 | 15453 | arXiv (Cornell University) | Thomas Kipf, Max Welling |
| 4 | [Advances in Neural Information Processing Systems 19](https://doi.org/10.7551/mitpress/7503.001.0001) | 2007 | 13 | 14539 | The MIT Press eBooks | Unknown |
| 5 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 12 | 85022 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 6 | [Graph Attention Networks](https://doi.org/10.48550/arxiv.1710.10903) | 2017 | 11 | 8001 | arXiv (Cornell University) | Petar Veličković, Guillem Cucurull, Arantxa Casanova, et al. |
| 7 | [Heterogeneous Graph Attention Network](https://doi.org/10.1145/3308558.3313562) | 2019 | 10 | 2263 |  | Xiao Wang, Houye Ji, Chuan Shi, et al. |
| 8 | [Graph neural networks: A review of methods and applications](https://doi.org/10.1016/j.aiopen.2021.01.001) | 2020 | 10 | 4030 | AI Open | Jie Zhou, Ganqu Cui, Shengding Hu, et al. |
| 9 | [node2vec](https://doi.org/10.1145/2939672.2939754) | 2016 | 9 | 9860 |  | Aditya Grover, Jure Leskovec |
| 10 | [Deep Residual Learning for Image Recognition](https://doi.org/10.1109/cvpr.2016.90) | 2016 | 9 | 192837 |  | Kaiming He, Xiangyu Zhang, Shaoqing Ren, et al. |

### Topic: machine learning

Topic: machine learning — window last 30 days. Sampled up to 2000 recent works. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Untitled](https://doi.org/10.1023/a:1010933404324) | 2001 | 138 | 107723 | Machine Learning | Leo Breiman |
| 2 | [Scikit-learn: Machine Learning in Python](https://doi.org/10.5555/1953048.2078195) | 2011 | 45 | 5561 | Journal of Machine Learning Research | PedregosaFabian, VaroquauxGaël, GramfortAlexandre, et al. |
| 3 | [Greedy function approximation: A gradient boosting machine.](https://doi.org/10.1214/aos/1013203451) | 2001 | 43 | 24495 | The Annals of Statistics | Jerome H. Friedman |
| 4 | [A Unified Approach to Interpreting Model Predictions](https://doi.org/10.48550/arxiv.1705.07874) | 2017 | 37 | 11830 | arXiv (Cornell University) | Scott Lundberg, Su‐In Lee |
| 5 | [From local explanations to global understanding with explainable AI for trees](https://doi.org/10.1038/s42256-019-0138-9) | 2020 | 32 | 5839 | Nature Machine Intelligence | Scott Lundberg, Gabriel Erion, Hugh Chen, et al. |
| 6 | [Deep learning](https://doi.org/10.1038/nature14539) | 2015 | 30 | 70108 | Nature | Yann LeCun, Yoshua Bengio, Geoffrey E. Hinton |
| 7 | [SMOTE: Synthetic Minority Over-sampling Technique](https://doi.org/10.1613/jair.953) | 2002 | 27 | 25921 | Journal of Artificial Intelligence Research | Nitesh V. Chawla, Kevin W. Bowyer, Lawrence Hall, et al. |
| 8 | [Extremely randomized trees](https://doi.org/10.1007/s10994-006-6226-1) | 2006 | 23 | 7304 | Machine Learning | Pierre Geurts, Damien Ernst, Louis Wehenkel |
| 9 | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | 23 | 85022 | Neural Computation | Sepp Hochreiter, Jürgen Schmidhuber |
| 10 | [The Elements of Statistical Learning](https://doi.org/10.1007/978-0-387-84858-7) | 2009 | 22 | 19350 | Springer series in statistics | Trevor Hastie, Robert Tibshirani, Jerome H. Friedman |

### Trending Preprints by Early Citations: bioRxiv

Trending bioRxiv preprints by early inbound citations — window last 30 days. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Diverse phage defence systems define West African South American pandemic Vibrio cholerae](https://doi.org/10.1101/2024.11.23.624991) | 2024 | 1 | 1 | bioRxiv (Cold Spring Harbor Laboratory) | David W. Adams, Milena Jaskólska, Alexandre Lemopoulos, et al. |
| 2 | [Ten new high-quality genome assemblies for diverse bioenergy sorghum genotypes](https://doi.org/10.1101/2022.09.26.509520) | 2022 | 1 | 0 | bioRxiv (Cold Spring Harbor Laboratory) | William G. Voelker, Krittika Krishnan, Kapeel Chougule, et al. |
| 3 | [The Anaerobic Efflux Pump MdtEF-TolC Confers Resistance to Cationic Biocides](https://doi.org/10.1101/570408) | 2019 | 1 | 11 | bioRxiv (Cold Spring Harbor Laboratory) | Diego E. Novoa, Otakuye Conroy‐Ben |
| 4 | [Genomic rearrangements have consequences for introgression breeding as revealed by genome assemblies of wild and cultivated lentil species](https://doi.org/10.1101/2021.07.23.453237) | 2021 | 1 | 55 | bioRxiv (Cold Spring Harbor Laboratory) | Larissa Ramsay, ChuShin Koh, Sateesh Kagale, et al. |
| 5 | [Building pangenome graphs](https://doi.org/10.1101/2023.04.05.535718) | 2023 | 1 | 80 | bioRxiv (Cold Spring Harbor Laboratory) | Erik Garrison, Andrea Guarracino, Simon Heumos, et al. |

### Trending Preprints by Early Citations: arXiv

Trending arXiv preprints by early inbound citations — window last 30 days. Showing top 10.

| # | Title | Year | Recent | Total | Venue | Authors |
|---:|---|---:|---:|---:|---|---|
| 1 | [Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM](https://doi.org/10.48550/arxiv.1303.3997) | 2013 | 1 | 4438 | arXiv (Cornell University) | Heng Li |
<!-- TRENDING-END -->
