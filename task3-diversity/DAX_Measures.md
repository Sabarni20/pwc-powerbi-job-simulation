# Task 3 — Diversity & Inclusion: DAX Measures

## Workforce Composition

```dax
-- Total Employees
Total Employees = COUNTROWS(diversity_inclusion)

-- Female Employees
Female Employees = CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Gender] = "Female")

-- Male Employees
Male Employees = CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Gender] = "Male")

-- Female % of Workforce
Female % =
DIVIDE([Female Employees], [Total Employees], 0) * 100

-- Male %
Male % =
DIVIDE([Male Employees], [Total Employees], 0) * 100
```

## Gender by Job Level (core D&I visual)

```dax
-- Female % at Current Job Level (use in matrix with JobLevel on rows)
Female % at Level =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Gender] = "Female"),
    COUNTROWS(diversity_inclusion),
    0
) * 100

-- Male % at Level
Male % at Level =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Gender] = "Male"),
    COUNTROWS(diversity_inclusion),
    0
) * 100
```

## Hiring

```dax
-- New Hires
New Hires = CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[NewHire] = "Yes")

-- Female New Hires %
Female New Hire % =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion),
        diversity_inclusion[NewHire] = "Yes",
        diversity_inclusion[Gender] = "Female"),
    CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[NewHire] = "Yes"),
    0
) * 100

-- Male New Hire %
Male New Hire % = 100 - [Female New Hire %]
```

## Promotions

```dax
-- Total Promoted
Total Promoted = CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Promoted] = "Yes")

-- Promotion Rate %
Promotion Rate % =
DIVIDE([Total Promoted], [Total Employees], 0) * 100

-- Female Promotion Rate %
Female Promotion Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion),
        diversity_inclusion[Promoted] = "Yes",
        diversity_inclusion[Gender] = "Female"),
    CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Gender] = "Female"),
    0
) * 100

-- Male Promotion Rate %
Male Promotion Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion),
        diversity_inclusion[Promoted] = "Yes",
        diversity_inclusion[Gender] = "Male"),
    CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Gender] = "Male"),
    0
) * 100

-- Promotion Gender Gap (Male % - Female %)
Promotion Gender Gap pp =
[Male Promotion Rate %] - [Female Promotion Rate %]

-- Avg Years in Level Before Promotion — Female
Avg YearsInLevel Female =
CALCULATE(
    AVERAGE(diversity_inclusion[YearsInLevel]),
    diversity_inclusion[Gender] = "Female",
    diversity_inclusion[Promoted] = "Yes"
)

-- Avg Years in Level Before Promotion — Male
Avg YearsInLevel Male =
CALCULATE(
    AVERAGE(diversity_inclusion[YearsInLevel]),
    diversity_inclusion[Gender] = "Male",
    diversity_inclusion[Promoted] = "Yes"
)

-- Promotion Velocity Gap (how many more years women wait)
Promotion Velocity Gap =
[Avg YearsInLevel Female] - [Avg YearsInLevel Male]
```

## Turnover

```dax
-- Total Turnover
Total Turnover = CALCULATE(COUNTROWS(diversity_inclusion), diversity_inclusion[Turnover] = "Yes")

-- Turnover Rate %
Turnover Rate % =
DIVIDE([Total Turnover], [Total Employees], 0) * 100

-- Female Turnover Rate %
Female Turnover Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion),
        diversity_inclusion[Turnover] = "Yes",
        diversity_inclusion[Gender] = "Female"),
    [Female Employees],
    0
) * 100

-- Male Turnover Rate %
Male Turnover Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(diversity_inclusion),
        diversity_inclusion[Turnover] = "Yes",
        diversity_inclusion[Gender] = "Male"),
    [Male Employees],
    0
) * 100
```

## Performance Ratings

```dax
-- Avg Performance Rating
Avg Performance Rating = AVERAGE(diversity_inclusion[PerformanceRating])

-- Avg Performance — Female
Avg Perf Female =
CALCULATE(AVERAGE(diversity_inclusion[PerformanceRating]), diversity_inclusion[Gender] = "Female")

-- Avg Performance — Male
Avg Perf Male =
CALCULATE(AVERAGE(diversity_inclusion[PerformanceRating]), diversity_inclusion[Gender] = "Male")

-- Performance Gap (Male - Female)
Perf Rating Gap =
[Avg Perf Male] - [Avg Perf Female]
```

## Year-over-Year (FY20 → FY21)

```dax
-- Female % FY20
Female % FY20 =
CALCULATE([Female %], diversity_inclusion[FiscalYear] = "FY20")

-- Female % FY21
Female % FY21 =
CALCULATE([Female %], diversity_inclusion[FiscalYear] = "FY21")

-- YoY Change in Female %
Female % YoY Change pp =
[Female % FY21] - [Female % FY20]
```

---

## Suggested Visuals Layout

| Visual | Fields |
|---|---|
| KPI Card | Female % |
| KPI Card | Female Promotion Rate % |
| KPI Card | Promotion Velocity Gap |
| KPI Card | Female Turnover Rate % |
| Funnel / Bar | Female % at Level (Entry → Executive) |
| Clustered Bar | Promotion Rate %: Male vs Female by Level |
| Column Chart | Avg Years to Promotion: Male vs Female by Level |
| Bar Chart | Turnover Rate %: Male vs Female |
| Line Chart | Female % by FY (FY20 vs FY21) per Level |
| Scatter | Performance Rating vs Years in Level (by Gender) |
| Slicer | FiscalYear, Department, AgeGroup, JobLevel |
