# Assignment 3 — Data Preprocessing (Car Price)

This project builds a clean, reproducible preprocessing pipeline for the `car_l3_dataset.csv` dataset. The script follows the 10 required steps from Lesson 3 (inspect, clean, fix categories, impute, de-duplicate, cap outliers, encode, engineer features, scale, and save).

## Dataset

Source file: `data/raw/car_l3_dataset.csv`  
Target file: `data/processed/car_l3_clean_ready.csv`

## Installation

```powershell
# from assignment-3/
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
```

## Environment Setup

This project was run on Windows with Python 3.11.  
If you are using a different version, recreate the virtual environment and reinstall dependencies.

## Dependencies

See `requirements.txt` for exact versions:

- pandas
- numpy
- scikit-learn

## How To Run

```powershell
python l3_preprocess.py
```

## Output

The cleaned dataset is saved to:

`data/processed/car_l3_clean_ready.csv`

## What The Script Does (Steps 1–10)

1. Load and inspect data (head/tail, shape, info, missing counts, and Location value counts).
2. Clean `Price` (strip currency/commas, convert to numeric, report dtype and skew).
3. Fix `Location` typos and unknowns, then recount categories and missing values.
4. Impute missing values (median for `Odometer_km`, mode for `Doors` and `Location`).
5. Remove duplicate rows and report the number removed.
6. Cap outliers using IQR for `Price` and `Odometer_km`.
7. One-hot encode `Location` into 0/1 columns.
8. Engineer features (`CarAge`, `Km_per_year`, `Is_Urban`, and `LogPrice`).
9. Standardize continuous features (`Odometer_km`, `CarAge`, `Km_per_year`).
10. Final checks and save the cleaned CSV.

## Folder Structure

```
assignment-3/
├─ data/
│  ├─ raw/
│  │  └─ car_l3_dataset.csv
│  └─ processed/
│     └─ car_l3_clean_ready.csv
├─ l3_preprocess.py
├─ requirements.txt
├─ README.md
└─ reflection.md
```
