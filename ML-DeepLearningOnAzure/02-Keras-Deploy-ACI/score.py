import json
import os
import numpy as np
import random
import tensorflow as tf

from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image

from azureml.core.model import Model
from azureml.core import Workspace

def init():
    try:
        
        # Create ResNet50 featurizer
        global featurizer
        
        featurizer = resnet50.ResNet50(
            weights = 'imagenet', 
            input_shape=(224,224,3), 
            include_top = False,
            pooling = 'avg')
        
        # Load top model
        global model   

        model_name = 'aerial_classifier'
        model_path = Model.get_model_path(model_name)
        model = tf.keras.models.load_model(model_path)
        
    except Exception as e:
        print('Exception during init: ', str(e))

  

def run(raw_data):
    try:
        # convert json to numpy array
        images = np.array(json.loads(raw_data)['data'])
        # normalize as required by ResNet50
        images = resnet50.preprocess_input(images)
        # Extract bottleneck featurs
        features = featurizer.predict(images)
        # Make prediction
        predictions = model.predict(features)
        
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
    
    # Return both numeric and string predictions
    # return json.dumps({"predictions": predictions.tolist(), "labels": string_predictions})
    return json.dumps({"predictions": predictions.tolist()})
