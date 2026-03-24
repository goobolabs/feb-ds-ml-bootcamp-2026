# 🏠 House Price Predictor - Frontend

A modern Next.js 15 frontend application for house price prediction with updated input features and multiple predictor models.

## ✨ Updated Features

### 🔄 **New Input Structure:**
- **Size** - House size in square feet
- **Bedrooms** - Number of bedrooms (1-6)
- **Bathrooms** - Number of bathrooms (1-5)
- **Location** - Property location (text input)
- **Year Built** - Construction year (1900-2024)

### 🤖 **Predictor Selection:**
- **Predictor-1** - Linear Regression Model 🤖
- **Predictor 2** - Random Forest Model 🌲
- **Predictor-3** - Ensemble Average Model ⚡

### 🎨 **UI Enhancements:**
- **Streamlined Form** - Simplified 5-field input structure
- **Predictor Selection** - Choose your preferred prediction model
- **Real-time Validation** - Instant feedback on required fields
- **Enhanced Results** - Shows selected predictor prominently
- **Input Summary** - Displays all entered features in results

## 🚀 Quick Start

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## 📊 Input Examples

### Example 1: Urban Apartment
- **Size**: 1200 sq ft
- **Bedrooms**: 2
- **Bathrooms**: 2
- **Location**: Downtown
- **Year Built**: 2015

### Example 2: Suburban House
- **Size**: 2500 sq ft
- **Bedrooms**: 4
- **Bathrooms**: 3
- **Location**: Suburb
- **Year Built**: 2010

### Example 3: Rural Property
- **Size**: 3000 sq ft
- **Bedrooms**: 3
- **Bathrooms**: 2
- **Location**: Rural
- **Year Built**: 1995

## 🎯 Predictor Models

### 🤖 Predictor-1 (Linear Regression)
- **Conservative estimates**
- **Fast predictions**
- **Simple linear relationships**
- **Good for baseline estimates**

### 🌲 Predictor 2 (Random Forest)
- **More complex patterns**
- **Higher accuracy potential**
- **Handles non-linear relationships**
- **Feature interaction modeling**

### ⚡ Predictor-3 (Ensemble Average)
- **Combines both models**
- **Balanced predictions**
- **Reduces individual model bias**
- **Most robust option**

## 🔗 API Integration

The frontend communicates with the Flask backend at `http://localhost:8080/api/predict` using the new input structure:

```json
{
  "size": 2500,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "Suburb",
  "yearBuilt": 2010,
  "selectedPredictor": "predictor-3"
}
```

## 🛠️ Tech Stack

- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **shadcn/ui** - Modern UI components
- **Lucide React** - Beautiful icons

## 📱 Responsive Design

The application is fully responsive and works seamlessly across:
- **Desktop** (1024px+)
- **Tablet** (768px - 1023px)
- **Mobile** (320px - 767px)

## 🎨 Design Features

- **Glass Morphism** - Modern translucent cards
- **Gradient Backgrounds** - Beautiful color transitions
- **Smooth Animations** - Loading states and transitions
- **Intuitive Controls** - Easy-to-use form inputs
- **Visual Feedback** - Clear success and error states