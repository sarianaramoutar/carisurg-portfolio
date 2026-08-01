# CARISURG PROJECT HANDOVER DOCUMENT

## 1. Project Summary

This project develops an explainable machine learning pipeline for Emergency Department (ED) triage prediction using the Emergency Severity Index (ESI 1–5). The pipeline processes clinical data, creates relevant features, trains and evaluates machine learning models, and saves the final trained model. The aim is to support clinical decision-making by providing an AI-based triage assistant while keeping clinicians responsible for final decisions.

---

## 2. Final Model Decision

> [!IMPORTANT]
> **Selected Model:** Optimised Random Forest Classifier  
>
> **Reason:** Random Forest was selected because it provides the best balance between predictive performance, ability to model complex clinical relationships, and explainability through feature importance analysis.

Logistic Regression remains included as a baseline comparison model due to its simplicity and high interpretability.

---

## 3. Repository Structure

```text
carisurg-portfolio/
│
├── data/              Dataset location (not included in repository)
├── docs/              Reports, decision logs, and project documentation
├── notebooks/         Development and analysis notebooks
├── scripts/           Executable project scripts
│   └── train.py       Main training pipeline
├── src/               Modular Python source code
│   ├── data.py        Data loading and cleaning functions
│   ├── features.py    Clinical feature engineering functions
│   ├── model.py       Model training and evaluation functions
│   └── utils.py       Helper functions
├── tests/             Automated tests
├── config.yaml        Model and pipeline configuration
├── README.md          Project overview
├── requirements.txt   Python package dependencies
├── LICENSE            MIT License
└── .gitignore         Files excluded from version control
```

---

## 4. Setup Instructions
Before running the project:
* Install Python 3.
* Install the required packages from `requirements.txt`.
* Place `yaleemmlc_admissionprediction_triage.csv` inside the `data/` folder.
* Check that the dataset path in `config.yaml` is correct.

### Clone the repository

```bash
git clone https://github.com/sarianaramoutar/carisurg-portfolio.git
cd carisurg-portfolio
```

### Create and activate a virtual environment

| Step     | Windows                  | macOS / Linux               |
| -------- | ------------------------ | --------------------------- |
| Create   | `python -m venv .venv`   | `python3 -m venv .venv`     |
| Activate | `.venv\Scripts\activate` | `source .venv/bin/activate` |

### Install dependencies

```bash
pip install -r requirements.txt
```


---

## 5. Running the Project

### Run the sanity tests
The test suite checks that data loading, feature creation, and the training pipeline work correctly.

```bash
pytest tests/
```

The test suite checks that:
* The dataset loads successfully.
* The required schema and ESI target values are valid.
* The complete training pipeline runs without errors on a small sample.

### Train the machine learning model
Run the complete training pipeline using:

```bash
python scripts/train.py --config config.yaml
```

During execution, The pipeline will:
1. Load project configuration.
2. Load and clean the dataset.
3. Create engineered clinical features.
4. Prepare predictor variables.
5. Split data into training and testing sets.
6. Train the selected machine learning model.
7. Evaluate model performance.
8. Save the trained model.

---

## 6. Data Location and Governance
The dataset should be placed in:

```
data/yaleemmlc_admissionprediction_triage.csv
```

The dataset used throughout this project was provided by the CariSurg Healthcare AI Training Programme for educational and research purposes.

Due to programme data governance requirements, the original dataset is not included in this repository. Users wishing to reproduce the analysis must obtain the dataset through the appropriate programme channels or use an equivalent publicly available dataset.

## 7. Model Configuration
The model used by the training pipeline is controlled through `config.yaml`.

The selected model can be changed by updating the model configuration.

Example:
```yaml
model:
  model_type: "random_forest"
```

Available models include:

| Model               | `model_type`            |
| ------------------- | ----------------------- |
| Random Forest       | `"random_forest"`       |
| Logistic Regression | `"logistic_regression"` |
| Gradient Boosting   | `"gradient_boosting"`   |

After changing the configuration, simply rerun:

```bash
python scripts/train.py --config config.yaml
```

---

## 8. Known Limitations

* The model was developed using the Yale Emergency Department dataset and has not been validated on Caribbean clinical data.
* The dataset represents a specific healthcare setting and may not fully capture differences in patient populations, resources, or clinical workflows in other regions.
* The system is designed as a clinical decision-support prototype and should not replace professional clinical judgement.

---

## 9. Contact

**Developer:** Sariana Ramoutar  
**Programme:** CariSurg MedTech Pathways Programme – Healthcare AI Cohort (2026)  
**Email:** sarianaivramoutar@gmail.com
