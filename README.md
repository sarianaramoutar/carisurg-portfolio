# CariSurg Portfolio
A portfolio repository containing coursework completed for the CariSurg Healthcare AI Training Programme 2026.

## Purpose
This repository documents work completed during the CariSurg Healthcare AI Training Programme. It contains exploratory data analysis notebooks, technical reports and research documents developed throughout the programme. 

The project focuses on clinical data analysis, machine learning and explainable AI for emergency department triage, with the long-term goal of supporting clinical decision-making and improving patient prioritisation in Caribbean healthcare settings. 

The repository is intended for programme instructors, reviewers and other readers who wish to understand the methods, findings and deliverables produced throughout this project. 

## Weekly Contents

| Week | Topic | Main Deliverables |
|:----:|-------|-------------------|
| **0** | Clinical Data Literacy | Data cleaning, validation, exploratory visualisations and Git/GitHub setup |
| **1** | Research Foundations | Problem definition, literature review and project planning |
| **2** | Preliminary Proposal | AI solution proposal, methodology and supporting research |
| **3** | Healthcare Workflows & Systems Thinking | Emergency Department workflow analysis, stakeholder analysis and workflow diagrams |
| **4** | Ethics, Safety & Risk Awareness | Risk register, risk analysis and AI governance documentation |
| **5** | Clinical Data Exploration | Dataset profiling, exploratory data analysis, feasibility memo and clinical visualisations |
| **6** | Baseline Machine Learning | Logistic Regression, Decision Tree, DummyClassifier, model evaluation and Explainable AI interpretation |
| **7** | Complex Machine Learning and Optimisation | Random Forest, Gradient Boosting and Multi-Layer Perceptron Evaluation and Comparison | 
| **8+** | *To be added* | Future coursework and project development |

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
Launch Jupyter Lab
```bash
jupyter lab
```

### Exploring the Notebooks 
Open any notebook from the `notebooks/` directory, which contains:
- `W0 Gender data cleaning`
- `W0 Respiratory rate cleaning and validation`
- `W0 Clinical data visualisation`
- `W5 Clinical data literacy`
- `W5 Data profiling`
- `W5 Exploratory visualisations`
- `W6 Baseline model` (Implementation and Evaluation of 3 baseline models)
- `W7 Optimisation techniques` (Implementation and Evaluation of 3 complex models and Optimisation of the leading model)

Notebooks in this folder were created using Google Colab and can be run independently of each other. 

### Viewing Documentation
The reports, research documents and written submissions can be found in the `docs/` directory as PDF files:
- `Week 0 reports`
- `Research Work` for Weeks 1-4
- `Preliminary Proposal` for Weeks 1-4
- `Feasibility Memo` for Week 5
- `Baseline Model Report` and `Primary Metric Justification` for Week 6
- `Cost Benefit Memo` for Week 7
- `Decision Journal` for documenting major decisions regarding the project made throughout the programme

### Data
Datasets used in this project are described in the `data/` directory. 

The datasets used throughout the CariSurg Healthcare AI Training Programme were provided by the programme team for educational purposes.

To respect programme guidelines and data-governance considerations, the original datasets are not redistributed within this repository. Users wishing to reproduce the analyses should obtain the relevant datasets directly through the programme or use equivalent publicly available datasets.

## Reproducibility
To ensure that results are reproducible across different environments, all machine learning models in this repository use a fixed random seed:

```python
random_state = 42
```

This random seed was used for the train/test split and all baseline machine learning models unless otherwise stated.

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

**Sariana Ramoutar**

Biomedical Technology Undergraduate  
The University of the West Indies, St Augustine

**CariSurg MedTech Pathways Programme**  
Healthcare AI Cohort (2026)

📧 **Email:** sarianaivramoutar@gmail.com
