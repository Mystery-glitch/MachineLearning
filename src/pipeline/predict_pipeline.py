import sys
import os
import pandas as pd

from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        model_path=os.path.join('artifacts', 'model.pkl')
        preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
        
        self.model=load_object(file_path=model_path)
        self.preprocessor=load_object(file_path=preprocessor_path)
    
    def predict(self, features):
        try:            
            # You're loading the model every time you predict, which is inefficient.
            """
            model_path=os.path.join('artifacts', 'model.joblib')
            preprocessor_path=os.path.join('artifacts','preprocessor.joblib')
    
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            """
            
            data_scaled=self.preprocessor.transform(features)
            preds=self.model.predict(data_scaled)
            return preds
        except Exception as ex:
            raise CustomException(ex,sys) 
    
class CustomData:
    # here 'unkown' can helping in avoiding errors if a required feature is missing
    def __init__(self, 
                gender:str = "unknown", 
                race_ethnicity:str = "unknown", 
                parental_level_of_education:str = "unknown", 
                lunch:str = "unknown", 
                test_preparation_course:str = "unknown", 
                reading_score:int = 0, 
                writing_score:int = 0):
        self.gender=gender if gender else "unknown"
        self.race_ethnicity=race_ethnicity if race_ethnicity else "unknown"
        self.parental_level_of_education=parental_level_of_education if parental_level_of_education else "unknown"
        self.lunch=lunch if lunch else "unknown"
        self.test_preparation_course=test_preparation_course if test_preparation_course else "unknown"
        self.reading_score=reading_score if reading_score else 0
        self.writing_score=writing_score if writing_score else 0
    

    
    # This function will reture all the input in the form of a dataFrame
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                'gender': [self.gender],
                'race/ethnicity':[self.race_ethnicity],
                'parental level of education': [self.parental_level_of_education],
                'lunch': [self.lunch],
                'test preparation course':[self.test_preparation_course],
                'reading score':[self.reading_score],
                'writing score':[self.writing_score]
            }
            df = pd.DataFrame(custom_data_input_dict)
            df.fillna("unknown", inplace=True)
            return df
        except Exception as ex:
            raise CustomException(ex,sys)
        