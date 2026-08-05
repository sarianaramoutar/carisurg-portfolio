# CARISURG PROJECT SYSTEM REQUIREMENTS

**Project Title:** An Explainable AI Assistant to Support Emergency Triage in the Caribbean  
**Author:** Sariana Ramoutar  
**Date:** Aug 04th, 2026
**Target Setting:** Main Emergency Department Triage Desk, Mercer General Hospital (Setting A – Human-Computer Interaction)  
**Selected Model:** Optimised Random Forest Classifier (ESI Levels 1–5)  

---

## I. Verdict

The Human-Computer Interaction (HCI) implementation was selected over a physical robot (HRI) because it integrates directly into existing Emergency Department (ED) desk workflows without physically obstructing the busy triage area. It keeps the experienced triage nurse firmly in control as the final decision-maker, using AI purely as a secondary supportive tool.

---

## II. Implementation Scope

The proposed system is designed for deployment at the main Emergency Department triage desks, where nurses perform initial assessments under high-volume, time-critical conditions (managing up to 40 complex patient intakes per shift). Compared with the Human-Robot Interaction (HRI) alternative, the HCI implementation was selected because it:

* **Maintains full human oversight** throughout the triage process, preventing over-reliance on automated systems.
* **Integrates directly with existing Electronic Health Record (EHR) workflows** without requiring physical floor space or complex mechanical maintenance.
* **Requires minimal changes** to current clinical practice, reducing staff training overhead and adoption friction.
* **Provides explainable recommendations instantly** during the standard triage assessment process using the fast-processing Optimised Random Forest Model (inference time < 0.01 seconds per patient).

---

## III. Functional Requirements (FR)

### FR-1: Patient Data Collection
* **FR-1.1:** The system shall retrieve available patient demographic information and clinical history from the EHR using the patient’s barcode or QR code.
* **FR-1.2:** The system shall allow nurses to manually enter the presenting complaint, pain score, and additional clinical observations via touch or stylus input.
* **FR-1.3:** The system shall receive vital signs automatically from compatible networked medical devices (such as pulse oximeters or blood pressure cuffs) where available, with a fast manual input form provided as an immediate fallback.

### FR-2: Explainable Acuity Recommendation
* **FR-2.1:** The system shall execute the trained Random Forest model to predict the patient's Emergency Severity Index level (ESI Levels 1–5: Level 1 for immediate life-threatening cases to Level 5 for non-urgent cases).
* **FR-2.2:** The system shall display the predicted ESI level together with a confidence score reflecting the model’s certainty.
* **FR-2.3:** The system shall display the top three clinical factors (e.g., *"High Heart Rate + Severe Chest Pain"*) that contributed most strongly to the prediction to improve transparency and clinician trust.
* **FR-2.4:** When prediction confidence is low (below a set safety threshold, such as 70%), the system shall display a prominent visual notice indicating that the case is complex and requires extra clinical review.

> [!NOTE]
> **Emergency Severity Index (ESI):** A 5-level emergency triage algorithm. ESI 1 represents critical, immediate life-threatening cases, while ESI 5 represents minor, non-urgent conditions.

### FR-3: Clinical Workflow Support
* **FR-3.1:** The system shall require the triage nurse to actively accept or override every AI recommendation via a single tap before a final ESI level is recorded.
* **FR-3.2:** The system shall allow nurses to record handwritten or typed clinical notes using a stylus-enabled tablet.
* **FR-3.3:** If an AI recommendation is overridden, the system shall prompt a quick 1-tap menu (e.g., *"Additional clinical findings / Patient improving / Patient deteriorating / Incorrect or Incomplete information"*) to log the reason for the override in the patient's audit record.
* **FR-3.4:** The system shall automatically update the ED patient queue following completion of triage.
* **FR-3.5:** The system shall allow clinicians to notify the appropriate physician directly from the dashboard when urgent high-acuity (ESI 1 or 2) review is required.

### FR-4: Audit & Continuous Feedback Logging
* **FR-4.1:** The system shall securely record patient inputs, AI predictions, confidence scores, clinician decisions, and override reasons to support ongoing clinical quality reviews and future model retraining.
* **FR-4.2:** All completed triage records shall be synchronised with the Electronic Health Record.

---

## IV. Non-Functional Requirements (NFR)

### NFR-1: Performance
* **NFR-1.1:** The system shall provide AI recommendations in real time (under 1 second total pipeline response time) without delaying the normal ED triage workflow.
* **NFR-1.2:** The interface shall remain responsive during periods of high patient volume and rapid consecutive data entry.

### NFR-2: Usability & Ergonomics
* **NFR-2.1:** The interface shall present information using a clear visual hierarchy with high-contrast, colour-coded badges (Red = Critical, Yellow = Urgent, Green = Non-Urgent) suitable for quick reading from a distance.
* **NFR-2.2:** High-priority recommendations shall be communicated using clear visual indicators and high-contrast screen banners rather than loud or repetitive audible alarms, preventing noise pollution and alarm fatigue in the crowded ED.
* **NFR-2.3:** The interface shall support touch and stylus input with large interactive targets (at least 48 × 48 pixels) to accommodate gloved hands, stylus use, and physical fatigue during long 12-hour shifts.
* **NFR-2.4:** The interface shall use accessible colour combinations, readable fonts, icons, and consistent layouts to support use under stressful clinical conditions.

> [!NOTE]
> **Alarm Fatigue:** Sensory overload caused by excessive or repetitive audible alerts in clinical environments. Suppressing audio chimes in favor of high-contrast visual banners prevents nurses from becoming desensitized to urgent patient warnings.

### NFR-3: Reliability & Infrastructure Resilience
* **NFR-3.1:** The system hardware shall operate with battery backup support (Uninterruptible Power Supply / local tablet battery) to ensure continued operation during temporary electrical grid drops or generator transitions.
* **NFR-3.2:** The system shall continue operating during temporary network outages by allowing local data capture and offline prediction caching.
* **NFR-3.3:** Patient records shall automatically synchronise with the Electronic Health Record once connectivity is restored.
* **NFR-3.4:** Manual data entry shall remain available whenever connected medical devices are unavailable.

---

## V. Integration Requirements (IR)

### IR-1: Hospital Systems & Standard Protocols
* **IR-1.1:** The system shall integrate with the Electronic Health Record for retrieval and storage of patient information using HL7 and FHIR protocols.
* **IR-1.2:** The system shall integrate with the hospital patient queue management system.
* **IR-1.3:** The system shall integrate with hospital staff scheduling systems to display available clinicians for escalation.
* **IR-1.4:** The administrative dashboard shall receive Emergency Medical Services (EMS) notifications, including incoming ambulance information and Mass Casualty Incident (MCI) alerts where available.

### IR-2: Clinical Devices
* **IR-2.1:** The system shall support barcode or QR-code patient identification.
* **IR-2.2:** The system shall support compatible digital medical devices via secure Bluetooth or USB connectivity for automatic vital sign collection.
* **IR-2.3:** The system shall support stylus-enabled tablets for clinical documentation.

> [!NOTE]
> **HL7 & FHIR:** Industry-standard protocol languages (Health Level 7 & Fast Healthcare Interoperability Resources) that allow disparate digital healthcare systems to exchange patient records securely without formatting errors.

---

## VI. Security and Safety Requirements (SR)

### SR-1: Human Oversight & Clinical Accountability
* **SR-1.1:** The AI shall function solely as a clinical decision-support tool and shall never automatically assign or submit a patient's final ESI level without active nurse confirmation.
* **SR-1.2:** Final responsibility for every triage decision shall remain explicitly with the attending nurse, supported by clear on-screen disclaimers stating that AI outputs do not replace clinical judgement.

### SR-2: Data Security & Access Controls
* **SR-2.1:** All patient information transmitted over hospital networks shall be encrypted using TLS standards.
* **SR-2.2:** All patient information stored locally on tablets or servers shall be encrypted using AES-256 standards.
* **SR-2.3:** Access to the system shall be restricted to authorised clinical staff using Single Sign-On (SSO) and Role-Based Access Control (RBAC).
* **SR-2.4:** All user activity, AI predictions, and clinician overrides shall be recorded through secure audit logging.

> [!NOTE]
> **Security Protocols Defined:**
> * **TLS (Transport Layer Security):** Encrypts data while moving across local networks or Wi-Fi to prevent interception (**data in transit**).
> * **AES-256 (Advanced Encryption Standard):** An industry-standard cryptographic lock securing data stored on physical drives or tablet memory (**data at rest**).
> * **SSO & RBAC:** Single Sign-On allows staff to log in securely with standard hospital credentials. Role-Based Access Control restricts interface screens so staff only access features necessary for their specific role.

### SR-3: Safe Failure & Graceful Degradation
* **SR-3.1:** If required patient information is incomplete, the system shall prevent an AI recommendation until the missing data have been addressed, clearly highlighting which inputs are missing.
* **SR-3.2:** If connected devices or network services become unavailable, clinicians shall be able to continue using the standard manual triage workflow without interruption or data loss.
* **SR-3.3:** The system shall clearly distinguish AI recommendations from confirmed clinical decisions at all times using visual labels.
