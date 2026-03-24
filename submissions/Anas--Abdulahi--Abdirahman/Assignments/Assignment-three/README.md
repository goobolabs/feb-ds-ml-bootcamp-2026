# Lesson 3 Data Preprocessing Assignment

This project preprocesses the `car_l3_dataset.csv` dataset to prepare it for machine learning. The pipeline (implemented in `l3_preprocess.py`) cleans the target `Price` column, fixes categorical typos in `Location`, imputes missing values (median for numeric, mode for categorical, median for Price), removes duplicates, caps outliers using IQR, one-hot encodes `Location`, engineers features (`CarAge`, `Km_per_year`, `Is_Urban`) and `LogPrice` as an alternative target, and standardizes continuous inputs while leaving targets and dummy variables unscaled. The cleaned dataset is saved as `car_l3_clean_ready.csv`. All preprocessing decisions are explained in `reflection.md` and the environment is reproducible using `requirements.txt`.


**Note:** This work was completed independently, following the assignment guidelines, and AI was only used for advice and clarification on concepts, not for generating code.