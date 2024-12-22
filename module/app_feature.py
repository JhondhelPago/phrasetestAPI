# Vocabulary Assessment
# Contextual Understanding
# Difficulty Assesment





# Vocab_Assess class what will accept PhraseExtract object instance.
# getting the count of the POS
# find the pos the the composition is lacking
# Indentify the the repeated word and make and suggest the alternate word to enrich the vocabulary
# Output - List of redundant word with its alternative replacement.

from wordfreq import word_frequency
from new_features_xtract import PhraseExtract



class Vocabulary:

    def __init__(self, Phrase : PhraseExtract):
        self.PhraseObject = Phrase
        self.wordList = []
        self.vocabulary = {}
        self.redundant_word = []

        self.__setupforThisClass()
    
    def __setupforThisClass(self):

        self.wordList = self.PhraseObject.pureWords()

    def freq_sample(self): # higher frequency distribution means it is a common word

        return f"{self.wordList[2]} : {word_frequency(self.wordList[2], 'en'):.9f}"








    