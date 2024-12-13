import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from new_features_xtract import PhraseExtract






for i in range (0, 26000):

    print(f"\n{i}")

    Phrase = PhraseExtract(question='What do you want to be when you grow up?', text='I want to be a software engineer that create software programs for computer. I want to create an application that will be useful for the people and push our technological adavancement.')
    print(Phrase.text)
    print(f"number of sentence : {Phrase.get_NumberOfSentence()}")
    print(Phrase.feature_list_sample())

    
     