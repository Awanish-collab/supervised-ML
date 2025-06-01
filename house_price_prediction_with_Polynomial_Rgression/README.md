# 🏠 House Price Prediction using Polynomial Regression

This project demonstrates how to predict house prices using **Polynomial Regression**, with a clean modular design in Python. The model is trained on housing data and uses advanced regression techniques to estimate the property price in Lakh INR.

---

## 📊 What is Polynomial Regression?

Polynomial Regression is a type of regression analysis in which the relationship between the **independent variable(s)** `X` and the **dependent variable** `y` is modeled as an nth-degree polynomial.

Mathematically:
```

y = b0 + b1*x + b2*x^2 + ... + bn\*x^n

````

Unlike **Linear Regression** (which fits a straight line), **Polynomial Regression** can fit **non-linear curves** by adding higher-degree terms of the input features.

However, it can also lead to **overfitting** if used carelessly, especially when:
- The dataset is small
- The features don't have nonlinear relationships
- Too high a polynomial degree is used

---

## 📁 Project Folder Structure

```markdown
house_price_prediction_with_Polynomial_Regression/
│
├── data/
│   └── House_price_data.xlsx       # Dataset file
│
├── src/
│   ├── main.py                     # Trains the model, evaluates, and saves it
│   ├── predict.py                  # Loads model and predicts new data
│   ├── models/
│   │   └── polynomial_pipeline.pkl # Saved trained pipeline (preprocessing + model)
│   └── utils/
│       ├── evaluation.py           # Evaluation metrics (MAE, MSE, RMSE, R2)
│       └── visualize.py            # Visualization for feature-target relationships
│
├── requirements.txt                # Python dependencies
└── README.md                       # This file
````

---

## 📌 Dataset Overview

The dataset contains the following columns:

* `Size_sqft`: Area of the house in square feet
* `Bedrooms`: Number of bedrooms
* `Location_Score`: A score representing location quality
* `Price_Lakh(INR)`: Target variable – House price in Lakh INR

---

## 🧠 How the Model Works

The model is built using a `Pipeline` that combines:

1. **Preprocessing:**

   * Standardizes numeric features
   * Applies polynomial feature transformation only on `Size_sqft` (since it shows non-linear relation)

2. **Model:**

   * Uses `LinearRegression` (or optionally `Ridge`) to fit the data

---

## 🚀 How to Train the Model

```bash
python src/main.py
```

This will:

* Load and preprocess the data
* Train a polynomial regression model
* Evaluate model using:

  * MAE (Mean Absolute Error)
  * MSE (Mean Squared Error)
  * RMSE (Root Mean Squared Error)
  * R² Score
* Save the full pipeline to `src/models/polynomial_pipeline.pkl`
* Display visualizations (only during training)

---

## 🔮 How to Make Predictions

After training, you can run:

```bash
python src/predict.py
```

This file:

* Loads the saved pipeline
* Accepts input features (`Size_sqft`, `Bedrooms`, `Location_Score`)
* Returns predicted price in Lakh INR

---

## 🧪 Example Prediction Input

```python
input_data = {
    "Size_sqft": [2100],
    "Bedrooms": [3],
    "Location_Score": [7]
}
```

---

## 📦 Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

### `requirements.txt` may include:

```txt
pandas
scikit-learn
matplotlib
seaborn
openpyxl
joblib
```

---

## 📈 Model Performance

Depending on the model:

* **Multiple Linear Regression:**

  * R² ≈ **0.83** (better performance)
* **Polynomial Regression (degree=2):**

  * R² ≈ **0.14** (overfitting, worse performance)

---

## ⚠️ Notes

* Polynomial regression is **not always better** than linear regression. Use it only when data shows non-linear trends.
* Overfitting is common with high-degree polynomials or unnecessary feature transformations.
* Try **regularization (Ridge, Lasso)** if you still want to use Polynomial Regression but with better generalization.

---

## 📬 Author

**Awanish Kumar**