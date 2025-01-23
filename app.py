from flask import Flask, request, jsonify
import joblib
from keras.models import load_model
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and preprocessor
model = load_model('dietary_risk_ann_model.h5')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/')
def home():
    return "Welcome to the Dietary Risk Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input JSON data
        data = request.get_json()

        # Extract features
        features = [
            data.get('Age'),
            data.get('Hormone_Level'),
            data.get('BMI'),
            data.get('Follow_Up_Time'),
            data.get('Gender'),
            data.get('Activity_Level'),
            data.get('Dietary_Pattern'),
            data.get('Life_Stage')
        ]

        # Preprocess the input
        input_data = [features]
        input_data_preprocessed = preprocessor.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_preprocessed)
        result = 'At Risk' if prediction[0][0] > 0.5 else 'Not at Risk'

        # Return the result
        return jsonify({'prediction': result, 'confidence': float(prediction[0][0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if name == "main":
    app.run(host='0.0.0.0', port=5000)
