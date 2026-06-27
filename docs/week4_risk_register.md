# Week 4: Risk Register & Memo

## Part 1: Comprehensive Risk Register
This risk register outlines the core technical, operational, ethical, and equity risks associated with deploying an AI-assisted triage system in an emergency department setting.

| Risk Name | Category | Likelihood | Impact | Mitigation Strategy | Signal of Success |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Incorrect Triage Recommendation** | AI-Technical | Medium | High | Limit AI output to advisory recommendations while keeping triage nurses fully responsible for final ESI assignment. Display clear confidence metrics and contributing vital signs inline so nurses can immediately audit the underlying reasoning. | Nurses regularly compare AI recommendations with their own assessments and confidently override the system when clinically necessary. |
| **Poor Performance on Caribbean Patients** | AI-Technical / Equity | **High** | High | Restrict prototype scope to "research only" in documentation. Evaluate system performance on a localized, independent testing dataset and establish routine monitoring protocols to flag demographic performance gaps. | Evaluation results show stable performance across different patient groups, or performance differences are clearly documented for future optimization. |
| **Misleading AI Explanations** | AI-Technical | **Medium** | High | Present explanations using clear visual methods and plain language that highlight the patient's most influential symptoms and vital signs instead of complex machine learning terms. | During demonstrations and testing, clinicians consistently report that they understand why the AI made its recommendation and can easily spot logical errors. |
| **Increased Triage Time** | Operational | Medium | Medium | Integrate the AI directly into existing Electronic Health Record workflows to automatically pull pre-recorded vital signs and presenting complaints, eliminating the need for duplicate manual data entry. | The average time needed to complete a triage assessment does **not** increase noticeably after introducing the AI prototype. Nurses report that the system fits naturally into their workflow. |
| **Over-Reliance on AI Recommendations** | Ethical | Medium | High | Explicitly state that the system is a decision-support tool only. The nurse remains responsible for the final triage decision, and the explanations provided by the AI must encourage critical thinking rather than blind acceptance. | Nurses continue making independent clinical decisions and occasionally override AI recommendations when their own assessment suggests a different priority level. |
| **Patient Privacy and Data Security** | Ethical | Low | High | Use strictly de-identified, publicly available data for research. Personal identifiers must never be included in AI training data, and access to patient information should be carefully controlled. | No patient-identifying information is included in the project dataset, and all project documentation confirms that de-identified data has been used throughout. |
| **Unfair Recs for Certain Patient Groups** | Equity | Medium | High | Evaluate model performance across different patient groups where possible, and actively discuss fairness and algorithmic bias as part of the system evaluation rather than focusing only on overall accuracy. | Evaluation results do not show large performance differences between patient groups, or any identified disparities are openly reported with recommendations for improvement. |
| **Clinicians Do Not Trust the AI** | Operational | Medium | Medium | Focus the prototype on explainability by showing the reasoning behind every recommendation instead of acting as a "black box." Integrate early feedback from clinicians to improve the user interface. | Users report that they understand the recommendations, find the explanations helpful, and achieve a high voluntary adoption rate during simulated triage walkthroughs. |
| **AI Fails to Work at Other Hospitals (Generalisation Failure)** | AI-Technical | Medium | **High** | Clearly describe the project's assumptions and limitations while recommending that future studies validate the model using local hospital data before any clinical deployment. | The project documentation clearly states the limitations of the prototype and identifies future validation using localized clinical data as a necessary next step. |
| **System Failure or Technical Downtime** | Operational | Low | High | Treat the AI as an optional support tool rather than an essential part of the workflow. Existing manual triage procedures must remain fully functional and uncompromised at all times. | During simulated software failures, nurses continue following the existing manual triage process without any disruption to patient care. |

---

## Part 2: Risk Memo

### Project Title
**An Explainable AI Assistant to Support Emergency Department Triage in the Caribbean**

This memo summarizes the **three highest-priority risks** identified for the proposed AI-assisted triage system. These risks were selected because they have the greatest potential to affect patient safety, clinical decision-making, and the successful adoption of the system in a live hospital environment. 

### Risk 1: Incorrect Triage Recommendation
The most serious risk is that the AI may recommend the **wrong Emergency Severity Index (ESI) level** for a patient. If a critically ill patient is mistakenly classified as lower priority, treatment could be delayed, increasing the risk of serious clinical harm. Likewise, assigning a low-risk patient to a higher priority category may unnecessarily use valuable emergency department resources.

> **Mitigation:** To reduce this risk, the AI will function *only* as a clinical decision-support tool. The triage nurse will always make the final decision, and the AI will display the symptoms and vital signs that influenced its recommendation. This allows nurses to compare the AI's reasoning with their own clinical assessment before deciding whether to accept or reject the recommendation. 

### Risk 2: Clinicians Do Not Trust the AI
Even a highly accurate AI system provides little benefit if clinicians do not trust it enough to use it. Many existing healthcare AI systems operate as **"black boxes,"** producing recommendations without explaining how they reached their conclusions. This lack of transparency can make clinicians reluctant to rely on the system during busy, high-stress emergency department workflows.

> **Mitigation:** This project directly addresses that problem by focusing heavily on **Explainable AI (XAI)**. Instead of presenting only a blind prediction, the system will clearly show the clinical factors that contributed most to its recommendation. Providing understandable explanations helps clinicians judge whether the recommendation is reasonable, increasing confidence in the system while supporting informed clinical decision-making.

### Risk 3: Over-Reliance on AI Recommendations
The opposite problem can also occur. As clinicians become familiar with the system, they may begin accepting AI recommendations automatically without applying their own professional judgement. This is known as **automation bias** and can become highly dangerous if the AI makes an undetected, incorrect recommendation.

> **Mitigation:** To minimize this risk, the proposed system is designed to support clinical judgement rather than replace clinician assessment. Nurses remain completely responsible for every triage decision, and the AI serves as an additional source of information, **not a final authority**. By making the AI's reasoning fully visible, clinicians are actively encouraged to critically evaluate each recommendation instead of accepting it without question.

### Summary
These three risks highlight the careful balance required for safe healthcare AI. The system must be accurate enough to support clinical decisions, transparent enough for clinicians to understand and trust, and carefully integrated into practice so that it supports professional judgement without replacing it. Addressing these risks is essential before any AI-assisted triage system can be safely introduced into clinical practice.
