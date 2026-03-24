## 🎓 Reflection Paper – House Price Prediction

## 1. What did you implement?

In this project, I implemented a machine learning model to predict house prices using two algorithms: Linear Regression and Random Forest Regressor.

First, I loaded the cleaned dataset using the pandas library. Then I prepared the data by separating the target variable (Price) from the input features (X). The dataset was then split into training data (80%) and testing data (20%) using train_test_split with random_state=42.

After preparing the data, I trained two different models. The first model was Linear Regression, which predicts house prices using a linear relationship between features and the target variable. The second model was Random Forest Regressor, which is an ensemble machine learning algorithm that combines many decision trees.

Finally, I evaluated both models using performance metrics such as R², MAE, MSE, and RMSE and compared their results.
### 2. Comparison of Models
When I tested the models using the sanity check, I compared the actual house price with the predictions produced by both models.

The Linear Regression prediction was closer to the actual price in that specific test row, while the Random Forest prediction had a larger difference. However, when evaluating the models using the entire test dataset, Random Forest produced better overall performance.

This shows that while Linear Regression can sometimes produce accurate predictions, Random Forest tends to perform better overall because it can capture more complex patterns in the data.

#### 3. Understanding Random Forest

Random Forest is a machine learning algorithm that is based on an ensemble of decision trees.

Instead of building only one decision tree, Random Forest creates multiple decision trees using random samples of the dataset. Each tree makes its own prediction, and the final prediction is calculated by averaging the predictions from all trees.

This method helps reduce overfitting and improves the model’s accuracy and stability. Because of this, Random Forest is often more powerful than simple models like Linear Regression when dealing with complex datasets.

### 4. Metrics Discussion
In my results, the Random Forest model had a higher R² score and lower error values (MAE and RMSE) compared to the Linear Regression model.

This indicates that Random Forest was able to explain more variation in the dataset and produced more accurate predictions overall. Linear Regression performed reasonably well but had slightly higher error values.

These results show that Linear Regression is a simple and fast algorithm, but Random Forest is generally more accurate when the relationships between features and target variables are complex.

#### 
# 🎓 Assignment – House Price Prediction with Linear Regression & Random Forest Due: Tuesday, September 18, 2025 — 12:00 PM (Africa/Mogadishu / EAT)  ## **Part A – Practical (Jupyter Notebook)**  **Objective:** In this part, you will implement **house price prediction** using **Linear Regression** and **Random Forest Regressor**. You will evaluate both models and compare their performance.  ---  ### **Instructions**  1. **Notebook Setup**     * Create a Jupyter Notebook named:      house_price_prediction.ipynb.  2. **Load Dataset**     * Use the cleaned dataset you generated in **Lesson 3** (clean_house_dataset.csv).  3. **Prepare Features & Target**     * Target (y) = Price    * Features (X) = all other columns except Price and LogPrice.  4. **Split Data**     * Split into **80% training** and **20% testing**.    * Use random_state=42.  5. **Train Models**     * Train a **LinearRegression** model.    * Train a **RandomForestRegressor** (use n_estimators=100, random_state=42).  6. **Evaluate Performance**     * Print **R², MAE, MSE, RMSE** for both models using a helper function.  7. **Single-row Sanity Check**     * Pick one row from the test set (X_test.iloc[[i]]) and compare actual price with predictions from both models. ---  ### **Expected Output**  * Metrics printed for both models, e.g.:    
Linear Regression Performance:     R²   : 0.84     MAE  : 63,086     RMSE : 75,624    Random Forest Performance:     R²   : 0.86     MAE  : 52,524     RMSE : 72,686
 * A single-row prediction from test set (Actual vs Predicted).  ---  ## **Part B – Reflection Paper**  Write a short paper (1–2 pages, Markdown or PDF) answering the following:  1. **What did you implement?**     * Briefly describe how you trained Linear Regression and Random Forest to predict house prices.  2. **Comparison of Models:**     * When you tested on **3 Sanity Check**, how did predictions differ?    * Which model gave more **realistic results**? Why?  3. **Understanding Random Forest:**     * Explain in your own words:       * What is Random Forest?      * How does it work (ensemble of decision trees, averaging predictions)?  4. **Metrics Discussion:**     * Which model (LR or RF) had better **R²** and **error metrics** (MAE, RMSE)?    * What does that tell you about the strengths and weaknesses of each model?  5. **Your Findings:**     * Summarize in 1–2 paragraphs which model you prefer for price prediction models and why.  ---  ### **Submission Format**  * house_price_prediction.ipynb (with all code + results). * reflection_paper.pdf or reflection_paper.md (your discu

Waxaan kuu sharaxayaa assignment-kaaga si fudud iyo sidoo kale code-ka Jupyter Notebook si aad si toos ah u isticmaali karto.

🎓 House Price Prediction – Guide
Waxaad samaynaysaa Machine Learning model si uu u saadaaliyo qiimaha guryaha adigoo isticmaalaya:

Linear Regression

Random Forest Regressor

Kadib waxaad barbardhigaysaa performance-kooda.

Part A – Jupyter Notebook Code
Notebook magaca:

house_price_prediction.ipynb
1️⃣ Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
2️⃣ Load Dataset
df = pd.read_csv("clean_house_dataset.csv")

df.head()
3️⃣ Prepare Features (X) and Target (y)
Target = Price

y = df["Price"]

X = df.drop(["Price", "LogPrice"], axis=1)
4️⃣ Split Dataset
80% training
20% testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
5️⃣ Train Models
Linear Regression
lr_model = LinearRegression()

lr_model.fit(X_train, y_train)
Random Forest
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)
6️⃣ Predictions
lr_pred = lr_model.predict(X_test)

rf_pred = rf_model.predict(X_test)
7️⃣ Evaluation Function
def evaluate_model(y_true, y_pred, name):

    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    print(name)
    print("R²  :", r2)
    print("MAE :", mae)
    print("MSE :", mse)
    print("RMSE:", rmse)
    print()
8️⃣ Evaluate Both Models
evaluate_model(y_test, lr_pred, "Linear Regression Performance")

evaluate_model(y_test, rf_pred, "Random Forest Performance")
Example Output:

Linear Regression Performance
R²  : 0.84
MAE : 63086
RMSE: 75624

Random Forest Performance
R²  : 0.86
MAE : 52524
RMSE: 72686
9️⃣ Single Row Sanity Check
i = 0

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

lr_prediction = lr_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]

print("Actual Price:", actual_price)
print("Linear Regression Prediction:", lr_prediction)
print("Random Forest Prediction:", rf_prediction)
Part B – Reflection Paper (Example Answer)
Waxaad ku qori kartaa Markdown ama PDF.

1️⃣ What did you implement?
I implemented a machine learning project to predict house prices using Linear Regression and Random Forest Regressor.
First, I loaded the cleaned dataset and separated the target variable (Price) from the features.

Then I split the dataset into training (80%) and testing (20%).

After that I trained two models:

Linear Regression

Random Forest Regressor

Finally, I evaluated the models using R², MAE, MSE, and RMSE.

2️⃣ Comparison of Models
When I tested the models using the sanity check, the predictions were slightly different.

The Random Forest model produced more realistic predictions compared to Linear Regression because it can capture non-linear relationships in the data.

3️⃣ Understanding Random Forest
Random Forest is a machine learning algorithm based on an ensemble of decision trees.

Instead of using one tree, Random Forest builds many decision trees using random samples of the dataset.

Each tree makes a prediction, and the final prediction is the average of all trees.
This helps reduce overfitting and improves accuracy.

4️⃣ Metrics Discussion
In most cases, Random Forest has:

Higher R²

Lower MAE

Lower RMSE

This means Random Forest usually predicts prices more accurately than Linear Regression.

Linear Regression is simpler and faster, but it may not capture complex patterns in the data.

5️⃣ My Findings
Based on the results, I prefer using Random Forest for house price prediction because it generally provides better accuracy and lower errors.

Random Forest can model complex relationships between features such as location, size, and number of rooms.

However, Linear Regression is still useful because it is simple, fast, and easy to interpret.

✅ Haddii aad rabto waxaan kuu diyaarin karaa sidoo kale:

Notebook complete ah oo aad si toos ah u submit gareyn karto

Reflection paper PDF diyaar ah

GitHub submission sida loo sameeyo

Haddii aad rabto ii sheeg.


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
# 2️⃣ Load Dataset

CSV_PATH = "Data_set/clean_house_l5_dataset.csv"


df = pd.read_csv(CSV_PATH)

df.head(10)
# print(df.head(10))

# 3️⃣ Prepare Features (X) and Target (y)

# Target = Price
y = df["Price"]

X = df.drop(["Price", "LogPrice"], axis=1)
#4️⃣ Split Dataset

# 80% training
# 20% testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 5️⃣ Train Models
# Linear Regression
lr_model = LinearRegression()

lr_model.fit(X_train, y_train)
# Random Forest
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)
# 6️⃣ Predictions


lr_pred = lr_model.predict(X_test)

rf_pred = rf_model.predict(X_test)
# 7️⃣ Evaluation Function

def evaluate_model(y_true, y_pred, name):

    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    print(name)
    print("R²  :", r2)
    print("MAE :", mae)
    print("MSE :", mse)
    print("RMSE:", rmse)
    print()
# 8️⃣ Evaluate Both Models

evaluate_model(y_test, lr_pred, "Linear Regression Performance")

evaluate_model(y_test, rf_pred, "Random Forest Performance")

# 9️⃣ Single Row Sanity Check
i = 0

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

lr_prediction = lr_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]

print("Actual Price:", actual_price)
print("Linear Regression Prediction:", lr_prediction)
print("Random Forest Prediction:", rf_prediction)   sidaan ayaan qoray waan xaliyay maahinoo 

Haa 👍 code-ka aad qortay waa sax, assignment-ka inta badan si fiican ayaad u xallisay. Waxaan eegay dhammaan qaybaha, waxayna ku jiraan waxyaabihii la rabay. Aan si kooban kuu tuso.

✔ Waxyaabaha Assignment-ku Rabay
1️⃣ Load Dataset
Adiga waad sameysay:

CSV_PATH = "Data_set/clean_house_l5_dataset.csv"
df = pd.read_csv(CSV_PATH)
✔ Sax.

2️⃣ Features & Target
Target = Price

y = df["Price"]
X = df.drop(["Price", "LogPrice"], axis=1)
✔ Sax.

3️⃣ Split Data (80/20 + random_state=42)
train_test_split(X, y, test_size=0.2, random_state=42)
✔ Sida assignment-ku rabay.

4️⃣ Train Models
Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
✔ Sax.

Random Forest
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)
✔ Sax.

5️⃣ Predictions
lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)
✔ Sax.

6️⃣ Metrics (R², MAE, MSE, RMSE)
Adiga waxaad sameysay function fiican:

def evaluate_model(y_true, y_pred, name):
✔ Tani waa practice fiican ML.

7️⃣ Evaluate Models
evaluate_model(y_test, lr_pred, "Linear Regression Performance")
evaluate_model(y_test, rf_pred, "Random Forest Performance")
✔ Sax.

8️⃣ Single-row Sanity Check
Assignment-ku wuxuu rabay:

X_test.iloc[[i]]
Adigana waad isticmaashay:

sample = X_test.iloc[[i]]
✔ Sax.

✔ Gunaanad
Code-kaaga:

✅ Dataset load
✅ Features & target
✅ Train/Test split
✅ Linear Regression
✅ Random Forest
✅ Metrics (R², MAE, MSE, RMSE)
✅ Single-row prediction

👉 Assignment Part A waa complete.

⚠ Hal talo yar (Optional Improvement)
Si output-ka u noqdo assignment example-ka la mid, waxaad ku dari kartaa:

print("Actual Price:", round(actual_price,2))
print("Linear Regression Prediction:", round(lr_prediction,2))
print("Random Forest Prediction:", round(rf_prediction,2))
🎯 Waxa kuu haray
Waxa keliya oo haray:

Part B – Reflection Paper

1–2 page:

What did you implement

Comparison of models

What is Random Forest

Metrics discussion

Your findings

✅ Haddii aad rabto, waxaan kuu samayn karaa Reflection Paper PDF diyaar ah oo aad submit gareyso.


⚠ Hal talo yar (Optional Improvement)

Si output-ka u noqdo assignment example-ka la mid, waxaad ku dari kartaa:xagee kudaraa

Waxaad ku dartaa dhamaadka code-kaaga, meesha aad ku print gareyso Actual Price iyo Predictions.

Hadda code-kaaga waa sidaan:

print("Actual Price:", actual_price)
print("Linear Regression Prediction:", lr_prediction)
print("Random Forest Prediction:", rf_prediction)
Adiga 3-da line-kan beddel oo ku qor sidan:

print("Actual Price:", round(actual_price,2))
print("Linear Regression Prediction:", round(lr_prediction,2))
print("Random Forest Prediction:", round(rf_prediction,2))
📍 Taasi waxay ku taalaa section-ka ugu dambeeya ee code-ka:

# 9️⃣ Single Row Sanity Check
Code-ka qaybtaas oo dhan wuxuu noqdaa:

# 9️⃣ Single Row Sanity Check

i = 0

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

lr_prediction = lr_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]

print("Actual Price:", round(actual_price,2))
print("Linear Regression Prediction:", round(lr_prediction,2))
print("Random Forest Prediction:", round(rf_prediction,2))
✔ Waxa uu sameynayo:

wuxuu ka dhigaa numbers-ka nadiif

wuxuu ka jaraa decimal badan

Tusaale output:

Actual Price: 210000.00
Linear Regression Prediction: 205430.55
Random Forest Prediction: 212340.87
Haddii aad rabto, waxaan sidoo kale ku tusi karaa 3 qalad oo arday badan ku dhacaan assignment-kan si aad marks-kaaga u hubiso 💯.


n.py
Linear Regression Performance
R²  : 0.8478474731443675
MAE : 63085.83804860746
MSE : 5718940940.596758
RMSE: 75623.67976101638

Random Forest Performance
R²  : 0.859437243835704
MAE : 52523.85
MSE : 5283317454.95
RMSE: 72686.43239938248

Actual Price: 642500.0
Linear Regression Prediction: 656754.67
Random Forest Prediction: 789031.0
Model trained successfull

Haa 👍 natiijada aad heshay waa sax, waxaana ka muuqata in model-kaagu si guul leh u shaqeeyay. Aan kuu sharxo waxa ay ka dhigan yihiin si aad ugu isticmaasho reflection paper-ka.

📊 Natiijooyinka Model-kaaga
1️⃣ Linear Regression Performance
R²: 0.8478

MAE: 63,085

RMSE: 75,623

Micnaha:

Model-ku wuxuu sharxayaa qiyaastii 84% xogta qiimaha guryaha.

Celcelis ahaan khaladka waa $63k.

2️⃣ Random Forest Performance
R²: 0.8594

MAE: 52,523

RMSE: 72,686

Micnaha:

Model-ku wuxuu sharxayaa 85.9% xogta.

Khaladka celceliska waa $52k.

🥇 Model-ka Fiican
Marka la barbar dhigo:

Metric	Linear Regression	Random Forest
R²	0.847	0.859
MAE	63k	52k
RMSE	75k	72k
👉 Random Forest ayaa ka fiican sababtoo ah:

R² waa ka sareeya

MAE waa ka yar

RMSE waa ka yar

Taasi waxay ka dhigan tahay Random Forest prediction-ku waa sax badan yahay.

🔎 Sanity Check
Actual Price: 642500
LR Prediction: 656754
RF Prediction: 789031
Farqiga:

Linear Regression ≈ +14k

Random Forest ≈ +146k

👉 Hal row keliya Linear Regression ayaa u dhow.
Laakiin overall dataset Random Forest ayaa fiican.

✅ Gunaanad (waxaad ku qori kartaa report-ka)
Example:

The Random Forest model performed better overall with a higher R² and lower error metrics. This shows that Random Forest can capture more complex relationships in the housing dataset. However, in some individual predictions, Linear Regression may still produce closer results. Overall, Random Forest is more reliable for house price prediction.

🎯 Gunaanad Kale
Output-kaaga wuxuu caddeynayaa:

✅ Code waa sax
✅ Models waa trained
✅ Metrics waa sax
✅ Sanity check waa sax

👉 Assignment Part A = Complete 💯

Haddii aad rabto, waxaan sidoo kale kuu diyaarin karaa:

Reflection Paper PDF (1–2 page) oo aad si toos ah GitHub ama LMS ugu submit gareyn karto.


ok part b

Waa hagaag 👍 Part B – Reflection Paper waxaad u baahan tahay 1–2 pages. Hoos waxaa ku qoran qoraal aad si toos ah u isticmaali karto (waxaad ku dhigi kartaa Markdown ama PDF).

🎓 Reflection Paper – House Price Prediction
1. What did you implement?
In this project, I implemented a machine learning model to predict house prices using two algorithms: Linear Regression and Random Forest Regressor.

First, I loaded the cleaned dataset using the pandas library. Then I prepared the data by separating the target variable (Price) from the input features (X). The dataset was then split into training data (80%) and testing data (20%) using train_test_split with random_state=42.

After preparing the data, I trained two different models. The first model was Linear Regression, which predicts house prices using a linear relationship between features and the target variable. The second model was Random Forest Regressor, which is an ensemble machine learning algorithm that combines many decision trees.

Finally, I evaluated both models using performance metrics such as R², MAE, MSE, and RMSE and compared their results.

2. Comparison of Models
When I tested the models using the sanity check, I compared the actual house price with the predictions produced by both models.

The Linear Regression prediction was closer to the actual price in that specific test row, while the Random Forest prediction had a larger difference. However, when evaluating the models using the entire test dataset, Random Forest produced better overall performance.

This shows that while Linear Regression can sometimes produce accurate predictions, Random Forest tends to perform better overall because it can capture more complex patterns in the data.

3. Understanding Random Forest
Random Forest is a machine learning algorithm that is based on an ensemble of decision trees.

Instead of building only one decision tree, Random Forest creates multiple decision trees using random samples of the dataset. Each tree makes its own prediction, and the final prediction is calculated by averaging the predictions from all trees.

This method helps reduce overfitting and improves the model’s accuracy and stability. Because of this, Random Forest is often more powerful than simple models like Linear Regression when dealing with complex datasets.

4. Metrics Discussion
In my results, the Random Forest model had a higher R² score and lower error values (MAE and RMSE) compared to the Linear Regression model.

This indicates that Random Forest was able to explain more variation in the dataset and produced more accurate predictions overall. Linear Regression performed reasonably well but had slightly higher error values.

These results show that Linear Regression is a simple and fast algorithm, but Random Forest is generally more accurate when the relationships between features and target variables are complex.

## 5. My Findings


Based on the results of this project, I found that Random Forest is a better model for house price prediction because it provides higher accuracy and lower prediction errors.

Random Forest can capture complex relationships between housing features such as size, location, and number of rooms. This allows it to make more reliable predictions compared to Linear Regression.

However, Linear Regression is still useful because it is simple, easy to interpret, and computationally efficient. For large datasets or quick baseline models, Linear Regression can still be a good starting point.
### ✅ Submission Files

house_price_prediction.ipynb

reflection_paper.pdf ama reflection_paper.md

