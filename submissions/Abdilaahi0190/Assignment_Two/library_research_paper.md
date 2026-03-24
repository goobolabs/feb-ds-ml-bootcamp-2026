# Research Paper: Public Library Book Circulation Dataset

## Title & Collection Method

**Title:** Public Library Book Popularity and Condition Dataset
**Collection Method:** I designed a **survey questionnaire** and asked 100 library visitors and staff to list details of books they recently borrowed or managed. The survey asked for the book title, genre, page count, condition, language, and how many copies they noticed. I then cross-referenced this with their perception of the book's popularity. Because the data was collected via survey, it contains some human errors like missing entries and duplicate reports.

---

## Description of Features & Labels

* **Features (X):**

  1. **Genre** (categorical: Fiction, Tech, Science, History, Arts, Business, etc.)
  2. **Page Count** (numeric: total number of pages)
  3. **Condition** (categorical: New, Good, Fair, Poor)
  4. **Language** (categorical: English, Somali, Arabic)
  5. **Copies Available** (numeric: number of physical copies in the library)

* **Label (y):**

  * **Popularity** → High / Low

This makes the problem a **classification task** (predicting whether a book will be highly borrowed or not).

---

## Dataset Structure

* **Rows:** 100 rows (including duplicates)
* **Columns:** 7 (6 features + 1 label)

### Sample Table (10 rows)

| Book Title | Genre | Page Count | Condition | Language | Copies Available | Popularity |
| ---------- | ----- | ---------- | --------- | -------- | ---------------- | ---------- |
| The Great Adventure | Fiction | 320 | Good | English | 3 | High |
| Advanced Python | Tech | 540 | New | English | 5 | High |
| World History Vol 1 | History | 450 | Fair | English | 2 | Low |
| Modern Science | Science | 280 | Good | English | 4 | High |
| Mystery of Nile | Mystery |  | Good | Arabic | 1 | Low |
| Machine Learning 101 | Tech | 600 | New | English | 4 | High |
| Machine Learning 101 | Tech | 600 | New | English | 4 | High |
| Ancient Rome | History | 400 | Poor | English | 1 | Low |
| Space Exploration | Science | 350 |  | English | 3 | High |
| Desert Tales | Fiction | 200 | Fair | Somali | 2 | Low |

---

## Quality Issues

* **Missing values:** Several respondents skipped fields like "Page Count" and "Condition," leaving empty cells in the CSV.
* **Duplicate Values:** Some books like "Machine Learning 101" and "Modern Arts" were reported multiple times by different survey participants.
* **Categorical text:** Genre, Condition, and Language are text-based and need encoding for ML models.
* **Imbalance:** There is a heavy concentration of "Tech" books due to the group of people surveyed.

---



---
