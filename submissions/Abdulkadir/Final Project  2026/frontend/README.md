# Cancer Risk Prediction System (Frontend)

React + Tailwind UI that calls your Flask endpoint:

- `POST http://127.0.0.1:8000/predict?model=lr|rf|xgb`

## Prerequisites

You need **Node.js** (which includes `npm`).

### Option A: Install Node.js via `winget` (recommended)

Run in PowerShell:

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

Then **close and reopen** PowerShell and verify:

```powershell
node -v
npm -v
```

### Option B: Manual install

Install Node.js from https://nodejs.org (LTS). Make sure it adds to PATH.

## Run the app

```powershell
cd "deployment/frontend"
npm install
npm run dev
```

Then open the URL shown by `npm run dev` (typically `http://localhost:5173`).

