# Crop Recommendation System

A modern web application that provides crop recommendations based on soil and climate conditions using machine learning.

## Features

- **Interactive Web Interface**: Beautiful, responsive UI
- **Machine Learning Model**: Uses RandomForest for accurate predictions
- **Real-time Predictions**: Get instant crop recommendations with confidence scores
- **Crop Information**: Detailed information about recommended crops

## Input Parameters

The system analyzes the following soil and climate parameters:

1. **Nitrogen (N)** - kg/ha (0-140)
2. **Phosphorus (P)** - kg/ha (5-145)
3. **Potassium (K)** - kg/ha (5-205)
4. **Temperature** - °C (8-44)
5. **Humidity** - % (14-100)
6. **pH Level** - (3.5-10)
7. **Rainfall** - mm (20-300)

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Deployment

### Railway Deployment (Recommended)

1. **Go to [railway.app](https://railway.app)**
2. **Sign up/Login with GitHub**
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Railway will automatically detect it's a Python app**
6. **Deploy with one click**

Your app will be live at: `https://your-app-name.railway.app`

## File Structure

```
crop-recommendation-system/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── requirements.txt       # Python dependencies
├── Procfile              # Railway configuration
└── README.md             # This file
```

## API Endpoints

- `GET /` - Main application page
- `POST /predict` - Get crop recommendation
- `GET /get_crop_info/<crop_name>` - Get information about a specific crop

## Technical Details

- **Backend**: Flask (Python)
- **Machine Learning**: RandomForest Classifier (scikit-learn)
- **Frontend**: Bootstrap 5 + Custom CSS
- **Deployment**: Railway (optimized)

## License

This project is open source and available under the MIT License. "# crop-recommendation" 
