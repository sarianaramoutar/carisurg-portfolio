# CARISURG PROJECT MODEL SELECTION AUDIT TRAIL & BENCHMARK RESULTS

**To:** Dr. de Freitas (Clinical Lead) & Martina Griffith (Clinical IT Lead)  
**From**: Sariana Ramoutar  
**Date:** July 31st, 2026

## **I. Model Comparison Benchmark Table**

This table summarises all machine learning models evaluated during Weeks 6–7. Models were compared using the same cleaned Emergency Severity Index (ESI) dataset with an 80/20 stratified train-test split (`random_state=42`).

Performance was assessed using accuracy, macro precision, macro recall, and macro F1-score to account for class imbalance across ESI triage levels.

| Model                          | Key Hyperparameters                      |  Accuracy | Macro Precision | Macro Recall |  Macro F1 | Training Time (s) | Inference Time (s/patient) |
| :----------------------------- | :--------------------------------------- | :-------: | :-------------: | :----------: | :-------: | :---------------: | :------------------------: |
| Dummy Classifier               | Stratified random baseline               |   0.204   |      0.375      |     0.204    |   0.204   |       0.003       |          0.0000004         |
| Logistic Regression            | `lbfgs`, `max_iter=1000`                 |   0.662   |      0.547      |     0.436    |   0.461   |       10.802      |          0.0000013         |
| Decision Tree                  | `max_depth=3`                            |   0.518   |      0.290      |     0.218    |   0.236   |       0.260       |          0.0000012         |
| **🏆 Optimised Random Forest** | **200 trees, `class_weight="balanced"`** | **0.636** |    **0.458**    |   **0.370**  | **0.390** |     **37.301**    |        **0.0000886**       |
| Gradient Boosting              | Sequential boosted trees                 |   0.504   |      0.646      |     0.391    |   0.421   |      100.569      |          0.0000085         |
| Multi-Layer Perceptron         | Neural network with early stopping       |   0.666   |      0.547      |     0.491    |   0.504   |       6.460       |          0.0000021         |

--- 

| Model               | Explainability                                         |
| ------------------- | ------------------------------------------------------ |
| Dummy Classifier    | No clinical reasoning; random predictions              |
| Logistic Regression | High; coefficients show feature impact                 |
| Decision Tree       | Very high; decisions can be followed visually          |
| Random Forest       | Moderate-high; feature importance + ensemble reasoning |
| Gradient Boosting   | Lower; sequential trees are harder to trace            |
| MLP                 | Low; hidden layers make reasoning difficult            |


**Selected model: Optimised Random Forest**

---

## **II. Final Model Selection**
> [!NOTE]
> The final implementation model selected was the **optimised Random Forest classifier**.

Logistic Regression achieved strong baseline performance and remained an important comparison model. However, it was not selected as the final model because it assumes mainly linear relationships between input features and the target outcome. In emergency triage, patient risk is often determined by combinations of factors rather than individual measurements alone. For example, the relationship between heart rate, blood pressure, oxygen saturation, and patient symptoms may create a risk pattern that is not captured well by a linear model.

Random Forest was selected because it can model these more complex, non-linear relationships while maintaining useful levels of explainability through feature importance analysis.

### **Reasons for Selection**

* **Non-linear modelling:** Captures complex interactions between clinical features without requiring manual feature engineering.
* **Class imbalance handling:** `class_weight="balanced"` improves representation of less frequent but clinically important triage classes.
* **Explainability:** Feature importance rankings allow review of which variables contribute most to model predictions.
* **Clinical suitability:** Provides a stronger balance between predictive flexibility and transparency compared with less interpretable models such as neural networks.

Logistic Regression will remain as a baseline comparison model because of its simplicity, speed, and strong interpretability.

---

## **III. Decision Journal Reference**

The complete model selection process, including evaluation criteria, trade-offs, and final decision reasoning, is documented in the Week 7 decision journal.

**Reference:** `docs/week7_decision_journal.md`

---

## **IV. Final Recommendation**

The optimised Random Forest model will be used as the final prototype model for the explainable AI emergency department triage assistant.

Before clinical use, additional validation using local Caribbean healthcare data, clinician review, and safety testing would be required.
