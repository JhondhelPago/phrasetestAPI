#import libraries
# from sentence_transformers import SentenceTransformer, util # need to be uninstall to he virtual envs
from rake_nltk import Rake










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
