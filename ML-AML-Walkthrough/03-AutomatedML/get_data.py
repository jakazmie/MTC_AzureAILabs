import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def get_data():
    # Load bottleneck features
    data_folder = os.environ["AZUREML_DATAREFERENCE_workspaceblobstore"]
    file_name = os.path.join(data_folder, 'used_cars', 'UsedCars_Affordability.csv')
    
    print("Data folder:", data_folder)
    print("Dataset:", file_name)
    print("Data folder content:", os.listdir(data_folder))
    
    df_affordability = pd.read_csv(file_name, delimiter=',')

    features = df_affordability[["Age", "KM"]]
    labels = df_affordability[["Affordable"]]

        
    # Split the data into training and validation partitions   
    train_X, test_X, train_Y, test_Y  = train_test_split(features, labels,
                                                               test_size=0.2,
                                                               shuffle=True)
        # Flatten labels
    train_Y = np.ravel(train_Y)
    test_Y = np.ravel(test_Y)
    
    # Convert to float
    train_X = train_X.astype(float)
    test_X = test_X.astype(float)
        

    return {'X': train_X, 'y': train_Y, 'X_valid': test_X, 'y_valid': test_Y}
