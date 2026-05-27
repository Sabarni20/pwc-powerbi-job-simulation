# Task 2 – Customer Retention (Churn) | DAX Measures

## Core Churn KPIs

### Total Customers
```dax
Total Customers = COUNTROWS('CustomerChurn')
```

### Total Churned Customers
```dax
Churned Customers = 
CALCULATE(
    COUNTROWS('CustomerChurn'),
    'CustomerChurn'[Churn] = "Yes"
)
```

### Churn Rate %
```dax
Churn Rate % = 
DIVIDE(
    [Churned Customers],
    [Total Customers],
    0
) * 100
```

### Retained Customers
```dax
Retained Customers = [Total Customers] - [Churned Customers]
```

### Retention Rate %
```dax
Retention Rate % = 100 - [Churn Rate %]
```

---

## Revenue Impact Measures

### Average Monthly Charges
```dax
Avg Monthly Charges = 
AVERAGE('CustomerChurn'[MonthlyCharges])
```

### Revenue at Risk (Monthly)
```dax
Revenue at Risk = 
CALCULATE(
    SUMX('CustomerChurn', 'CustomerChurn'[MonthlyCharges]),
    'CustomerChurn'[Churn] = "Yes"
)
```

### Avg Monthly Charge – Churned vs Retained
```dax
Avg Charge Churned = 
CALCULATE(
    AVERAGE('CustomerChurn'[MonthlyCharges]),
    'CustomerChurn'[Churn] = "Yes"
)

Avg Charge Retained = 
CALCULATE(
    AVERAGE('CustomerChurn'[MonthlyCharges]),
    'CustomerChurn'[Churn] = "No"
)
```

---

## Contract & Tenure Analysis

### Churn Rate by Contract Type
```dax
Churn Rate by Contract = 
DIVIDE(
    CALCULATE(COUNTROWS('CustomerChurn'), 'CustomerChurn'[Churn] = "Yes"),
    COUNTROWS('CustomerChurn'),
    0
) * 100
-- Use this in a visual filtered/grouped by Contract field
```

### Avg Tenure – Churned
```dax
Avg Tenure Churned = 
CALCULATE(
    AVERAGE('CustomerChurn'[Tenure]),
    'CustomerChurn'[Churn] = "Yes"
)
```

### Avg Tenure – Retained
```dax
Avg Tenure Retained = 
CALCULATE(
    AVERAGE('CustomerChurn'[Tenure]),
    'CustomerChurn'[Churn] = "No"
)
```

### Tenure Band (Calculated Column)
```dax
Tenure Band = 
SWITCH(
    TRUE(),
    'CustomerChurn'[Tenure] <= 12, "0–12 Months",
    'CustomerChurn'[Tenure] <= 24, "13–24 Months",
    'CustomerChurn'[Tenure] <= 48, "25–48 Months",
    "49+ Months"
)
```

---

## Demographic Segmentation

### Senior Citizen Churn Rate
```dax
Senior Churn Rate % = 
CALCULATE(
    [Churn Rate %],
    'CustomerChurn'[SeniorCitizen] = "Yes"
)
```

### Churn by Internet Service
```dax
-- Apply this measure in visuals filtered by InternetService column
Fiber Churn Rate % = 
CALCULATE(
    [Churn Rate %],
    'CustomerChurn'[InternetService] = "Fiber optic"
)
```

---

## Risk Scoring

### Churn Risk Score (Calculated Column)
```dax
Churn Risk Score = 
VAR ContractRisk = IF('CustomerChurn'[Contract] = "Month-to-month", 3,
                    IF('CustomerChurn'[Contract] = "One year", 1, 0))
VAR TenureRisk = IF('CustomerChurn'[Tenure] <= 12, 3,
                 IF('CustomerChurn'[Tenure] <= 24, 1, 0))
VAR InternetRisk = IF('CustomerChurn'[InternetService] = "Fiber optic", 2, 0)
VAR PaymentRisk = IF('CustomerChurn'[PaymentMethod] = "Electronic check", 1, 0)
VAR SecurityRisk = IF('CustomerChurn'[OnlineSecurity] = "No", 1, 0)
RETURN
    ContractRisk + TenureRisk + InternetRisk + PaymentRisk + SecurityRisk
```

### High Risk Customers Count
```dax
High Risk Customers = 
CALCULATE(
    COUNTROWS('CustomerChurn'),
    'CustomerChurn'[Churn Risk Score] >= 6
)
```

### Risk Tier (Calculated Column)
```dax
Risk Tier = 
SWITCH(
    TRUE(),
    'CustomerChurn'[Churn Risk Score] >= 6, "High Risk",
    'CustomerChurn'[Churn Risk Score] >= 3, "Medium Risk",
    "Low Risk"
)
```

---

## Conditional Formatting

### Churn Rate Color
```dax
Churn Rate Color = 
SWITCH(
    TRUE(),
    [Churn Rate %] >= 40, "Red",
    [Churn Rate %] >= 25, "Amber",
    "Green"
)
```
