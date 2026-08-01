# Decision Journal
> [!IMPORTANT]
> The purpose of this file is to document any major decisions made regarding the main project over the course of the programme. 

## Model Selection
**Date:** July 20th, 2026
### Context
- Six machine learning models were benchmarked using the Yale Emergency Department dataset (80/20 train/test split) to determine which offered the most appropriate balance between predictive performance, explainability and practical implementation.
- The objective was to recommend a model for an explainable AI clinical decision-support system intended to support, rather than replace, Emergency Department triage decisions.

### Alternatives Considered
- **Random Forest** – Strong overall performance with moderate interpretability through feature importance, making it suitable for clinical review.
- **Gradient Boosting** – Competitive predictive performance but offered lower interpretability and the longest training time of the models evaluated.
- **Neural Network (Multi-Layer Perceptron)** – Achieved the strongest benchmark performance but functioned as a largely black-box model, making individual predictions more difficult to explain.

### Decision
**Random Forest was selected because it provided the best overall balance between predictive performance, explainability and practical deployment.**

### Reasoning
- The small improvement in predictive performance achieved by the neural network was not considered sufficient to justify the reduction in transparency for a clinical decision-support system.
- Random Forest allows clinicians to examine which clinical factors influenced each prediction, supporting clinical review and increasing confidence in the model's recommendations.
- Although Random Forest requires longer training than the simpler models, training occurs only periodically, while prediction remains sufficiently fast for routine Emergency Department use.

### Things I Do Not Yet Know
- Whether the selected model will achieve similar performance when evaluated using Caribbean Emergency Department data rather than the current dataset.
- Whether clinicians will find the model's explanations sufficiently clear and useful during routine clinical decision-making.

### Reflection
This decision prioritises a model that clinicians are more likely to understand, review and trust rather than simply selecting the highest benchmark score. Future optimisation may change this recommendation if another model demonstrates substantially better performance while maintaining an acceptable level of explainability.
