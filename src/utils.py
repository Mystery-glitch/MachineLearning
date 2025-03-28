import sys
import os
import dill
import pandas as pd
import numpy as np

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path) # os.path.dirname(): used to get the directory name from a file path
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as ex:
        raise CustomException(ex, sys)
    
def evaluate_models(x_train,x_test,y_train,y_test,models,param):
    try:
        report={}
        
        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]
            
            # Hyperparameter tuning
            gs=GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)
            model.set_params(**gs.best_params_)
            
            model.fit(x_train,y_train)
            
            y_train_pred=model.predict(x_train)
            y_test_pred=model.predict(x_test)
            
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score
            
        return report
    except Exception as ex:
        raise CustomException(ex, sys)