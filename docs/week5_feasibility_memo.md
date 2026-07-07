# CARISURG PROJECT FEASIBILITY MEMORANDUM

**To:** Emergency Department Clinical Board  
**From:** Sariana Ramoutar  
**Date:** Jul 06th, 2026  
**Subject:** Feasibility Analysis and Recommendations for Caribbean AI-Assisted Triage Deployment  

---

## I. Verdict

> [!IMPORTANT]
> The dataset is suitable for developing an initial prototype of an AI-assisted triage system, provided that information which would only become available after triage is excluded and all recommendations remain subject to clinical review.

---

## II. Dataset Summary

The evaluation was conducted on a dataset containing 55,121 adult emergency department encounters from patients aged 18 years and older. 

The primary target variable is the Emergency Severity Index (ESI), a 5-level clinical triage scale where Level 1 represents immediate, life-threatening conditions and Level 5 represents non-urgent complaints. 

### Categorical Distribution Across the Dataset

| ESI Level | Clinical Classification | Encounters Count | Percentage of Cases |
| :--- | :--- | :--- | :--- |
| **ESI 1** | Resuscitation | 77 encounters | 0.1% of cases |
| **ESI 2** | Emergent | 17,924 encounters | 32.5% of cases |
| **ESI 3** | Urgent | 27,010 encounters | 49.0% of cases |
| **ESI 4** | Less Urgent | 8,896 encounters | 16.1% of cases |
| **ESI 5** | Non-Urgent | 1,214 encounters | 2.2% of cases |

* **Traffic Concentration:** Over 81% of the total patient traffic is concentrated within ESI Levels 2 and 3, meaning the dataset mainly represents patients with moderate-to-high clinical urgency.
* **Feature Volume:** Each patient record contains approximately 225 variables, including demographic information, vital signs and around 200 chief complaint indicators.
* **Metrics Note:** All body temperatures in the dataset are uniformly recorded in degrees Fahrenheit (°F).

---

## III. Top Three Concerns & Mitigations

### 1. Information Available after Triage
* **Concern:** Some variables in the original dataset, such as final patient disposition (e.g., discharge, ward admission or ICU transfer), are only known after the triage decision has been made. If these variables were included during training, the model would learn from information that would not be available at the front desk.
* **Mitigation:** All post-triage outcome variables were excluded. The model is restricted solely to information available at the time of patient arrival.

### 2. Severe Class Imbalance (ESI Level 1 Scarcity)
* **Concern:** ESI Level 1 patients account for only 0.1% of the entire dataset (77 cases). Because the data is heavily weighted toward less critical patients, the model might fail to recognise an active resuscitation case due to lack of exposure.
* **Mitigation:** Training will use techniques such as class weighting or balanced sampling, and all high-risk predictions will remain subject to review by a triage nurse.

### 3. Geographic Population and Resource Mismatch
* **Concern:** The dataset comes from a US emergency department, while the intended application is in Caribbean hospitals. Differences in patient populations, disease patterns and available resources may affect model performance.
* **Mitigation:** The system should be treated as an initial prototype. Before any clinical use, it should be validated and refined using Caribbean emergency department data and local clinician feedback.

---

## IV. Top 3 Reasons to Proceed

### 1. Reliable Triage Labels
Every record within the 55,121 cases features a fully completed ESI designation assigned by on-duty clinical healthcare professionals. This provides a highly consistent, clean and verified target standard for training a baseline triage model.

### 2. Vital Signs Follow Expected Clinical Patterns
The data follows real human biology perfectly. Patients designated with high-acuity ESI scores demonstrate clear visible escalations in resting heart rates and respiratory rates, coupled with corresponding declines in baseline blood oxygen saturation levels.

### 3. Large and Clinically Diverse Dataset
The dataset contains more than 55,000 emergency department encounters spanning all five ESI categories. This provides a broad range of patient presentations and offers enough data to evaluate whether a baseline AI-assisted triage approach is feasible.

---

## V. Operational Caveats

### 1. Adult-Only Dataset
The dataset contains only patients aged 18 years and older. Any future deployment would need separate validation before being used for paediatric triage.

### 2. Many Chief Complaints are Uncommon
Most of the approximately 200 chief complaint indicators occur very infrequently. Some complaints may therefore provide limited information on their own and may need to be grouped into broader clinical categories during future model development.

### 3. Temperature Recorded in Fahrenheit
All temperatures in the dataset are recorded in degrees Fahrenheit rather than Celsius. Any future Caribbean implementation would need appropriate conversion and validation within local clinical workflows.

## VI. Top 10 Clinical Feature Shortlist

The following features were selected using a combination of clinical judgement and their observed relationship with Emergency Severity Index (ESI) during the exploratory analysis.

| Feature Name | Type | Justification |
| :--- | :--- | :--- |
| `triage_vital_o2` | Vital Sign | Oxygen saturation is strongly associated with patient acuity, with lower values indicating more urgent respiratory compromise. |
| `triage_vital_rr` | Vital Sign | Respiratory rate increases in critically ill patients and is an important indicator of respiratory distress. |
| `triage_vital_hr` | Vital Sign | Elevated heart rate may indicate shock, infection or physiological stress, making it useful for triage decisions. |
| `triage_vital_sbp` | Vital Sign | Low systolic blood pressure can indicate poor circulation or shock and is commonly used in emergency assessment. |
| `age` | Demographic | Older patients are generally at greater risk of serious illness and often require higher clinical priority. |
| `cc_shortnessofbreath` | Chief Complaint | Shortness of breath is a high-risk presenting complaint that is frequently associated with urgent care. |
| `cc_chestpain` | Chief Complaint | Chest pain may indicate acute cardiac disease and usually requires prompt assessment. |
| `triage_vital_temp` | Vital Sign | Abnormal body temperature can indicate infection or other systemic illness that affects urgency. |
| `triage_vital_dbp` | Vital Sign | Diastolic blood pressure provides additional information on cardiovascular status when interpreted alongside systolic pressure. |
| `triage_vital_o2_device` | Clinical Indicator | Requiring supplemental oxygen at presentation suggests respiratory compromise and may indicate increased acuity. |

---

## APPENDIX: SUPPORTING FIGURES

### Figure 0. Missingness in the Dataset
*Missingness Density Map of Structured Columns in Dataset*

<img width="975" height="364" alt="image" src="https://github.com/user-attachments/assets/63773800-a7e4-4f96-b1fd-7fef04d4dc9f" />

> [!NOTE]
> **Observations:**
> The diagnostic summary and the missingness density map both indicate that there are no missing values in the structured columns of the dataset after the cleaning process.

---

### Figure 1. ESI Distribution and Age Distribution
*Distribution of ESI Levels & Distribution of Patient Age*

<img width="975" height="349" alt="image" src="https://github.com/user-attachments/assets/7539c78b-fffe-4aed-9af4-0be1602dd7c1" />

> [!NOTE]
> **Observations:**
> * The dataset is dominated by ESI Levels 2 and 3, while Level 1 cases are very uncommon.
> * Patient ages cover a broad adult range, indicating that the dataset represents a diverse adult emergency department population.
> * The imbalance in ESI levels highlights the need for additional care when developing the model so that rare, high-acuity cases are not overlooked.

---

### Figure 2. Top Chief Complaints
*Top 15 Most Common Chief Complaints*

<img width="975" height="581" alt="image" src="https://github.com/user-attachments/assets/8c5b5ae4-3893-40a5-96f1-2a995427ed5c" />

> [!NOTE]
> **Observations:**
> * A small number of chief complaints account for a large proportion of emergency department presentations, while many complaint categories occur only rarely.
> * Common presentations such as chest pain and shortness of breath appear frequently and are clinically important indicators of potentially serious illness.
> * The large number of infrequent complaint categories suggests that some may need to be grouped into broader clinical categories during future model development.

---

### Figures 3.1 and 3.2. Vital Signs by ESI Level
*Distribution of Key Vital Signs by ESI Level with Normal Ranges / Clinical Validation: Vital Sign Trends Across Triage Urgency Levels*

<img width="975" height="544" alt="image" src="https://github.com/user-attachments/assets/4d74c661-faac-43fa-825a-8574f9b06219" />

<img width="975" height="289" alt="image" src="https://github.com/user-attachments/assets/bbd59662-563d-47b2-8914-32c9e0f61ba5" />

> [!NOTE]
> **Observations:**
> * Heart rate and respiratory rate generally increase as patient acuity increases (lower ESI levels).
> * Oxygen saturation tends to decrease in the more urgent ESI groups, consistent with respiratory compromise.
> * Blood pressure, body temperature and blood glucose show greater overlap between ESI categories and are less effective as individual indicators of urgency.
> * Overall, no single vital sign completely separates the ESI groups, supporting the need to combine multiple clinical features when developing an AI-assisted triage model.

---

### Figure 4. Correlation Heatmap
*Correlation Matrix of Vital Signs and ESI*

<img width="975" height="818" alt="image" src="https://github.com/user-attachments/assets/699d2862-d543-47c9-b871-718319379be1" />

> [!NOTE]
> **Observations:**
> * Systolic and diastolic blood pressure show the strongest positive correlation, which is expected because they measure related aspects of cardiovascular function.
> * Heart rate and respiratory rate display weaker positive relationships, while oxygen saturation shows a negative relationship with measures associated with higher acuity.
> * Individual vital signs have only weak to moderate correlations with the ESI score, indicating that no single measurement is sufficient to predict triage level accurately.
> * These findings support the use of multiple clinical variables together when developing an AI-assisted decision-support tool.

---

### Figures 5.1 and 5.2. Race and Ethnicity Distribution
*Distribution of Race, Distribution of Ethnicity, and ESI Distribution within Each Race Category*

<img width="975" height="295" alt="image" src="https://github.com/user-attachments/assets/e5dca8bf-d65a-44b2-82bd-5918694cd21a" />

<img width="975" height="390" alt="image" src="https://github.com/user-attachments/assets/3638d665-4e3c-4356-81c9-45852a7d0cd6" />

> [!NOTE]
> **Observations:**
> * The patient population includes multiple race and ethnicity groups, reflecting the demographics of the original US emergency department.
> * These demographic variables are important when assessing fairness because AI models may perform differently across population groups if some groups are underrepresented.
> * Since this dataset does not represent Caribbean populations, local validation using regional patient data will be necessary before any clinical deployment.
