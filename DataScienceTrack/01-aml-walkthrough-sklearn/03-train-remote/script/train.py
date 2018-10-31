
import os
import argparse

from azureml.core import Run

import numpy as np
import random
import h5py

from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib



# Training regime
def train_evaluate(run):
   
    print("Loading bottleneck features")
    train_file_name = os.path.join(args.data_folder, args.training_file_name)
    valid_file_name = os.path.join(args.data_folder, args.validation_file_name)
    
    # Load bottleneck training features and labels
    with h5py.File(train_file_name, "r") as hfile:
        train_features = np.array(hfile.get('features'))
        train_labels = np.array(hfile.get('labels'))
        
        
    # Load bottleneck validation features and labels
    with h5py.File(valid_file_name, "r") as hfile:
        valid_features = np.array(hfile.get('features'))
        valid_labels = np.array(hfile.get('labels'))
        
    # Conver one-hot labels to integers
    y_train = np.argmax(train_labels, axis=1)
    y_valid = np.argmax(valid_labels, axis=1)
    
    # Train logistics regresssion model
    print("Starting training on")
    print("  Features:", train_features.shape)
    print("  Labels:", y_train.shape)
    clf = LogisticRegression(
        C=1.0/args.reg, 
        multi_class='multinomial',
        solver='lbfgs',
        random_state=42)
    clf.fit(train_features, y_train)
    
    
    # Validate
    print("Starting validation")
    y_hat = clf.predict(valid_features)
    
    # Calculate accuracy 
    acc = np.average(y_hat == y_valid)
    print('Validatin accuracy is:', acc)
    
    # Log to AML Experiment
    run.log('regularization_rate', np.float(args.reg))
    run.log('validation_acc', np.float(acc))
          
    # Save the trained model to outp'uts which is a standard folder expected by AML
    model_file = 'aerial_sklearn.pkl'
    model_file = os.path.join('outputs', model_file)
    print("Saving the model to: ", model_file)
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=clf, filename=model_file)
    

  

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Training, evaluation worklfow")

    ### Model parameters
    
    parser.add_argument(
        '--data-folder',
        type=str,
        default = './bottleneck',
        help='Folder with bottleneck features and labels')

    parser.add_argument(
        '--training-file-name',
        type=str,
        default = 'aerial_bottleneck_train.h5',
        help='Training file name')

    parser.add_argument(
        '--validation-file-name',
        type=str,
        default = 'aerial_bottleneck_valid.h5',
        help='Validation file name')

    parser.add_argument(
        '--regularization', 
        type=float, dest='reg', 
        default=0.01, 
        help='regularization rate')
    
    args = parser.parse_args()
    
    # get hold of the current run
    run = Run.get_submitted_run()
    train_evaluate(run)
    