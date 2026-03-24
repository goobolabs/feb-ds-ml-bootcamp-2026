## Dataset Description

This project includes two versions of the same dataset collected from the GitHub REST API, covering public repositories created between **2015 and 2024**.

### 1. `github_repos.csv`

* A comma-separated values (CSV) file containing raw GitHub repository metadata.
* Each row represents a single public repository.
* Includes repository details such as creation date, primary language, stars, forks, watchers, open issues, and size.
* Suitable for quick inspection, scripting, and machine learning pipelines.

### 2. `github_repos.xlsx`

* An Excel (XLSX) version of the same dataset as the CSV file.
* Contains identical rows and columns as `github_repos.csv`.
* Intended for manual exploration, filtering, and analysis using spreadsheet tools.

### Notes

* No data balancing or preprocessing has been applied.
* The dataset is naturally imbalanced, with most repositories having low star counts and a small number having very high popularity.
* Both files contain the same data; only the file format differs.

---

