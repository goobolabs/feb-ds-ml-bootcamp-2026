# Customer Water Consumption Dataset

## Overview
This dataset captures monthly water consumption and billing records for residential customers. It is designed to analyze usage patterns, billing efficiency, and payment behavior.

## Dataset Details
- **File Name:** `Customer Water Consumption Dataset.csv`
- **Rows:** 137
- **Columns:** 9

## Column Descriptions
| Column Name | Description | Type |
|-------------|-------------|------|
| **Guri No** | House Number / Unique Identifier | Categorical/Numeric |
| **A.H** | Akhriska Hore (Previous Meter Reading) | Numeric ($m^3$) |
| **A.D** | Akhriska Dambe (Current Meter Reading) | Numeric ($m^3$) |
| **Farqi** | Difference / Consumption (A.D - A.H) | Numeric ($m^3$) |
| **Dalacan** | Current Month Bill Amount | Currency (USD) |
| **R.Hore** | Previous Balance / Arrears | Currency (USD) |
| **Qabasho** | Amount Paid | Currency (USD) |
| **Resto** | Remaining Balance / Outstanding Debt | Currency (USD) |
| **Bixin** | Discount/Adjustment (Currently Empty) | Null |

## Potential Uses
- **Predictive Modeling:** Predict remaining balance (`Resto`) based on usage and previous history.
- **Customer Segmentation:** Cluster customers by usage volume (`Farqi`).
- **Anomaly Detection:** Identify irregular billing or reading errors.

## Notes
- Currency columns contain `$` symbols and parentheses `()` for negative values (credits).
- The `Bixin` column contains missing values and may need to be dropped during preprocessing.
