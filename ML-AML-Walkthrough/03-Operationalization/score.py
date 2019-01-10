
import json
import os
import numpy as np
import pandas as pd
from sklearn import linear_model 
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from azureml.core import Run
from azureml.core import Workspace
from azureml.core.run import Run
from azureml.core.experiment import Experiment
import pickle
from sklearn.externals import joblib

def init():
    try:
        # One-time initialization of predictive model and scaler
        from azureml.core.model import Model
        
        global model   

        model_name = 'propensity_to_buy_predictor'
        model_path = Model.get_model_path(model_name, _workspace=ws)
        model = pickle.load(open(model_path, 'rb'))
        
    except Exception as e:
        print('Exception during init: ', str(e))

def run(input_json):     
    try:
        inputs = json.loads(input_json)

        #Get the scored result
        prediction = json.dumps(model.predict(inputs).tolist())

    except Exception as e:
        prediction = str(e)
    return prediction
