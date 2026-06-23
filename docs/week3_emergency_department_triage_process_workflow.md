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
