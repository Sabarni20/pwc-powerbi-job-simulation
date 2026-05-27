# Task 1 — Call Center Trends: DAX Measures

## Core KPIs

```dax
-- Total Calls
Total Calls = COUNTROWS(call_center)

-- Total Answered
Total Answered = CALCULATE(COUNTROWS(call_center), call_center[Answered (Y/N)] = "Y")

-- Total Unanswered
Total Unanswered = CALCULATE(COUNTROWS(call_center), call_center[Answered (Y/N)] = "N")

-- Answer Rate (%)
Answer Rate % = DIVIDE([Total Answered], [Total Calls], 0) * 100

-- Total Resolved
Total Resolved = CALCULATE(COUNTROWS(call_center), call_center[Resolved (Y/N)] = "Y")

-- Resolution Rate (%)
Resolution Rate % = DIVIDE([Total Resolved], [Total Answered], 0) * 100

-- Average Satisfaction Rating
Avg Satisfaction Rating =
CALCULATE(
    AVERAGE(call_center[Satisfaction Rating]),
    call_center[Answered (Y/N)] = "Y"
)

-- Average Speed of Answer (seconds)
Avg Speed of Answer =
CALCULATE(
    AVERAGE(call_center[Speed of Answer (seconds)]),
    call_center[Answered (Y/N)] = "Y"
)
```

## Agent Performance

```dax
-- Calls Per Agent (used in a Table/Matrix visual grouped by Agent)
Calls Per Agent = COUNTROWS(call_center)

-- Agent Resolution Rate
Agent Resolution Rate % =
DIVIDE(
    CALCULATE(COUNTROWS(call_center), call_center[Resolved (Y/N)] = "Y"),
    CALCULATE(COUNTROWS(call_center), call_center[Answered (Y/N)] = "Y"),
    0
) * 100

-- Agent Avg Satisfaction
Agent Avg Satisfaction =
CALCULATE(
    AVERAGE(call_center[Satisfaction Rating]),
    call_center[Answered (Y/N)] = "Y"
)
```

## Time Intelligence

```dax
-- Calls by Hour (add a calculated column first)
Hour of Call = HOUR(call_center[Time])

-- Peak Hour Label
Peak Hour =
VAR _tbl =
    ADDCOLUMNS(
        VALUES(call_center[Hour of Call]),
        "Cnt", CALCULATE(COUNTROWS(call_center))
    )
RETURN
    MAXX(TOPN(1, _tbl, [Cnt], DESC), call_center[Hour of Call])

-- Calls Month-over-Month Change %
MoM Calls Change % =
VAR _currentMonth = CALCULATE([Total Calls], DATESMTD(call_center[Date]))
VAR _prevMonth    = CALCULATE([Total Calls], PREVIOUSMONTH(call_center[Date]))
RETURN DIVIDE(_currentMonth - _prevMonth, _prevMonth, 0) * 100
```

## Topic Analysis

```dax
-- Top Topic by Volume
Top Topic =
CALCULATE(
    FIRSTNONBLANK(call_center[Topic], 1),
    TOPN(1,
        SUMMARIZE(call_center, call_center[Topic], "Cnt", COUNTROWS(call_center)),
        [Cnt], DESC
    )
)
```

---

## Suggested Visuals Layout

| Visual | Fields |
|---|---|
| KPI Card | Total Calls |
| KPI Card | Answer Rate % |
| KPI Card | Avg Satisfaction Rating |
| KPI Card | Avg Speed of Answer |
| Bar Chart | Calls by Topic (Topic vs Total Calls) |
| Line Chart | Calls Over Time (Date hierarchy) |
| Column Chart | Calls by Hour of Day (Hour of Call) |
| Matrix | Agent × [Total Calls, Answered, Resolution Rate %, Avg Satisfaction] |
| Donut Chart | Answered vs Unanswered |
| Slicer | Month, Agent, Topic |
