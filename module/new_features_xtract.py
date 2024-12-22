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
      

        self.word_count = self.wordCount(self.doc_text)
        self.unique_words_ratio = self.unique_word()
        self.topic_relevance_score = self.TopicRelevance()
        self.readability_score = ReadbilityMeasure.getReadabilityScore(self.text)
        self.readability_grade_level = ReadbilityMeasure.getReadabilityGradeLevel(self.text)
        self.avg_sentence_length = self.ave_sentence_len()
        self.cohesive_device_count = self.cohesive_device_indentifier(only_count=True)
        self.number_of_sentence = self.get_NumberOfSentence()
        self.sentence_variation = self.SentenceVariationAnalyzer()
        self.sentence_simple = self.sentence_variation['simple']
        self.sentence_compound = self.sentence_variation['compound']
        self.sentence_complex = self.sentence_variation['complex']


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
    def wordCount(self, doc: spacy.tokens.doc):
    
        # tokenization of the word

        token_list = [token for token in doc if token.is_alpha]

        # count = 1
        # for token in doc:

        #     if token.is_alpha:

        #         print(f"word: {token.text},  token_count: {count}")
        #         count += 1

        return len(token_list)

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

    def SentenceVariationAnalyzer(self, with_sent_index=False):

        #Diversity of Sentence Types approach


        simple_sentence = 0
        compound_sentence = 0
        complex_sentence = 0

        token_roots = []

        sentence_index_variation = []

        for index, sent in enumerate(self.doc_text.sents):

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


        #return [simple_sentence, compound_sentence, complex_sentence]
        return {
            'simple' : simple_sentence,
            'compound' : compound_sentence,
            'complex' : complex_sentence
        }
    
    def ave_sentence_len(self):

        #function here to clean the format of the text
        # more than two white spaces must be automatically formatted before the code blocks below runs.

        char_len = 0
        sent_quanti = 0

        #print('printing the sent from the generator')

        for sent in self.doc_text.sents:

            # print(f"sent: {sent}")
            # print(len(str(sent)))
            char_len += len(str(sent))
            sent_quanti += 1

        return char_len / sent_quanti
    
    
    def cohesive_device_indentifier(self, only_count=False):

        doc = self.doc_text
       
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
    


    # secondary function
    def pureWords(self) -> list[str]: # return a word -> str type, pure none stopping owrd from the text property of this class

        words = [token.text.strip() for token in self.doc_text if not token.is_stop and not token.is_punct and token.is_alpha and token.text.strip() != '']

        return words

    def ArrayOfSent(self):

        return list(sent.text + '' for sent in self.doc_text.sents)

    def ArrayOfSentNOEndSpace(self):
                              
        return list(sent.text for sent in self.doc_text.sents)
    
    def get_NumberOfSentence(self):

        return len(self.ArrayOfSent())
    
    ## Analysing the topic Relevance of the sentence of each sentence to the context in this object
    def topic_relevance_sent_level(self):

        per_sent_relevance = list()

        
        for sent in self.doc_text.sents:

            sent_doc = nlp_md(sent.text)

            similarity = self.doc_question.similarity(sent_doc)

            per_sent_relevance.append(similarity)



        return per_sent_relevance



    def feature_dict(self):

        return {
            #pos
            'word_count' : self.word_count,
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
            'avg_sentence_length' : self.avg_sentence_length,
            'sentence_count' : self.number_of_sentence,
            'sentence_variation' : self.sentence_variation,
            'sentence_simple' : self.sentence_simple,
            'sentence_compound' : self.sentence_compound,
            'sentence_complex' : self.sentence_complex,
            'cohesive_device_count' : self.cohesive_device_count,
            'readability_score' : self.readability_score,
            'readanility_grade_level' : self.readability_grade_level,
            'topic_relevance_score' : self.topic_relevance_score,
        }
    
    def feature_list_sample(self):

        return [
            float(self.noun_freq), #noun
            float(self.verb_freq), #verb
            float(self.adj_freq), #adjective
            float(self.adv_freq),  #adverb
            float(self.pronoun_freq), #pronoun
            float(self.determiner), #determiner
            float(self.proper_noun_freq), #propernoun
            float(self.adpostiton), #adposition
            float(self.connecting_conjuction), #conencting_conjuction
            float(self.subor_conjunc), # subordinating_conjuction
            float(self.interjection), #interjection
            float(self.numeral), # numeral
            float(self.aux), # auxilliary
            float(self.punc), # punctuation
            float(self.symbl), #symbol

            float(self.word_count), # word_count
            float(self.unique_words_ratio), #vocabulary_score
            float(self.avg_sentence_length), #sentence_length
            float(self.number_of_sentence), #number_of_setence
            float(self.sentence_simple), #sentence_simmple
            float(self.sentence_compound), #sentence_compound
            float(self.sentence_complex), #sentence_complex
            float(self.cohesive_device_count), #cohesive_device
            float(self.readability_score), #readability_score
            float(self.readability_grade_level), #readability_grade_level
            float(self.topic_relevance_score) #topic_relevance
        ]

    def feature_dict_test(self):

        return {
            #pos
            'word_count' : self.word_count,
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
            'avg_sentence_length' : self.avg_sentence_length,
            'sentence_count' : self.number_of_sentence,
            'sentence_variation' : self.sentence_variation,
            'sentence_simple' : self.sentence_simple,
            'sentence_compound' : self.sentence_compound,
            'sentence_complex' : self.sentence_complex,
            'cohesive_device_count' : self.cohesive_device_count,
            'readability_score' : self.readability_score,
            'readanility_grade_level' : self.readability_grade_level,
            'topic_relevance_score' : self.topic_relevance_score,
        }
    
    def feature_list_sample_test(self):

        return [
            float(self.noun_freq), #noun
            float(self.verb_freq), #verb
            float(self.adj_freq), #adjective
            float(self.adv_freq),  #adverb
            float(self.pronoun_freq), #pronoun
            float(self.determiner), #determiner
            float(self.proper_noun_freq), #propernoun
            float(self.adpostiton), #adposition
            float(self.connecting_conjuction), #conencting_conjuction
            float(self.subor_conjunc), # subordinating_conjuction
            float(self.interjection), #interjection
            float(self.numeral), # numeral
            float(self.aux), # auxilliary
            float(self.punc), # punctuation
            float(self.symbl), #symbol

            float(self.word_count), # word_count
            float(self.unique_words_ratio), #vocabulary_score
            float(self.avg_sentence_length), #sentence_length
            float(self.number_of_sentence), #number_of_setence
            float(self.sentence_simple), #sentence_simmple
            float(self.sentence_compound), #sentence_compound
            float(self.sentence_complex), #sentence_complex
            float(self.cohesive_device_count), #cohesive_device
            float(self.readability_score), #readability_score
            float(self.readability_grade_level), #readability_grade_level
            float(self.topic_relevance_score) #topic_relevance
        ]

    

