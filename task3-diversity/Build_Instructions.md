# Task 3 — Diversity & Inclusion Dashboard: Build Instructions

## 1. Data Import

1. **Get Data → Text/CSV** → Load `datasets/diversity_inclusion.csv`
2. In Power Query Editor:
   - `PerformanceRating` → Decimal Number
   - `YearsInLevel` → Decimal Number
   - Rename query: `diversity_inclusion`
3. **Close & Apply**

## 2. Sort Order Column (Data View)

```dax
-- Add to diversity_inclusion
Job Level Order =
SWITCH(
    diversity_inclusion[JobLevel],
    "Entry",          1,
    "Junior",         2,
    "Senior",         3,
    "Manager",        4,
    "Senior Manager", 5,
    "Director",       6,
    "Executive",      7
)
```
Set **Sort by Column**: JobLevel → Job Level Order

## 3. Measures

Copy all measures from `DAX_Measures.md`.

## 4. Page Layout — "Gender Balance" Page

### Row 1 – KPI Cards
| Total Employees | Female % | Male % | Female % YoY Change pp |

### Row 2 – Funnel/Bar: Gender Representation by Level
- Plot **Female % at Level** with JobLevel on Y-axis (sorted Entry → Executive)
- Use a diverging bar centered at 50%: left = Female %, right = Male %
- Expected pattern: Female % drops steeply from ~52% at Entry to ~12% at Executive
- Add a 50% reference line as target

### Row 3 – Clustered Column: New Hire Gender Split by Department
- X: Department, Y: Female New Hire % and Male New Hire %
- Stacked 100% bar recommended

## 5. Page Layout — "Promotions & Velocity" Page

### Row 1 – KPI Cards
| Female Promotion Rate % | Male Promotion Rate % | Promotion Gender Gap pp | Promotion Velocity Gap |

### Row 2 – Clustered Bar: Promotion Rate by Level × Gender
- X: Promotion Rate % (two bars per level — Female, Male)
- Y: JobLevel (sorted Entry → Executive)
- Color: Female = `#E91E8C`, Male = `#1565C0`

### Row 3 – Grouped Column: Avg Years to Promotion — Male vs Female by Level
- X: JobLevel, Y: YearsInLevel (two series)
- Data labels on top of each bar
- Expected: Female bars visibly taller at Manager–Executive levels

### Row 4 – Small Multiples: FY20 vs FY21 Female Promotion Rate by Level
- Use Small Multiples on FiscalYear
- Shows whether the gap is improving or widening over time

## 6. Page Layout — "Turnover & Performance" Page

### Row 1 – KPI Cards
| Female Turnover Rate % | Male Turnover Rate % | Avg Perf Female | Avg Perf Male |

### Row 2 – Bar Chart: Turnover Rate by Level × Gender
- Side-by-side bars per level
- Expected: Female turnover higher at Manager and above

### Row 3 – Box Plot / Violin (or Column Chart): Avg Performance Rating by Level × Gender
- X: JobLevel, Y: Avg Performance Rating (two series)
- Key insight: Despite comparable or higher female ratings, promotion rates are lower

### Row 4 – Scatter Plot: Performance Rating vs. Promotion (colored by Gender)
- X: YearsInLevel, Y: PerformanceRating
- Color: Gender
- Shape: Promoted (Yes/No)
- Bubble size: count of employees

## 7. Slicers (all pages)

- FiscalYear (FY20 / FY21 toggle)
- Department
- Age Group
- JobLevel

## 8. Formatting Tips

- Color theme: **Purple + Orange** (`#5C2D91` for female, `#D04A02` for male — PwC brand)
- Canvas: **1280 × 720**
- Page title: *"Pharma Corp — Diversity & Inclusion HR Dashboard"*

## 9. Key Analytical Insights to Highlight

1. **The pipeline breaks at Manager level** — women are 40% of seniors but only 34% of managers
2. **Women wait ~1.2–1.8 more years** than men for promotions at Director level
3. **Female performance ratings are comparable** to male — the gap is NOT performance-driven
4. **Female turnover spikes at Manager level**, suggesting a "broken rung" phenomenon
5. **FY20 → FY21 shows minimal progress** in executive female representation (12% → 12%)

---

## Recommended Storytelling Flow (for presentation)

```
Slide/Page 1 → "Where are we?" — Gender balance overview (pipeline visual)
Slide/Page 2 → "Who gets promoted?" — Promotion rates + velocity gap
Slide/Page 3 → "Why are women leaving?" — Turnover + performance comparison
Slide/Page 4 → "What changed?" — FY20 vs FY21 trend
```
