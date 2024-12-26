import logging
from src.data_processing import load_data, preprocess_data
from src.eda import perform_eda
from src.model import train_models, plot_feature_importance

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    file_path = "Data/Maths.xlsx"
    logging.info(f"Loading data from {file_path}")

    # Load the data
    data = load_data(file_path)

    # Check if the data was successfully loaded
    if data is not None:
        logging.info("Data loaded successfully.")

        try:
            # Preprocess data
            data, label_encoders = preprocess_data(data)
            logging.info("Data preprocessing completed.")

            # Perform Exploratory Data Analysis (EDA)
            perform_eda(data)
            logging.info("Exploratory Data Analysis completed.")

            # Train models
            lr, rf = train_models(data)
            logging.info("Models trained successfully.")

            # Visualize feature importance of the RandomForest model
            plot_feature_importance(rf, data.drop(columns=['G3']))  # Drop 'G3' as the target variable
            logging.info("Feature importance plot generated.")

        except Exception as e:
            logging.error(f"An error occurred during data processing: {e}")

    else:
        logging.error("Failed to load data.")

if __name__ == "__main__":
    main()
