# Feasibility Memo (First Draft - Outline)

**Project Title:** 	An Explainable AI Assistant to Support Emergency Department Triage in the Caribbean

**Audience:** 	Emergency Department Clinical Board

**Author:**	Sariana Ramoutar

## I.  Verdict
The dataset is suitable for developing an AI-assisted triage model, provided known limitations are addressed and information that would only become available after triage is excluded. 

## II.  Dataset Summary
Dataset Overview: The analysis evaluated a dataset containing 55,121 adult emergency department encounters (restricted entirely to individuals 18 or older). 

Emergency Severity Index (ESI): Patients were classified into 5 ESI levels, where Level 1 represents the most urgent cases requiring immediate care and Level 5 represents the least urgent. The clinical breakdown shows: 
- ESI 1 (Resuscitation): 77 encounters (0.1% of cases).
- ESI 2 (Emergent): 17,924 encounters (32.5% of cases).
- ESI 3 (Urgent): 27,010 encounters (49.0% of cases).
- ESI 4 (Less Urgent): 8,896 encounters (16.1% of cases).
- ESI 5 (Non-Urgent): 1,214 encounters (2.2% of cases).

Most patients fell into ESI Levels 2 and 3 (making up over 81% of all traffic), meaning the dataset mainly represents patients with moderate urgency. Very few patients were classified as ESI Level 1.  

Each patient record contains approximately 225 variables, including demographic information, vital signs and around 200 chief complaints. All body temperatures are recorded in degrees Fahrenheit (°F). 

## III.  Top 3 Concerns (with Clinical Mitigations)
### 1. Information Available after Triage

**Concern:** Some variables, such as final patient disposition, are only known after the triage decision has been made. Including them would allow the model to learn from information it would never have during real patient assessment. 

**Mitigation:** These variables were excluded from the model inputs.

### 2. Missing Data

**Concern:** Some patient records contained missing vital signs or missing ESI labels. 

**Mitigation:** Records without an ESI label were removed because they cannot be used for training. Missing vital signs were replaced with the median value so the dataset remained complete while avoiding unrealistic values. 

### 3. Geographic Population and Resource Mismatch

**Concern:** This dataset comes from a large academic hospital in the United States. Patient populations, available resources and disease patterns may differ from those seen in Caribbean hospitals. 

**Mitigation:** The model should therefore be treated as an initial prototype until it has been evaluated using local Caribbean data. 

## IV.  Top 3 Reasons to Proceed
### 1. Reliable Triage Labels

Nearly every remaining patient record has a valid ESI level assigned by healthcare professionals, providing a reliable outcome for model development.

### 2. Vital Signs Follow Expected Clinical Patterns

The vital signs generally change in the expected direction across ESI levels. Patients with more urgent conditions tend to have faster heart rates, higher respiratory rates and lower oxygen saturation.

### 3. Clear and Documented Data Preparation

Every cleaning decision was recorded, making the process easy to repeat and review.

## V.  Caveats
### 1. Temperature Recorded in Fahrenheit

Temperatures are recorded in degrees Fahrenheit rather than Celsius. Any future implementation in Caribbean hospitals would need appropriate conversion and validation. 

### 2. Many Chief Complaints are Uncommon

Most chief complaint variables occur very rarely, meaning some provide little information on their own and may need to be grouped during future modelling.

### 3. Limited Applicability to Caribbean Hospitals

Because the dataset represents patients treated in a US hospital, its findings may not fully reflect Caribbean populations, healthcare systems or disease patterns. Local validation would be essential before any clinical use. 
