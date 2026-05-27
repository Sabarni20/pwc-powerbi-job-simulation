# Task 2 — Customer Retention (Churn) Analysis: DAX Measures

## Core Churn KPIs

```dax
-- Total Customers
Total Customers = COUNTROWS(customer_churn)

-- Total Churned
Total Churned = CALCULATE(COUNTROWS(customer_churn), customer_churn[Churned] = "Yes")

-- Churn Rate %
Churn Rate % = DIVIDE([Total Churned], [Total Customers], 0) * 100

-- Retained Customers
Retained Customers = [Total Customers] - [Total Churned]

-- Retention Rate %
Retention Rate % = DIVIDE([Retained Customers], [Total Customers], 0) * 100
```

## Revenue at Risk

```dax
-- Avg Monthly Charge
Avg Monthly Charge = AVERAGE(customer_churn[MonthlyCharges])

-- Monthly Revenue Lost to Churn
Monthly Revenue at Risk =
CALCULATE(
    SUM(customer_churn[MonthlyCharges]),
    customer_churn[Churned] = "Yes"
)

-- Estimated Annual Revenue at Risk
Annual Revenue at Risk = [Monthly Revenue at Risk] * 12

-- Avg Tenure of Churned Customers
Avg Tenure (Churned) =
CALCULATE(AVERAGE(customer_churn[Tenure]), customer_churn[Churned] = "Yes")

-- Avg Tenure of Retained Customers
Avg Tenure (Retained) =
CALCULATE(AVERAGE(customer_churn[Tenure]), customer_churn[Churned] = "No")
```

## Churn by Segment

```dax
-- Churn Rate by Contract Type (use in visual with Contract slicer/axis)
Churn Rate by Contract % =
DIVIDE(
    CALCULATE(COUNTROWS(customer_churn), customer_churn[Churned] = "Yes"),
    COUNTROWS(customer_churn),
    0
) * 100

-- Month-to-Month Churn Rate
MTM Churn Rate % =
CALCULATE(
    [Churn Rate %],
    customer_churn[Contract] = "Month-to-month"
)

-- One Year Contract Churn Rate
OneYear Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[Contract] = "One year")

-- Two Year Contract Churn Rate
TwoYear Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[Contract] = "Two year")

-- Senior Citizen Churn Rate
Senior Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[SeniorCitizen] = 1)

-- Non-Senior Churn Rate
NonSenior Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[SeniorCitizen] = 0)
```

## Tenure Bucketing (Calculated Column)

```dax
-- Add this as a calculated column on customer_churn table
Tenure Band =
SWITCH(
    TRUE(),
    customer_churn[Tenure] <= 6,   "0–6 Months",
    customer_churn[Tenure] <= 12,  "7–12 Months",
    customer_churn[Tenure] <= 24,  "13–24 Months",
    customer_churn[Tenure] <= 48,  "25–48 Months",
    "49+ Months"
)

-- Sort order column
Tenure Band Order =
SWITCH(
    customer_churn[Tenure Band],
    "0–6 Months",   1,
    "7–12 Months",  2,
    "13–24 Months", 3,
    "25–48 Months", 4,
    "49+ Months",   5
)
```

## Internet Service Risk

```dax
-- Fiber Optic Churn Rate
Fiber Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[InternetService] = "Fiber optic")

-- DSL Churn Rate
DSL Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[InternetService] = "DSL")

-- No Internet Churn Rate
NoInternet Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[InternetService] = "No")
```

## Payment Method

```dax
-- Electronic Check Churn Rate (highest-risk payment method)
ECheck Churn Rate % =
CALCULATE([Churn Rate %], customer_churn[PaymentMethod] = "Electronic check")
```

---

## Suggested Visuals Layout

| Visual | Fields |
|---|---|
| KPI Card | Total Customers |
| KPI Card | Churn Rate % |
| KPI Card | Monthly Revenue at Risk |
| KPI Card | Annual Revenue at Risk |
| Stacked Bar | Churn by Contract Type |
| Column Chart | Churn Rate by Tenure Band |
| Donut | Churned vs Retained |
| Bar Chart | Churn by Internet Service |
| Bar Chart | Churn by Payment Method |
| Matrix | Churn Rate by Gender × Senior Citizen |
| Scatter Plot | Monthly Charges vs Tenure (colored by Churn) |
| Slicer | Contract, Gender, Senior Citizen, Internet Service |
