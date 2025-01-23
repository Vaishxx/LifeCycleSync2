import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import joblib

# Load the data (assuming this will be used with an input array)
file_path = 'LifeCycleSync_AI_Model_Dataset_30k_Final.csv'
data = pd.read_csv(file_path)

# Drop 'User_ID' column
data = data.drop('User_ID', axis=1)

# Preprocessing
# Define preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), [
         'Age', 'Hormone_Level', 'BMI', 'Follow_Up_Time']),
        ('cat', OneHotEncoder(), [
         'Gender', 'Activity_Level', 'Dietary_Pattern', 'Life_Stage'])
    ],
    remainder='passthrough'
)

# Prepare features and target
X = data.drop('Dietary_Risk_Event', axis=1)
y = data['Dietary_Risk_Event']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Apply preprocessing to training and test sets
X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)

# Create ANN Model
model = Sequential()
model.add(
    Dense(64, input_dim=X_train_preprocessed.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
# Output layer with sigmoid for binary classification
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train_preprocessed, y_train, epochs=20,
          batch_size=32, validation_split=0.2)

# Save the model and preprocessor
model_path = 'dietary_risk_ann_model.h5'
preprocessor_path = 'preprocessor.pkl'
model.save(model_path)
joblib.dump(preprocessor, preprocessor_path)

print("Model trained and saved successfully.")
