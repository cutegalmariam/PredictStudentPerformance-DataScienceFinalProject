from src.data_processing import load_data, preprocess_data
from src.eda import perform_eda
from src.model import train_models, plot_feature_importance

def main():
    file_path = "Data/Maths.xlsx"
    data = load_data(file_path)

    if data is not None:
        data, label_encoders = preprocess_data(data)
        perform_eda(data)
        lr, rf = train_models(data)
        plot_feature_importance(rf, data.drop(columns=['G3']))  # Visualize feature importance

if __name__ == "__main__":
    main()
