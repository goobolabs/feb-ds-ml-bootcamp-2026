import React, { useMemo, useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

const MODEL_OPTIONS = [
  { value: "lr", label: "Logistic Regression" },
  { value: "rf", label: "Random Forest" },
  { value: "xgb", label: "XGBoost" }
];

const CANCER_CLASSES = ["Breast", "Colon", "Lung", "Prostate", "Skin"];

function getSelectOptionLabel(options, value) {
  const found = options.find((o) => Number(o.value) === Number(value));
  return found ? found.label : String(value);
}

function parseNumberOrFallback(value, fallback) {
  const n = Number(value);
  return Number.isFinite(n) ? n : fallback;
}

export default function App() {
  const initialForm = useMemo(
    () => ({
      // Numeric
      Age: 45,
      BMI: 25,

      // Binary 0/1
      Gender: 0,
      Smoking: 0,
      Alcohol_Use: 0,
      Obesity: 0,
      Family_History: 0,
      Diet_Red_Meat: 0,
      Diet_Salted_Processed: 0,
      Physical_Activity: 0,
      Air_Pollution: 0,
      Occupational_Hazards: 0,
      BRCA_Mutation: 0,
      H_Pylori_Infection: 0,
      // Diet intensity / environment
      Fruit_Veg_Intake: 0,
      Calcium_Intake: 0,

      // Multi-level 0/1/2
      Physical_Activity_Level: 1
    }),
    []
  );

  const [model, setModel] = useState("lr");
  const [form, setForm] = useState(initialForm);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  const fields = useMemo(
    () => [
      { key: "Age", label: "Age", kind: "number", step: 0.1 },
      { key: "BMI", label: "BMI", kind: "number", step: 0.1 },

      {
        key: "Gender",
        label: "Gender",
        kind: "select",
        options: [
          { value: 0, label: "0 = Female" },
          { value: 1, label: "1 = Male" }
        ]
      },
      {
        key: "Smoking",
        label: "Smoking",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Alcohol_Use",
        label: "Alcohol_Use",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Obesity",
        label: "Obesity",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Family_History",
        label: "Family_History",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Diet_Red_Meat",
        label: "Diet_Red_Meat",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Diet_Salted_Processed",
        label: "Diet_Salted_Processed",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Fruit_Veg_Intake",
        label: "Fruit_Veg_Intake",
        kind: "select",
        options: [
          { value: 0, label: "0 = Low" },
          { value: 1, label: "1 = High" }
        ]
      },
      {
        key: "Physical_Activity",
        label: "Physical_Activity",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Air_Pollution",
        label: "Air_Pollution",
        kind: "select",
        options: [
          { value: 0, label: "0 = Low" },
          { value: 1, label: "1 = High" }
        ]
      },
      {
        key: "Occupational_Hazards",
        label: "Occupational_Hazards",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "BRCA_Mutation",
        label: "BRCA_Mutation",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "H_Pylori_Infection",
        label: "H_Pylori_Infection",
        kind: "select",
        options: [
          { value: 0, label: "0 = No" },
          { value: 1, label: "1 = Yes" }
        ]
      },
      {
        key: "Calcium_Intake",
        label: "Calcium_Intake",
        kind: "select",
        options: [
          { value: 0, label: "0 = Low" },
          { value: 1, label: "1 = High" }
        ]
      },
      {
        key: "Physical_Activity_Level",
        label: "Physical_Activity_Level",
        kind: "select",
        options: [
          { value: 0, label: "0 = Low" },
          { value: 1, label: "1 = Medium" },
          { value: 2, label: "2 = High" }
        ]
      }
    ],
    []
  );

  function validate() {
    const age = Number(form.Age);
    const bmi = Number(form.BMI);
    if (!Number.isFinite(age) || age <= 0) return "Please enter a valid Age.";
    if (!Number.isFinite(bmi) || bmi <= 0) return "Please enter a valid BMI.";
    return "";
  }

  async function onPredict() {
    setError("");
    setResult(null);

    const msg = validate();
    if (msg) {
      setError(msg);
      return;
    }

    const payload = {
      Age: Number(form.Age),
      BMI: Number(form.BMI),
      Gender: Number(form.Gender),
      Smoking: Number(form.Smoking),
      Alcohol_Use: Number(form.Alcohol_Use),
      Obesity: Number(form.Obesity),
      Family_History: Number(form.Family_History),
      Diet_Red_Meat: Number(form.Diet_Red_Meat),
      Diet_Salted_Processed: Number(form.Diet_Salted_Processed),
      Fruit_Veg_Intake: Number(form.Fruit_Veg_Intake),
      Physical_Activity: Number(form.Physical_Activity),
      Air_Pollution: Number(form.Air_Pollution),
      Occupational_Hazards: Number(form.Occupational_Hazards),
      BRCA_Mutation: Number(form.BRCA_Mutation),
      H_Pylori_Infection: Number(form.H_Pylori_Infection),
      Calcium_Intake: Number(form.Calcium_Intake),
      Physical_Activity_Level: Number(form.Physical_Activity_Level)
    };

    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/predict?model=${encodeURIComponent(model)}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) {
        throw new Error(data?.error || `Request failed with status ${res.status}`);
      }

      setResult(data);
    } catch (e) {
      setError(e?.message || "Prediction failed. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  const predictedLabel = result?.prediction_label || "";
  const probabilities = result?.probabilities || {};

  return (
    <div className="min-h-screen bg-gradient-to-br from-brand-50 via-white to-indigo-50">
      <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6">
        <header className="mb-6">
          <div className="flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <h1 className="font-display text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">
                Cancer Risk Prediction System
              </h1>
              <p className="mt-2 max-w-2xl text-sm leading-6 text-slate-600 sm:text-base">
                Enter your health and lifestyle features to get a model prediction.
              </p>
            </div>
          </div>
        </header>

        <div className="flex flex-col gap-6 lg:flex-row">
          {/* LEFT: Input */}
          <section className="w-full lg:w-1/2">
            <div className="rounded-3xl bg-white/85 p-5 shadow-soft ring-1 ring-brand-100/80 backdrop-blur-sm sm:p-6">
              <div className="mb-5 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div>
                  <h2 className="font-display text-xl font-bold text-slate-900">Input Form</h2>
                  <p className="text-sm text-slate-600">17 features required for the models.</p>
                </div>

                <div className="w-full sm:w-56">
                  <label className="text-sm font-semibold text-slate-700" htmlFor="modelSelect">
                    Model Selection
                  </label>
                  <select
                    id="modelSelect"
                    value={model}
                    onChange={(e) => setModel(e.target.value)}
                    className="mt-2 w-full rounded-xl border border-brand-100 bg-white px-3 py-2 text-sm text-slate-900 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-300"
                  >
                    {MODEL_OPTIONS.map((m) => (
                      <option key={m.value} value={m.value}>
                        {m.label}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
                {fields.map((f) => {
                  const inputId = `field_${f.key}`;
                  const value = form[f.key];

                  return (
                    <div key={f.key} className="col-span-1">
                      <label
                        htmlFor={inputId}
                        className="mb-2 block text-xs font-semibold uppercase tracking-wide text-slate-600"
                      >
                        {f.label}
                      </label>

                      {f.kind === "number" ? (
                        <input
                          id={inputId}
                          type="number"
                          step={f.step || 1}
                          value={value}
                          onChange={(e) => {
                            const v = e.target.value;
                            setForm((prev) => ({ ...prev, [f.key]: parseNumberOrFallback(v, 0) }));
                          }}
                          className="w-full rounded-xl border border-brand-100 bg-white px-3 py-2 text-sm text-slate-900 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-300"
                        />
                      ) : (
                        <select
                          id={inputId}
                          value={String(value)}
                          onChange={(e) =>
                            setForm((prev) => ({ ...prev, [f.key]: Number(e.target.value) }))
                          }
                          className="w-full rounded-xl border border-brand-100 bg-white px-3 py-2 text-sm text-slate-900 shadow-sm transition focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-300"
                        >
                          {f.options.map((o) => (
                            <option key={o.value} value={String(o.value)}>
                              {o.label}
                            </option>
                          ))}
                        </select>
                      )}

                      <div className="mt-2 rounded-lg bg-slate-50 px-2 py-1 text-[11px] text-slate-500">
                        Selected:{" "}
                        {f.kind === "number"
                          ? String(form[f.key])
                          : getSelectOptionLabel(f.options, form[f.key])}
                      </div>
                    </div>
                  );
                })}
              </div>

              {error ? (
                <div className="mt-4 rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-800">
                  {error}
                </div>
              ) : null}

              <div className="mt-5 flex items-center justify-end">
                <button
                  type="button"
                  onClick={onPredict}
                  disabled={loading}
                  className="inline-flex items-center justify-center rounded-xl bg-brand-600 px-6 py-2.5 text-sm font-semibold text-white shadow-glow transition hover:bg-brand-700 disabled:cursor-not-allowed disabled:opacity-60"
                >
                  {loading ? "Predicting..." : "Predict"}
                </button>
              </div>
            </div>
          </section>

          {/* RIGHT: Result */}
          <section className="w-full lg:w-1/2">
            <div className="rounded-3xl bg-white/90 p-5 shadow-soft ring-1 ring-brand-100/80 backdrop-blur-sm sm:p-6">
              <div className="mb-4 flex items-center justify-between gap-3">
                <div>
                  <h2 className="font-display text-xl font-bold text-slate-900">Prediction Result</h2>
                  <p className="text-sm text-slate-600">Probabilities are shown for all cancer types.</p>
                </div>
                <div className="rounded-xl bg-brand-50 px-3 py-1.5 text-xs font-semibold text-brand-700">
                  Model: {model.toUpperCase()}
                </div>
              </div>

              {!result && !loading ? (
                <div className="rounded-xl border border-dashed border-brand-200 bg-brand-50/50 p-4 text-sm text-slate-600">
                  Click <span className="font-semibold text-slate-900">Predict</span> to see the
                  predicted cancer type and class probabilities.
                </div>
              ) : null}

              {loading ? (
                <div className="space-y-4">
                  <div className="h-4 w-2/3 animate-pulse rounded bg-slate-200" />
                  <div className="h-4 w-full animate-pulse rounded bg-slate-200" />
                  <div className="h-4 w-5/6 animate-pulse rounded bg-slate-200" />
                  <div className="h-6 w-32 animate-pulse rounded bg-slate-200" />
                </div>
              ) : null}

              {result ? (
                <div className="space-y-5">
                  <div className="rounded-2xl border border-accent-100 bg-gradient-to-br from-accent-50 to-white p-4">
                    <div className="text-sm text-slate-600">Predicted Cancer Type</div>
                    <div className="mt-1 font-display text-2xl font-bold text-slate-900">
                      {predictedLabel}
                    </div>
                    <div className="mt-3">
                      <div className="flex items-center justify-between">
                        <div className="text-sm font-medium text-slate-700">Confidence</div>
                        <div className="text-sm font-semibold text-accent-700">
                          {typeof result.confidence === "number"
                            ? `${(result.confidence * 100).toFixed(1)}%`
                            : "-"}
                        </div>
                      </div>
                      <div className="mt-2 h-2.5 w-full overflow-hidden rounded-full bg-slate-200">
                        <div
                          className="h-full rounded-full bg-accent-500"
                          style={{
                            width:
                              typeof result.confidence === "number"
                                ? `${Math.max(0, Math.min(1, result.confidence)) * 100}%`
                                : "0%"
                          }}
                        />
                      </div>
                    </div>
                  </div>

                  <div className="space-y-3">
                    {CANCER_CLASSES.map((label) => {
                      const prob = typeof probabilities[label] === "number" ? probabilities[label] : 0;
                      const pct = prob * 100;
                      const isPred = label === predictedLabel;

                      return (
                        <div key={label}>
                          <div className="flex items-center justify-between">
                            <div className="text-sm font-semibold text-slate-800">
                              {label} {isPred ? <span className="text-accent-600">• Predicted</span> : null}
                            </div>
                            <div className="text-sm font-semibold text-slate-700">{pct.toFixed(1)}%</div>
                          </div>

                          <div className="mt-2 h-3 w-full overflow-hidden rounded-full bg-slate-200">
                            <div
                              className={`h-full rounded-full ${isPred ? "bg-accent-600" : "bg-brand-500"}`}
                              style={{ width: `${Math.max(0, Math.min(1, prob)) * 100}%` }}
                            />
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  <div className="rounded-xl border border-slate-200/80 bg-slate-50/80 p-3">
                    <div className="text-xs font-semibold uppercase tracking-wide text-slate-600">
                      Raw Probabilities
                    </div>
                    <pre className="mt-2 overflow-auto whitespace-pre-wrap break-words text-xs text-slate-700">
                      {JSON.stringify(probabilities, null, 2)}
                    </pre>
                  </div>
                </div>
              ) : null}

              {result?.error ? (
                <div className="mt-4 rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-800">
                  {result.error}
                </div>
              ) : null}
            </div>
          </section>
        </div>

        <footer className="mt-8 text-xs tracking-wide text-slate-500">
          This UI is for prediction visualization and does not provide medical advice.
        </footer>
      </div>
    </div>
  );
}

