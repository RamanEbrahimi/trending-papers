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

Last update: 2025-08-12 20:54 UTC

<!-- TRENDING-START -->
Results for window last 90 days; topic: All topics. Sampled up to 2000 recent works.

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
| 11 | [Generalized Gradient Approximation Made Simple](https://doi.org/10.1103/physrevlett.77.3865) | 1996 | 11 | 189283 | Physical Review Letters | John P. Perdew, Kieron Burke, Matthias Ernzerhof |
| 12 | [AI enhanced metasurface sensor design for ultra-sensitive terahertz gas detection using 2D materials](https://doi.org/10.1063/5.0265295) | 2025 | 10 | 14 | AIP Advances | Jacob Wekalao, Hussein A. Elsayed, Nassir Saad Alarifi, et al. |
| 13 | [A High-Sensitivity Terahertz Metasurface Biosensor with Graphene-MXene-Black Phosphorus Integration for Early Pregnancy Detection](https://doi.org/10.1007/s11468-025-02981-x) | 2025 | 10 | 17 | Plasmonics | Jacob Wekalao, Ahmed Mehaney, Mahmood Basil A. Al‐Rawi, et al. |
| 14 | [DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations](https://doi.org/10.1088/1475-7516/2025/02/021) | 2025 | 10 | 280 | Journal of Cosmology and Astroparticle Physics | A. G. Adame, José Edgar Madriz Aguilar, S. Ahlen, et al. |
| 15 | [A consistent and accurate<i>ab initio</i>parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu](https://doi.org/10.1063/1.3382344) | 2010 | 10 | 47407 | The Journal of Chemical Physics | Stefan Grimme, Jens Antony, Stephan Ehrlich, et al. |
| 16 | [Efficient iterative schemes for<i>ab initio</i>total-energy calculations using a plane-wave basis set](https://doi.org/10.1103/physrevb.54.11169) | 1996 | 10 | 107280 | Physical review. B, Condensed matter | Georg Kresse, J. Furthmüller |
| 17 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). X. Dust Substructures, Disk Geometries, and Dust-disk Radii](https://doi.org/10.3847/1538-4357/adc7b0) | 2025 | 9 | 9 | The Astrophysical Journal | Miguel Vioque, N. T. Kurtovic, Leon Trapman, et al. |
| 18 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). I. Program Overview and Summary of First Results](https://doi.org/10.3847/1538-4357/addebe) | 2025 | 9 | 10 | The Astrophysical Journal | Ke Zhang, Laura M. Pérez, Ilaria Pascucci, et al. |
| 19 | [Design and optimization of a hybrid graphene-metallic metasurfaces terahertz biosensor for high-precision detection of reproductive hormones, integrating locally weighted linear regression analysis and 2-bit encoding capabilities](https://doi.org/10.1140/epjb/s10051-025-00933-2) | 2025 | 9 | 12 | The European Physical Journal B | Jacob Wekalao, Hussein A. Elsayed, Ahmed M. El‐Sherbeeny, et al. |
| 20 | [Advanced plasmonic sensor design for sperm detection with machine learning-driven optimization](https://doi.org/10.1007/s11082-025-08151-x) | 2025 | 9 | 13 | Optical and Quantum Electronics | Jacob Wekalao, Ngaira Mandela, Gideon Mwendwa, et al. |
| 21 | [A Graphene-Based Surface Plasmon Resonance Metasurfaces Terahertz Sensor for Early Brain Tumor Detection with Machine Learning Optimization](https://doi.org/10.1007/s11468-025-02930-8) | 2025 | 9 | 15 | Plasmonics | Jacob Wekalao, Yahya Ali Abdelrahman Ali, Taoufik Saidani, et al. |
| 22 | [Enhanced Malaria Detection Using a Hybrid Borophene-Based Terahertz Biosensor with Random Forest Regression Analysis](https://doi.org/10.1007/s13538-025-01759-0) | 2025 | 9 | 17 | Brazilian Journal of Physics | Jacob Wekalao, Stephen Maina Njoroge, Oumaymah Elamri |
| 23 | [Graphene-Based Metasurface Terahertz Biosensing Platform for Accurate Alpha-Fetoprotein Detection in Liver Cancer Diagnosis Enhanced with Machine Learning Optimization](https://doi.org/10.1007/s11468-025-02968-8) | 2025 | 9 | 18 | Plasmonics | Jacob Wekalao, Abdulkarem H. M. Almawgani, Refka Ghodhbani, et al. |
| 24 | [The Pantheon+ Analysis: Cosmological Constraints](https://doi.org/10.3847/1538-4357/ac8e04) | 2022 | 9 | 707 | The Astrophysical Journal | Dillon Brout, D. Scolnic, B Popovic, et al. |
| 25 | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://doi.org/10.1038/s41586-024-07487-w) | 2024 | 9 | 4708 | Nature | Josh Abramson, Jonas Adler, Jack Dunger, et al. |
| 26 | [HEALPix: A Framework for High‐Resolution Discretization and Fast Analysis of Data Distributed on the Sphere](https://doi.org/10.1086/427976) | 2005 | 9 | 5267 | The Astrophysical Journal | K. M. Górski, E. Hivon, A. J. Banday, et al. |
| 27 | [<tt>emcee</tt>: The MCMC Hammer](https://doi.org/10.1086/670067) | 2013 | 9 | 10659 | Publications of the Astronomical Society of the Pacific | Daniel Foreman-Mackey, David W. Hogg, Dustin Lang, et al. |
| 28 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). XI. Beam-corrected Gas Disk Sizes from Fitting <sup>12</sup>CO Moment Zero Maps](https://doi.org/10.3847/1538-4357/adc7af) | 2025 | 8 | 9 | The Astrophysical Journal | Leon Trapman, Miguel Vioque, N. T. Kurtovic, et al. |
| 29 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). V. Protoplanetary Gas Disk Masses](https://doi.org/10.3847/1538-4357/adcd6e) | 2025 | 8 | 9 | The Astrophysical Journal | Leon Trapman, Ke Zhang, Giovanni Rosotti, et al. |
| 30 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). III. Dust and Gas Disk Properties in the Lupus Star-forming Region](https://doi.org/10.3847/1538-4357/add43a) | 2025 | 8 | 9 | The Astrophysical Journal | Dingshan Deng, Miguel Vioque, Ilaria Pascucci, et al. |
| 31 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). IV. Dust and Gas Disk Properties in the Upper Scorpius Star-forming Region](https://doi.org/10.3847/1538-4357/adc7ab) | 2025 | 8 | 9 | The Astrophysical Journal | Carolina Agurto-Gangas, Laura M. Pérez, Anibal Sierra, et al. |
| 32 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). II. Dust and Gas Disk Properties in the Ophiuchus Star-forming Region](https://doi.org/10.3847/1538-4357/add2ec) | 2025 | 8 | 9 | The Astrophysical Journal | Dary Ruíz-Rodríguez, Camilo González-Ruilova, Lucas A. Cieza, et al. |
| 33 | [High-Sensitivity Terahertz Plasmon Resonance Biosensor Incorporating Graphene-Perovskite Metasurfaces for Waterborne BactefInformaticsrial Detection](https://doi.org/10.1007/s11468-025-02948-y) | 2025 | 8 | 10 | Plasmonics | Abdessalem Bouhenna, Oussama Zeggai, Hind Ahmed, et al. |
| 34 | [Square-slotted metasurface optical sensor based on graphene material for efficient detection of brain tumor using machine learning](https://doi.org/10.1016/j.measurement.2025.117812) | 2025 | 8 | 11 | Measurement | Jacob Wekalao, Osamah Alsalman, Shobhit K. Patel |
| 35 | [Design and Optimization of a Graphene-Enhanced Terahertz Metasurfaces Surface Plasmon Resonance Biosensor with Multi-Material Architecture for Cancer Detection Integrating 1D-CNN Machine Learning for Performance Prediction and Analysis](https://doi.org/10.1007/s11468-025-02912-w) | 2025 | 8 | 14 | Plasmonics | Jacob Wekalao, Hussein A. Elsayed, Ahmed M. El‐Sherbeeny, et al. |
| 36 | [Plasmon-Enhanced Charge Transport in Graphene-Au-SiO₂ Metasurfaces for Terahertz Biosensor Applications](https://doi.org/10.1007/s11468-025-02945-1) | 2025 | 8 | 15 | Plasmonics | Jacob Wekalao, Marouan Kouki, Sana Ben Khalifa, et al. |
| 37 | [Locally weighted linear regression–optimized graphene–metal metasurface sensor for high-sensitivity organic compound detection in terahertz regime](https://doi.org/10.1515/zna-2025-0050) | 2025 | 8 | 15 | Zeitschrift für Naturforschung A | Jacob Wekalao, Ahmed Mehaney, Bashir Salah, et al. |
| 38 | [Novel terahertz biosensor integrating MXene/black phosphorus/graphene on metasurface architecture for enhanced pregnancy detection](https://doi.org/10.1007/s11082-025-08205-0) | 2025 | 8 | 16 | Optical and Quantum Electronics | Jacob Wekalao, Oumaymah Elamri |
| 39 | [Graphene metasurfaces biosensor for COVID-19 detection in the infra-red regime](https://doi.org/10.1038/s41598-025-92991-w) | 2025 | 8 | 26 | Scientific Reports | Hussein A. Elsayed, Jacob Wekalao, Ahmed Mehaney, et al. |
| 40 | [ALMA SURVEY OF LUPUS PROTOPLANETARY DISKS. I. DUST AND GAS MASSES](https://doi.org/10.3847/0004-637x/828/1/46) | 2016 | 8 | 595 | The Astrophysical Journal | Megan Ansdell, Jonathan P. Williams, Nienke van der Marel, et al. |
| 41 | [<i>Planck</i>2018 results](https://doi.org/10.1051/0004-6361/201833886) | 2019 | 8 | 628 | Astronomy and Astrophysics | N. Aghanim, Y. Akrami, M. Ashdown, et al. |
| 42 | [A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km s<sup>−1</sup> Mpc<sup>−1</sup> Uncertainty from the Hubble Space Telescope and the SH0ES Team](https://doi.org/10.3847/2041-8213/ac5c5b) | 2022 | 8 | 1445 | The Astrophysical Journal Letters | Adam G. Riess, Wenlong Yuan, Lucas M. Macri, et al. |
| 43 | [The Astropy Project: Sustaining and Growing a Community-oriented Open-source Project and the Latest Major Release (v5.0) of the Core Package*](https://doi.org/10.3847/1538-4357/ac7c74) | 2022 | 8 | 2698 | The Astrophysical Journal | The Astropy Collaboration, Adrian M. Price-Whelan, Pey Lian Lim, et al. |
| 44 | [<i>Gaia</i> Data Release 2](https://doi.org/10.1051/0004-6361/201833051) | 2018 | 8 | 7647 | Astronomy and Astrophysics | A. G. A. Brown, A. Vallenari, T. Prusti, et al. |
| 45 | [The PRISMA 2020 statement: an updated guideline for reporting systematic reviews](https://doi.org/10.1136/bmj.n71) | 2021 | 8 | 55181 | BMJ | Matthew J. Page, Joanne E. McKenzie, Patrick M. Bossuyt, et al. |
| 46 | [The ALMA Survey of Gas Evolution of PROtoplanetary Disks (AGE-PRO). VI. Comparison of Dust Evolution Models to AGE-PRO Observations](https://doi.org/10.3847/1538-4357/add1d0) | 2025 | 7 | 7 | The Astrophysical Journal | N. T. Kurtovic, Matías Gárate, Paola Pinilla, et al. |
| 47 | [High-Sensitivity Graphene-MoS₂ Hybrid Metasurface Biosensor with Machine Learning Optimization for Hemoglobin Detection](https://doi.org/10.1007/s11468-025-02886-9) | 2025 | 7 | 13 | Plasmonics | Jacob Wekalao |
| 48 | [Enhanced Terahertz Graphene Metasurface Biosensor for Early Breast Cancer Detection with Machine Learning Optimization Based on Locally Weighted Linear Regression](https://doi.org/10.1007/s11468-025-02905-9) | 2025 | 7 | 14 | Plasmonics | Jacob Wekalao |
| 49 | [Design and Performance Evaluation of a Graphene Biosensor for Protein Detection with Two, Three Bit Encoding and Machine Learning Optimization](https://doi.org/10.1007/s11468-025-02925-5) | 2025 | 7 | 14 | Plasmonics | Jacob Wekalao, Yahya Ali Abdelrahman Ali, Taoufik Saidani, et al. |
| 50 | [High-Sensitivity Terahertz Gas Sensor Using Graphene-Enhanced Metasurfaces with Machine Learning Optimization](https://doi.org/10.1007/s11468-025-02843-6) | 2025 | 7 | 15 | Plasmonics | Jacob Wekalao |
<!-- TRENDING-END -->
