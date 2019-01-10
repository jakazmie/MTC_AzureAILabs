import pandas as pd
import numpy as np
import os


def get_data():
 
    # Load the dataset
    data_folder = os.environ["AZUREML_DATAREFERENCE_workspaceblobstore"]
    file_name = os.path.join(data_folder, 'banking_train.csv')
    df = pd.read_csv(file_name)

    # Preprocess the data
    feature_columns = [
                   # Demographic
                   'age', 
                   'job', 
                   'education', 
                   'marital',  
                   'housing', 
                   'loan', 
                   # Previous campaigns
                   'month',
                   'campaign',
                   'poutcome',
                   # Economic indicators
                   'emp_var_rate',
                   'cons_price_idx',
                   'cons_conf_idx',
                   'euribor3m',
                   'nr_employed']

    df = df[feature_columns + ['y']]
    features = df.drop(['y'], axis=1)                                         
    
    # Flatten labes
    labels = np.ravel(df.y)    
    
    return { "X" : features, "y" : labels}
