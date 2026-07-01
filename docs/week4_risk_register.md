# Week 4: Risk Register & Memo

## Part 1: Comprehensive Risk Register
This risk register outlines the core technical, operational, ethical, and equity risks associated with deploying an AI-assisted triage system in an emergency department setting.

| Risk Name | Category | Likelihood | Impact | Mitigation Strategy | Signal of Success |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Incorrect Triage Recommendation** | AI-Technical | **Medium** | High | Validate the model before each testing phase using a separate dataset. The AI provides recommendations only, while the triage nurse remains responsible for the final ESI decision. The interface explains the clinical factors influencing each recommendation. | Validation testing shows fewer than **2%** of high-acuity (ESI 1–2) patients are under-triaged, and nurses override incorrect recommendations when appropriate. |
| **Poor Performance on Caribbean Patients** | Equity | **Medium** | High | Evaluate model performance across available patient groups and clearly document any limitations before deployment. Future versions should be validated using Caribbean clinical data. | Performance differences between patient groups remain small, or any limitations are clearly documented for future improvement. |
| **Misleading AI Explanations** | AI-Technical | **Low** | High | Present explanations using clear, non-technical language that highlights the patient's most influential symptoms and vital signs. Review explanations during testing to ensure they accurately reflect the model's reasoning. | Clinicians report that explanations are easy to understand and accurately represent the AI's reasoning during user testing. |
| **Increased Triage Time** | Operational | **Medium** | Medium | Use information already collected during routine triage to avoid duplicate data entry. Measure assessment time during usability testing and simplify the interface if delays occur. | Average triage time increases by **less than one minute** compared with the existing workflow. |
| **Over-Reliance on AI Recommendations** | Ethical | **Medium** | High | Clearly state that the AI is a decision-support tool only. Nurses remain responsible for every triage decision and are encouraged to compare the AI's recommendation with their own clinical judgement. | Clinicians continue overriding AI recommendations when appropriate, demonstrating that independent clinical judgement is maintained. |
| **Patient Privacy and Data Security** | Ethical | **Low** | High | Use only de-identified, publicly available datasets during development. Restrict access to project data and exclude all patient-identifying information from the prototype. | No patient-identifiable information is used or stored during development or testing. |
| **Unfair Recs for Certain Patient Groups** | Equity | **Medium** | High | Compare prediction accuracy across different patient groups during evaluation and investigate any significant differences before further development. | No patient group performs substantially worse than the overall model, or any differences are clearly reported. |
| **Clinicians Do Not Trust the AI** | Operational | **Medium** | Medium | Focus the prototype on explainability by showing why each recommendation was made. Collect clinician feedback after testing and improve explanations where necessary. | Most clinicians report that they understand the AI's recommendations and find the explanations useful. |
| **AI Fails to Work at Other Hospitals (Generalisation Failure)** | AI-Technical | **Medium** | High | Clearly state that the prototype has only been validated on the available dataset. Future deployment should include validation using local hospital data before clinical use. | Project documentation clearly identifies external validation as a requirement before deployment in another hospital. |
| **System Failure or Technical Downtime** | Operational | **Low** | High | Ensure existing manual triage procedures remain available at all times so patient care can continue if the AI becomes unavailable. | During testing, manual triage continues safely whenever the AI system is unavailable. |

---

## Part 2: Risk Memo

### Project Title
**An Explainable AI Assistant to Support Emergency Department Triage in the Caribbean**

This memo summarises the **three highest-priority risks** identified for the proposed AI-assisted triage system. These risks were selected because they have the greatest potential to affect patient safety, clinical decision-making, and the successful adoption of the system in a live hospital environment. 

### Risk 1: Incorrect Triage Recommendation

The most serious risk is that the AI may recommend the **wrong Emergency Severity Index (ESI) level** for a patient. If a critically ill patient is mistakenly classified as lower priority, treatment could be delayed, increasing the risk of serious clinical harm. Likewise, assigning a low-risk patient to a higher priority category may unnecessarily use valuable emergency department resources.

> **Mitigation:** The AI will function only as a clinical decision-support tool. The triage nurse will always make the final decision, and the system will display the symptoms and vital signs that contributed most to its recommendation. This allows nurses to compare the AI's reasoning with their own clinical assessment before accepting or rejecting the recommendation.

### Risk 2: Clinicians Do Not Trust the AI

Even a highly accurate AI system provides little benefit if clinicians do not trust it enough to use it. Many healthcare AI systems operate as **"black boxes"**, producing recommendations without explaining how they reached their conclusions. This lack of transparency can discourage clinicians from using the system during busy emergency department workflows.

> **Mitigation:** This project focuses on **Explainable AI (XAI)** by showing the clinical factors that contributed most to each recommendation. Clear explanations help clinicians understand the AI's reasoning, supporting informed decision-making and appropriate trust in the system.

### Risk 3: Over-Reliance on AI Recommendations

The opposite problem can also occur. As clinicians become familiar with the system, they may begin accepting AI recommendations automatically without applying their own professional judgement. This is known as **automation bias** and can become dangerous if the AI makes an incorrect recommendation.

> **Mitigation:** The proposed system is designed to support clinical judgement rather than replace clinician assessment. Nurses remain responsible for every triage decision, and the AI serves as an additional source of information—not a final authority. By making the AI's reasoning visible, clinicians are encouraged to critically evaluate each recommendation before acting on it.

### Summary

These three risks highlight the balance required for safe healthcare AI. The system must be accurate enough to support clinical decisions, transparent enough for clinicians to understand and trust, and carefully integrated into practice so that it supports professional judgement without replacing it. Addressing these risks is essential before any AI-assisted triage system can be safely introduced into clinical practice.
