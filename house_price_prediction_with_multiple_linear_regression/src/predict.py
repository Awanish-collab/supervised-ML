import joblib
import pandas as pd

def predict_price(size, location_score, bedrooms):
    model = joblib.load("models/model.pkl")
    # Use DataFrame with column name same as training data
    input_data = pd.DataFrame([[size, location_score, bedrooms]], columns=["Size_sqft", "Location_Score", "Bedrooms"])
    prediction = model.predict(input_data)

    return round(prediction[0], 2)

if __name__ == "__main__":
    size = float(input("Enter house size (sqft): "))
    location_score = float(input("Enter location score (1-10): "))
    bedrooms = int(input("Enter number of bedrooms: "))

    predicted_price = predict_price(size, location_score, bedrooms)
    print(f"Predicted House Price: ₹ {predicted_price} Lakh")
