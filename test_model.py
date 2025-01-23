import numpy as np
import pandas as pd
import joblib
from keras.models import load_model

# Load the pre-trained model and preprocessor
model_path = 'dietary_risk_ann_model.h5'
preprocessor_path = 'preprocessor.pkl'

model = load_model(model_path)
preprocessor = joblib.load(preprocessor_path)

# Sample input array (replace with actual input data)
# Example input: [Age, Gender, Hormone_Level, BMI, Activity_Level, Dietary_Pattern, Life_Stage, Follow_Up_Time]
input_array = np.array(
    [[45, 'Male', 1.0, 50.5, 'High', 'Vegetarian', 'Middle-aged', 4]])

# Preprocess the input data
input_transformed = preprocessor.transform(pd.DataFrame(input_array, columns=[
                                           'Age', 'Gender', 'Hormone_Level', 'BMI', 'Activity_Level', 'Dietary_Pattern', 'Life_Stage', 'Follow_Up_Time']))

# Predict using the trained model
prediction = model.predict(input_transformed)

# Output the prediction
# If probability is > 0.5, it's likely 1 (event), else 0 (no event)
dietary_risk_event = prediction[0][0]
print(f'Dietary Risk Event Prediction: {dietary_risk_event}')
