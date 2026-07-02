from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

app = Flask(__name__)

# Global variables for the model
model = None

def train_model():
    """Train the model with sample data"""
    global model
    
    print("Training RandomForest model...")
    
    # Create sample data
    np.random.seed(42)
    n_samples = 500
    
    # Generate sample data
    data = {
        'N': np.random.randint(0, 140, n_samples),
        'P': np.random.randint(5, 145, n_samples),
        'K': np.random.randint(5, 205, n_samples),
        'temperature': np.random.uniform(8.0, 44.0, n_samples),
        'humidity': np.random.uniform(14.0, 100.0, n_samples),
        'ph': np.random.uniform(3.5, 10.0, n_samples),
        'rainfall': np.random.uniform(20.0, 300.0, n_samples)
    }
    
    # Create sample crop labels
    crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 
             'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
             'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
             'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
    
    data['crop'] = np.random.choice(crops, n_samples)
    
    df = pd.DataFrame(data)
    
    # Prepare features and target
    X = df.drop('crop', axis=1)
    y = df['crop']
    
    # Train RandomForest model ONLY
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=1)
    model.fit(X, y)
    
    print(f"RandomForest model trained successfully with {len(model.estimators_)} trees")
    
    # Save the model
    with open('crop_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("RandomForest model saved successfully")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        data = request.get_json()
        
        # Extract features
        features = [
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]
        
        # Make prediction
        if model is not None:
            # Convert to numpy array with proper shape
            features_array = np.array(features).reshape(1, -1)
            
            prediction = model.predict(features_array)[0]
            probability = model.predict_proba(features_array)[0]
            max_prob = max(probability)
            
            return jsonify({
                'success': True,
                'prediction': prediction,
                'confidence': round(max_prob * 100, 2),
                'all_probabilities': dict(zip(model.classes_, [round(p * 100, 2) for p in probability]))
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Model not loaded'
            })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/get_crop_info/<crop_name>')
def get_crop_info(crop_name):
    """Return information about a specific crop"""
    crop_info = {
        'rice': {
            'description': 'Rice is a cereal grain and the most important staple food for a large part of the world population.',
            'optimal_conditions': 'Warm climate, high humidity, plenty of water',
            'growing_season': '3-6 months',
            'water_requirement': 'High'
        },
        'maize': {
            'description': 'Maize (corn) is a cereal grain first domesticated by indigenous peoples in Mexico.',
            'optimal_conditions': 'Warm climate, moderate rainfall, well-drained soil',
            'growing_season': '3-4 months',
            'water_requirement': 'Moderate'
        },
        'chickpea': {
            'description': 'Chickpea is a legume that is rich in protein and fiber.',
            'optimal_conditions': 'Cool to warm climate, moderate rainfall',
            'growing_season': '3-5 months',
            'water_requirement': 'Low to moderate'
        },
        'cotton': {
            'description': 'Cotton is a soft, fluffy staple fiber that grows in a boll around the seeds of cotton plants.',
            'optimal_conditions': 'Warm climate, moderate rainfall, well-drained soil',
            'growing_season': '5-6 months',
            'water_requirement': 'Moderate'
        },
        'jute': {
            'description': 'Jute is a long, soft, shiny vegetable fiber that can be spun into coarse, strong threads.',
            'optimal_conditions': 'Warm and humid climate, plenty of water',
            'growing_season': '4-5 months',
            'water_requirement': 'High'
        },
        'coffee': {
            'description': 'Coffee is a brewed drink prepared from roasted coffee beans.',
            'optimal_conditions': 'Tropical climate, moderate rainfall, well-drained soil',
            'growing_season': '3-4 years to first harvest',
            'water_requirement': 'Moderate'
        }
    }
    
    return jsonify(crop_info.get(crop_name.lower(), {
        'description': 'Information not available for this crop.',
        'optimal_conditions': 'Please consult agricultural resources.',
        'growing_season': 'Varies by crop type.',
        'water_requirement': 'Varies by crop type.'
    }))

# Initialize model - ALWAYS train new RandomForest model
if __name__ == '__main__':
    train_model()
    
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
else:
    # For Railway deployment - ALWAYS train new RandomForest model
    train_model() 