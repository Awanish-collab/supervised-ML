```markdown
# 🏠 House Price Prediction using Simple Linear Regression

This project demonstrates a **Simple Linear Regression** model to predict house prices based on the house size (in square feet). It uses a synthetic dataset and provides a clean structure for training, evaluating, and making predictions.

---

## 📘 Project Structure



house_price_prediction_with_simple_linear_regression/
│
├── src/ # All source code and files
│ ├── data/ # Input datasets (Excel)
│ │ └── house_data_simple.xlsx
│ │
│ ├── models/ # Trained model file
│ │ └── model.pkl
│ │
│ ├── utils/ # Utility scripts (reusable functions)
│ │ └── preprocess.py
│ │
│ ├── predict.py # Script to predict price based on user input
│ ├── main.py # Main training and evaluation script
│ 
│
├── requirements.txt # All required Python packages
└── README.md # This file


---

## 🧠 Concept Used

### 🔹 Simple Linear Regression

- A supervised learning technique used for **predicting a continuous value**.
- This model learns the relationship between:
  - **Input (independent variable):** House Size (in sqft)
  - **Output (dependent variable):** House Price (in Lakh ₹)

---

### 🔹 Why Use Linear Regression?

- Easy to understand and interpret.
- Great for baseline regression models.
- Draws a straight line that best fits the data (minimizes error).

---

### 🔹 Why Use `joblib`?

- `joblib` efficiently **saves and loads ML models**.
- We use it to save the trained model as `model.pkl` and load it later for prediction without retraining.

---

## 🧪 Evaluation Metrics

| Metric | Meaning |
|--------|---------|
| **MAE** (Mean Absolute Error) | Average error in original units |
| **MSE** (Mean Squared Error) | Squares errors, penalizes large mistakes |
| **RMSE** (Root Mean Squared Error) | Like MAE, but gives more weight to large errors |
| **R² Score** | Shows how well model explains the data (0 to 1) |

---

## 🛠 Installation

### 🔹 Step 1: Clone the repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
````

### 🔹 Step 2: Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 🔹 Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Project

### 🔹 Train the model

```bash
python src/train.py
```

This will:

* Load dataset from Excel.
* Train the Linear Regression model.
* Evaluate model using metrics.
* Save the trained model to `models/model.pkl`.

---

### 🔹 Make a prediction

```bash
python predict.py
```

It will prompt:

```
Enter house size in sqft:
```

Example:

```
Enter house size in sqft: 1000
Predicted Price: ₹ 54.85 Lakh
```

---

## 📦 Required Packages (in `requirements.txt`)

```
pandas
scikit-learn
joblib
openpyxl
```

---

## ✅ Output Example

```
Model Evaluation Metrics:
MAE  : 19.97
MSE  : 627.28
RMSE : 25.05
R²   : 0.83
```

---

## 💡 Author Notes

* This is a beginner-friendly machine learning project.
* Designed for educational and demonstration purposes.
* Synthetic data is used for simplicity and hands-on learning.

---

## 📌 Next Steps

* Implement **Multiple Linear Regression** (when more features are involved like location, number of rooms, etc).