# CariSurg Portfolio
A portfolio repository containing coursework completed for the CariSurg Healthcare AI Training Programme 2026.

## Purpose
This repository documents work completed during the CariSurg Healthcare AI Training Programme. It contains exploratory data analysis notebooks, technical reports, research documents and a modular machine learning pipeline developed throughout the programme. 

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
| **8** | Reproducibility & Modular Project Design | Modular source refactoring (`src/`), YAML config management, end-to-end training pipeline script (`scripts/train.py`), unit test suite (`pytest`), and handover documentation | 
| **9+** | *To be added* | Future coursework and project development |

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

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

3. Install the required libraries: 
```bash
pip install -r requirements.txt
```

## Usage 
### Running Automated Tests
Run the test suite to check that data loading, feature creation, and model training components are working correctly:

```bash
pytest tests/
```

### Training the Machine Learning Model
The main training pipeline can be run using: 

```bash
python scripts/train.py --config config.yaml
```
This script loads the dataset, performs preprocessing, creates clinical features, trains the optimised Random Forest model, evaluates performance, and saves the results.

### Exploring the Notebooks 
Launch Jupyter Lab:

```bash
jupyter lab
```

The `notebooks/` directory contains:
- `W0 Gender data cleaning`
- `W0 Respiratory rate cleaning and validation`
- `W0 Clinical data visualisation`
- `W5 Clinical data literacy`
- `W5 Data profiling`
- `W5 Exploratory visualisations`
- `W6 Baseline model` (Implementation and Evaluation of 3 baseline models)
- `W7 Optimisation techniques` (Implementation and Evaluation of 3 complex models and Optimisation of the leading model)

> The notebooks were created using Google Colab and can be run independently.

### Viewing Documentation
Reports, research documents, and project documentation can be found in the `docs/` directory:
- `Week 0 reports`
- `Research Work` for Weeks 1-4
- `Preliminary Proposal` for Weeks 1-4
- `Feasibility Memo` for Week 5
- `Baseline Model Report` and `Primary Metric Justification` for Week 6
- `Cost Benefit Memo` and `Decision Journal` for Week 7
- `Model Selection` for Week 8

> The `HANDOVER.md` file exists in the main part of the repo, containing setup instructions and the project handover guide. 

### Data
Datasets used in this project are described in the `data/` directory. 

The datasets used throughout the CariSurg Healthcare AI Training Programme were provided by the programme team for educational purposes.

> To respect programme guidelines and data-governance considerations, the original datasets are not redistributed within this repository. Users wishing to reproduce the analyses should obtain the relevant datasets directly through the programme or use an equivalent publicly available dataset.

## Reproducibility
To improve reproducibility, all model development uses a fixed random seed:

```python
random_state = 42
```

This random seed was used for the train/test split and all baseline machine learning models unless otherwise stated.

## Repository Structure
```text
carisurg-portfolio/

├── data/              Dataset files (not included in repository)
├── docs/              Reports, decision logs, and written documentation
├── notebooks/         Jupyter notebooks for analysis and development
├── scripts/           Executable project scripts
│   └── train.py       Main model training pipeline
├── src/               Reusable Python modules
├── tests/             Automated tests
├── config.yaml        Model and pipeline configuration settings
├── HANDOVER.md        Project setup and handover guide
├── requirements.txt   Required Python packages
├── LICENSE            MIT License
├── README.md          Repository overview
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
