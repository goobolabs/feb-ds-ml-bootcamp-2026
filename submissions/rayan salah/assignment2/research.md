# Research Paper: Empirical Analysis of University Student Commuting Patterns

## 1. Title & Collection Method
**Project Title:** Predictors of Commute Duration: A Primary Dataset on Student Mobility and Urban Traffic Impact.

**Collection Method:**
The data for this study was gathered through a **primary research design** using an online **Google Forms survey**. The target population consisted of university students across various academic faculties. This method was chosen to ensure a diverse cross-section of data, capturing different geographical starting points and socioeconomic commuting factors.

While Google Forms provided a structured digital entry point, the survey intentionally utilized open-text fields for several key variables. This design choice allowed for the collection of "natural noise"—such as inconsistent units, typos, and illogical entries—to simulate a real-world data environment. This provides a robust foundation for the upcoming data preprocessing phase in Lesson 3.

---

## 2. Description of Features & Labels
To facilitate supervised machine learning, the dataset is categorized into input features ($X$) and a specific target label ($y$).

### **Input Variables (Features $X$):**
* **Gender:** A categorical variable (Male/Female) to observe demographic trends in commuting.
* **Faculty:** The student’s academic department (e.g., Computer Science, Engineering, Medicine), which acts as a proxy for their campus destination.
* **Distance:** The physical length of the commute, captured in varying formats such as kilometers or descriptive text.
* **Departure Time:** The timestamp representing when the student begins their journey, critical for analyzing peak-hour traffic impact.
* **Mode of Transport:** The vehicle type used (e.g., Bus, Car/Caasi, Bajaj, Walking).
* **Financial Cost:** The monetary expenditure per trip, recorded with various currency markers.
* **Traffic Level:** An ordinal scale from 1 to 5, representing the student's subjective experience of road congestion.

### **Output Variable (Label $y$):**
* **Duration:** This is the **Target Variable**. It represents the total elapsed travel time from home to campus. The objective of the research is to build a model that predicts this value based on the interactions of the input features.

---

## 3. Dataset Structure
The dataset comprises over **50 observations (rows)** and **8 distinct features (columns)**. Below is a representative sample of the raw data collected from the survey:

### **Sample Data Table (Representative Rows)**
| Gender | Faculty | Distance | Time | Mode | Cost | Traffic Level | **Duration (y)** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Female | Computer Science & IT | 15 | 7:30 | Car (caasi) | 25 | 2 | 50 |
| Male | Faculty of Computing | **20 years** | 7:00 | Bus | 24 dollar | 3 | **18min** |
| Female | Software Engineer | *(Blank)* | 7:00 | Car (caasi) | 45$ | 2 | ***(Blank)*** |
| Female | Software Engineer | **I don't know** | 7:00 | Car (caasi) | 45$ | 2 | **Two** |
| Male | Economics | 7km | 7:10 | Car (caasi) | 25 | 1 | 1:25 |
| Female | Software | *(Blank)* | 7:00 | Walking | 50$ | 2 | **Ma bdno** |

---

## 4. Quality Issues (The "Messy" Reality)
As this is a raw, student-reported dataset, it exhibits several critical data quality issues that will be the focus of **Lesson 3 Preprocessing**:

1.  **Semantic and Logical Errors:** There are instances where users provided non-sensical data for specific fields, such as entering *"20 years"* in the Distance column.
2.  **Inconsistent Formatting and Units:**
    * **Time:** Entries vary between standard timestamps ("7:30"), 12-hour formats ("7:00 AM"), and descriptive phrases ("When I clear" or "From Sabti").
    * **Cost:** Values include various currency symbols and text (e.g., "25", "$24", "24 dollar", "Nothing", or "0.25").
    * **Duration:** The target variable is highly inconsistent, mixing integers ("50"), strings ("18min"), written numbers ("Two"), and Somali text ("Ma bdno mana yaro").
3.  **Missing Values (Null Data):** Several entries are incomplete, with blank cells in the Distance and Duration columns. These require advanced imputation techniques (like using the mean or median) or row deletion.
4.  **Typographical Errors:** Inconsistent naming of faculties (e.g., "Agriculcure" vs "Agriculture" or "IT" vs "Computer Science") will require string standardization.

---

## 5. Use Case in Machine Learning
This dataset serves as a foundational tool for three major types of Machine Learning applications:

### **A. Regression (Primary Use Case)**
By setting **Duration** as the continuous numerical target ($y$), we can develop a **Linear Regression** model. The logic follows that as Distance and Traffic Level increase, Duration should also increase. This model can help students predict their arrival times with higher accuracy based on their specific commute variables.

### **B. Classification**
The `Traffic Level` (1–5) can be binned into categorical classes: **Low (1-2)**, **Medium (3)**, and **High (4-5)**. A classification algorithm (like a Decision Tree) can then predict the *likelihood* of a student facing "High" traffic based on their `Faculty` location and `Departure Time`.

### **C. Clustering (Unsupervised Learning)**
Using the **K-Means algorithm**, we can group students into "Commuter Profiles" based on their `Mode`, `Cost`, and `Distance`. This could reveal hidden clusters, such as:
* **"Budget Commuters":** Low cost, high distance, primarily walking or using buses.
* **"Premium/Fast Commuters":** High cost, shorter durations, primarily using Bajaj or private cars.
* **"On-Campus/Local":** Minimal distance and zero cost.

---

## 6. Conclusion
The University Students Transportation Survey successfully captures the complexity of urban student life. While the current state of the data is "noisy" and "messy," it provides the perfect raw material for learning the end-to-end data science process. By applying cleaning, encoding, and scaling in the next lesson, this dataset will move from a raw survey output to a predictive tool capable of optimizing student mobility.
