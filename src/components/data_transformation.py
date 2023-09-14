from src.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from src.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
        
        data=pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data, test_size=0.20)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splitted the data into training and test.")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)