# Task 2 — Customer Retention Dashboard: Build Instructions

## 1. Data Import

1. **Get Data → Text/CSV** → Load `datasets/customer_churn.csv`
2. In Power Query Editor:
   - Set `SeniorCitizen` → Whole Number
   - Set `Tenure`, `MonthlyCharges`, `TotalCharges` → correct numeric types
   - `TotalCharges` may have blank strings → replace with `0` via **Replace Values**
   - Rename query: `customer_churn`
3. **Close & Apply**

## 2. Calculated Columns (Data View)

```dax
Tenure Band = (see DAX_Measures.md)
Tenure Band Order = (see DAX_Measures.md)
```
Set **Sort by Column**: Tenure Band → Tenure Band Order

## 3. Measures

Copy all measures from `DAX_Measures.md`.

## 4. Page Layout — "Churn Overview" Page

### Row 1 – KPI Cards
| Total Customers | Total Churned | Churn Rate % | Monthly Revenue at Risk |

### Row 2, Col 1 – Donut: Churned vs Retained
- Values: Total Customers, Legend: Churned

### Row 2, Col 2 – Stacked Column: Churn Rate by Contract Type
- X: Contract, Y: Churn Rate by Contract %, color split by Churned
- Add data labels showing churn %

### Row 3 – Column Chart: Churn Rate by Tenure Band
- X-Axis: Tenure Band (sorted by Tenure Band Order)
- Y-Axis: Churn Rate %
- Add trend line (polynomial)
- Expected insight: steep churn in 0–6 month cohort

### Row 4 – Clustered Bar: Churn by Internet Service + Payment Method (side by side)

## 5. Page Layout — "Customer Profiles at Risk" Page

### Scatter Plot: Monthly Charges vs. Tenure
- X: Tenure
- Y: MonthlyCharges
- Size: TotalCharges
- Color: Churned (Yes = red, No = teal)
- Add zoom slider

### Matrix: Demographics Breakdown
- Rows: Contract, Columns: Gender + Senior Citizen
- Values: Churn Rate %, Total Customers
- Conditional formatting (heat map) on Churn Rate %

### Top 5 Risk Factors (Text/Smart Narrative)
Use Power BI's Smart Narrative visual to auto-generate key insights, or add a text box summarizing:
> "Month-to-month customers with Fiber optic internet paying via Electronic check and under 6 months tenure represent the highest churn risk segment."

## 6. Slicers

- Contract Type
- Internet Service
- Gender
- Senior Citizen (Yes / No toggle)
- Tenure Band

## 7. Formatting Tips

- Color theme: **Reds + Teal** (churn = `#E8384F`, retained = `#00B5AD`)
- Page title: *"PhoneNow — Customer Retention & Churn Risk Dashboard"*
- Canvas: **1280 × 720**

## 8. Key Analytical Insights to Highlight

1. **Month-to-month contracts churn ~3× more** than two-year contracts
2. **0–6 month tenure** is highest-risk window → intervention needed early
3. **Fiber optic + electronic check** combination = highest churn combo
4. **Senior citizens** churn at ~10pp more than non-seniors
5. **Higher monthly charges** correlate positively with churn among short-tenure customers
