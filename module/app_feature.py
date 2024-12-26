# Vocabulary Assessment
# Contextual Understanding
# Difficulty Assesment





# Vocab_Assess class what will accept PhraseExtract object instance.
# getting the count of the POS
# find the pos the the composition is lacking
# Indentify the the repeated word and make and suggest the alternate word to enrich the vocabulary
# Output - List of redundant word with its alternative replacement.

from nltk.corpus import words, wordnet
from wordfreq import word_frequency
from PyDictionary import PyDictionary
from new_features_xtract import PhraseExtract


default_dictionary =  PyDictionary()


def synonyms(word : str):

    return default_dictionary.synonym(word.lower())

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def sort_synonyms(word : str, alter_word : list[str]):



    return 


class Vocabulary:

    def __init__(self, Phrase : PhraseExtract):
        self.PhraseObject = Phrase
        self.wordList = []
        self.vocabulary = {}
        self.repeated_word = []
        self.word_freq_pair = [] # the elements are tuples ('word', frequency_value : float)

        self.__setupforThisClass()
    
    def __setupforThisClass(self):

        self.wordList = list(set(self.PhraseObject.pureWords()))

        self.word_freq_process()
        self.repeatedWordPreProcess()

    def isWordExist(self, word : str):

        return word.lower() in words.words()

    def freq_sample(self): # higher frequency distribution means it is a common word

        return f"{'asdagadff'} : {word_frequency('asdagadff', 'en'):.9f}"
    
    def word_freq(self, word : str):

        return word_frequency(word, 'en')
    
    def word_freq_process(self):

        word_pairs = list()

        for word in self.wordList:

            word_pairs.append((word, self.word_freq(word)))

        
        self.word_freq_pair = sorted(word_pairs, key=lambda x: x[1], reverse=True)


    def display_freq(self):

        for word in self.wordList:

            print(f"{word} : {self.word_freq(word):.9f}")


    #detecting the redundant word in the self.PhraseObject.pureWords()
    #append to a list those word that is repeatedly used.
    #sort the word by its number its detected/used. reverse=True
    #return the list of redundant word
    def repeatedWordPreProcess(self):

        word_dict = dict()

        for word in self.PhraseObject.pureWords():

            word = word.lower()

            if word in word_dict:

                word_dict[word] += 1

            else:

                word_dict[word] = 1


        dict_key_list = list(word_dict.keys())

        for key in dict_key_list:

            self.repeated_word.append((key, word_dict[key]))

        
        self.repeated_word = sorted(self.repeated_word, key=lambda x: x[1], reverse=True)


# cut the self.repeated_word.
# get the top 10 and remove the single instance
# for each word in list of ten words, pass the word to the get_synonyms funtion
# return the list of synonyms, then pre-process it to the semanrtic similarity, and sort the result, get the only the relevant word for the final return















    