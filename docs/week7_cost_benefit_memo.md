# CARISURG PROJECT COST-BENEFIT MEMORANDUM

**To:** Dr. De Freitas, Emergency Department Clinical Board and Martina Griffith (Clinical IT Lead)  
**From:** Sariana Ramoutar  
**Date:** July 21st, 2026  
**Subject:** Model Optimisation Recommendation for Explainable AI Emergency Department Triage Assistant  

---

## I. Verdict

> [!IMPORTANT]
> The Random Forest model is recommended because it provides the best overall balance between the predictive performance, explainability, computing requirements and suitability for clinical deployment.

---

## II. Dataset and Methods

The models included traditional machine learning methods (3 Baseline: Dummy Classifier, Logistic Regression, Decision Tree; 2 Complex: Random Forest, Gradient Boosting) and a neural network (Multi-Layer Perceptron), a type of AI model that learns complex patterns from data but is often more difficult for people to understand. 

Performance was assessed using seven criteria: Accuracy, Macro Precision, Macro Recall, Macro F1-score, Training Time, Inference Time (time taken to produce a prediction) and Interpretability (how easily clinicians can understand how the model reaches its recommendations). The aim was to identify the model that provides the most practical balance between predictive performance, transparency and implementation cost for an explainable AI assistant. 

### Table 1. Comprehensive Benchmark Table.

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Training Time (seconds) | Inference Time per Prediction (seconds) | Interpretability (the +1 axis) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Dummy Classifier** | 0.375 | 0.204 | 0.204 | 0.204 | 0.004 | 0.0000004 | Very High (Random/Simple) |
| **Logistic Regression** | 0.662 | 0.547 | 0.436 | 0.461 | 6.336 | 0.0000017 | High (Direct Coefficients) |
| **Decision Tree** | 0.518 | 0.290 | 0.218 | 0.168 | 0.260 | 0.0000014 | Very High (Visual Flowchart) |
| **Random Forest** | 0.636 | 0.509 | 0.384 | 0.412 | 51.418 | 0.0001691 | Moderate (Ensemble/ Importance) |
| **Gradient Boosting** | 0.646 | 0.531 | 0.405 | 0.440 | 89.294 | 0.0000086 | Low (Complex Tree Sequences) |
| **Multi-Layer Perceptron** | 0.667 | 0.540 | 0.449 | 0.472 | 16.933 | 0.0000022 | Very Low (Difficult to Explain) |

---

<img width="1043" height="521" alt="image" src="https://github.com/user-attachments/assets/e15ce2c2-e5fc-48d6-ba70-49d4d9bfd487" />

### Figure 1. Model Benchmark Comparison

---

## III. Arguments Supporting the Recommended Model

### 1. It provides the best balance between performance and explainability.
Although the neural network (Multi-Layer Perceptron) achieved slightly higher benchmark scores, Random Forest produced competitive predictive performance while allowing clinicians to identify which clinical variables contributed most to its recommendations. This makes the model easier to review and supports the project’s aim of assisting clinical decision-making rather than replacing it.

### 2. It is practical to implement.
Random Forest requires more computing time during model training than the simpler models. However, training is performed only when the model is updated, whereas predictions are generated quickly during routine use. As a result, the additional computing cost is unlikely to affect patient care while providing a more robust model.

### 3. It supports safer long-term use.
Clinical AI systems must be monitored and reviewed as new data becomes available. Random Forest allows clinicians to see which patient information, such as vital signs or presenting complaints, had the greatest influence on each recommendation. This makes it easier to investigate unexpected results, monitor performance over time and identify opportunities for improvement than with a neural network.

---

## IV. Arguments Against the Recommended Model

### 1. It did not achieve the highest predictive performance.
The Multi-Layer Perceptron achieved highest Accuracy, Macro Recall and Macro F1-score during benchmarking. Choosing Random Forest therefore involves accepting a small reduction in predictive performance in exchange for greater transparency.

### 2. It requires more computing resources.
Random Forest takes longer to train than the simpler models, increasing the computing resources required whenever the model is retrained using the updated data. This may increase maintenance costs over time.

### 3. It is not completely transparent.
Although Random Forest is easier to understand than a neural network, it still combines the results of many decision trees. This means some individual predictions may still require additional investigation before they can be fully explained.

---

## V. Risks and Unknowns

Several important uncertainties remain.

* The dataset was obtained from a single institution and has not yet been validated using Caribbean Emergency Department data.
* Model performance across different patient groups requires further evaluation to identify any potential sources of bias.
* Further optimisation of the Gradient Boosting and multi-Layer Perceptron models may produce different benchmark results.

---

## VI. Recommendation

Based on the current evidence, Random Forest is recommended for continued development because it provides the most appropriate balance between predictive performance, transparency, computing requirements and long-term maintainability. Although the Multi-Layer Perceptron achieved slightly stronger benchmark scores, the improvement was too small to outweigh the advantages of using a model that clinicians can more easily understand, review and trust.

Future work should focus on further improving model performance, validating the model using additional clinical datasets and evaluating its performance within representative Caribbean healthcare settings before any real-work implementation.
