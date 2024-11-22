import joblib
import numpy as np
import random

rf_model = joblib.load(r'C:\Users\jhondhelpago\Documents\GitHub\phrasetestAPI\module\rf_model.pkl')

def predict_writing_level(writing_composition: str):

    labels = ['below average', 'average', 'above average']

    return random.choice(labels)

def predict_level(features_dict : dict) -> str:

    labels = ['below average', 'average', 'above average']

    return random.choice(labels)


def rf_model_predict(feature_list : list):

    feature_list = [feature_list]
    feature_list_array = np.array(feature_list)

    result = rf_model.predict(feature_list_array)

    return result


    


    





