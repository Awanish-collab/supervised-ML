import joblib
import numpy as np

def predict_price(size_sqft):
    model = joblib.load("models/model.pkl")
    input_data = np.array([[size_sqft]])
    prediction = model.predict(input_data)
    return round(prediction[0], 2)

if __name__ == "__main__":
    user_input = float(input("Enter house size in sqft: "))
    price = predict_price(user_input)
    print(f"Predicted Price: ₹ {price} Lakh")
