#import libraries
# from sentence_transformers import SentenceTransformer, util # need to be uninstall to he virtual envs
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rake_nltk import Rake
from features_xtrct import PhraseExtract, PhraseExtract1


import random

import spacy.tokens

#helping functions





# this class should return a floating type that ranges to 1-4. 4 being the highest and 1 being the lowest
# 1 - The ideas weren't connected to each other
# 2 - The ideas were good but some weren't there
# 3 - The ideas has shown a bit understanding with good details
# 4 - The ideas flow logically and connected well.
# check the essay composition if the sentence follows a logical flow - inner_context1, inner_context2 
class Ideas:

    #return a list of key words that relate to the topic or the contenxt of the essay composition
    @staticmethod
    def rake_KeyWord(text): 

        r = Rake()
        r.extract_keywords_from_text(text)

        keywords = r.get_ranked_phrases()
        return keywords



class Gram_Punc:

    def mainfunction():

        pass


class Transition:

    def mainfunction():

        pass

class Clarity:

    def mainfunction():

        pass

class WordChoice:

    def mainfunction():

        pass

class Structure:

    def mainfunction():

        pass

class Lang_Mechs:

    def mainfunction():

        pass



class rubrics_benchmark: 


    def __init__(self, phase_intance):
        
        self.Ideas_criterion = None
        self.Gram_Punc_criterion = None
        self.Transition_criterion = None
        self.Clarity_criterion = None
        self.WordChoice_criterion = None
        self.Structure_criterion = None
        self.Lang_Mechs_criterion = None


        self.__prediction_values = [1, 2, 3, 4]
        

        self.Benchmark_run()


    def Benchmark_run(self):


        self.Ideas_criterion = random.choice(self.__prediction_values)
        self.Gram_Punc_criterion = random.choice(self.__prediction_values)
        self.Transition_criterion = random.choice(self.__prediction_values)
        self.Clarity_criterion = random.choice(self.__prediction_values)
        self.WordChoice_criterion = random.choice(self.__prediction_values)
        self.Structure_criterion = random.choice(self.__prediction_values)
        self.Lang_Mechs_criterion = random.choice(self.__prediction_values)



def grade_corpus(text):

    nlp = spacy.load("en_core_web_sm")
    # Step 1: Analyze the coherence and flow of the text using NLP
    doc = nlp(text)

    # Step 2: Check for cohesive devices (e.g., conjunctions like "but", "and", "however")
    cohesive_devices = {"however", "but", "and", "therefore", "because", "since"}
    cohesive_count = sum(1 for token in doc if token.text.lower() in cohesive_devices)
    
    # Step 3: Analyze topic consistency by measuring sentence similarity
    sentences = list(doc.sents)
    if len(sentences) > 1:
        vectorizer = TfidfVectorizer().fit_transform([sent.text for sent in sentences])
        similarity_matrix = cosine_similarity(vectorizer)
        avg_similarity = similarity_matrix.mean()
    else:
        avg_similarity = 1  # If there's only one sentence, it's fully consistent   

    print(f"avg_similarity:{avg_similarity}")

    # Step 4: Assign a grade based on flow and cohesion
    if avg_similarity > 0.7 and cohesive_count > 2:
        return 4  # Ideas flow logically and are well-connected
    elif avg_similarity > 0.5 and cohesive_count > 1:
        return 3  # Shows understanding with some good detail
    elif avg_similarity > 0.3:
        return 2  # Some ideas are there but incomplete
    else:
        return 1  # Ideas are not connected to each other



#def IdeaCreterion(doc : spacy.)


#adjust the grade_corpus using the PhraseExtract similarity return value
#then define the condition ladder

#this function is suject to be tested
def IdeaCriterion(PhraseObj : PhraseExtract):


    similarity_score = PhraseObj.getSimilarityScore()
    cohesive_device_count = PhraseObj.cohesive_device_count
    #threshold = 0.4

    #need to have an alternative return if the parameter do not pass the condition ladder
    alternative_return = None
    

    if similarity_score < .4: 

        if PhraseObj.cohesive_device_count <=1: 

            print('alter 1')
            alternative_return = 1

        elif PhraseObj.cohesive_device_count >= 2 and PhraseObj.cohesive_device_count <=4:

            print('alter 2')
            alternative_return = 2
        
        else:
            print('alter 3')
            alternative_return = 1

    
    if similarity_score < .5 and similarity_score >= .4:

        if cohesive_device_count >= 2 and cohesive_device_count <= 4: 

            print('alter 4')
            alternative_return = 2

        elif cohesive_device_count > 4:

            print('alter 5')
            alternative_return = 3

        else:

            print('alter 6')
            alternative_return = 2 

    if similarity_score < .6 and similarity_score >= .5:

        if cohesive_device_count >= 3 and cohesive_device_count <= 5:

            print('alter 7')
            alternative_return = 3

        elif cohesive_device_count > 5:

            print('alter 8')
            alternative_return = 4

        else: 

            print('alter 9')
            alternative_return = 3
   
    if similarity_score < .75 and similarity_score >= .6:


        if cohesive_device_count >= 4:

            print('alter 10')
            alternative_return = 4

        else:

            print('alter 11')
            alternative_return = 3


    return alternative_return



#use the parameter readability_score from the PhraseExtract instance
def ClarityAndConciseness(PhraseAObj: PhraseExtract):


    return None
    

