import joblib
import numpy as np
import random
import pickle
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
rf_model_path = os.path.join(current_dir, 'rf_model.pkl')
rf_model = joblib.load(rf_model_path)

nb_model_path = os.path.join(current_dir, 'nb_model.pkl')
nb_model = joblib.load(nb_model_path)

knn_model_path = os.path.join(current_dir, 'knn_model2.pkl')
knn_model = joblib.load(knn_model_path)


# gb_model
gb_model_path = os.path.join(current_dir, 'main_gb_model.pkl')
gb_model = joblib.load(gb_model_path)

def predict_writing_level(writing_composition: str):

    labels = ['below average', 'average', 'above average']

    return random.choice(labels)

def predict_level(features_list : list) -> str:

    labels = ['below average', 'average', 'above average']

    # 0 - inadequete
    # 1 - good
    # 2 - fair


    #rf model predict equivalent
    #0 - inadequete
    #1 - good
    #2 - fair

    print('feature_list')
    print(features_list)
    result = rf_model_predict(features_list)
    # result = knn_model_predict(features_list)
    print(f"result for  predict_level {result}")

    # if features_list[0] < 15:

    #     return 'inadequete'



    if result == 0:

        return 'need improvement'
    
    elif result == 1: 

        return 'good'
    
    elif result == 2:

        return 'fair'


def rf_model_predict(feature_list : list):

    feature_list = [feature_list]
    feature_list_array = np.array(feature_list)

    result = rf_model.predict(feature_list_array)
    # result = nb_model.predict(feature_list_array)

    return result[0]

def nb_model_predict(feature_list : list):

    feature_list = [feature_list]
    feature_list_array = np.array(feature_list)


    result = nb_model.predict(feature_list_array)


    return result[0]



##
# model interation here
# each model should have its own function
# return value should be align to its label
# ##


def knn_model_predict(feature_list : list):

    feature_list = [feature_list]
    feature_list_array = np.array(feature_list)

    result = knn_model.predict(feature_list)

def gb_model_predict(feature_list : list):

    # 0 = need improvement
    # 1 = fair
    # 2 = good

    feature_list_array = np.array([feature_list])


    result = gb_model.predict(feature_list_array)

    if result == 0:

        return 'need improvements'
    
    elif result == 1:

        return 'fair'
    
    elif result == 2:

        return 'good'
    
    else:

        return 'cannot be determined'


    


    





