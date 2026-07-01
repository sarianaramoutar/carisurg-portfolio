# A Real Case Study of Where AI Could Have Caused Harm
## Root-Cause Analysis
Wong, A., Otles, E., Donnelly, J. P., Krumm, A., McCullough, J., DeTroyer-Cooley, O., Pestrue, J., Phillips, M., Konye, J., Penoza, C., Ghous, M., & Singh, K. (2021). External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. *JAMA Internal Medicine, 181(8), 1065–1070*. https://doi.org/10.1001/jamainternmed.2021.2626

### 1. What happened?

The Epic Sepsis Model (ESM) is an AI software tool designed to automatically flag early signs of sepsis (a life-threatening, full-body medical emergency triggered by a severe infection). It was deployed across hundreds of US hospitals. Because catching sepsis early is a literal matter of life and death, hospitals trusted the software to protect patients. 

However, when independent researchers tracked the AI’s performance across 38,455 real hospital stays, they discovered a major failure. The AI completely missed 67% of patients who actually developed sepsis. At the same time, the software constantly cried wolf, sounding automated alarms for 18% of all hospitalised patients. This meant that nearly 9 out of 10 alerts were false alarms, creating a massive burden of alert fatigue – a dangerous state where nurses and doctors become so mentally exhausted by non-stop buzzing that they begin tuning out the alerts entirely. 

### 2. Why did it happen?

The root cause of this failure was the system’s “black box” design. In healthcare technology, a black box refers to an AI system that gives a final conclusion, like a risk score or diagnosis, but completely hides the internal mathematical logic and data it used to get there. 

Because the software company kept the AI’s internal formulae a secret, hospitals turned it on blindly. It turned out the AI was originally trained on neat, historical insurance billing records rather than live, messy bedside charts. When deployed in hospitals, the model suffered from dataset shift – a glitch where the live environment an AI is dropped into looks completely different from the historical data it was trained on. Because it was an unreadable black box, no one could see this data mismatch, so the AI quietly failed in the real environment. 

### 3. What did the system fail to anticipate?

The developers of the AI failed to anticipate basic human psychology and clinical workflows. In a computer lab, engineers often assume that generating more alerts creates a safer safety net for patients. But in a chaotic hospital ward, the exact opposite is true. 

The software developers failed to realise that flooding clinical staff with thousands of inaccurate alarms forces those humans to develop a psychological blind spot. By treating the hospital as an isolated data spreadsheet, the system failed to anticipate that an unreadable, inaccurate AI alert system actually degrades a doctor’s or nurse’s ability to focus on actually deteriorating patients. 

### 4. What would have caught it?

This systemic failure could have been identified earlier and its impact reduced by combining an Explainable AI (XAI) interface with rigorous external validation before deployment.  

If the software had been designed to be transparent, it wouldn’t just give an arbitrary danger score. It would display its reasoning inline. For example, the interface would have to display something like: “Sepsis Risk High – based 80% on patient age, 20% on recent heart rate.”


If clinicians had been given this visibility of the clinical factors contributing to a recommendation, they would have quickly noticed that the AI was making calculations based on missing, delayed or irrelevant data points. Explainability helps clinicians know whether to accept the AI’s judgement and recommendations or override it, without compromising patient safety. 
