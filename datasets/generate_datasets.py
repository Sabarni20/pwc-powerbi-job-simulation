import csv
import random
from datetime import datetime, timedelta

random.seed(42)

# ─── Dataset 1: Call Center ───────────────────────────────────────────────────
agents = ["Jim", "Martha", "Dan", "Diane", "Greg", "Joe", "Sarah", "Stewart"]
topics = ["Streaming", "Technical Support", "Payment related", "Admin Support", "Contract related"]
start_date = datetime(2021, 1, 1)

rows_cc = []
for i in range(1, 5001):
    call_date = start_date + timedelta(days=random.randint(0, 89))
    hour = random.choices(range(9, 21), weights=[3,5,7,9,10,10,9,8,7,6,5,4], k=1)[0]
    minute = random.randint(0, 59)
    answered = random.choices(["Y", "N"], weights=[81, 19])[0]
    resolved = "Y" if answered == "Y" and random.random() < 0.73 else "N"
    speed = random.randint(10, 180) if answered == "Y" else ""
    rating = random.choices([1,2,3,4,5], weights=[5,8,15,40,32])[0] if answered == "Y" else ""
    rows_cc.append([
        f"C{i:04d}",
        random.choice(agents),
        call_date.strftime("%Y-%m-%d"),
        f"{hour:02d}:{minute:02d}:00",
        random.choice(topics),
        answered,
        resolved,
        speed,
        rating
    ])

with open("/home/claude/pwc-powerbi-simulation/datasets/call_center.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Call ID","Agent","Date","Time","Topic","Answered (Y/N)","Resolved (Y/N)","Speed of Answer (seconds)","Satisfaction Rating"])
    w.writerows(rows_cc)
print("call_center.csv written:", len(rows_cc), "rows")

# ─── Dataset 2: Customer Churn ────────────────────────────────────────────────
contracts = ["Month-to-month","One year","Two year"]
payments  = ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"]
internet  = ["DSL","Fiber optic","No"]
rows_churn = []
for i in range(1, 7044):
    tenure   = random.randint(0, 72)
    contract = random.choices(contracts, weights=[55,25,20])[0]
    monthly  = round(random.uniform(18, 118), 2)
    total    = round(monthly * tenure * random.uniform(0.95, 1.05), 2) if tenure > 0 else 0.0
    churn_p  = 0.45 if contract=="Month-to-month" else (0.10 if contract=="One year" else 0.03)
    if tenure < 6: churn_p = min(churn_p * 1.6, 0.75)
    churn    = "Yes" if random.random() < churn_p else "No"
    rows_churn.append([
        f"CUST-{i:04d}",
        random.choice(["Male","Female"]),
        random.choices([0,1], weights=[84,16])[0],
        random.choices(["Yes","No"], weights=[48,52])[0],
        random.choices(["Yes","No"], weights=[30,70])[0],
        tenure,
        random.choices(["Yes","No"], weights=[90,10])[0],
        random.choices(["Yes","No"], weights=[85,15])[0],
        random.choices(internet, weights=[34,44,22])[0],
        random.choices(["Yes","No"], weights=[44,56])[0],
        random.choices(["Yes","No"], weights=[29,71])[0],
        random.choices(["Yes","No"], weights=[38,62])[0],
        random.choices(["Yes","No","No internet service"], weights=[29,44,27])[0],
        random.choices(["Yes","No","No internet service"], weights=[22,51,27])[0],
        random.choices(["Yes","No","No internet service"], weights=[16,57,27])[0],
        random.choices(["Yes","No","No internet service"], weights=[29,44,27])[0],
        contract,
        random.choices(["Yes","No"], weights=[59,41])[0],
        random.choices(payments, weights=[34,23,22,21])[0],
        monthly,
        total,
        churn
    ])

with open("/home/claude/pwc-powerbi-simulation/datasets/customer_churn.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["CustomerID","Gender","SeniorCitizen","Partner","Dependents","Tenure",
                "PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup",
                "DeviceProtection","TechSupport","StreamingTV","StreamingMovies","PaperlessBilling",
                "Contract","PaperlessBilling2","PaymentMethod","MonthlyCharges","TotalCharges","Churned"])
    w.writerows(rows_churn)
print("customer_churn.csv written:", len(rows_churn), "rows")

# ─── Dataset 3: Diversity & Inclusion ────────────────────────────────────────
levels     = ["Entry","Junior","Senior","Manager","Senior Manager","Director","Executive"]
depts      = ["HR","Finance","Operations","Technology","Sales","Legal","Strategy"]
age_groups = ["16-24","25-34","35-44","45-54","55-64","65+"]
female_pct = [0.52,0.46,0.40,0.34,0.26,0.18,0.12]   # drops with seniority

rows_di = []
eid = 1
for fy in ["FY20","FY21"]:
    for level_idx, level in enumerate(levels):
        count = [200,180,150,80,50,25,12][level_idx]
        for _ in range(count):
            gender = "Female" if random.random() < female_pct[level_idx] else "Male"
            perf   = round(random.gauss(3.0 if gender=="Female" else 3.1, 0.6), 1)
            perf   = max(1.0, min(5.0, perf))
            promo_rate = [0.18,0.14,0.11,0.09,0.07,0.05,0.02][level_idx]
            if gender=="Female": promo_rate *= 0.82
            hired  = random.choices(["Yes","No"], weights=[30,70])[0]
            turnover = random.choices(["Yes","No"], weights=[
                [22,20,15,11,9,7,5][level_idx], 100])[0]
            yrs_in_level = round(random.uniform(0.5, 8.0), 1)
            rows_di.append([
                f"EMP-{eid:04d}", fy, level, gender,
                random.choice(age_groups),
                random.choice(depts),
                hired, turnover,
                "Yes" if random.random() < promo_rate else "No",
                round(perf, 1),
                yrs_in_level
            ])
            eid += 1

with open("/home/claude/pwc-powerbi-simulation/datasets/diversity_inclusion.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["EmployeeID","FiscalYear","JobLevel","Gender","AgeGroup","Department",
                "NewHire","Turnover","Promoted","PerformanceRating","YearsInLevel"])
    w.writerows(rows_di)
print("diversity_inclusion.csv written:", len(rows_di), "rows")
