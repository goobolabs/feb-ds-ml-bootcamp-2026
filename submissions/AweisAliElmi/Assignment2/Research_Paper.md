# Research Paper: Residential Water Consumption Dataset

## Title & Collection Method
**Title:** Residential Water Consumption and Payment Billing Dataset

**Collection Method:** I collected this dataset from the manual billing records of a local utility service provider. I recorded water meter readings and financial ledger entries for 137 households to analyze their consumption and payment behaviors during a single billing cycle.

## Description of Features & Labels
**Features (X):**

*   Guri No (categorical: House ID)
*   A.H (numeric: Previous Reading in $m^3$)
*   A.D (numeric: Current Reading in $m^3$)
*   Farqi (numeric: Consumption in $m^3$)
*   R.Hore (numeric: Previous Balance in Currency)
*   Dalacan (numeric: Current Bill in Currency)
*   Qabasho (numeric: Payment Made in Currency)

**Label (y):**

*   Resto → Remaining Balance
This makes the problem a regression task (predicting the exact amount of debt) or a classification task (predicting Default/Clear).

## Dataset Structure
**Rows:** 137 households (samples)
**Columns:** 9 (8 features + 1 label) Note: 'Bixin' is included but empty.

**Sample Table (10 rows)**
| Guri No | A.H | A.D | Farqi | Dalacan | R.Hore | Qabasho | Resto |
| :--- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 4398 | 148 | 156 | 8 | $12.00 | ($0.20) | $0.00 | $11.80 |
| 4282 | 7 | 9 | 2 | $3.00 | $0.00 | $0.00 | $3.00 |
| 7405 | 323 | 323 | 0 | $15.00 | ($0.10) | $0.00 | $14.90 |
| 5859 | 83 | 87 | 4 | $6.00 | $0.00 | $0.00 | $6.00 |
| 5590 | 560 | 573 | 13 | $19.50 | ($0.10) | $0.00 | $19.40 |
| 3946 | 226 | 239 | 13 | $19.50 | $0.50 | $0.00 | $20.00 |
| 5399 | 163 | 171 | 8 | $12.00 | ($0.10) | $0.00 | $11.90 |
| 8403 | 1408 | 1412 | 4 | $6.00 | $0.00 | $0.00 | $6.00 |
| 5305 | 54 | 63 | 9 | $13.50 | ($0.10) | $0.00 | $13.40 |
| 8307 | 137 | 147 | 10 | $15.00 | $0.90 | $0.00 | $15.90 |

## Quality Issues
*   **Missing values:** The "Bixin" column is completely empty and needs removal.
*   **Format issues:** Money columns (`Dalacan`, `Resto`) have `$` signs and parentheses for negatives (e.g., `($0.20)`), which must be cleaned for ML.
*   **Ambiguity:** Some rows show 0 consumption (`Farqi`) but still have a bill charged.
*   **Outliers:** A few customers have unusually large previous balances or payments.

## Use Case
This dataset can be used to train a regression model to predict the **Resto** (Remaining Balance) based on a customer's usage and previous history.

**Possible algorithms:** Linear Regression, Random Forest, Decision Tree.
It could help utility companies identify high-risk accounts and improve debt collection strategies.
