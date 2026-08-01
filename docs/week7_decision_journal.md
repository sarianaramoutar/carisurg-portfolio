# CARISURG PROJECT DECISION JOURNAL
**Author:** Sariana Ramoutar

> [!IMPORTANT]
> The purpose of this file is to document major decisions made regarding the main project throughout the programme.

## Model Selection

**Date:** July 20th, 2026

### Context

* Six machine learning models were benchmarked using the Yale Emergency Department dataset with an 80/20 stratified train-test split.
* Models were compared based on predictive performance, explainability, computational requirements, and suitability for an explainable AI clinical decision-support system.
* The aim was to select a model that supports Emergency Department triage decisions rather than replace clinical judgement.

### Alternatives Considered

* **Logistic Regression** – Strong baseline performance with high interpretability. However, it assumes mainly linear relationships between clinical features and may not capture more complex interactions between patient measurements.
* **Random Forest** – Strong predictive performance with improved ability to model non-linear relationships. Feature importance analysis provides useful insight into which variables contribute most to overall model behaviour.
* **Gradient Boosting** – Competitive performance but required the longest training time and provided lower interpretability due to its sequential tree structure.
* **Neural Network (Multi-Layer Perceptron)** – Achieved the strongest benchmark performance but operated as a largely black-box model, making clinical interpretation more difficult.

### Decision

**Random Forest was selected as the final model because it provided the strongest balance between predictive capability, explainability, and suitability for an emergency clinical decision-support system.**

### Reasoning

* Although the `Multi-Layer Perceptron` achieved slightly stronger benchmark metrics, the improvement was not considered sufficient to justify reduced transparency in a clinical setting.
* `Logistic Regression` provided a strong and interpretable baseline but was limited by its assumption of mainly linear relationships between input features and triage outcomes.
* `Random Forest` can capture more complex relationships between clinical variables while still allowing review of overall feature importance and model behaviour.
* Although Random Forest requires longer training compared with simpler models, this process occurs during development and optimisation. Prediction time remains suitable for prototype emergency department use.

### Things I Do Not Yet Know

* Whether the selected model will maintain similar performance when evaluated using Caribbean Emergency Department data rather than the current dataset.
* Whether clinicians will find the provided explanations sufficiently clear and useful during real-world decision-making.
* Whether additional explainability methods, such as local prediction explanations, would improve clinician understanding.

### Reflection

This decision prioritises a model that balances predictive performance with transparency and clinical usability rather than selecting a model based only on benchmark scores. Future optimisation may change this recommendation if another approach demonstrates substantially improved performance while maintaining acceptable explainability.
