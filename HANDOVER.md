# CARISURG PROJECT HANDOVER DOCUMENT

## 1. Project Summary

This project implements a modular machine learning pipeline for Emergency Department (ED) triage prediction using the Emergency Severity Index (ESI 1–5). The pipeline loads and cleans patient data, engineers clinical features, trains a machine learning model, evaluates its performance, and saves the trained model for future use.

---

## 2. Final Model

> [!IMPORTANT]
> **Selected Model:** Optimised Random Forest Classifier
>
> Logistic Regression is also included in the project as a baseline model and alternative candidate. The model used for training can be changed in `config.yaml`.

---

## 3. Repository Structure

```text
carisurg-portfolio/
│
├── data/              Dataset location (not included in the repository)
├── docs/              Reports, proposals, and project documentation
├── notebooks/         Development and analysis notebooks
├── scripts/           Executable project scripts
│   └── train.py
├── src/               Modular source code
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── utils.py
├── tests/             Automated sanity tests
│   ├── test_data.py
│   └── test_train.py
├── config.yaml        Project configuration
├── README.md          Project overview
├── requirements.txt   Python package dependencies
├── LICENSE            MIT License
└── .gitignore         Files excluded from version control
```

---

## 4. Getting Started

> [!NOTE]
> Before running the project:
>
> * Install Python 3.
> * Install the required packages from `requirements.txt`.
> * Place `yaleemmlc_admissionprediction_triage.csv` inside the `data/` folder.
> * Check that the dataset path in `config.yaml` is correct.

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

Before training, verify that the project is set up correctly.

```bash
pytest tests/
```

The test suite checks that:

* The dataset loads successfully.
* The required schema and ESI target values are valid.
* The complete training pipeline runs without errors on a small sample.

### Train the model

Run the full training pipeline using:

```bash
python scripts/train.py --config config.yaml
```

> [!NOTE]
> During execution, the pipeline will:
>
> 1. Load the configuration file.
> 2. Load and clean the dataset.
> 3. Create engineered clinical features.
> 4. Select predictor variables.
> 5. Split the data into training and testing sets.
> 6. Impute missing values.
> 7. Train the selected model.
> 8. Evaluate model performance.
> 9. Save the trained model.

---

## 6. Changing the Model

The model used by the training pipeline is controlled in `config.yaml`.

```yaml
model:
  model_type: "random_forest"
```

Available options are:

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

## 7. Known Limitations

* The project was developed using the Yale Emergency Department dataset and has not been validated on Caribbean clinical data.
* The repository does not include the dataset. It must be obtained separately and placed in the `data/` folder before running the pipeline.
* This project is intended for research and educational purposes and should not be used as a replacement for clinical judgement.

---

## 8. Contact

**Developer:** Sariana Ramoutar  
**Programme:** CariSurg MedTech Pathways Programme – Healthcare AI Cohort (2026)  
**Contact:** sarianaivramoutar@gmail.com
