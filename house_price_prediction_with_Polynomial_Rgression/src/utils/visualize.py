import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_relationships(df, target_col):
    numeric_features = df.select_dtypes(include=['float64', 'int64']).columns
    for feature in numeric_features:
        if feature != target_col:
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=df[feature], y=df[target_col])
            plt.title(f"{feature} vs {target_col}")
            plt.xlabel(feature)
            plt.ylabel(target_col)
            plt.tight_layout()
            plt.show()
