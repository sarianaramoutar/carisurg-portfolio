# Emergency Department Triage Process at Mercer General ED

``` mermaid
flowchart TD

classDef terminal stroke:#2ca02c,stroke-width:2px;
classDef process stroke:#333333,stroke-width:1.5px;
classDef decision stroke:#d6b656,stroke-width:2px;
classDef ai stroke:#9673a6,stroke-width:1.5px,stroke-dasharray:4 4;
classDef mainAI stroke:#ff7f0e,stroke-width:3px;

A([Patient Arrives]):::terminal
B["Registration<br/>(2–3 min)"]:::process
C["Nurse Triage<br/>(3–5 min)"]:::process
D{"ESI Level?"}:::decision

E["Resuscitation Bays<br/>(2 beds | ESI 1)"]:::process
F["Acute & Observation<br/>(~16 beds | ESI 2–3)"]:::process
G["Fast-Track Area<br/>(~20 seats | ESI 4–5)"]:::process

H["Re-Triage Loop<br/>(Waiting Room)"]:::process

I["ED Physician Assessment<br/>(15–30 min)"]:::process
J["Treatment & Review<br/>(30 min–3 hr)"]:::process
K{"Disposition?"}:::decision
L([Patient Leaves]):::terminal

AI1["AI #1: Digital Reg Assistant"]:::ai
AI2["★ MAIN PROJECT ★<br/>AI #2: Explainable Triage"]:::mainAI
AI3["AI #3: Workflow Monitor"]:::ai
AI4["AI #4: Disposition Support"]:::ai

A --> B
B --> C
C --> D

D -->|ESI 1| E
D -->|ESI 2–3| F
D -->|ESI 4–5| G

G --> H
H -->|Patient deteriorates| C

E --> I
F --> I
G -->|Patient called| I

I --> J
J --> K
K --> L

B -.-> AI1
C -.-> AI2
I -.-> AI3
K -.-> AI4
```

## Process Notes
### Registration
Takes 2-3 minutes. AI Opportunity #1 auto-retrieves previous records and streamlines administrative data entry. 

### Nurse Triage
A 3-5 minute evaluation. AI Opportunity #2 (Main Project) uses recorded inputs (vitals, pain score, history, pregnancy tracking) to assist with explainable ESI category predictions. 

### Zone Split Rules
ESI 1 routes immediately to the 2 resuscitation beds. 

ESI 2-3 use the ~16 general acute and observation beds. 

ESI 4-5 report to the ~20 seat waiting area and fast-track zones. 

### ED MD Assessment
Lasts 15-30 minutes per patient. AI Opportunity #3 monitors outstanding test orders and flags delays caused by shared hospital lab/imaging resources. 

### Treatment & Review
Lasts 30 minutes to 3 hours. AI Opportunity #4 flags delays in physical departure, highlighting severe boarding backlog when ward beds are completely full. 
