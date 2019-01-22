import json
import os
import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.models import load_model

from azureml.core.model import Model

import azureml.contrib.brainwave.models.utils as utils
from azureml.contrib.brainwave.models import QuantizedResnet50

def init():
    # Instantiate ResNet50 featurizer
    global featurizer
    
    # Create ResNet50 
    model_path = os.path.expanduser('~/models')
    featurizer = QuantizedResnet50(model_path, is_frozen=True)

    # Load the pretrained top
    global model
    # retreive the path to the model file using the model name
    model_path = Model.get_model_path(model_name = 'aerial-classifier-brainwave')
    #model = load_model(model_path)
    print(model_path)
  

def run(raw_data):
    try:
        # convert json to numpy array
        images = np.array(json.loads(raw_data)['data'])
        # normalize as required by ResNet50
        
        predictions = str(images.shape)
        
        # Call the top
        # predictions = model.predict(features)
        # Add string labels
        #labels = ["Barren",
        #          "Cultivated",
        #          "Developed",
        #          "Forest",
        #          "Herbaceous",
        #          "Shrub"]
        
        # Get string labels for predictions
        #string_predictions = [labels[pred] for pred in predictions]
        
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
    
    # Return both numeric and string predictions
    # return json.dumps({"predictions": predictions.tolist(), "labels": string_predictions})
    return json.dumps({"predictions": predictions})
