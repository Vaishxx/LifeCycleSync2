import os
from flask import Flask, request, jsonify
import joblib
from keras.models import load_model
import numpy as np
import pandas as pd

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
        required_fields = [
            'Age', 'Hormone_Level', 'BMI', 'Follow_Up_Time',
            'Gender', 'Activity_Level', 'Dietary_Pattern', 'Life_Stage'
        ]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f"Missing fields in input data: {', '.join(missing_fields)}"}), 400

        features = [
            data['Age'],
            data['Hormone_Level'],
            data['BMI'],
            data['Follow_Up_Time'],
            data['Gender'],
            data['Activity_Level'],
            data['Dietary_Pattern'],
            data['Life_Stage']
        ]

        # Convert input to DataFrame
        input_data_df = pd.DataFrame([features], columns=required_fields)

        # Preprocess the input
        input_data_preprocessed = preprocessor.transform(input_data_df)

        # Make prediction
        prediction = model.predict(input_data_preprocessed)
        result = 'At Risk' if prediction[0][0] > 0.5 else 'Not at Risk'

        # Return the result
        return jsonify({'prediction': result, 'confidence': float(prediction[0][0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Get the port from environment variable (Render will set this)
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port, debug=False)  # Bind to 0.0.0.0 for external access
