import random



def predict_writing_level(writing_composition: str):

    labels = ['below average', 'average', 'above average']

    return random.choice(labels)

def predict_level(features_dict : dict) -> str:

    labels = ['below average', 'average', 'above average']

    return random.choice(labels)

    





