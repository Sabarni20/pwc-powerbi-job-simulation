# 📊 PwC Switzerland — Power BI Job Simulation

> A complete end-to-end Power BI project built as part of the **PwC Switzerland Virtual Case Experience** on Forage. The simulation covers three real-world corporate analytics scenarios: call centre operations, customer churn prediction, and HR diversity & inclusion.

---

## 🗂️ Project Structure

```
pwc-powerbi-simulation/
│
├── datasets/
│   ├── call_center.csv           # 5,000 rows — PhoneNow telecom operations
│   ├── customer_churn.csv        # 7,043 rows — customer profiles & churn status
│   ├── diversity_inclusion.csv   # 1,394 rows — HR employee metrics FY20–FY21
│   └── generate_datasets.py      # Script used to generate the above datasets
│
├── task1-call-center/
│   ├── DAX_Measures.md           # All DAX formulas for Task 1
│   └── Build_Instructions.md     # Step-by-step Power BI setup guide
│
├── task2-churn/
│   ├── DAX_Measures.md           # All DAX formulas for Task 2
│   └── Build_Instructions.md     # Step-by-step Power BI setup guide
│
├── task3-diversity/
│   ├── DAX_Measures.md           # All DAX formulas for Task 3
│   └── Build_Instructions.md     # Step-by-step Power BI setup guide
│
└── docs/
    └── key_insights.md           # Written analytical findings per task
```

---

## 📋 Tasks Overview

### Task 1 — Call Centre Trends 📞
<img width="1020" height="557" alt="01_call_centre_trends_dashboard" src="https://github.com/user-attachments/assets/4cd3dd61-4f03-449e-a04e-c877e0e6bfc9" />

**Business Question:** What are the key operational trends and performance issues within the PhoneNow Call Centre?

**Dataset:** `call_center.csv` — 5,000 call records across January–March 2021

| KPI | Description |
|---|---|
| Total Calls | Count of all inbound calls |
| Answer Rate % | % of calls picked up by an agent |
| Resolution Rate % | % of answered calls that were resolved |
| Avg Satisfaction Rating | Mean customer rating (1–5) for answered calls |
| Avg Speed of Answer | Mean seconds to pick up |
| Calls by Hour | Hourly distribution to identify peak periods |
| Agent Performance Matrix | Per-agent breakdown of all KPIs |

**Key Insights Found:**
- Peak call hours are **10 AM – 12 PM** daily
- Answer rate is ~81%; ~19% of calls go unanswered
- Agent performance varies significantly — top agents resolve 78% vs. bottom at 58%
- **Streaming** and **Technical Support** are the top 2 call topics

---

### Task 2 — Customer Retention (Churn) Analysis 🔄

<img width="1020" height="545" alt="02_customer_churn_dashboard" src="https://github.com/user-attachments/assets/a23f2aaf-427d-415a-ba29-eb0366c0f382" />

<img width="1020" height="550" alt="03_customer_risk_dashboard" src="https://github.com/user-attachments/assets/2168a0f2-90c7-48cf-96b1-ee3f825f6a11" />

**Business Question:** Which customer profiles are at the highest risk of churning, and what proactive steps can be taken?

**Dataset:** `customer_churn.csv` — 7,043 customer records

| KPI | Description |
|---|---|
| Churn Rate % | % of customers who left |
| Monthly Revenue at Risk | Monthly charges from churned customers |
| Annual Revenue at Risk | Projected yearly loss from churn |
| Churn Rate by Contract | Segmented by Month-to-month / 1yr / 2yr |
| Churn Rate by Tenure Band | Early (0–6m) vs. established customers |
| Churn Rate by Internet Type | Fiber optic vs. DSL vs. None |

**Key Insights Found:**
- **Month-to-month contract** customers churn at ~43% vs ~3% for two-year contracts
- **0–6 month tenure** cohort is highest-risk — early intervention window is critical
- **Electronic check** payment method correlates with highest churn
- **Fiber optic** internet customers churn more than DSL customers
- Senior citizens churn at ~10 percentage points higher than non-seniors

---

### Task 3 — Diversity & Inclusion 🏢

<img width="1020" height="510" alt="04_diversity_inclusion_dashboard" src="https://github.com/user-attachments/assets/375ac846-929d-4893-9c47-e88fbcfbe660" />

**Business Question:** What does the HR data reveal regarding gender balance, promotion velocity, and performance ratings across executive levels?

**Dataset:** `diversity_inclusion.csv` — 1,394 employee records across FY20 and FY21

| KPI | Description |
|---|---|
| Female % by Job Level | Gender pipeline from Entry to Executive |
| Female Promotion Rate % | % of women promoted per level |
| Promotion Velocity Gap | Extra years women wait for promotion vs. men |
| Female Turnover Rate % | Attrition rate by gender per level |
| Performance Rating by Gender | Avg performance score comparison |

**Key Insights Found:**
- Women represent **~52% at Entry level** but only **~12% at Executive** — a dramatic pipeline drop
- Women wait **~1.2–1.8 more years** than men for promotions at Director/Executive level
- Female **performance ratings are comparable** to male — the gap is structural, not meritocratic
- Female **turnover spikes at Manager level**, indicating a "broken rung" effect
- FY20 → FY21 shows **minimal improvement** in executive gender representation

---

## 🛠️ How to Reproduce These Dashboards

### Prerequisites
- Microsoft Power BI Desktop (free download from [powerbi.microsoft.com](https://powerbi.microsoft.com))
- Python 3.x (only needed if regenerating datasets)

### Steps

1. **Clone this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/pwc-powerbi-simulation.git
   cd pwc-powerbi-simulation
   ```

2. **Open Power BI Desktop**

3. **For each task**, follow the guide in `taskN-xxx/Build_Instructions.md`:
   - Import the relevant CSV from `datasets/`
   - Create calculated columns as listed
   - Paste in DAX measures from `DAX_Measures.md`
   - Build the visuals following the layout instructions

4. **(Optional) Regenerate datasets**
   ```bash
   cd datasets
   python3 generate_datasets.py
   ```

---

## 📐 DAX Highlights

A few of the more complex DAX patterns used across all three tasks:

```dax
-- Churn Rate by any dimension (works with any slicer)
Churn Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(customer_churn), customer_churn[Churned] = "Yes"),
    COUNTROWS(customer_churn),
    0
) * 100

-- Promotion Velocity Gap (extra years women wait vs. men)
Promotion Velocity Gap =
CALCULATE(AVERAGE(diversity_inclusion[YearsInLevel]),
    diversity_inclusion[Gender] = "Female", diversity_inclusion[Promoted] = "Yes")
-
CALCULATE(AVERAGE(diversity_inclusion[YearsInLevel]),
    diversity_inclusion[Gender] = "Male", diversity_inclusion[Promoted] = "Yes")

-- Month-over-Month call volume change %
MoM Calls Change % =
VAR _cur  = CALCULATE([Total Calls], DATESMTD(call_center[Date]))
VAR _prev = CALCULATE([Total Calls], PREVIOUSMONTH(call_center[Date]))
RETURN DIVIDE(_cur - _prev, _prev, 0) * 100
```

---

## 📬 Context

This project was completed as part of the **PwC Switzerland Power BI Virtual Case Experience** hosted on [Forage](https://www.theforage.com/). The simulation reflects the types of data analytics work done at PwC for real clients across industries.

---

## 📄 License

For educational and portfolio purposes. Datasets are synthetically generated and do not represent real individuals or companies.
