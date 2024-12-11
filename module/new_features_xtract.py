import spacy.tokens

from token_tools import MATTR
from token_tools import CTTR
from constants import cohesive_device
from nlp_module import ReadbilityMeasure

class TypeTokenRatioError(Exception):
    
    def __init__(self, err_message):
        self.error_message = err_message
        super().__init__(self.error_message)

#single instance of the nlp model to be used in the custome classes
#load an nlp module both sm and md above the file

nlp_sm = spacy.load('en_core_web_sm')
nlp_md = spacy.load('en_core_web_md')


#define the important class
# PhraseExtract

# TYPE TOKEN RATIO


class PhraseExtract:

    def __init__(self,question: str, text: str):

        self.doc_text = nlp_md(text)
        self.doc_question = nlp_md(question)

        self.text = self.doc_text.text
        self.question = self.doc_question.text




        self.noun_freq = 0
        self.adj_freq = 0
        self.adv_freq = 0
        self.verb_freq = 0
        self.pronoun_freq = 0
        self.proper_noun_freq = 0
        self.determiner = 0
        self.adpostiton = 0
        self.connecting_conjuction = 0
        self.subor_conjunc = 0
        self.interjection = 0
        self.numeral = 0
        self.aux = 0
        self.punc = 0
        self.symbl = 0
        self.other = 0
        self.sentence_count = 0
      

        self.unique_words_ratio = self.unique_word()
        self.topic_relevance_score = self.TopicRelevance()

        #Initial function run

        self.Pos_Identifier()
      

        #Make the document instance of the text and question
        #self.__SimilaritLevel =  self.TopicRelevance()


    
    #part of speech frequency

    def Pos_Identifier(self):

        for token in self.doc_text:

            if token.pos_ == 'NOUN':

                self.noun_freq += 1

            elif token.pos_ == 'VERB':

                self.verb_freq += 1

            elif token.pos_ == 'ADJ':

                self.adj_freq += 1 

            elif token.pos_ == 'ADV':

                self.adv_freq =+ 1

            elif token.pos_ == 'PRON':

                self.pronoun_freq += 1

            elif token.pos_ == 'DET':

                self.determiner += 1

            elif token.pos_ == 'PROPN':

                self.proper_noun_freq += 1

            elif token.pos_ == 'ADP':

                self.adpostiton += 1

            elif token.pos_ == 'CCONJ':

                self.connecting_conjuction += 1

            elif token.pos_ == 'SCONJ':

                self.subor_conjunc += 1

            elif token.pos_ == 'INTJ':

                self.interjection += 1

            elif token.pos_ == 'NUM':

                self.numeral += 1

            elif token.pos_ == 'AUX':

                self.aux += 1

            elif token.pos_ == 'PUNCT':

                self.punc += 1

            elif token.pos_ == 'SYM':

                self.symbl += 1

    # feature function
    def unique_word(self, token_ratio_technique='mattr') -> float:

        #MATTR
        if token_ratio_technique == 'mattr':

            return MATTR(self.doc_text)

        #CTTR
        elif token_ratio_technique == 'cttr':

            return CTTR(self.doc_text)
        
        else:

            raise TypeTokenRatioError('Invalid argument value for token_ratio_technique. The option value for \'token_ratio_technique\' are \'mattr\' | \'cttr\' only.')

    def TopicRelevance(self):

        similarity_score = self.doc_question.similarity(self.doc_text)

        return similarity_score


    # secondary function
    def ArrayOfSent(self):

        return list(sent.text + '' for sent in self.doc_text.sents)

    def ArrayOfSentNOEndSpace(self):
                              
        return list(sent.text for sent in self.doc_text.sents)
    
    def get_NumberOfSentence(self):

        return len(self.ArrayOfSent())

    def feature_dict(self):

        return {
            #pos
            'noun': self.noun_freq,
            'verb': self.verb_freq,
            'adjective': self.adj_freq,
            'adverb': self.adv_freq,
            'pronoun': self.pronoun_freq,
            'determiner': self.determiner,
            'proper_noun': self.proper_noun_freq,
            'adposition': self.adpostiton,
            'conjunction': self.connecting_conjuction,
            'subordinating_conjunction': self.subor_conjunc,
            'interjection': self.interjection,
            'numeral': self.numeral,
            'auxiliary': self.aux,
            'punctuation': self.punc,
            'symbol': self.symbl,

            #feature_param
            'unique_words_ratio' : self.unique_words_ratio,
            'topic_relevance_score' : self.topic_relevance_score
            

        }


    

