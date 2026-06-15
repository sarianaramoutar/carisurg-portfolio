# CariSurg Portfolio
A portfolio repository containing coursework completed for the CariSurg Healthcare AI Training Programme 2026.

## Purpose
This repository documents work completed during the CariSurg Healthcare AI Training Programme. It contains exploratory data analysis notebooks, technical reports and research documents developed throughout the programme. 

The project focuses on clinical data analysis and AI-assisted clinical decision support. Its intended aim is to improve patient prioritisation and operational efficiency in Caribbean healthcare settings. 

The repository is intended for programme instructors, reviewers and other readers who wish to understand the methods, findings and deliverables produced throughout this project. 

## Installation
1. Clone the repository and open it: 
```bash
git clone https://github.com/sarianaramoutar/carisurg-portfolio.git 

cd carisurg-portfolio
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

4. Install the required libraries: 
```bash
pip install -r requirements.txt
```

## Usage 
### Running the Notebooks
Launch Jyupiter Lab
```bash
jupyter lab
```

### Exploring the Notebooks 
Open any notebook from the `notebooks/` directory, which contains:
- `Gender data cleaning`
- `Respiratory rate cleaning and validation`
- `Clinical data visualisation`

Notebooks in this folder were created using Google Colab and can be run independently of each other. 

### Viewing Documentation
The reports, research documents and written submissions can be found in the `docs/` directory as PDF files:
- `Week 0 reports`
- `Week 1 literature review`
- `Week 1 preliminary proposal`

### Data
Datasets used in this project are described in the `data/` directory. 

The datasets used throughout the CariSurg Healthcare AI Training Programme were provided by the programme team for educational purposes.

To respect programme guidelines and data-governance considerations, the original datasets are not redistributed within this repository. Users wishing to reproduce the analyses should obtain the relevant datasets directly through the programme or use equivalent publicly available datasets.

## Repository Structure
```text
carisurg-portfolio/

├── data/              Datasets used throughout the programme
├── docs/              Reports, proposals and written submissions
├── notebooks/         Jupyter notebooks for analysis
├── src/               Source code and future project scripts
├── README.md          Project overview and documentation
├── requirements.txt   Python package dependencies
├── LICENSE            MIT license
└── .gitignore         Files excluded from version control
```

## Contributing
This repository was created as part of the CariSurg Healthcare AI Training Programme. Future updates should be made through feature branches and merged using pull requests to maintain a clear and auditable version history.

## License
This project is licensed under the MIT License. See `LICENSE` file for details. 

## Author
Sariana Ramoutar

sarianaivramoutar@gmail.com

CariSurg MedTech Pathways Programme, Healthcare AI Cohort (2026)
