import joblib
import pandas as pd

# Load saved pipeline (includes scaler + polynomial features + regression model)
model = joblib.load("models/polynomial_pipeline.pkl")

# Example input for prediction
input_data = {
    'Size_sqft': [2100],
    'Bedrooms': [3],
    'Location_Score': [7]
}
input_df = pd.DataFrame(input_data)

# Direct prediction using the full pipeline
prediction = model.predict(input_df)

# Output
print(f"Predicted House Price: ₹{prediction[0]:,.2f} Lakh")
