import spacy
import numpy as np
import spacy.tokens

from token_tools import MATTR
from token_tools import CTTR
from constants import cohesive_device

class TypeTokenRatioError(Exception):
    
    def __init__(self, err_message):
        self.error_message = err_message
        super().__init__(self.error_message)


def nlp_loader_sm():

    return spacy.load('en_core_web_sm')

def nlp_loader_md():
    
    return spacy.load('en_core_web_md')


def wordCount(doc: spacy.tokens.doc):
    
    # tokenization of the word

    token_list = [token for token in doc if token.is_alpha]

    # count = 1
    # for token in doc:

    #     if token.is_alpha:

    #         print(f"word: {token.text},  token_count: {count}")
    #         count += 1

    return len(token_list)


def tokenGenerator(doc: spacy.tokens.doc):

    for token in doc:

        if not token.is_space:
            print(f"text: {token.text}, pos_:{token.pos_}")


def tokenSize(doc : spacy.tokens.doc):

    return len([token for token in doc if not token.is_space])


class PhraseExtract:

    def __init__(self,question: str, text: str):

        self.text = text
        self.question = question

        self.__noun_freq = 0
        self.__adj_freq = 0
        self.__adv_freq = 0
        self.__verb_freq = 0
        self.__pronoun_freq = 0
        self.__proper_noun_freq = 0
        self.__determiner = 0
        self.__adpostiton = 0
        self.__connecting_conjuction = 0
        self.__subor_conjunc = 0
        self.__interjection = 0
        self.__numeral = 0
        self.__aux = 0
        self.__punc = 0
        self.__symbl = 0
        self.__other = 0


        # model instance in the inside the class
        self.en_core_web_sm = self.__load_sm_Model()
        self.en_core_web_md = self.__load_md_Model()


        #spacy document instance
        self.doc_sm = self.__load_sm_Model()(self.text)
        self.doc_md = self.__load_md_Model()(self.text)
        self.doc_md_question = self.__load_md_Model()(self.question)

        self.__SimilaritLevel =  self.TopicRelevance()

        # initial function opertions
        self.__tokenPOS_Identifier()

    
    #load small english language model
    def __load_sm_Model(self): #private function only on the scope of the class

        return spacy.load('en_core_web_sm')

    #load medium english language model    
    def __load_md_Model(self):  #private function only on the scope of the class

        return spacy.load('en_core_web_md')
    

    def wordCount(self):

        return wordCount(self.doc_sm)
    
    
    def tokenSize(self):

        return tokenSize(self.doc_sm)
    

    def tokenGenerator(self):

        tokenGenerator(self.doc_sm)


    def getSimilarityScore(self):

        return self.__SimilaritLevel

    ## MATTR or CTTR
    def unique_word(self, token_ratio_technique='mattr'):

        #MATTR
        if token_ratio_technique == 'mattr':

            return MATTR(self.doc_sm)

        #CTTR
        elif token_ratio_technique == 'cttr':

            return CTTR(self.doc_sm)
        
        else:

            raise TypeTokenRatioError('Invalid argument value for token_ratio_technique. The option value for \'token_ratio_technique\' are \'mattr\' | \'cttr\' only.')
        

    def avg_word_length(self):

        nlp = self.__load_sm_Model()

        doc = nlp(self.text)

        list_token_len = [] 

        for token in doc:

            if token.is_alpha:

                list_token_len.append(len(token.text))

        return sum(list_token_len)/len(list_token_len)


    def __tokenPOS_Identifier(self):

        nlp = self.__load_md_Model()

        for token in nlp(self.text):

            if token.pos_ == 'NOUN':

                self.__noun_freq += 1

            elif token.pos_ == 'VERB':

                self.__verb_freq += 1

            elif token.pos_ == 'ADJ':

                self.__adj_freq += 1

            elif token.pos_ == 'ADV':

                self.__adv_freq += 1

            elif token.pos_ == 'PRON':

                self.__pronoun_freq += 1

            elif token.pos_ == 'DET':

                self.__determiner += 1

            elif token.pos_ == 'PROPN':

                self.__proper_noun_freq += 1

            elif token.pos_ == 'ADP':

                self.__adpostiton += 1

            elif token.pos_ == 'CCONJ': 

                self.__connecting_conjuction += 1

            elif token.pos_ == 'SCONJ':

                self.__subor_conjunc += 1

            elif token.pos_ == 'INTJ':

                self.__interjection += 1

            elif token.pos_ == 'NUM': 

                self.__numeral += 1 

            elif token.pos_ == 'AUX': 

                self.__aux += 1

            elif token.pos_ == 'PUNCT': 

                self.__punc += 1

            elif token.pos_ == 'SYM':

                self.__symbl += 1

            else:

                self.__other += 1    


    def noun_count(self):

        return self.__noun_freq
    
    def adj_count(self):

        return self.__adj_freq

    def adv_count(self):

        return self.__adv_freq
    
    def pronoun_count(self):

        return self.__pronoun_freq
    
    def verb_count(self):
        
        return self.__verb_freq 
    
    def proper_noun_count(self):

        return self.__proper_noun_freq
    
    def determiner_count(self):

        return self.__determiner
    
    def adposition_count(self):

        return self.__adpostiton
    
    def connecting_conjuction_count(self):

        return self.__connecting_conjuction
    
    def subordination_conjunction_count(self):

        return self.__subor_conjunc
    
    def interjection_count(self):

        return self.__interjection
    
    def numerical_count(self):

        return self.__numeral
    
    def auxiliary_verb_count(self):

        return self.__aux
    
    def punctuation_count(self):

        return self.__punc
    
    def symbol_count(self):

        return self.__symbl
    
    def undefined_pos_(self):

        return self.__other
    
    def POS_frequency(self):

        return {
            'noun' : self.noun_count(),
            'adjective' : self.adj_count(),
            'adverb' : self.adv_count(),
            'pronoun' : self.pronoun_count(),
            'verb' : self.verb_count(),
            'proper_noun' : self. proper_noun_count(),
            'determiner' : self.determiner_count(),
            'adpostion' : self.adposition_count(),
            'connecting_conjuction' : self.connecting_conjuction_count(),
            'subordination_conjunction' : self.subordination_conjunction_count(),
            'interjection' : self.interjection_count(),
            'numerical' : self.numerical_count(),
            'auxiliary_verb' : self.auxiliary_verb_count(),
            'punctuation' : self.punctuation_count(),
            'auxiliary_verb' : self.auxiliary_verb_count(),
            'punctuation' : self.punctuation_count(),
            'symbol' : self.symbol_count(),
            'undefined_pos' : self.undefined_pos_() 
        }

    def ave_sentence_len(self):
        
        nlp = self.__load_sm_Model()

        doc = nlp(self.text)


        #function here to clean the format of the text
        # more than two white spaces must be automatically formatted before the code blocks below runs.

        char_len = 0
        sent_quanti = 0

        print('printing the sent from the generator')

        for sent in doc.sents:

            print(f"sent: {sent}")
            print(len(str(sent)))
            char_len += len(str(sent))
            sent_quanti += 1

        return char_len / sent_quanti
    

    def display_meta_pos(self):

        print(f"noun count: {self.noun_count()}")
        print(f"adjective count: {self.adv_count()}")
        print(f"adverb count: {self.adv_count()}")
        print(f"pronoun count: {self.pronoun_count()}")
        print(f"verb count: {self.verb_count()}")


    def sentence_count(self) -> int:

        sentence_number = len([sent for sent in self.doc_sm.sents])

        return sentence_number


    def cohesive_device_indentifier(self):

        doc = self.doc_sm 
       
        cohesive_devices_freq = {
            'addition' : 0,
            'contrast' : 0,
            'result' : 0,
            'comparison' : 0,
            'enumeration' : 0,
            'exemplification' : 0,
            'reformulation' : 0,
            'summary' : 0,
            'time' : 0,
            'inference' : 0
        }

        key_list = list(cohesive_device.keys())

        device_found = []

        for sent in doc.sents:

            # new condition to ask here
            # loop to the cohesive device and ask if the cohive device is substring of a suoer string,  the super string is the sentence in lowercase format 

            string_sent = sent.text

            token_lower_list = [token.text.lower() for token in sent]

            string_sent = ' '.join(token_lower_list)

            for key in key_list:

                for device in cohesive_device[key]:

                    if device in string_sent:

                        cohesive_devices_freq[key] += 1

                        device_found.append(device)

        return cohesive_devices_freq
    
    def TopicRelevance(self):

        similarity_score = self.doc_md_question.similarity(self.doc_md)

        return similarity_score
    
    def ArrayOfSents(self):

        return list(sent.text for sent in self.doc_sm.sents)
    


        



    
class TopicRelevance:

    def __init__(self, question, essaycomposition) -> None:
        
        self.question = self.__nlp_Loader_md(question)
        self.essaycomposition = self.__nlp_Loader_md(essaycomposition)


    def __nlp_Loader_md(self, text):

        nlp = spacy.load('en_core_web_md')
        doc = nlp(text)

        return doc


    def calculateRelevance(self):

        similarity_score = self.essaycomposition.similarity(self.essaycomposition)

        return similarity_score


