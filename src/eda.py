import matplotlib.pyplot as plt
import seaborn as sns
from src.data_processing import load_data, preprocess_data
import pandas as pd
import numpy as np


def perform_eda(data):
    print("Performing EDA...")

    # Select only the numeric columns for the correlation heatmap
    numeric_data = data.select_dtypes(include=[np.number])
    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

    # Scatterplot: Failures vs. Final Grade
    sns.scatterplot(x='failures', y='G3', data=data)
    plt.title("Impact of Failures on Final Grade (G3)")
    plt.show()

    # Boxplot: G3 by Gender
    sns.boxplot(x='sex', y='G3', data=data)
    plt.title("Comparison of G3 by Gender")
    plt.show()

    # Histograms for numerical features
    data.hist(figsize=(12, 8), bins=30)
    plt.suptitle("Histograms of Numerical Features")
    plt.show()

    school_map = {0: 'GP', 1: 'MS'}
    data['school'] = data['school'].map(school_map)

    # Barplot for categorical variables (e.g., school vs. G3)
    sns.barplot(x='school', y='G3', data=data)
    plt.title("Average Final Grade by School")
    plt.show()
