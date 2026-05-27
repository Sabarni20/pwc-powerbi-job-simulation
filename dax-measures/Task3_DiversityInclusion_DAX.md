# Task 3 – Diversity & Inclusion | DAX Measures

## Headcount & Gender Balance

### Total Employees
```dax
Total Employees = COUNTROWS('DiversityInclusion')
```

### Female Employees
```dax
Female Count = 
CALCULATE(
    COUNTROWS('DiversityInclusion'),
    'DiversityInclusion'[Gender] = "Female"
)
```

### Male Employees
```dax
Male Count = 
CALCULATE(
    COUNTROWS('DiversityInclusion'),
    'DiversityInclusion'[Gender] = "Male"
)
```

### % Women in Workforce
```dax
% Women = 
DIVIDE([Female Count], [Total Employees], 0) * 100
```

### % Women by Job Level (use in visual grouped by JobLevel)
```dax
% Women by Level = 
DIVIDE(
    CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[Gender] = "Female"),
    COUNTROWS('DiversityInclusion'),
    0
) * 100
```

---

## Promotion Analysis

### FY20 Promotion Rate – Overall
```dax
FY20 Promotion Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY20_Promoted] = "Yes"),
    [Total Employees],
    0
) * 100
```

### FY21 Promotion Rate – Overall
```dax
FY21 Promotion Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY21_Promoted] = "Yes"),
    [Total Employees],
    0
) * 100
```

### FY20 Female Promotion Rate
```dax
FY20 Female Promo Rate = 
CALCULATE(
    DIVIDE(
        CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY20_Promoted] = "Yes"),
        [Female Count],
        0
    ) * 100,
    'DiversityInclusion'[Gender] = "Female"
)
```

### FY20 Male Promotion Rate
```dax
FY20 Male Promo Rate = 
CALCULATE(
    DIVIDE(
        CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY20_Promoted] = "Yes"),
        [Male Count],
        0
    ) * 100,
    'DiversityInclusion'[Gender] = "Male"
)
```

### Promotion Gap (Male vs Female)
```dax
Promotion Gap % = [FY20 Male Promo Rate] - [FY20 Female Promo Rate]
```

---

## Time-in-Level (Promotion Velocity)

### Avg Years in Level – Female
```dax
Avg Years in Level (F) = 
CALCULATE(
    AVERAGE('DiversityInclusion'[YearsInLevel]),
    'DiversityInclusion'[Gender] = "Female"
)
```

### Avg Years in Level – Male
```dax
Avg Years in Level (M) = 
CALCULATE(
    AVERAGE('DiversityInclusion'[YearsInLevel]),
    'DiversityInclusion'[Gender] = "Male"
)
```

### Promotion Velocity Gap
```dax
Promotion Velocity Gap = 
[Avg Years in Level (F)] - [Avg Years in Level (M)]
-- Positive = women wait longer before promotion
```

---

## Performance Ratings

### Avg Performance Rating FY20
```dax
Avg Perf FY20 = AVERAGE('DiversityInclusion'[FY20_PerformanceRating])
```

### Avg Performance Rating FY21
```dax
Avg Perf FY21 = AVERAGE('DiversityInclusion'[FY21_PerformanceRating])
```

### Avg FY20 Perf – Female
```dax
Avg FY20 Perf (F) = 
CALCULATE(
    AVERAGE('DiversityInclusion'[FY20_PerformanceRating]),
    'DiversityInclusion'[Gender] = "Female"
)
```

### Avg FY20 Perf – Male
```dax
Avg FY20 Perf (M) = 
CALCULATE(
    AVERAGE('DiversityInclusion'[FY20_PerformanceRating]),
    'DiversityInclusion'[Gender] = "Male"
)
```

---

## Turnover Analysis

### FY20 Turnover Rate
```dax
FY20 Turnover Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY20_Turnover] = "Yes"),
    [Total Employees],
    0
) * 100
```

### FY21 Turnover Rate
```dax
FY21 Turnover Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY21_Turnover] = "Yes"),
    [Total Employees],
    0
) * 100
```

### Female Turnover Rate FY21
```dax
Female Turnover FY21 = 
CALCULATE(
    DIVIDE(
        CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY21_Turnover] = "Yes"),
        [Female Count],
        0
    ) * 100,
    'DiversityInclusion'[Gender] = "Female"
)
```

### Male Turnover Rate FY21
```dax
Male Turnover FY21 = 
CALCULATE(
    DIVIDE(
        CALCULATE(COUNTROWS('DiversityInclusion'), 'DiversityInclusion'[FY21_Turnover] = "Yes"),
        [Male Count],
        0
    ) * 100,
    'DiversityInclusion'[Gender] = "Male"
)
```

---

## Hiring Analysis

### FY21 Female Hiring Rate
```dax
FY21 Female Hire Rate = 
CALCULATE(
    DIVIDE(
        CALCULATE(COUNTROWS('DiversityInclusion'),
            'DiversityInclusion'[FY21_NewHire] = "Yes",
            'DiversityInclusion'[Gender] = "Female"),
        CALCULATE(COUNTROWS('DiversityInclusion'),
            'DiversityInclusion'[FY21_NewHire] = "Yes"),
        0
    ) * 100
)
```

### Executive Gender Ratio
```dax
% Women at Executive Level = 
CALCULATE(
    [% Women],
    'DiversityInclusion'[JobLevel] = "Executive"
)
```
