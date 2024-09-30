import spacy
import spacy.tokens
import math
from typing import Union
from constants import cohesive_device
from spellchecker import SpellChecker

def nlp_loader_sm():

    return spacy.load('en_core_web_sm')

def nlp_loader_md():
    
    return spacy.load('en_core_web_md')

#type token ratio
def TTR(token_list):

    unique_token = set()
    numberOfToken = 0

    for word_token in token_list:

        numberOfToken += 1

        

        if not word_token in unique_token:

            unique_token.add(word_token)

    TTR_score = len(unique_token) / numberOfToken
    # print(TTR_score)

    return TTR_score

#moving average type token ratio
def MATTR(doc:spacy.tokens.doc , window_size = 50, showtoken_len = False):

    token_list = [token.text.lower() for token in doc if IsValidVocabularyWord(token)]

    if len(token_list) > window_size :

        left_border = 0
        right_border = window_size

        TTR_score_list  = []

        while right_border < len(token_list):

            window_token_range = token_list[left_border:right_border] #sublist of tokens

            TTR_score_list.append(TTR(window_token_range))

            left_border += 1
            right_border +=1  
        
        if showtoken_len == True:
            print(f"token length: {len(token_list)}")
        
        #'the return of this funuction is from the calculation of MTTR.'
        return  sum(TTR_score_list) / len(TTR_score_list)    
    
    # if the window size is more thean the length of the actual token_list -> will simply return TTR calculation
    else:
        #'the return of this function is from the calculation of simple TTR because the window is greater than the actaul size of the token_list.'
        return TTR(token_list=token_list)





def CTTR(doc:spacy.tokens.doc):

    token_length = numberOfTokens(spacy_Doc_Instance=doc)
    unique_tokens = set()

    token_text_list = [token.text.lower() for token in doc if IsValidVocabularyWord(token)]

    for token_text in token_text_list:

        if not token_text in unique_tokens:

            unique_tokens.add(token_text)

    
    unique_words_count = len(unique_tokens)
    total_word_count = token_length

    # print(f"number of unique token: {unique_words_count}")
    # print(f"total number of tokens: {total_word_count}")

    # print(f"{2 * total_word_count}")
    # print(math.sqrt(2 * total_word_count))
    

    CTTR_value = unique_words_count / (math.sqrt(2 * total_word_count))

    # print(f"cttr_value: {CTTR_value}")

    return CTTR_value


def sample_run(text: str, window_size = 50): 

    nlp  = nlp_loader_sm()

    doc = nlp(text)

    token_list = [(token.text, token.pos_) for token in doc]

    print(token_list)

def numberOfTokens(text : str = '', spacy_Doc_Instance : spacy.tokens.Doc = nlp_loader_sm()('')):

    if text: 

        nlp = nlp_loader_sm()

        doc = nlp(text)

        token_list = [token for token in doc]

        return len(token_list)
    
    elif type(spacy_Doc_Instance) == type(nlp_loader_sm()('')):

        token_list = [token for token in spacy_Doc_Instance]

        return len(token_list)

    else:

      return 0
    

def identified_cohesive_device(doc : spacy.tokens.Doc):
    
    cohesive_devices_freq = {
        'addition' : 0,
        'contrast' : 0,
        'cause_and_effect' : 0,
        'comparison' : 0,
        'sequence' : 0,
        'exemplification' : 0,
        'clarification' : 0,
        'conlusion' : 0,
        'time' : 0
    }

    for token in doc:

        if token in cohesive_device['addition']:

            cohesive_devices_freq['addition'] += 1

        elif token in cohesive_device['contrast']:

            cohesive_devices_freq['contrast'] += 1

        else:

            cohesive_devices_freq['time'] += 1



    return cohesive_devices_freq



def IsValidVocabularyWord(token):

    #Noun
    #Verbs
    #Adjectives
    #Adverbs

    # needs condition here to check and validate the right token to contribute on the unique word

    if token.pos_ == 'NOUN' or 'VERB' or 'ADV' or 'ADJ':
        return True
    

class mini_nlp:

    @staticmethod
    def doc_loader(text:str, model='sm'):

        if model == 'sm':

            nlp = nlp_loader_sm()

            doc = nlp(text)

            return doc

        elif model == 'md':

            nlp = nlp_loader_md()

            doc = nlp(text)

            return doc
        

    @staticmethod
    def tokenlist_alpha_lowered(text:str):

        tokenlist = [token.text.lower() for token in mini_nlp.doc_loader(text=text) if token.is_alpha]

        return tokenlist
    


class SpellingDetector:

    def __init__(self, text):

        self.__checker = SpellChecker()
        self.wordcollection_text = mini_nlp.tokenlist_alpha_lowered(text=text)
        self.correctionCollection = []


        #initialize checking method
        self.InitializeErrorDetection()


    def InitializeErrorDetection(self):

        for word in self.__checker.unknown(self.wordcollection_text):

            spell_correction  = SpellCorrection(text=word, correction=self.__checker.correction(word), candidates=self.__checker.candidates(word))

            self.correctionCollection.append(spell_correction.serialized_dict())
         

    
class SpellCorrection:

    def __init__(self, text, correction, candidates):

        self.original_text = text
        self.spelling_correction = correction
        self.spelling_candidates = candidates

    def getOriginalText(self):

        return self.original_text
    
    def getCorrection(self):

        return self.spelling_correction
    
    def getCorrectionCandidates(self):

        return self.spelling_candidates
    
    def serialized_dict(self):

        return {
            'original_text' : self.original_text,
            'spelling_correction' : self.spelling_correction,
            'spelling_candidates' : list(self.spelling_candidates) 
        }

