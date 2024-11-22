import joblib
import numpy as np
import random

rf_model = joblib.load(r'C:\Users\jhondhelpago\Documents\GitHub\phrasetestAPI\module\rf_model.pkl')

def predict_writing_level(writing_composition: str):

    labels = ['below average', 'average', 'above average']

    return random.choice(labels)

def predict_level(features_list : list) -> str:

    labels = ['below average', 'average', 'above average']

    # 0 - inadequete
    # 1 - good
    # 2 - fair

    result = rf_model_predict(features_list)
    print(f"result for  predict_level {result}")

    if result == 0:

        return 'inadequete'
    
    elif result == 1: 

        return 'good'
    
    elif result == 2:

        return 'fair'
    
    else:

        return 'not classified'




def rf_model_predict(feature_list : list):

    feature_list = [feature_list]
    feature_list_array = np.array(feature_list)

    result = rf_model.predict(feature_list_array)

    return result[0]


    


    





