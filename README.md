# LifeCycleSync  API

This README provides guidance on using the **LifeCycleSync API**, which predicts dietary health risk based on user input data.

## Overview
The API uses a trained Artificial Neural Network (ANN) model to predict dietary risk based on specific user features such as age, hormone levels, BMI, activity level, and dietary patterns. The `/predict` endpoint accepts user details in JSON format and returns the risk classification along with confidence scores.

---

## API Endpoints

### **1. Home Endpoint**

- **URL:** `/`
- **Method:** `GET`
- **Purpose:** Test the API connectivity.
- **Response:**
  ```
  "Welcome to the Dietary Risk Prediction API!"
  ```

---

### **2. Predict Endpoint**

- **URL:** `/predict`
- **Method:** `POST`
- **Purpose:** Predict dietary risk based on user input.
- **Headers:**
  ```json
  {
      "Content-Type": "application/json"
  }
  ```
- **Body:** JSON formatted user details (see below).
- **Response:**
  ```json
  {
      "prediction": "At Risk",
      "confidence": 0.87
  }
  ```

---

## Input JSON Format

The `/predict` endpoint requires the following fields in the JSON body:

| Field             | Type     | Description                                    | Example          |
|-------------------|----------|------------------------------------------------|------------------|
| `Age`             | Integer  | Age of the individual                         | 55               |
| `Hormone_Level`   | Float    | Hormone level measurement                     | 1.03             |
| `BMI`             | Float    | Body Mass Index                               | 26.72            |
| `Follow_Up_Time`  | Integer  | Follow-up period in months                    | 6                |
| `Gender`          | String   | Gender of the individual (`Male`/`Female`)    | Male             |
| `Activity_Level`  | String   | Physical activity level (`High`, `Moderate`, `Low`) | High         |
| `Dietary_Pattern` | String   | Dietary preference (`Vegetarian`, `Non-Vegetarian`, `Vegan`) | Vegetarian |
| `Life_Stage`      | String   | Life stage of the individual (`Adolescent`, `Young Adult`, `Middle-aged`) | Middle-aged |

### Example Input JSON
```json
{
    "Age": 55,
    "Hormone_Level": 1.03,
    "BMI": 26.72,
    "Follow_Up_Time": 6,
    "Gender": "Male",
    "Activity_Level": "High",
    "Dietary_Pattern": "Vegetarian",
    "Life_Stage": "Middle-aged"
}
```

---

## Response Format

The response contains the following fields:

| Field         | Type   | Description                            | Example      |
|---------------|--------|----------------------------------------|--------------|
| `prediction`  | String | Risk prediction (`At Risk`/`Not at Risk`) | At Risk      |
| `confidence`  | Float  | Confidence score for the prediction     | 0.87         |

### Example Response
```json
{
    "prediction": "At Risk",
    "confidence": 0.87
}
```

---

## Error Handling

If there is an error in the request (e.g., missing fields, invalid data types), the API returns an error response with status code `400` and the error message.

### Example Error Response
```json
{
    "error": "BMI is missing in the input JSON."
}
```

---

## How to Test

### Using Postman
1. Open Postman and create a new request.
2. Set the method to `POST` and the URL to `http://<host>:5000/predict`.
3. Add the following header:
   ```json
   {
       "Content-Type": "application/json"
   }
   ```
4. Include a valid JSON body based on the input format.
5. Send the request and check the response.

### Using cURL
**Command:**
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
    "Age": 55,
    "Hormone_Level": 1.03,
    "BMI": 26.72,
    "Follow_Up_Time": 6,
    "Gender": "Male",
    "Activity_Level": "High",
    "Dietary_Pattern": "Vegetarian",
    "Life_Stage": "Middle-aged"
}'
```

---

## Notes
- Replace `<host>` with the actual server host (e.g., `127.0.0.1` for local testing).
- Ensure the model and preprocessor files (`dietary_risk_ann_model.h5` and `preprocessor.pkl`) are correctly loaded and accessible by the Flask app.

For further assistance, please contact the development team.






