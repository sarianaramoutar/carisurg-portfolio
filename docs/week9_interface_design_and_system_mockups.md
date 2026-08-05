# CARISURG PROJECT INTERFACE DESIGN AND SYSTEM MOCK-UPS

**Author:** Sariana Ramoutar  
**Date:** Aug 04th, 2026  
**Target Setting:** Main Emergency Department Triage Desk, Mercer General Hospital  
**Selected Approach:** Screen-Based Human-Computer Interaction (HCI)  

---

## I. Overview of the Dashboards

This document presents the visual designs for the CariSurg AI triage system. The system includes two separate screens designed for different clinical roles at Mercer General Hospital.

### Model 1: Triage Nurse Dashboard (Nurse View)
Designed for triage nurses managing busy shifts. The screen focuses on one patient at a time to keep decision-making fast, accurate, and safe.

<img width="1536" height="1024" alt="ED Triage Dashboard Mock-Up Draft 3 - simple vers" src="https://github.com/user-attachments/assets/80384038-97df-4918-b5bd-e77d38e77a8e" />

**Version 1.** Shows static vital signs, the AI triage recommendation, the top reasons for the decision, and a handwritten notes area.


<img width="1536" height="1024" alt="ED Triage Dashboard Mock-Up Draft 4 - lil more complex vers" src="https://github.com/user-attachments/assets/8b2216a9-3db2-4b2d-a779-b9e25ac60118" />

**Version 2.** Adds visual trend lines next to each vital sign (for example: *Heart Rate 92 bpm ↓ previously 108 bpm*).

> [!NOTE]
> **Design Trade-off:** Version 2 gives better insight into whether a patient is improving or getting worse over time. However, to keep the screen simple and avoid visual clutter during peak hours, nurses can toggle between the simple view (Version 1) and the detailed trend view (Version 2).

### Model 2: Hospital Admin Dashboard
Designed for charge nurses and hospital managers. It gives a real-time overview of the entire department without cluttering the screen with individual private health records.

<img width="1536" height="1024" alt="ED Admin Dashboard Mock-Up Draft 1" src="https://github.com/user-attachments/assets/095093f9-5eaf-4550-b019-f53525722e70" />

---

## II. Key & System Features

| Feature Name | Primary Screen | Purpose & Clinical Value |
| :--- | :--- | :--- |
| **Explainable AI Box** | Triage Nurse Dashboard | Displays the top three clinical drivers behind the prediction (e.g., *"Elevated BP + Severe Chest Pain"*) to build trust and explain *why* the AI chose that ESI level. |
| **Live Vital Trends** | Triage Nurse Dashboard | Shows directional arrows and mini-sparkline graphs (e.g., *Heart Rate 92 bpm ↓ prev 108 bpm*) to help staff spot patient deterioration or improvement early. |
| **1-Tap Override Reason Logging** | Triage Nurse Dashboard | Allows nurses to change the AI recommendation with a single tap while logging a required reason (e.g., *"Patient deteriorating"*), preserving clinical authority and building an audit log. |
| **Stylus-Enabled Notes Canvas** | Triage Nurse Dashboard | Lets nurses quickly write digital notes by hand using a stylus, drastically reducing keyboard typing during busy, fast-paced shifts. |
| **Missing Clinical Information Alert** | Triage Nurse Dashboard | Warns staff if important patient data or vital signs are missing or outdated before a decision is finalised, preventing premature triage. |
| **Next Patient Queue & On-Call Escalation** | Triage Nurse Dashboard | Focuses on the next few patients awaiting assessment to prevent visual clutter, while enabling 1-tap patient summary sharing to on-call doctors. |
| **Mass Casualty Incident (MCI) Alert Panel** | Admin Operations Dashboard | Displays real-time feeds of major incoming emergency incidents, expected patient counts by acuity, and estimated arrival times so departments can activate emergency plans early. |
| **Inbound Ambulance Tracker** | Admin Operations Dashboard | Tracks en-route ambulances and pre-hospital assessments, allowing trauma teams and resuscitation bays to prepare before the patient arrives. |
| **Department Throughput & Patient Flow** | Admin Operations Dashboard | Tracks patients across every stage (Waiting → Triage → Physician → Treatment → Admission) to immediately highlight bottlenecks and delay points. |
| **Hospital Bed & Capacity Gauge** | Admin Operations Dashboard | Provides live tracking of overall ED occupancy (e.g., 88% capacity), available observation beds, isolation rooms, and resus bays for rapid placement decisions. |

> [!NOTE]
> **Emergency Severity Index (ESI):** A standard 5-level scale used to sort emergency patients. ESI Level 1 represents critical, immediate life-threatening conditions, while ESI Level 5 represents non-urgent conditions.

---

## III. How the System Works Step-by-Step

1. **Patient Arrival:** The nurse scans the patient's QR wristband using the tablet to open their record instantly.
2. **Data Entry:** Vitals stream automatically from connected monitors (or are typed in manually). The nurse types or handwrites the patient's main complaint.
3. **AI Recommendation:** The system analyses the data in less than a second and displays a colour-coded ESI level along with a clear explanation.
4. **Nurse Decision:** The nurse reviews the suggestion, compares it with their own clinical judgement, and either accepts or overrides it.
5. **Department Update:** Once saved, the main waiting queue updates automatically, and high-priority cases trigger an instant notification to on-call doctors.

---

## IV. System Connections & Security

* **Connected Medical Devices:** Vital signs flow directly into the tablet from compatible blood pressure cuffs, oxygen monitors, and thermometers using secure Bluetooth connections.
* **Offline Backup Support:** If the hospital network or power grid drops, the tablet saves all data locally and syncs automatically once connection returns.
* **Data Security & Privacy:** All records are locked behind staff logins and protected using strict encryption standards during transfer and storage.

> [!NOTE]
> **Technical Term Explanations:**
> * **EHR (Electronic Health Record):** The central computer database used by hospitals to store patient medical histories.
> * **Data Encryption:** A digital lock that scrambles information so unauthorised people cannot read patient records if a device is lost or intercepted.
