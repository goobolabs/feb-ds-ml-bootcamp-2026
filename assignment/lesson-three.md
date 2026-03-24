# Lesson 3 — Data Preprocessing (Assignment)

**Dataset (required):** Use Car Price — **car\_l3\_dataset.csv**

**Due:** **Wednesday, February 10, 2026 — 12:00 PM (Africa/Mogadishu / EAT)**

**Goal:** Build a clean, reproducible preprocessing pipeline on a messy tabular dataset.

---

## Dataset overview

Columns: Price (mixed numeric and currency strings), Odometer\_km, Doors, Accidents, Location (City/Suburb/Rural plus typos/unknowns), Year.
The file intentionally includes missing values, typos, outliers, and duplicates.

---

## Tasks (follow these ten steps, with brief checkpoints after each)

1. **Load & Inspect** — show head(10), shape, info, missing counts, and Location value counts; note key issues.
2. **Clean Target Formatting (Price)** — remove currency/commas; ensure numeric; report dtype and skewness.
3. **Fix Category Errors before Imputation** — normalize Location text, map typos (e.g., Subrb→Suburb), convert unknowns (e.g., “??”) to missing; recount including missing.
4. **Impute Missing Values (justify choices)** — Odometer\_km→median; Doors/Accidents→mode; Location→mode; confirm post-imputation missing counts.
5. **Remove Duplicates** — report shape before/after and rows removed.
6. **Outliers (IQR capping)** — compute bounds and clip for Price and Odometer\_km; show a short summary after capping.
7. **One-Hot Encode Categorical(s)** — encode Location as 0/1 columns; list the new columns created.
8. **Feature Engineering (no leakage)** — add at least three sensible features (e.g., CarAge, Km\_per\_year with safe handling, Is\_Urban). Add **LogPrice = log(Price+1)** as an alternative target (not a feature).
9. **Feature Scaling (X only)** — standardize continuous features; do **not** scale Price or LogPrice; prefer leaving 0/1 dummies unscaled; show a small sample of scaled values.
10. **Final Checks & Save** — final info, missing counts (all zero), a small describe table; save to **car\_l3\_clean\_ready.csv**.

---

## Deliverables

* **Script:** `l3_preprocess.py` implementing Steps 1–10 with clear print checkpoints.
* **Cleaned data:** `car_l3_clean_ready.csv`.
* **Reflection:** `reflection.md` (≤ 1 page) explaining your decisions for each major step (why median vs mode, why IQR capping, which features you engineered and why).
* **requirements.txt** with exact package versions used.

---

## AI usage policy (read carefully)

* You may use AI **only for advice and concept clarification** (e.g., “What is IQR capping?”, “When should I use mode imputation?”).
* **Do not use AI to generate code or full solutions.** All implementation must be written by **you**.

---

## Minimal sanity checks (recommended as assertions)

* Price is float; LogPrice exists and is numeric.
* No missing values remain at the end.
* At least one Location\_\* dummy column exists.
* Scaled columns have mean ≈ 0 and population std ≈ 1.

---

## Grading rubric (100 pts)

* Load & inspect (issues identified) — 8
* Clean target formatting — 7
* Fix categories before impute — 7
* Imputation choices (correct & justified) — 10
* Duplicates removed — 5
* Outliers (IQR bounds, clip, evidence) — 12
* One-hot encoding (0/1) — 8
* Feature engineering (≥3, sensible, no leakage) — 14
* Scaling (X only; sensible exclusions) — 8
* Final checks & saved CSV — 6
* Reflection (decisions and reasoning) — 10
* Reproducibility (requirements.txt; clean run) — 5