import pandas as pd
import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from utils.evaluation import evaluate_model
from utils.visualize import visualize_relationships

# Load data
df = pd.read_excel("./data/House_price_data.xlsx")

# Visualize data
visualize_relationships(df, target_col='Price_Lakh(INR)')

# Features and target
X = df.drop("Price_Lakh(INR)", axis=1)
y = df["Price_Lakh(INR)"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Columns
poly_cols = ['Size_sqft']  # Only apply Polynomial to Size
pass_through = ['Bedrooms', 'Location_Score']

# Preprocessing
preprocessor = ColumnTransformer([
    ("poly_size", Pipeline([
        ("scaler", StandardScaler()),
        ("poly", PolynomialFeatures(degree=2, include_bias=False))
    ]), poly_cols),
    ("pass", StandardScaler(), pass_through)
])

# Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Evaluate
mae, mse, rmse, r2 = evaluate_model(y_test, y_pred)
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/polynomial_pipeline.pkl")
