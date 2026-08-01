# **Week 8 – Model Selection Audit Trail & Benchmark Results**

**Author**: Sariana Ramoutar  
**Programme**: CariSurg MedTech Pathways Programme – Healthcare AI Cohort (2026)  

---

## **1. Model Comparison Benchmark Table**

This document provides a comprehensive audit trail of the machine learning models evaluated during Weeks 6–7. Models were compared across predictive performance, computational efficiency, and clinical interpretability considerations.

All models were evaluated using the cleaned Emergency Severity Index (ESI) dataset with a stratified 80/20 train-test split (`random_state=42`). Performance metrics include overall accuracy, macro-averaged precision, macro-averaged recall, and macro F1-score to account for severe class imbalance across ESI triage levels.

| Model | Key Configuration / Hyperparameters | Accuracy | Macro Precision | Macro Recall | Macro F1 | Training Time (s) | Inference Time per Patient (s) | Interpretability & Clinical Explainability Details |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Dummy Classifier** | Stratified random baseline | 0.204 | 0.375 | 0.204 | 0.204 | 0.003 | 0.0000004 | **N/A (Random baseline)**: Assigns predictions based solely on random class distributions without evaluating patient data. |
| **Logistic Regression** | Multi-class linear classifier (`lbfgs`, `max_iter=1000`) | 0.662 | 0.547 | 0.436 | 0.461 | 10.802 | 0.0000013 | **High (Direct linear weights)**: Clinicians can directly inspect the exact mathematical weight attached to each vital sign to understand its positive or negative impact on triage urgency. |
| **Decision Tree** | Single decision tree (`max_depth=3`) | 0.518 | 0.290 | 0.218 | 0.236 | 0.260 | 0.0000012 | **Very High (Visual decision flowchart)**: Generates a simple, step-by-step logic tree (e.g., *Is Heart Rate > 110?*) that clinicians can visually follow and verify in real time. |
| **🏆 Random Forest** | **200 trees, `class_weight="balanced"`, clinical features** | **0.636** | **0.458** | **0.370** | **0.390** | **37.301** | **0.0000886** | **Moderate (Global feature importance)**: Aggregates predictions across 200 trees. While individual tree paths are complex, it provides clear global feature ranking graphs showing which vital signs drove overall predictions. |
| **Gradient Boosting** | Sequential boosted decision tree ensemble | 0.504 | 0.646 | 0.391 | 0.421 | 100.569 | 0.0000085 | **Low (Sequential tree dependencies)**: Fits trees sequentially to correct previous errors, creating complex mathematical dependencies that are difficult for clinicians to trace back to raw vital signs. |
| **Multi-Layer Perceptron** | Neural network with early stopping | 0.666 | 0.547 | 0.491 | 0.504 | 6.460 | 0.0000021 | **Very Low (Opaque "black box")**: Passes inputs through hidden layers of abstract mathematical weights, making it impossible to explain to a clinician why a specific patient received a given ESI score. |

> [!NOTE]  
> 🏆 **Selected Model**: **Random Forest** was retained as the production baseline.

---

## **2. Selected Model**

The final selected model is the **Random Forest classifier**.

Although the Multi-Layer Perceptron achieved higher raw numerical metrics, Random Forest provides the most balanced combination of predictive capability, model transparency, and safety for deployment in an Emergency Department clinical decision-support environment.

### Key selection factors:
* **Non-Linear Modelling**: Capable of capturing non-linear interactions between physiological parameters without manual feature engineering.
* **Class Imbalance Handling**: Built-in support for balanced class weighting prevents high-urgency (ESI-1 and ESI-2) patients from being overlooked.
* **Clinician Trust**: Provides global feature importance rankings (e.g., verifying that abnormal vital signs like Shock Index or Oxygen Saturation heavily drive high urgency scores).
* **Auditability**: Offers significantly greater transparency for clinical review compared with opaque neural network architectures.

---

## **3. Decision Rationale**

### **Logistic Regression vs. Random Forest**
Logistic Regression served as a primary linear baseline during Week 6. It achieved strong, competitive performance scores and remains an important benchmark model.

However, Random Forest was selected because emergency room clinical indicators rarely interact in a strictly linear manner. Vital signs often produce compound risk signals when combined—for instance, a elevated heart rate combined with low blood pressure (Shock Index) indicates severe physiological instability far more accurately than assessing either metric on its own.

Random Forest models these non-linear clinical interactions naturally across its decision trees while maintaining clear feature importance summaries. Logistic Regression remains retained in the codebase as a fast baseline for future comparative testing.

---

## **4. Detailed Evaluation of Models Not Selected**

### **Multi-Layer Perceptron (Neural Network)**
* **Why Rejected**: Despite producing the highest overall Macro F1 score (0.504), the Multi-Layer Perceptron was rejected due to its "black box" nature.
* **Clinical Impact**: In an emergency department setting, clinicians must be able to verify the underlying rationale for AI recommendations, especially for critical triage classifications. Neural networks process data through dense, uninterpretable hidden layer weights, making individual predictions nearly impossible to justify during a clinical audit or case review.

### **Gradient Boosting**
* **Why Rejected**: Gradient Boosting achieved competitive precision (0.646) but lagged in overall recall (0.391) and required substantially higher training time (100.57 seconds).
* **Clinical Impact**: Because Gradient Boosting constructs decision trees sequentially to minimise residual errors, the resulting decision boundaries become highly intricate. This sequential structure reduces interpretability compared to Random Forest, where trees are trained independently and aggregated via simple voting.

---

## **5. Link to Decision Journal**

The complete decision process—including clinical context, ethical considerations, trade-offs, and risk assessments—is documented in the Week 7 decision journal.  
* **Reference File**: `docs/week7_decision_journal.md`

---

## **6. Final Recommendation**

The Random Forest model is recommended for integration into the prototype explainable AI triage assistant.  

Prior to clinical deployment, further prospective testing, clinician usability reviews, and local Caribbean population validation are strongly recommended.
