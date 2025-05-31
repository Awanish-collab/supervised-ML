import joblib
import pandas as pd

def predict_price(size_sqft):
    model = joblib.load("models/model.pkl")
    # Use DataFrame with column name same as training data
    input_data = pd.DataFrame([[size_sqft]], columns=["Size_sqft"])
    prediction = model.predict(input_data)
    return round(prediction[0], 2)

if __name__ == "__main__":
    user_input = float(input("Enter house size in sqft: "))
    price = predict_price(user_input)
    print(f"Predicted Price: ₹ {price} Lakh")
