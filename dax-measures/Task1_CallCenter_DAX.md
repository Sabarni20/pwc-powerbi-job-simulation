# Task 1 – Call Center Trends | DAX Measures

## KPI Measures

### Total Calls
```dax
Total Calls = COUNTROWS('CallCenter')
```

### Total Answered Calls
```dax
Total Answered = 
CALCULATE(
    COUNTROWS('CallCenter'),
    'CallCenter'[Answered (Y/N)] = "Y"
)
```

### Total Unanswered Calls
```dax
Total Unanswered = 
CALCULATE(
    COUNTROWS('CallCenter'),
    'CallCenter'[Answered (Y/N)] = "N"
)
```

### Answer Rate %
```dax
Answer Rate % = 
DIVIDE(
    [Total Answered],
    [Total Calls],
    0
) * 100
```

### Total Resolved Calls
```dax
Total Resolved = 
CALCULATE(
    COUNTROWS('CallCenter'),
    'CallCenter'[Resolved (Y/N)] = "Y"
)
```

### Resolution Rate %
```dax
Resolution Rate % = 
DIVIDE(
    [Total Resolved],
    [Total Answered],
    0
) * 100
```

### Average Satisfaction Rating
```dax
Avg Satisfaction = 
CALCULATE(
    AVERAGEX(
        FILTER('CallCenter', 'CallCenter'[Satisfaction Rating] <> BLANK()),
        'CallCenter'[Satisfaction Rating]
    )
)
```

### Average Speed of Answer (seconds)
```dax
Avg Speed of Answer (sec) = 
CALCULATE(
    AVERAGEX(
        FILTER('CallCenter', 'CallCenter'[Answered (Y/N)] = "Y"),
        'CallCenter'[Speed of Answer (seconds)]
    )
)
```

### Calls Handled per Agent
```dax
Calls Per Agent = 
DIVIDE(
    [Total Answered],
    DISTINCTCOUNT('CallCenter'[Agent]),
    0
)
```

---

## Time Intelligence Measures

### Calls by Hour (for Peak Hour Analysis)
```dax
-- Add a calculated column first:
Hour of Call = HOUR('CallCenter'[Time])
```

### Monthly Call Volume
```dax
Monthly Calls = 
CALCULATE(
    [Total Calls],
    DATESMTD('CallCenter'[Date])
)
```

### MoM Call Volume Change %
```dax
MoM Call Change % = 
VAR CurrentMonth = [Total Calls]
VAR PrevMonth = CALCULATE([Total Calls], DATEADD('CallCenter'[Date], -1, MONTH))
RETURN
    DIVIDE(CurrentMonth - PrevMonth, PrevMonth, 0) * 100
```

---

## Agent Performance Measures

### Agent Satisfaction Ranking
```dax
Agent Satisfaction Rank = 
RANKX(
    ALL('CallCenter'[Agent]),
    [Avg Satisfaction],
    ,
    DESC,
    DENSE
)
```

### Agent Resolution Rate
```dax
Agent Resolution Rate = 
DIVIDE(
    CALCULATE(COUNTROWS('CallCenter'), 'CallCenter'[Resolved (Y/N)] = "Y"),
    CALCULATE(COUNTROWS('CallCenter'), 'CallCenter'[Answered (Y/N)] = "Y"),
    0
) * 100
```

---

## Topic Analysis

### Top Topic by Call Volume
```dax
Top Topic = 
FIRSTNONBLANK(
    TOPN(1,
        VALUES('CallCenter'[Topic]),
        [Total Calls],
        DESC
    ),
    1
)
```

### Unresolved by Topic
```dax
Unresolved Calls = 
CALCULATE(
    COUNTROWS('CallCenter'),
    'CallCenter'[Resolved (Y/N)] = "N",
    'CallCenter'[Answered (Y/N)] = "Y"
)
```

---

## Conditional Formatting Helpers

### Satisfaction Color Flag
```dax
Satisfaction Flag = 
SWITCH(
    TRUE(),
    [Avg Satisfaction] >= 4.0, "Green",
    [Avg Satisfaction] >= 3.0, "Amber",
    "Red"
)
```
