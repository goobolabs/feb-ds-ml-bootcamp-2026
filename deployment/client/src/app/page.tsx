"use client";

import { useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { Home, TrendingUp, Calculator, Star, BarChart3 } from "lucide-react";

interface PredictionResult {
  input: {
    Bathrooms: number;
    Bedrooms: number;
    Location: string;
    Size_sqft: number;
    YearBuilt: number;
  };
  model_used: string;
  prediction: number;
}

export default function HomePage() {
  const [formData, setFormData] = useState({
    Size_sqft: "",
    Bedrooms: "3",
    Bathrooms: "2",
    Location: "City",
    YearBuilt: "",
    selectedPredictor: "Predictor 2",
  });

  const [prediction, setPrediction] = useState<PredictionResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleInputChange = (field: string, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const getModelParam = () => {
    switch (formData.selectedPredictor) {
      case "predictor-1":
        return "lr";
      case "Predictor 2":
        return "rf";
      default:
        return "rf";
    }
  };

  const getPrimaryPrediction = () => {
    if (!prediction?.prediction) return "N/A";
    return `$${prediction.prediction.toLocaleString("en-US", {
      maximumFractionDigits: 0,
    })}`;
  };

  const getPredictorLabel = () => {
    switch (formData.selectedPredictor) {
      case "predictor-1":
        return "Predictor-1";
      case "Predictor 2":
        return "Predictor 2";
      default:
        return "Predictor 2";
    }
  };

  const handlePredict = async () => {
    if (!formData.Size_sqft) {
      setError("Please enter the size of the house");
      return;
    }
    if (!formData.Location) {
      setError("Please select a location");
      return;
    }
    if (!formData.YearBuilt) {
      setError("Please enter the year built");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const apiUrl = process.env.API_URL;
      const modelParam = getModelParam();

      const requestData = {
        Size_sqft: parseFloat(formData.Size_sqft),
        Bedrooms: parseInt(formData.Bedrooms),
        Bathrooms: parseInt(formData.Bathrooms),
        YearBuilt: parseInt(formData.YearBuilt),
        Location: formData.Location,
      };

      const response = await fetch(`${apiUrl}/predict?model=${modelParam}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      setPrediction(result);
    } catch (error) {
      console.error("Prediction error:", error);
      setError(
        "Error calculating prediction. Please check your inputs and ensure the backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  // Real model performance data
  const mockModelInfo = {
    metrics: {
      linear_regression: {
        r2_score: 0.848,
        mae: 63086,
        mse: 5718940941,
        rmse: 75624,
      },
      random_forest: {
        r2_score: 0.859,
        mae: 52524,
        mse: 5283317455,
        rmse: 72686,
      },
      best_model: "Random Forest",
    },
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 relative overflow-hidden">
      {/* Background Pattern */}
      <div
        className="absolute inset-0 opacity-40"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.02'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        }}
      ></div>

      {/* Floating Shapes */}
      <div className="absolute top-20 left-10 w-72 h-72 bg-blue-200 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse"></div>
      <div className="absolute top-40 right-10 w-72 h-72 bg-purple-200 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse animation-delay-2000"></div>
      <div className="absolute -bottom-8 left-20 w-72 h-72 bg-pink-200 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-pulse animation-delay-4000"></div>

      {/* Header */}
      <div className="relative backdrop-blur-lg bg-white/80 border-b border-white/20 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="relative">
                <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl blur opacity-75"></div>
                <div className="relative bg-gradient-to-r from-blue-600 to-purple-600 p-3 rounded-xl">
                  <Home className="h-8 w-8 text-white" />
                </div>
              </div>
              <div>
                <h1 className="text-4xl font-bold bg-gradient-to-r from-slate-900 via-blue-900 to-slate-900 bg-clip-text text-transparent">
                  PropertyValuer
                </h1>
                <p className="text-lg text-slate-600 font-medium">
                  Professional Real Estate Valuation Platform
                </p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-6">
              <div className="text-right">
                <div className="text-sm font-semibold text-slate-500 uppercase tracking-wide">
                  Trusted by
                </div>
                <div className="text-lg font-bold text-slate-700">
                  10,000+ Agents
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
          {/* Prediction Form */}
          <div className="lg:col-span-2 relative flex flex-col">
            <div className="relative">
              <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 rounded-2xl blur opacity-25"></div>
              <Card className="relative backdrop-blur-xl bg-white/90 border-0 shadow-2xl rounded-2xl overflow-hidden flex-1">
                {/* Premium Header */}
                <div className="relative bg-gradient-to-r from-slate-900 via-blue-900 to-slate-900 text-white">
                  <div className="absolute inset-0 bg-black/20"></div>
                  <CardHeader className="relative z-10 pb-8 pt-8">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-3">
                        <div className="p-2 bg-white/20 rounded-lg backdrop-blur-sm">
                          <Calculator className="h-6 w-6 text-white" />
                        </div>
                        <div>
                          <CardTitle className="text-2xl font-bold text-white">
                            Property Valuation
                          </CardTitle>
                          <CardDescription className="text-blue-100 text-base mt-1">
                            Professional-grade property assessment powered by
                            advanced algorithms
                          </CardDescription>
                        </div>
                      </div>
                      <div className="hidden sm:flex items-center space-x-2 bg-white/10 rounded-lg px-3 py-2 backdrop-blur-sm">
                        <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                        <span className="text-sm font-medium text-white">
                          Demo
                        </span>
                      </div>
                    </div>
                  </CardHeader>
                </div>

                <CardContent className="p-8 space-y-8">
                  {/* Property Specifications */}
                  <div className="space-y-6">
                    <div className="flex items-center space-x-2">
                      <div className="w-1 h-6 bg-gradient-to-b from-blue-500 to-purple-500 rounded-full"></div>
                      <Label className="text-lg font-semibold text-slate-800">
                        Property Specifications
                      </Label>
                    </div>

                    {/* Bedrooms and Bathrooms Row */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-3">
                        <Label className="text-sm font-medium text-slate-700">
                          Bedrooms
                        </Label>
                        <div className="grid grid-cols-3 gap-2">
                          {[1, 2, 3, 4, 5, 6].map((num) => (
                            <button
                              key={num}
                              type="button"
                              onClick={() =>
                                handleInputChange("Bedrooms", num.toString())
                              }
                              className={`py-3 px-4 rounded-lg font-medium transition-all ${
                                formData.Bedrooms === num.toString()
                                  ? "bg-blue-500 text-white shadow-lg"
                                  : "bg-gray-100 text-gray-700 hover:bg-gray-200"
                              }`}
                            >
                              {num}
                            </button>
                          ))}
                        </div>
                      </div>

                      <div className="space-y-3">
                        <Label className="text-sm font-medium text-slate-700">
                          Bathrooms
                        </Label>
                        <div className="grid grid-cols-3 gap-2">
                          {[1, 2, 3, 4, 5].map((num) => (
                            <button
                              key={num}
                              type="button"
                              onClick={() =>
                                handleInputChange("Bathrooms", num.toString())
                              }
                              className={`py-3 px-4 rounded-lg font-medium transition-all ${
                                formData.Bathrooms === num.toString()
                                  ? "bg-blue-500 text-white shadow-lg"
                                  : "bg-gray-100 text-gray-700 hover:bg-gray-200"
                              }`}
                            >
                              {num}
                            </button>
                          ))}
                        </div>
                      </div>
                    </div>

                    {/* Size and Year Built Row */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-3">
                        <Label
                          htmlFor="Size_sqft"
                          className="text-sm font-medium text-slate-700 flex items-center space-x-2"
                        >
                          <span>Property Size</span>
                          <span className="text-red-500">*</span>
                        </Label>
                        <div className="relative">
                          <Input
                            id="Size_sqft"
                            type="number"
                            placeholder="Enter square footage"
                            value={formData.Size_sqft}
                            onChange={(e) =>
                              handleInputChange("Size_sqft", e.target.value)
                            }
                            className="text-lg pl-4 pr-20 py-3 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all"
                          />
                          <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-sm font-medium text-slate-500 bg-slate-100 px-2 py-1 rounded">
                            sq ft
                          </div>
                        </div>
                      </div>

                      <div className="space-y-3">
                        <Label
                          htmlFor="YearBuilt"
                          className="text-sm font-medium text-slate-700 flex items-center space-x-2"
                        >
                          <span>Year Built</span>
                          <span className="text-red-500">*</span>
                        </Label>
                        <Input
                          id="YearBuilt"
                          type="number"
                          placeholder="e.g., 2015"
                          min="1900"
                          max={new Date().getFullYear()}
                          value={formData.YearBuilt}
                          onChange={(e) =>
                            handleInputChange("YearBuilt", e.target.value)
                          }
                          className="text-lg px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all"
                        />
                      </div>
                    </div>

                    {/* Location and Predictor Row */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div className="space-y-3">
                        <Label className="text-sm font-medium text-slate-700 flex items-center space-x-2">
                          <span>Location</span>
                          <span className="text-red-500">*</span>
                        </Label>
                        <Select
                          value={formData.Location}
                          onValueChange={(value) =>
                            handleInputChange("Location", value)
                          }
                        >
                          <SelectTrigger className="text-lg px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all">
                            <SelectValue />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="City">City</SelectItem>
                            <SelectItem value="Suburb">Suburb</SelectItem>
                            <SelectItem value="Rural">Rural</SelectItem>
                          </SelectContent>
                        </Select>
                      </div>

                      <div className="space-y-3">
                        <Label className="text-sm font-medium text-slate-700">
                          Predictor Selection
                        </Label>
                        <Select
                          value={formData.selectedPredictor}
                          onValueChange={(value) =>
                            handleInputChange("selectedPredictor", value)
                          }
                        >
                          <SelectTrigger className="text-lg px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 transition-all">
                            <SelectValue />
                          </SelectTrigger>
                          <SelectContent>
                            <SelectItem value="predictor-1">
                              Predictor-1
                            </SelectItem>
                            <SelectItem value="Predictor 2">
                              Predictor 2
                            </SelectItem>
                          </SelectContent>
                        </Select>
                      </div>
                    </div>
                  </div>

                  {error && (
                    <div className="relative overflow-hidden bg-gradient-to-r from-red-50 to-pink-50 border border-red-200 rounded-xl p-4">
                      <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-red-400 to-pink-400"></div>
                      <div className="flex items-center space-x-3">
                        <div className="p-2 bg-red-100 rounded-lg">
                          <span className="text-red-600 text-sm">⚠️</span>
                        </div>
                        <p className="text-red-700 font-medium">{error}</p>
                      </div>
                    </div>
                  )}

                  {/* Premium Submit Button */}
                  <div className="pt-4">
                    <button
                      onClick={handlePredict}
                      disabled={loading}
                      className="group relative w-full overflow-hidden bg-gradient-to-r from-slate-900 via-blue-900 to-slate-900 text-white font-semibold py-4 px-8 rounded-xl transition-all duration-300 transform hover:scale-[1.02] hover:shadow-2xl disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                    >
                      {/* Button Background Effect */}
                      <div className="absolute inset-0 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

                      {/* Button Content */}
                      <div className="relative z-10 flex items-center justify-center space-x-3">
                        {loading ? (
                          <>
                            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                            <span className="text-lg">
                              Analyzing Property...
                            </span>
                          </>
                        ) : (
                          <>
                            <TrendingUp className="h-6 w-6 transition-transform group-hover:scale-110" />
                            <span className="text-lg">
                              Get Professional Valuation
                            </span>
                            <div className="ml-2 bg-white/20 px-2 py-1 rounded text-sm">
                              Demo
                            </div>
                          </>
                        )}
                      </div>

                      {/* Shine Effect */}
                      <div className="absolute inset-0 -top-1 -left-1 bg-gradient-to-r from-transparent via-white/20 to-transparent skew-x-12 -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
                    </button>

                    {/* Trust Indicators */}
                    <div className="flex items-center justify-center space-x-6 mt-4 text-sm text-slate-500">
                      <div className="flex items-center space-x-1">
                        <span>🔒</span>
                        <span>Secure</span>
                      </div>
                      <div className="flex items-center space-x-1">
                        <span>⚡</span>
                        <span>Instant</span>
                      </div>
                      <div className="flex items-center space-x-1">
                        <span>✅</span>
                        <span>Accurate</span>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>

          {/* Results Panel */}
          <div className="space-y-8">
            {/* Prediction Results */}
            {prediction && (
              <div className="relative">
                <div className="absolute -inset-1 bg-gradient-to-r from-emerald-600 via-green-600 to-teal-600 rounded-2xl blur opacity-25"></div>
                <Card className="relative backdrop-blur-xl bg-white/95 border-0 shadow-2xl rounded-2xl overflow-hidden">
                  {/* Premium Results Header */}
                  <div className="relative bg-gradient-to-r from-emerald-900 via-green-900 to-teal-900 text-white">
                    <div className="absolute inset-0 bg-black/10"></div>
                    <CardHeader className="relative z-10 pb-6 pt-6">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center space-x-3">
                          <div className="p-2 bg-white/20 rounded-lg backdrop-blur-sm">
                            <Star className="h-6 w-6 text-white" />
                          </div>
                          <div>
                            <CardTitle className="text-2xl font-bold text-white">
                              Property Valuation
                            </CardTitle>
                            <div className="text-emerald-100 text-sm mt-1">
                              {getPredictorLabel()} Analysis
                            </div>
                          </div>
                        </div>
                        <div className="bg-white/10 rounded-lg px-3 py-2 backdrop-blur-sm">
                          <span className="text-sm font-medium text-white">
                            Demo Report
                          </span>
                        </div>
                      </div>
                    </CardHeader>
                  </div>

                  <CardContent className="p-8 space-y-6">
                    {/* Main Price Display */}
                    <div className="text-center bg-gradient-to-br from-slate-50 to-blue-50 rounded-2xl p-6 border border-slate-200">
                      <div className="text-5xl font-bold bg-gradient-to-r from-emerald-600 to-green-600 bg-clip-text text-transparent mb-3">
                        {getPrimaryPrediction()}
                      </div>
                      <div className="flex items-center justify-center space-x-2">
                        <Badge className="bg-emerald-100 text-emerald-800 border-emerald-200 px-3 py-1">
                          {getPredictorLabel()} Result
                        </Badge>
                        <div className="text-sm text-slate-500">•</div>
                        <div className="text-sm text-slate-600">
                          Market Value
                        </div>
                      </div>
                    </div>

                    {/* Model Information */}
                    <div className="space-y-4">
                      <div className="flex items-center space-x-2">
                        <div className="w-1 h-5 bg-gradient-to-b from-emerald-500 to-green-500 rounded-full"></div>
                        <h4 className="font-semibold text-slate-800">
                          Model Information
                        </h4>
                      </div>

                      <div className="flex items-center justify-between p-4 bg-slate-50 rounded-xl border border-slate-200">
                        <div className="flex items-center space-x-3">
                          <div className="w-3 h-3 rounded-full bg-blue-500"></div>
                          <div>
                            <div className="font-medium text-slate-800">
                              {formData.selectedPredictor === "predictor-1"
                                ? "Linear Regression"
                                : "Random Forest"}
                            </div>
                            <div className="text-sm text-slate-500">
                              {formData.selectedPredictor === "predictor-1"
                                ? "Standard Analysis Model"
                                : "Advanced AI Model"}
                            </div>
                          </div>
                        </div>
                        <div className="text-right">
                          <div className="font-bold text-slate-900 text-lg">
                            {getPrimaryPrediction()}
                          </div>
                          <div className="text-sm text-slate-500">
                            Predicted Value
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Property Summary */}
                    <div className="space-y-4">
                      <div className="flex items-center space-x-2">
                        <div className="w-1 h-5 bg-gradient-to-b from-blue-500 to-purple-500 rounded-full"></div>
                        <h4 className="font-semibold text-slate-800">
                          Property Summary
                        </h4>
                      </div>

                      <div className="grid grid-cols-2 gap-4">
                        <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-4 border border-blue-200">
                          <div className="text-2xl font-bold text-blue-900">
                            {formData.Size_sqft}
                          </div>
                          <div className="text-sm text-blue-600 font-medium">
                            Square Feet
                          </div>
                        </div>
                        <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-4 border border-purple-200">
                          <div className="text-2xl font-bold text-purple-900">
                            {formData.Bedrooms}bd • {formData.Bathrooms}ba
                          </div>
                          <div className="text-sm text-purple-600 font-medium">
                            Bedrooms • Bathrooms
                          </div>
                        </div>
                        <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl p-4 border border-green-200">
                          <div className="text-lg font-bold text-green-900 truncate">
                            {formData.Location}
                          </div>
                          <div className="text-sm text-green-600 font-medium">
                            Location
                          </div>
                        </div>
                        <div className="bg-gradient-to-br from-orange-50 to-amber-50 rounded-xl p-4 border border-orange-200">
                          <div className="text-2xl font-bold text-orange-900">
                            {formData.YearBuilt}
                          </div>
                          <div className="text-sm text-orange-600 font-medium">
                            Year Built
                          </div>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            )}

            {/* Model Performance - Only show before prediction */}
            {!prediction && (
              <div className="relative flex flex-col">
                <div className="absolute -inset-1 bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 rounded-2xl blur opacity-25"></div>
                <Card className="relative backdrop-blur-xl bg-white/95 border-0 shadow-2xl rounded-2xl overflow-hidden flex-1">
                  <div className="relative bg-gradient-to-r from-slate-900 via-indigo-900 to-slate-900 text-white">
                    <div className="absolute inset-0 bg-black/10"></div>
                    <CardHeader className="relative z-10 pb-6 pt-6">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center space-x-3">
                          <div className="p-2 bg-white/20 rounded-lg backdrop-blur-sm">
                            <BarChart3 className="h-6 w-6 text-white" />
                          </div>
                          <div>
                            <CardTitle className="text-2xl font-bold text-white">
                              Performance Analytics
                            </CardTitle>
                            <div className="text-indigo-100 text-sm mt-1">
                              Model accuracy and reliability metrics
                            </div>
                          </div>
                        </div>
                        <Badge className="bg-green-100 text-green-800">
                          Demo Active
                        </Badge>
                      </div>
                    </CardHeader>
                  </div>

                  <CardContent className="p-8 space-y-6 flex-1 flex flex-col">
                    {/* Performance Metrics */}
                    <div className="grid gap-4">
                      <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
                        <div className="flex items-center justify-between mb-4">
                          <div className="flex items-center space-x-2">
                            <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
                            <span className="font-semibold text-blue-900">
                              Standard Analysis
                            </span>
                          </div>
                          <span className="text-2xl font-bold text-blue-900">
                            {(
                              mockModelInfo.metrics.linear_regression.r2_score *
                              100
                            ).toFixed(1)}
                            %
                          </span>
                        </div>
                        <Progress
                          value={
                            mockModelInfo.metrics.linear_regression.r2_score *
                            100
                          }
                          className="h-3 bg-blue-200"
                        />
                        <div className="mt-2 text-sm text-blue-600">
                          R² Score • Linear Regression Model
                        </div>
                      </div>

                      <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-200">
                        <div className="flex items-center justify-between mb-4">
                          <div className="flex items-center space-x-2">
                            <div className="w-3 h-3 bg-purple-500 rounded-full"></div>
                            <span className="font-semibold text-purple-900">
                              Advanced AI Model
                            </span>
                          </div>
                          <span className="text-2xl font-bold text-purple-900">
                            {(
                              mockModelInfo.metrics.random_forest.r2_score * 100
                            ).toFixed(1)}
                            %
                          </span>
                        </div>
                        <Progress
                          value={
                            mockModelInfo.metrics.random_forest.r2_score * 100
                          }
                          className="h-3 bg-purple-200"
                        />
                        <div className="mt-2 text-sm text-purple-600">
                          R² Score • Random Forest Algorithm
                        </div>
                      </div>
                    </div>

                    {/* Best Model Indicator */}
                    <div className="bg-gradient-to-r from-emerald-50 to-green-50 rounded-xl p-4 border border-emerald-200">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center space-x-3">
                          <div className="p-2 bg-emerald-100 rounded-lg">
                            <span className="text-emerald-600">🏆</span>
                          </div>
                          <div>
                            <div className="font-semibold text-emerald-900">
                              Recommended Model
                            </div>
                            <div className="text-sm text-emerald-600">
                              {mockModelInfo.metrics.best_model}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Error Metrics */}
                    <div className="grid grid-cols-2 gap-4 mt-auto">
                      <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 text-center">
                        <div className="text-2xl font-bold text-slate-900">
                          $
                          {mockModelInfo.metrics.linear_regression.mae.toLocaleString()}
                        </div>
                        <div className="text-sm text-slate-600 font-medium">
                          Linear Regression MAE
                        </div>
                      </div>
                      <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 text-center">
                        <div className="text-2xl font-bold text-slate-900">
                          $
                          {mockModelInfo.metrics.random_forest.mae.toLocaleString()}
                        </div>
                        <div className="text-sm text-slate-600 font-medium">
                          Random Forest MAE
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
