import spacy.tokens

from token_tools import MATTR
from token_tools import CTTR
from constants import cohesive_device
from nlp_module import ReadbilityMeasure

#single instance of the nlp model to be used in the custome classes
#load an nlp module both sm and md above the file

nlp_sm = spacy.load('en_core_web_sm')
nlp_md = spacy.load('en_core_web_md')


#define the important class
# PhraseExtract

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


    def ArrayOfSent(self):

        return list(sent.text + '' for sent in self.doc_text.sents)

    def ArrayOfSentNOEndSpace(self):
                              
        return list(sent.text for sent in self.doc_text.sents)
    
    def get_NumberOfSentence(self):

        return len(self.ArrayOfSent())

    def feature_dict(self):

        return {
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
            'symbol': self.symbl

        }


    

