import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataIngestion:
    def __init__(self, csv_file_path: str, test_size: float = 0.2, random_state: int = 42):
        """
        Initializes the DataIngestion class with parameters
        :param csv_file_path: Path to the CSV file
        :param test_size: Fraction of data to be used for testing
        :param random_state: Random state for reproducibility
        """
        self.csv_file_path = csv_file_path
        self.test_size = test_size
        self.random_state = random_state
        self.data_dir = ".\dataset"  # Directory where data will be saved/loaded
    
    def load_data(self) -> pd.DataFrame:
        """
        Loads the Boston Housing dataset from a CSV file.
        :return: DataFrame containing the Boston Housing dataset
        """
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"The file {self.csv_file_path} does not exist.")
        
        # Load dataset from CSV
        data = pd.read_csv(self.csv_file_path)
        
        # Optionally save a copy of the dataset to a standard location for future use
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        data.to_csv(os.path.join(self.data_dir, "HousingData.csv"), index=False)
        
        return data
    
    def split_data(self, data: pd.DataFrame):
        """
        Splits the dataset into training and test sets.
        :param data: DataFrame containing the dataset to be split
        :return: Tuple of train and test datasets (X_train, X_test, y_train, y_test)
        """
        X = data.drop("MEDV", axis=1)  # Features (drop the target column)
        y = data["MEDV"]  # Target column (House prices)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
        return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Path to the downloaded CSV file
    csv_file_path = "D:\AIMLPortfolio\BostonHousePricePrediction\Dataset\HousingData.csv"
    
    # Initialize the DataIngestion class with the CSV file path
    data_ingestion = DataIngestion(csv_file_path=csv_file_path)
    
    # Load and split the data
    data = data_ingestion.load_data()
    X_train, X_test, y_train, y_test = data_ingestion.split_data(data)
    
    print("Data successfully ingested and split!")
    print(f"Training data shape: {X_train.shape}")
    print(f"Testing data shape: {X_test.shape}")
