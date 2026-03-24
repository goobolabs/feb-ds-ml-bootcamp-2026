'use client'

import { useState, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Progress } from '@/components/ui/progress'
import { BarChart3, TrendingUp, Activity } from 'lucide-react'

interface ModelMetrics {
  linear_regression: {
    r2_score: number
    mse: number
    mae: number
  }
  random_forest: {
    r2_score: number
    mse: number
    mae: number
  }
  best_model: string
}

interface FeatureImportance {
  feature: string
  importance: number
}

interface ModelInfoProps {
  modelInfo?: {
    metrics: ModelMetrics
    feature_importance: FeatureImportance[]
    success: boolean
  } | null
}

export default function ModelInfo({ modelInfo }: ModelInfoProps) {
  const [healthStatus, setHealthStatus] = useState<'healthy' | 'unhealthy' | 'loading'>('loading')

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch('http://localhost:8080/api/health')
        if (response.ok) {
          const data = await response.json()
          setHealthStatus(data.models_loaded ? 'healthy' : 'unhealthy')
        } else {
          setHealthStatus('unhealthy')
        }
      } catch {
        setHealthStatus('unhealthy')
      }
    }

    checkHealth()
    const interval = setInterval(checkHealth, 30000) // Check every 30 seconds
    return () => clearInterval(interval)
  }, [])

  const getHealthColor = () => {
    switch (healthStatus) {
      case 'healthy': return 'bg-green-100 text-green-800'
      case 'unhealthy': return 'bg-red-100 text-red-800'
      default: return 'bg-gray-100 text-gray-800'
    }
  }

  const getHealthText = () => {
    switch (healthStatus) {
      case 'healthy': return 'Models Loaded'
      case 'unhealthy': return 'Backend Offline'
      default: return 'Checking...'
    }
  }

  if (!modelInfo) {
    return (
      <div className="relative">
        <div className="absolute -inset-1 bg-gradient-to-r from-indigo-600 via-blue-600 to-purple-600 rounded-2xl blur opacity-25"></div>
        <Card className="relative backdrop-blur-xl bg-white/95 border-0 shadow-2xl rounded-2xl overflow-hidden">
          <div className="relative bg-gradient-to-r from-slate-900 via-indigo-900 to-slate-900 text-white">
            <div className="absolute inset-0 bg-black/10"></div>
            <CardHeader className="relative z-10 pb-6 pt-6">
              <CardTitle className="flex items-center space-x-3">
                <div className="p-2 bg-white/20 rounded-lg backdrop-blur-sm">
                  <Activity className="h-6 w-6 text-white" />
                </div>
                <div>
                  <div className="text-2xl font-bold text-white">System Status</div>
                  <div className="text-indigo-100 text-sm mt-1">Real-time monitoring</div>
                </div>
              </CardTitle>
            </CardHeader>
          </div>
          <CardContent className="p-8">
            <div className="flex items-center justify-between p-4 bg-slate-50 rounded-xl border border-slate-200">
              <div className="flex items-center space-x-3">
                <div className="p-2 bg-blue-100 rounded-lg">
                  <span className="text-blue-600">🖥️</span>
                </div>
                <div>
                  <div className="font-semibold text-slate-800">Backend Service</div>
                  <div className="text-sm text-slate-500">API connectivity status</div>
                </div>
              </div>
              <Badge className={getHealthColor()}>
                {getHealthText()}
              </Badge>
            </div>
            {healthStatus === 'unhealthy' && (
              <div className="mt-6 bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-xl p-4">
                <div className="flex items-center space-x-3">
                  <div className="p-2 bg-amber-100 rounded-lg">
                    <span className="text-amber-600">⚠️</span>
                  </div>
                  <div>
                    <div className="font-semibold text-amber-900">Service Unavailable</div>
                    <p className="text-amber-700 text-sm mt-1">
                      Ensure the Flask backend is running on port 8080 to access advanced analytics.
                    </p>
                  </div>
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="space-y-8">
      {/* Model Performance */}
      <div className="relative">
        <div className="absolute -inset-1 bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 rounded-2xl blur opacity-25"></div>
        <Card className="relative backdrop-blur-xl bg-white/95 border-0 shadow-2xl rounded-2xl overflow-hidden">
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
                <Badge className={getHealthColor()}>
                  {getHealthText()}
                </Badge>
              </div>
            </CardHeader>
          </div>
          
          <CardContent className="p-8 space-y-6">
            {/* Performance Metrics */}
            <div className="grid gap-4">
              <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center space-x-2">
                    <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
                    <span className="font-semibold text-blue-900">Standard Analysis</span>
                  </div>
                  <span className="text-2xl font-bold text-blue-900">
                    {(modelInfo.metrics.linear_regression.r2_score * 100).toFixed(1)}%
                  </span>
                </div>
                <Progress value={modelInfo.metrics.linear_regression.r2_score * 100} className="h-3 bg-blue-200" />
                <div className="mt-2 text-sm text-blue-600">
                  R² Score • Linear Regression Model
                </div>
              </div>
              
              <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-6 border border-purple-200">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center space-x-2">
                    <div className="w-3 h-3 bg-purple-500 rounded-full"></div>
                    <span className="font-semibold text-purple-900">Advanced AI Model</span>
                  </div>
                  <span className="text-2xl font-bold text-purple-900">
                    {(modelInfo.metrics.random_forest.r2_score * 100).toFixed(1)}%
                  </span>
                </div>
                <Progress value={modelInfo.metrics.random_forest.r2_score * 100} className="h-3 bg-purple-200" />
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
                    <div className="font-semibold text-emerald-900">Recommended Model</div>
                    <div className="text-sm text-emerald-600">{modelInfo.metrics.best_model}</div>
                  </div>
                </div>
              </div>
            </div>

            {/* Error Metrics */}
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 text-center">
                <div className="text-2xl font-bold text-slate-900">
                  ${modelInfo.metrics.linear_regression.mae.toLocaleString()}
                </div>
                <div className="text-sm text-slate-600 font-medium">Standard MAE</div>
              </div>
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 text-center">
                <div className="text-2xl font-bold text-slate-900">
                  ${modelInfo.metrics.random_forest.mae.toLocaleString()}
                </div>
                <div className="text-sm text-slate-600 font-medium">Advanced MAE</div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Feature Importance */}
      {modelInfo.feature_importance && modelInfo.feature_importance.length > 0 && (
        <div className="relative">
          <div className="absolute -inset-1 bg-gradient-to-r from-green-600 via-emerald-600 to-teal-600 rounded-2xl blur opacity-25"></div>
          <Card className="relative backdrop-blur-xl bg-white/95 border-0 shadow-2xl rounded-2xl overflow-hidden">
            <div className="relative bg-gradient-to-r from-slate-900 via-emerald-900 to-slate-900 text-white">
              <div className="absolute inset-0 bg-black/10"></div>
              <CardHeader className="relative z-10 pb-6 pt-6">
                <CardTitle className="flex items-center space-x-3">
                  <div className="p-2 bg-white/20 rounded-lg backdrop-blur-sm">
                    <TrendingUp className="h-6 w-6 text-white" />
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-white">Feature Impact</div>
                    <div className="text-emerald-100 text-sm mt-1">
                      Key factors affecting property value
                    </div>
                  </div>
                </CardTitle>
              </CardHeader>
            </div>
            
            <CardContent className="p-8">
              <div className="space-y-4">
                {modelInfo.feature_importance.slice(0, 6).map((feature, index) => (
                  <div key={feature.feature} className="flex items-center justify-between p-4 bg-slate-50 rounded-xl border border-slate-200 hover:bg-slate-100 transition-colors">
                    <div className="flex items-center space-x-3">
                      <div className={`w-8 h-8 rounded-lg flex items-center justify-center text-white font-bold text-sm ${
                        index === 0 ? 'bg-emerald-500' :
                        index === 1 ? 'bg-blue-500' :
                        index === 2 ? 'bg-purple-500' :
                        index === 3 ? 'bg-pink-500' :
                        index === 4 ? 'bg-orange-500' : 'bg-gray-500'
                      }`}>
                        #{index + 1}
                      </div>
                      <div>
                        <div className="font-semibold text-slate-800 capitalize">
                          {feature.feature.replace(/[_]/g, ' ')}
                        </div>
                        <div className="text-sm text-slate-500">
                          Impact on property valuation
                        </div>
                      </div>
                    </div>
                    <div className="text-right">
                      <div className="text-xl font-bold text-slate-900">
                        {(feature.importance * 100).toFixed(1)}%
                      </div>
                      <div className="w-24 mt-1">
                        <Progress value={feature.importance * 100} className="h-2" />
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  )
}
