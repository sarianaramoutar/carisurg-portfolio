# Week 4 Risk Memo
## Project
### An Explainable AI Assistant to Support Emergency Department Triage in the Caribbean
This memo summarises the `three` highest-priority risks identified for the proposed AI-assisted triage system. These risks were selected because they have the greatest potential to affect patient safety, clinical decision-making and the successful adoption of the system in a hospital environment. 

## Risk 1: Incorrect Triage Recommendation
The most serious risk is that the AI may recommend the **wrong Emergency Severity Index (ESI) level** for a patient. If a critically ill patient is mistakenly classified as lower priority, treatment could be delayed, increasing the risk of serious harm. Likewise, assigning a low-risk patient to a higher priority category may unnecessarily use valuable emergency department resources.

To reduce this risk, the AI will function only as a clinical decision-support tool. The triage nurse will always make the final decision, and the AI will explain the symptoms and vital signs that influenced its recommendation. This allows nurses to compare the AI's reasoning with their own clinical assessment before deciding whether to accept or reject the recommendation. 

## Risk 2: Clinicians Do Not Trust the AI
Even a highly accurate AI system provides little benefit if clinicians do not trust it enough to use it. Many existing healthcare AI systems operate as "black boxes," producing recommendations without explaining how they reached their conclusions. This **lack of transparency** can make clinicians reluctant to rely on the system during busy emergency department workflows.

This project addresses that problem by focusing on Explainable AI (XAI). Instead of presenting only a prediction, the system will clearly show the clinical factors that contributed most to its recommendation. Providing understandable explanations helps clinicians judge whether the recommendation is reasonable, increasing confidence in the system while supporting informed clinical decision-making.

## Risk 3: Over-Reliance on AI Recommendations
The opposite problem can also occur. As clinicians become familiar with the system, they may begin accepting AI recommendations automatically without applying their own professional judgement. This is known as **automation bias** and can become dangerous if the AI makes an incorrect recommendation.

To minimise this risk, the proposed system is designed to support clinical judgement rather than replace clinician assessment. Nurses remain responsible for every triage decision, and the AI serves as an additional source of information, **not a final authority**. By making the AI's reasoning visible, clinicians are encouraged to critically evaluate each recommendation instead of accepting it without question.

# Summary
These three risks highlight the balance required for safe healthcare AI. The system must be accurate enough to support clinical decisions, transparent enough for clinicians to understand and trust, and carefully integrated into practice so that it supports professional judgement without replacing it. Addressing these risks is essential before any AI-assisted triage system can be safely introduced into clinical practice.
