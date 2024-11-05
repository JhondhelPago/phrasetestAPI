import random



def predict_writing_level(writing_composition: str):

    labels = ['underdeveloped', 'mediocre', 'advanced']

    return random.choice(labels)





