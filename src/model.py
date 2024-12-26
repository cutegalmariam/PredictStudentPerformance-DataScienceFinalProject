import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_processing import load_data, preprocess_data
from sklearn.preprocessing import LabelEncoder

# Preprocessing function to handle categorical data
def preprocess_data(data):
    # Convert categorical columns into numeric using LabelEncoder or OneHotEncoding
    label_encoder = LabelEncoder()

    # Apply label encoding to categorical columns (example: 'school', 'sex', etc.)
    categorical_columns = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']

    for column in categorical_columns:
        data[column] = label_encoder.fit_transform(data[column])

    return data

# Train models and evaluate performance
def train_models(data):
    # Preprocess the data
    data = preprocess_data(data)

    # Define features (X) and target (y)
    X = data.drop(columns=['G3'])
    y = data['G3']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    print("Linear Regression:")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_lr))}")
    print(f"R2 Score: {r2_score(y_test, y_pred_lr)}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred_lr)}")

    # Train Random Forest Regressor
    rf = RandomForestRegressor(random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    print("Random Forest Regressor:")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_rf))}")
    print(f"R2 Score: {r2_score(y_test, y_pred_rf)}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred_rf)}")

    # Call the plot_feature_importance method for Random Forest model
    plot_feature_importance(rf, X_train)

    return lr, rf

# Visualize Feature Importance from Random Forest
def plot_feature_importance(model, X_train):
    feature_importance = model.feature_importances_
    sorted_idx = np.argsort(feature_importance)[::-1]
    features = X_train.columns

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importance[sorted_idx], y=features[sorted_idx])
    plt.title("Feature Importance - Random Forest")
    plt.show()


# if __name__ == "__main__":
#     file_path = "/Users/mariam/PycharmProjects/DataScienceFinalProject/Data/Maths.xlsx"
#     data = load_data(file_path)
#     train_models(data)
