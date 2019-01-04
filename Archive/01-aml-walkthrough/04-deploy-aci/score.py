import json
import os
import pickle
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.applications import resnet50

from azureml.core.model import Model
import azureml.train.automl

def init():
    # Instantiate ResNet50 featurizer
    global featurizer
    featurizer = resnet50.ResNet50(
            weights = 'imagenet', 
            input_shape=(224,224,3), 
            include_top = False,
            pooling = 'avg')

    # Load the model
    global model
    # retreive the path to the model file using the model name
    model_path = Model.get_model_path(model_name = 'AutoMLac5fd8f37best')
    model = joblib.load(model_path)
  

def run(raw_data):
    try:
        # convert json to numpy array
        images = np.array(json.loads(raw_data)['data'])
        # normalize as required by ResNet50
        images = resnet50.preprocess_input(images.astype(float))
        # extract bottleneck features
        features = featurizer.predict(images)
        # make prediction
        predictions = model.predict(features)
        # Add string labels
        labels = ["Barren",
                  "Cultivated",
                  "Developed",
                  "Forest",
                  "Herbaceous",
                  "Shrub"]
        
        # Get string labels for predictions
        string_predictions = [labels[pred] for pred in predictions]
        
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
    
    # Return both numeric and string predictions
    return json.dumps({"predictions": predictions.tolist(), "labels": string_predictions})