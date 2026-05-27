# Task 1 — Call Center Dashboard: Build Instructions

## 1. Data Import

1. Open Power BI Desktop → **Get Data → Text/CSV**
2. Load `datasets/call_center.csv`
3. In Power Query Editor:
   - Set `Date` column → Data type: **Date**
   - Set `Time` column → Data type: **Time**
   - Set `Satisfaction Rating` → Data type: **Whole Number** (blank rows stay blank)
   - Set `Speed of Answer (seconds)` → Data type: **Whole Number**
   - Rename the query to `call_center`
4. Click **Close & Apply**

## 2. Calculated Columns (add in Data view)

```dax
-- Add to call_center table
Hour of Call = HOUR(call_center[Time])
Month Name   = FORMAT(call_center[Date], "MMMM YYYY")
Month Number = MONTH(call_center[Date])   -- for sorting Month Name
```

## 3. Measures (add via New Measure)

Copy all measures from `DAX_Measures.md` into Power BI.

## 4. Page Layout — "Overview" Page

### Visual 1 – KPI Cards (top row, 4 cards)
- Total Calls
- Answer Rate %
- Avg Satisfaction Rating (with a star icon)
- Avg Speed of Answer

### Visual 2 – Donut Chart: Answered vs Unanswered
- Values: Total Calls
- Legend: Answered (Y/N)

### Visual 3 – Bar Chart: Calls by Topic
- Y-Axis: Topic
- X-Axis: Total Calls
- Sort descending

### Visual 4 – Line Chart: Daily Call Volume
- X-Axis: Date
- Y-Axis: Total Calls
- Secondary line: Avg Satisfaction Rating (use secondary axis)

### Visual 5 – Column Chart: Calls by Hour of Day
- X-Axis: Hour of Call (0–23)
- Y-Axis: Total Calls
- Color-code peak hours (9 AM–12 PM) with conditional formatting

### Visual 6 – Matrix: Agent Performance Table
| Agent | Total Calls | Total Answered | Resolution Rate % | Avg Satisfaction | Avg Speed of Answer |
- Add data bars on Avg Satisfaction column

## 5. Page Layout — "Agent Deep-Dive" Page

- Slicer: Agent (vertical list)
- KPI Cards filtered to selected agent
- Trend line: daily satisfaction over time
- Comparison bar: selected agent vs. team average

## 6. Slicers (both pages)

- Month slicer (dropdown)
- Topic slicer (multi-select checklist)
- Agent slicer (dropdown, synced across pages)

## 7. Formatting Tips

- Color theme: **Blues** (PwC palette: `#D04A02` orange accent, `#2D2D2D` dark)
- Enable **Tooltips** on all visuals to show supporting metrics
- Add a text box title at top: *"PhoneNow — Call Centre Performance Dashboard"*
- Report canvas size: **1280 × 720**
