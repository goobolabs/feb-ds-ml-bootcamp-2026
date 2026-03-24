# 🎓 **Certificate Verification System — Data Science & Machine Learning Bootcamp**

Welcome to the official **certificate verification system** for graduates of the
**Data Science & Machine Learning Bootcamp** by **ToodMind**.

This folder serves as a **public registry of issued certificates**, allowing anyone to verify the authenticity and project record of ToodMind Bootcamp graduates.

---

## 🧭 **Purpose**

The goal of this system is to provide a **transparent and trusted verification method** for all certificates issued by **ToodMind**.

Each certificate includes a unique **ID** recorded in an official JSON file — [`index.json`](./index.json).
If the ID appears in this file and is marked as **valid**, the certificate is confirmed as genuine.

---

## 📁 **Folder Structure**

```
certifications/
│
├── index.json                      # Official list of issued certificates
├── certificate_farah_mohamed.pdf   # Example certificate PDF
├── certificate_halima_adam.pdf     # Example certificate PDF
└── README.md                       # This documentation file
```

---

## 📜 **How It Works**

1. Every graduate receives a **PDF certificate** with a unique ID (e.g., `DSML2025-01`).
2. That ID and relevant details are published in [`index.json`](./index.json).
3. Anyone can check the file to confirm whether a certificate is valid.
4. Each entry also includes a `project_link` so that the graduate’s final project can be reviewed.

If the record exists and `"status": "valid"`, the certificate is **officially verified by ToodMind**.

---

## 🧩 **Example Record**

```json
{
  "id": "DSML2025-01",
  "name": "Farah Mohamed",
  "course": "Data Science & Machine Learning Bootcamp",
  "issued_on": "2025-10-09",
  "valid_until": "Lifetime",
  "status": "valid",
  "project": "Customer Churn Prediction",
  "project_link": "https://github.com/toodmind/ds-ml-bootcamp/tree/main/projects/farah-mohamed",
  "verifier": "ToodMind"
},
{
  "id": "DSML2025-02",
  "name": "Halima Adam",
  "course": "Data Science & Machine Learning Bootcamp",
  "issued_on": "2025-10-09",
  "valid_until": "Lifetime",
  "status": "valid",
  "project": "House Price Prediction",
  "project_link": "https://github.com/toodmind/ds-ml-bootcamp/tree/main/projects/halima-adam",
  "verifier": "ToodMind"
}
```

---

## 🔎 **How to Verify a Certificate**

1. Open the [`index.json`](./index.json) file.
2. Find the **certificate ID** shown on the PDF (e.g., `DSML2025-01`).
3. If the record exists and `"status": "valid"`, the certificate is authentic.
4. Visit the `project_link` to explore the graduate’s project.

---

## 🔒 **Verification Integrity**

| Check Type       | Purpose                                                     | Managed By          |
| ---------------- | ----------------------------------------------------------- | ------------------- |
| **ID Check**     | Confirms that the certificate is officially issued          | ToodMind            |
| **Project Link** | Provides proof of real project completion                   | ToodMind            |
| **Status Field** | Shows whether the certificate is valid, expired, or revoked | ToodMind            |

---

### 🧾 **License**

All contents © 2026 **Goobo Labs**.
Certificate and verification data are provided for educational and authenticity purposes only.

---
