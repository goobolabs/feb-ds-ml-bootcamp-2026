import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ================= LOAD DATA =================
CSV_PATH = "Employee.csv"
df = pd.read_csv(CSV_PATH)

# ================= RENAME COLUMNS =================
rename_map = {
    "Work Hours": "Work_Hours",
    "Sleep Hours": "Sleep_Hours",
    "Attendance %": "Attendance_Pct",
    "Performance Rating": "Performance_Rating",
    "Coffee Consumption_Heavy": "Coffee_Heavy",
    "Coffee Consumption_Light": "Coffee_Light",
    "Coffee Consumption": "Coffee_Consumption"
}
df = df.rename(columns=rename_map)

# ================= STANDARDIZE COFFEE =================
if {"Coffee_Heavy", "Coffee_Light"}.issubset(df.columns):
    df["Coffee_Heavy"] = df["Coffee_Heavy"].astype("boolean")
    df["Coffee_Light"] = df["Coffee_Light"].astype("boolean")

    def coffee_label(row):
        if row["Coffee_Heavy"] is True:
            return "Heavy"
        if row["Coffee_Light"] is True:
            return "Light"
        return "None"

    df["Coffee_Consumption"] = df.apply(coffee_label, axis=1)

elif "Coffee_Consumption" in df.columns:
    df["Coffee_Consumption"] = (
        df["Coffee_Consumption"]
        .astype("string")
        .str.strip()
        .str.title()
        .replace({"Hevy": "Heavy", "Ligt": "Light"})
    )
else:
    df["Coffee_Consumption"] = "None"

# ================= CLEAN CATEGORICALS =================
df["Department"] = (
    df["Department"]
    .astype("string")
    .str.strip()
    .str.title()
    .replace({"It": "IT"})
)

df["Performance_Rating"] = (
    df["Performance_Rating"]
    .astype("string")
    .str.strip()
    .str.title()
)

# ================= HANDLE MISSING VALUES =================
for col in ["Work_Hours", "Sleep_Hours", "Attendance_Pct"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

for col in ["Department", "Performance_Rating", "Coffee_Consumption"]:
    if col in df.columns and df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# ================= REMOVE DUPLICATES =================
df = df.drop_duplicates()

# ================= OUTLIER CLIPPING =================
def iqr_bounds(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr

for col in ["Work_Hours", "Sleep_Hours", "Attendance_Pct"]:
    if col in df.columns:
        low, high = iqr_bounds(df[col])
        df[col] = df[col].clip(lower=low, upper=high)

df["Work_Hours"] = df["Work_Hours"].clip(0, 16)
df["Sleep_Hours"] = df["Sleep_Hours"].clip(0, 16)
df["Attendance_Pct"] = df["Attendance_Pct"].clip(0, 100)

# ================= ONE HOT ENCODING =================
df = pd.get_dummies(
    df,
    columns=["Department", "Performance_Rating", "Coffee_Consumption"],
    drop_first=False,
    dtype="int"
)

# ================= FEATURE ENGINEERING =================
df["Work_Sleep_Ratio"] = df["Work_Hours"] / df["Sleep_Hours"].replace(0, np.nan)

if "Performance_Rating_Excellent" in df.columns:
    df["Is_Excellent"] = df["Performance_Rating_Excellent"].astype(int)
else:
    df["Is_Excellent"] = 0

if "Coffee_Consumption_Heavy" in df.columns:
    df["Coffee_Heavy_Flag"] = df["Coffee_Consumption_Heavy"].astype(int)
else:
    df["Coffee_Heavy_Flag"] = 0

# ================= PREVENT DATA LEAKAGE =================
# Drop Performance_Rating dummies (they contain target info)
df = df.drop(columns=[c for c in df.columns if c.startswith("Performance_Rating_")])

# ================= SCALING =================
exclude = ["Is_Excellent", "Coffee_Heavy_Flag"]
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
num_to_scale = [c for c in num_cols if c not in exclude]

scaler = StandardScaler()
df[num_to_scale] = scaler.fit_transform(df[num_to_scale])

# ================= TRAIN MODEL =================
target = "Is_Excellent"
X = df.drop(columns=[target])
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ================= EVALUATION =================
print("\n=== TEST SET RESULTS ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ================= CROSS VALIDATION =================
cv_scores = cross_val_score(model, X, y, cv=5)

print("\n=== CROSS VALIDATION ===")
print("CV Scores:", cv_scores)
print("Mean CV Accuracy:", cv_scores.mean())