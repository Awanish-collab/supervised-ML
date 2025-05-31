import pandas as pd

def load_data(file_path: str):
    df = pd.read_excel(file_path)
    X = df[['Size_sqft']]
    y = df['Price_Lakh(INR)']
    return X, y
