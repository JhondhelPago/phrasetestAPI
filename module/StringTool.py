import numpy as np
import spacy

class StringToolkit:

    @staticmethod
    def wordCount(text: str):

        word_array = np.array(text.split())

        return word_array.size

    





    
        