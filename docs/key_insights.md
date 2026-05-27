# Key Analytical Insights — PwC Power BI Simulation

This document summarises the written analytical findings across all three tasks, formatted as insights you would deliver to a client or stakeholder.

---

## Task 1: Call Centre — PhoneNow

### Operational Summary
The PhoneNow call centre handled approximately 5,000 inbound calls between January and March 2021. Overall performance is adequate but has clear gaps that represent service risk.

### Findings

**Volume & Availability**
- Roughly 81% of calls were answered. The remaining 19% (≈950 calls) represent missed service opportunities — each unanswered call is a potential customer dissatisfaction event.
- Call volume peaks sharply between **10:00 AM and 12:00 PM**, suggesting understaffing during this window.

**Customer Satisfaction**
- Average satisfaction rating sits at approximately **3.4 / 5.0**, indicating a moderate but improvable baseline.
- Satisfaction is noticeably lower for calls related to **Technical Support** and **Streaming** topics, which also tend to have longer resolution times.

**Agent Performance**
- There is meaningful variance between agents. Top performers maintain resolution rates above 75% and satisfaction scores above 3.8, while lower performers sit at 58% and 2.9 respectively.
- Average speed of answer is approximately **67 seconds**, which is within acceptable range but could be reduced with better queuing during peak hours.

### Recommendations
1. **Increase staffing or stagger shifts** to cover the 10 AM–12 PM peak window.
2. **Implement targeted coaching** for agents with consistently below-average satisfaction scores.
3. **Create topic-specific routing** — direct Technical Support calls to agents with higher resolution rates in that category.
4. Set a KPI target: push Answer Rate to 90%+ and Satisfaction to 3.8+ within two quarters.

---

## Task 2: Customer Retention — Churn Analysis

### Business Context
Customer churn is one of the most direct threats to revenue stability in subscription-based telecoms. The data reveals that approximately **26–28% of customers churned**, representing significant recurring revenue loss.

### Findings

**Contract Type is the Strongest Predictor**
- Month-to-month customers churn at approximately **43%** — far higher than one-year (≈10%) or two-year (≈3%) contract holders.
- This single variable likely explains the majority of churn variance.

**The First Six Months Are Critical**
- Customers in the **0–6 month tenure** band show the steepest churn rates. If a customer survives past 12 months, their churn probability drops dramatically.
- This suggests onboarding experience, early perceived value, and switching costs are decisive.

**Service & Payment Patterns**
- **Fiber optic internet** customers churn more than DSL customers, possibly due to higher price sensitivity or unmet performance expectations.
- Customers paying via **electronic check** churn at higher rates than those on automatic bank transfer or credit card — possibly a proxy for lower commitment/engagement.

**Demographics**
- **Senior citizens** (flag = 1) churn at a meaningfully higher rate, likely due to fixed income sensitivity to monthly charges.
- Customers without **dependents** or **partners** are more likely to churn, consistent with lower switching costs.

### Recommendations
1. **Prioritise contract upgrade campaigns** targeting month-to-month customers at the 3-month mark.
2. **Design an onboarding programme** with check-in calls or support touchpoints in months 1–6.
3. **Introduce a senior citizen discount tier** or a value-add bundle to address price sensitivity.
4. **Investigate fiber optic service quality** — if churn is driven by unmet performance expectations, this is a product problem, not a pricing problem.

---

## Task 3: Diversity & Inclusion — HR Analysis

### Business Context
The HR data spans FY20 and FY21 across seven job levels (Entry to Executive) and five departments. The data tells a clear story: gender equity at lower levels does not translate upward, and the gap compounds with seniority.

### Findings

**The Pipeline Breaks in the Middle**
- Women represent ~52% of Entry-level employees — a near-equal start.
- This drops progressively: ~40% at Senior, ~34% at Manager, ~26% at Senior Manager, ~18% at Director, and approximately **12% at Executive**.
- The steepest drop occurs between Senior and Manager — the classic "broken rung."

**Promotion Velocity Gap**
- When women are promoted, they tend to have spent **1.2–1.8 more years in their current level** than men who were promoted at the same level.
- This gap is most pronounced at Director and Senior Manager levels, precisely where the pipeline narrows most.
- This is not explained by performance: female average ratings are statistically comparable to male ratings at every level.

**Turnover Concentration**
- Female turnover is noticeably higher at **Manager and Senior Manager** levels. This is likely the exit point for women who were passed over for promotion multiple times.
- Retaining women at this level is the single highest-leverage intervention available.

**Year-over-Year Progress**
- Comparing FY20 to FY21, executive-level female representation moved from approximately 11% to 12% — essentially flat.
- At the current rate of change, gender parity at the executive level is decades away.

### Recommendations
1. **Audit the promotion process at Manager level** — introduce structured calibration sessions with explicit gender-bias checks.
2. **Set a time-in-level trigger**: if any employee of any gender has been in level for X years without promotion consideration, an automatic review should be mandated.
3. **Build a sponsorship programme** pairing Senior Manager–level women with Executive sponsors, not just mentors.
4. **Set time-bound targets** for FY22 and FY23 (e.g., raise female Director % to 22%, Senior Manager to 30%) and hold department heads accountable.
5. **Exit interview analysis**: understand specifically why women leave at Manager level — whether it is blocked promotion, culture, pay, or flexibility — and act on it.

---

*Prepared as part of PwC Switzerland Power BI Virtual Case Experience on Forage.*
