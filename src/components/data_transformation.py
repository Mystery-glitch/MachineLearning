import sys
import os
import dataclasses as dataclass
import numpy as np
import pandas as pd

from src.utils import save_object

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessing_obj_file_path=os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        # This function is responsible for data transformation
        try:
            numerical_columns=['reading score', 'writing score']
            categorical_columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']

            num_pipeline=Pipeline(
                steps=[("impute",SimpleImputer(strategy='median')),
                       ("scaler",StandardScaler(with_mean=False))
                       ]
            )
            cat_pipeline=Pipeline(
                steps=[("impute", SimpleImputer(strategy='most_frequent')),
                       ("one_hot_encoder", OneHotEncoder()),
                       ("scaling", StandardScaler(with_mean=False))
                       ]
            )
            logging.info(f"Numerical Columns: {numerical_columns}")
            logging.info(f"Categorical Columns: {categorical_columns}")

            preprocessor=ColumnTransformer(
                [("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        except Exception as ex:
            raise CustomException(sys, ex)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Train and Test data completed")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math score"
            numerical_columns=['reading score', 'writing score']

            input_feature_train_df=train_df.drop(columns=[target_column_name], axis=1) # axis=1 means operate on columns
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name], axis=1) # axis=1 means operate on columns
            target_feature_test_df=test_df[target_column_name]
            logging.info("Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.fit_transform(input_feature_test_df)

            train_arr=np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessing_obj_file_path,
                obj=preprocessing_obj
            )

            return train_arr, test_arr, self.data_transformation_config.preprocessing_obj_file_path
        except Exception as ex:
            raise CustomException(ex, sys)
