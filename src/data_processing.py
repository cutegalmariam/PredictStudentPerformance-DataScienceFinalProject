import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load dataset
def load_data(file_path):
    try:
        data = pd.read_excel(file_path)
        print("File loaded successfully. Here's a preview:")
        print(data.head())
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def preprocess_data(data):
    # Handle missing values for numeric columns
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

    # Handle missing values for categorical columns (if any)
    categorical_columns = data.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        data[column] = data[column].fillna(data[column].mode()[0])

    # Encode categorical variables
    label_encoders = {}
    for column in categorical_columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

    return data, label_encoders

