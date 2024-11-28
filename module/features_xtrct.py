import spacy
import numpy as np
import spacy.tokens

from token_tools import MATTR
from token_tools import CTTR
from constants import cohesive_device
from nlp_module import ReadbilityMeasure

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

def text_precleaning(text):


        nlp = nlp_loader_sm()

        doc = nlp(text)

        initial_string = ''

        for sent in doc.sents:

            new_sent = ' '.join(sent.text.split())
            initial_string += new_sent + ' '
      
        return initial_string


class PhraseExtract:

    def __init__(self,question: str, text: str):

        self.text = text_precleaning(text)
        self.question = text_precleaning(question)


        self.__noun_freq = 0
        self.__adj_freq = 0
        self.__adv_freq = 0
        self.__verb_freq = 0
        self.__pronoun_freq = 0
        self._proper_noun_freq = 0
        self._determiner = 0
        self._adpostiton = 0
        self._connecting_conjuction = 0
        self._subor_conjunc = 0
        self._interjection = 0
        self._numeral = 0
        self._aux = 0
        self._punc = 0
        self._symbl = 0
        self._other = 0
        self.__sentence_count = 0
      
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

        #readability_score 
        #self.readability_score = self.__readability_score()



        
        self._word_Count = self.wordCount()
        self.unique_words_ratio = self.unique_word()
        self.average_word_length = self.avg_word_length()
        self._noun_count = self.__noun_freq
        self._adj_count = self.__adj_freq
        self._adv_count = self.__adv_freq
        self._pronoun_count = self.__pronoun_freq
        self._verb_count = self.__verb_freq
        #self.subordinate_clauses_count = None
        #self.grammar_error_count = None
        #self.spelling_error_count = None
        #self.sentiment_polarity
        self.cohesive_device_count = self.cohesive_device_indentifier(only_count=True)
        self.readability_score = self.__readability_score()
        self.avg_sentence_length = self.ave_sentence_len()
        self.sentence_variation = self.SentenceVariationAnalyzer()
        self.number_of_sentence = self.get_NumberOfSentence()
        self.sentence_simple = self.sentence_variation['simple_sentence']
        self.sentence_compound = self.sentence_variation['compound']
        self.sentence_complex = self.sentence_variation['complex']
        self.topic_relevance_score = self.TopicRelevance()


    #

    
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
    def unique_word(self, token_ratio_technique='mattr') -> float:

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
    
    def __SetSelf_NumberOfSentence(self):

        self.__sentence_count = len(self.ArrayOfSents())
    
    def get_NumberOfSentence(self):

        sentence_list =  self.ArrayOfSents()

        return len(sentence_list)

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

                self._determiner += 1

            elif token.pos_ == 'PROPN':

                self._proper_noun_freq += 1

            elif token.pos_ == 'ADP':

                self._adpostiton += 1

            elif token.pos_ == 'CCONJ': 

                self._connecting_conjuction += 1

            elif token.pos_ == 'SCONJ':

                self._subor_conjunc += 1

            elif token.pos_ == 'INTJ':

                self._interjection += 1

            elif token.pos_ == 'NUM': 

                self._numeral += 1 

            elif token.pos_ == 'AUX': 

                self._aux += 1

            elif token.pos_ == 'PUNCT': 

                self._punc += 1

            elif token.pos_ == 'SYM':

                self._symbl += 1

            else:

                self._other += 1    


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

        #print('printing the sent from the generator')

        for sent in doc.sents:

            # print(f"sent: {sent}")
            # print(len(str(sent)))
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


    def cohesive_device_indentifier(self, only_count=False):

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

        COHESIVE_DEVICE_COUNT = 0
        if only_count:

            for key in key_list:

                COHESIVE_DEVICE_COUNT += cohesive_devices_freq[key]

            return COHESIVE_DEVICE_COUNT
        


        return cohesive_devices_freq
    
    def TopicRelevance(self):

        similarity_score = self.doc_md_question.similarity(self.doc_md)

        return similarity_score
    
    def __readability_score(self):

        return ReadbilityMeasure.getReadabilityScore(self.text)
    
    def getReadabilityScore(self):

        return 
    
    def SentenceVariationAnalyzer(self, with_sent_index=False):

        #Diversity of Sentence Types approach


        simple_sentence = 0
        compound_sentence = 0
        complex_sentence = 0

        token_roots = []

        sentence_index_variation = []

        for index, sent in enumerate(self.doc_sm.sents):

            root_token = [token for token in sent if token.dep_ == 'ROOT'][0]

            if any([token.dep_ == 'cc' for token in sent]):

                compound_sentence += 1

                sentence_index_variation.append((index, 'compound'))

            elif any([token.dep_ == 'mark' for token in sent]):

                complex_sentence += 1

                sentence_index_variation.append((index, 'complex'))

            else:

                simple_sentence += 1 

                sentence_index_variation.append((index, 'simple'))

            # print(sent)

        
        if with_sent_index:

            return  {
                'simple_sentence' : simple_sentence,
                'compound' : compound_sentence,
                'complex' : complex_sentence,
                'sentence_index_variation' : sentence_index_variation
            }
        
        else: 

            return  {
                'simple_sentence' : simple_sentence,
                'compound' : compound_sentence,
                'complex' : complex_sentence,
            }
        
    
    def ArrayOfSents(self):

        return list(sent.text + ' ' for sent in self.doc_sm.sents)
    
    def ArrayOfSentNoEndSpace(self):

        return list(sent.text for sent in self.doc_sm.sents)
    
    def displayFeatures(self):

        # self.wordCount = 0
        # self.unique_words_ratio = 0
        # self.avg_word_length = 0
        # self.noun_count = self.__noun_freq
        # self.adj_count = self.__adj_freq
        # self.adv_count = self.__adv_freq
        # self.pronoun_count = self.__pronoun_freq
        # self.verb_count = self.__verb_freq
        # #self.subordinate_clauses_count = None
        # #self.grammar_error_count = None
        # #self.spelling_error_count = None
        # #self.sentiment_polarity
        # #self.cohesive_device_count
        # self.readability_score = self.__readability_score()
        # self.sentence_variation = self.SentenceVariationAnalyzer()
        # self.topic_relevance_score = self.TopicRelevance()

        print(f"_word_count : {self._word_Count}")
        print(f"unique_words_ratio: {self.unique_words_ratio}")
        print(f"average_word_length : {self.average_word_length}")
        print(f"_noun_count : {self._noun_count}")
        print(f"_adj_count : {self._adj_count}")
        print(f"_adv_count : {self._adv_count}")
        print(f"_pronoun_count : {self._pronoun_count}")
        print(f"_verb_count : {self._verb_count}")
        print(f"subordinating_clauses_count : {'None for now'}")
        print(f"grammar_error_count : {'None for now'}")
        print(f"spelling_errpr_count : {'None for now'}")
        print(f"sentiment_polarity : {'None for now'}")
        print(f"cohesive_device_count : {self.cohesive_device_count}")
        print(f"readability_score : {self.readability_score}")
        print(f"avg_sentence_length : {self.avg_sentence_length}")
        print(f"sentence_variation : {self.sentence_variation}")
        print(f"sentence_simple : {self.sentence_simple}")
        print(f"sentence_compound : {self.sentence_compound}")
        print(f"sentence_complex : {self.sentence_complex}")
        print(f"topic_relevance_score : {self.topic_relevance_score}")

    def displayFeaturesSample(self):

        # self.wordCount = 0
        # self.unique_words_ratio = 0
        # self.avg_word_length = 0
        # self.noun_count = self.__noun_freq
        # self.adj_count = self.__adj_freq
        # self.adv_count = self.__adv_freq
        # self.pronoun_count = self.__pronoun_freq
        # self.verb_count = self.__verb_freq
        # #self.subordinate_clauses_count = None
        # #self.grammar_error_count = None
        # #self.spelling_error_count = None
        # #self.sentiment_polarity
        # #self.cohesive_device_count
        # self.readability_score = self.__readability_score()
        # self.sentence_variation = self.SentenceVariationAnalyzer()
        # self.topic_relevance_score = self.TopicRelevance()

        print(f"_word_count : {self._word_Count}")
        print(f"unique_words_ratio: {self.unique_words_ratio}")
        print(f"average_word_length : {self.average_word_length}")
        print(f"_noun_count : {self._noun_count}")
        print(f"_adj_count : {self._adj_count}")
        print(f"_adv_count : {self._adv_count}")
        print(f"_pronoun_count : {self._pronoun_count}")
        print(f"_verb_count : {self._verb_count}")
        print(f"_proper_noun_count : {self.__proper_noun_freq}")
        print(f"_determiner : {self.__determiner}")
        print(f"_adposition : {self.__adpostiton}")
        print(f"_connecting_conjuction : {self.__connecting_conjuction}")
        print(f"_subor_conjunc : {self.__subor_conjunc}")
        print(f"_interjection : {self.__interjection}")
        print(f"_numeral : {self.__numeral}")
        print(f"_aux : {self.__aux}")
        print(f"_punc : {self.__punc}")
        print(f"_symb : {self.__symbl}")
        print(f"subordinating_clauses_count : {'None for now'}")
        print(f"grammar_error_count : {'None for now'}")
        print(f"spelling_errpr_count : {'None for now'}")
        print(f"sentiment_polarity : {'None for now'}")
        print(f"cohesive_device_count : {self.cohesive_device_count}")
        print(f"readability_score : {self.readability_score}")
        print(f"avg_sentence_length : {self.avg_sentence_length}")
        print(f"sentence_count: {self.number_of_sentence}")
        # print(f"sentence_variation : {self.sentence_variation}")
        print(f"sentence_simple : {self.sentence_simple}")
        print(f"sentence_compound : {self.sentence_compound}")
        print(f"sentence_complex : {self.sentence_complex}")
        print(f"topic_relevance_score : {self.topic_relevance_score}")



    def getFeatures(self):

        return {
            "word_count": self._word_Count,
            "unique_word_ratio": self.unique_words_ratio,
            "average_word_length": self.average_word_length,
            "noun_count": self._noun_count,
            "adj_count": self._adj_count,
            "adv_count": self._adv_count,
            "pronoun_count": self._pronoun_count,
            "verb_count": self._verb_count,
            "subordinating_clauses_count": 0,
            "grammar_error_count": 0,
            "spelling_error_count": 0,
            "sentiment_polarity": 0,
            "cohesive_device_count": self.cohesive_device_count,
            "readability_score" : self.readability_score,
            "avg_sentence_length" : self.avg_sentence_length,
            "sentence_variation" : self.sentence_variation,
            "sentence_simple" : self.sentence_simple,
            "sentence_compound" : self.sentence_compound,
            "sentence_complex" : self.sentence_complex,
            "topic_relevance_score" : self.topic_relevance_score
        }
    


class PhraseExtract1(PhraseExtract):

    def displayFeatures(self):
        
        print(f"_word_count : {self._word_Count}")
        print(f"unique_words_ratio: {self.unique_words_ratio}")
        print(f"average_word_length : {self.average_word_length}")
        print(f"_noun_count : {self._noun_count}")
        print(f"_adj_count : {self._adj_count}")
        print(f"_adv_count : {self._adv_count}")
        print(f"_pronoun_count : {self._pronoun_count}")
        print(f"_verb_count : {self._verb_count}")
        # print(f"subordinating_clauses_count : {'None for now'}")
        # print(f"grammar_error_count : {'None for now'}")
        # print(f"spelling_errpr_count : {'None for now'}")
        # print(f"sentiment_polarity : {'None for now'}")
        print(f"cohesive_device_count : {self.cohesive_device_count}")
        print(f"readability_score : {self.readability_score}")
        print(f"avg_sentence_length : {self.avg_sentence_length}")
        print(f"sentence_count: {self.number_of_sentence}")
        # print(f"sentence_variation : {self.sentence_variation}")
        print(f"sentence_simple : {self.sentence_simple}")
        print(f"sentence_compound : {self.sentence_compound}")
        print(f"sentence_complex : {self.sentence_complex}")
        print(f"topic_relevance_score : {self.topic_relevance_score}")

        return
    
    def FeatureList(self):

        return [
            float(self._word_Count),
            float(self.unique_words_ratio),
            float(self.average_word_length),
            float(self._noun_count),
            float(self._adj_count),
            float(self._adv_count),
            float(self._pronoun_count),
            float(self._verb_count),
            float(self.cohesive_device_count),
            float(self.readability_score),
            float(self.avg_sentence_length),
            float(self.number_of_sentence),
            float(self.sentence_simple),
            float(self.sentence_compound),
            float(self.sentence_complex),
            float(self.topic_relevance_score)
        ]
    
    def FeatureList(self):

        return [
            # float(self._word_Count),
            float(self.unique_words_ratio),
            float(self.average_word_length),
            float(self._noun_count),
            float(self._adj_count),
            float(self._adv_count),
            float(self._pronoun_count),
            float(self._proper_noun_freq),
            float(self._determiner),
            float(self._adpostiton),
            float(self._connecting_conjuction),
            float(self._subor_conjunc),
            float(self._interjection),
            float(self._numeral),
            float(self._aux),
            float(self._punc),
            float(self._symbl),
            float(self._verb_count),
            float(self.cohesive_device_count),
            float(self.readability_score),
            # float(self.avg_sentence_length),
            float(self.number_of_sentence),
            float(self.sentence_simple),
            float(self.sentence_compound),
            float(self.sentence_complex),
            float(self.topic_relevance_score)
        ]
    
    def FeatureList1(self):
       
         return [
            # float(self._word_Count),
            float(self.unique_words_ratio),
            float(self.average_word_length),
            float(self._noun_count),
            float(self._adj_count),
            float(self._adv_count),
            float(self._pronoun_count),
            float(self._verb_count),
            float(self.cohesive_device_count),
            float(self.readability_score),
            # float(self.avg_sentence_length),
            float(self.sentence_simple),
            float(self.sentence_compound),
            float(self.sentence_complex),
            float(self.topic_relevance_score)
        ]



    


        



    
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
    


class Sent_Variation_Analyzer:



    def main():


        return


