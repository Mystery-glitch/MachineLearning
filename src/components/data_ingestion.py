import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
# dataclass is used to simplify the creation of classes that are primarily used for storing data.
# We don't need to manually define the __init__ constructor for assigning attributes.
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Here we are reading the dataset
            df = pd.read_csv(os.path.join('notebook', 'stud.csv'))
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # Converting it into the raw data path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Then we are doing train test split, i.e., training the datas
            logging.info("Train Test Split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
            )
        except Exception as ex:
            logging.error(f"Error in data ingestion: {ex}")
            raise CustomException(ex, sys)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()