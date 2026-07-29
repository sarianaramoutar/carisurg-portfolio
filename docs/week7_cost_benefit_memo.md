# CARISURG Project Cost-Benefit Memorandum

**To:** Dr. De Freitas, Emergency Department Clinical Board and Martina Griffith (Clinical IT Lead)

**From:** Sariana Ramoutar

**Date:** 28 July 2026

**Subject:** Model Optimisation Recommendation for Explainable AI Emergency Department Triage Assistant

---

# I. Verdict

> [!IMPORTANT]
> **The Random Forest model is recommended because it provides the best balance between predictive performance, explainability and practical clinical use.**

---

# II. Dataset and Methods

The models included traditional machine learning methods (**3 baseline:** Dummy Classifier, Logistic Regression and Decision Tree; **2 advanced:** Random Forest and Gradient Boosting) together with one neural network (Multi-Layer Perceptron), a type of AI model that learns complex patterns from data but is generally more difficult for people to understand.

Performance was assessed using Accuracy, Macro Precision, Macro Recall, Macro F1-score, Training Time, Inference Time (time taken to produce a prediction) and Interpretability (how easily clinicians can understand how the model reaches its recommendations). Confusion matrices were also used to show where each model correctly classified patients and where misclassifications occurred.

> [!NOTE]
> **Key Terms**
>
> - **Accuracy:** The proportion of all predictions that were correct.
> - **Macro Precision:** How often the model's predictions were correct across all ESI levels.
> - **Macro Recall:** How well the model identified patients in each ESI level.
> - **Macro F1-score:** A balanced measure that combines Precision and Recall.
> - **Training Time:** Time required to train the model.
> - **Inference Time:** Time taken to generate a prediction for one patient.
> - **Interpretability:** How easily clinicians can understand why the model made its recommendation.

## Table 1. Comprehensive Benchmark Table

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Training Time (s) | Inference Time per Prediction (s) | Interpretability |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| **Dummy Classifier** | 0.375 | 0.204 | 0.204 | 0.204 | 0.003 | 0.0000004 | Very High (Baseline Guess/Random) |
| **Logistic Regression** | 0.662 | 0.547 | 0.436 | 0.461 | 10.802 | 0.0000013 | High (Direct Feature Weights) |
| **Decision Tree** | 0.518 | 0.290 | 0.218 | 0.236 | 0.260 | 0.0000012 | Very High (Visual Decision Flowchart) |
| **Random Forest** | 0.636 | 0.458 | 0.370 | 0.390 | 37.301 | 0.0000886 | Moderate (Average Feature Importance) |
| **Gradient Boosting** | 0.646 | 0.504 | 0.391 | 0.421 | 100.569 | 0.0000085 | Low (Complex Tree Sequences) |
| **Multi-Layer Perceptron** | 0.666 | 0.547 | 0.491 | 0.504 | 6.460 | 0.0000021 | Very Low (Difficult to Explain) |

---

<img width="2453" height="1387" alt="image" src="https://github.com/user-attachments/assets/0968d975-4cfa-47fa-ad3f-188e14a66356" />

**Figure 1.** Confusion matrices comparing ESI predictions made by the six machine learning models. Values along the diagonal represent correct classifications, while off-diagonal values show misclassifications.

---

# III. Arguments Supporting the Recommended Model

## 1. It provides the best balance between performance and explainability.

Although the Multi-Layer Perceptron achieved the highest benchmark scores, its improvement over Random Forest was relatively small. Random Forest consistently classified the major ESI levels while remaining easier to interpret through feature importance analysis. Clinicians can also identify which variables most influenced the model overall, supporting the project's aim of assisting rather than replacing clinical judgement.

## 2. It is practical to implement.

Random Forest requires more training time than the simpler models, but training only occurs when the model is updated. Predictions are still produced in a fraction of a second, making the additional computing cost unlikely to affect patient care.

## 3. It supports safer long-term use.

Clinical AI systems must be monitored as new data becomes available. Random Forest allows clinicians to identify which clinical variables have the greatest overall influence on model predictions, making it easier to investigate unexpected results and improve the system over time than with a neural network.

---

# IV. Arguments Against the Recommended Model

## 1. It did not achieve the highest predictive performance.

The Multi-Layer Perceptron achieved the highest Accuracy, Macro Recall and Macro F1-score. However, this improvement was relatively small and came at the cost of much lower interpretability.

## 2. It requires more computing resources.

Random Forest takes longer to train than the simpler models, increasing the computing resources required whenever the model is retrained using updated data. This may increase maintenance costs over time.

## 3. It is not completely transparent.

Although Random Forest is easier to understand than a neural network, it still combines the results of many decision trees. This means some individual predictions may still require additional investigation before they can be fully explained.

---

# V. Risks and Unknowns

Several important uncertainties remain.

- The dataset was obtained from a single institution and has not yet been validated using Caribbean emergency department data.
- Model performance across different patient groups requires further evaluation to identify potential sources of bias.
- Further optimisation of the Gradient Boosting and Multi-Layer Perceptron models may produce different benchmark results.

---

# VI. Recommendation

Based on the current evidence, Random Forest is recommended for continued development because it provides the most appropriate balance between predictive performance, transparency, computing requirements and long-term maintainability. Although the Multi-Layer Perceptron achieved slightly stronger benchmark scores, the improvement was not large enough to outweigh the benefits of a model that clinicians can more easily understand, review and trust.

Future work should focus on further improving model performance, validating the model using additional clinical datasets and evaluating its performance within representative Caribbean healthcare settings before any real-world implementation.
