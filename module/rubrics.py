#import libraries
from sentence_transformers import SentenceTransformer, util
from rake_nltk import Rake





#helping functions



class Ideas:

    @staticmethod
    def testingSimilarity(text_list):

        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

        sentence_list = text_list

        embiddings = model.encode(sentence_list, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embiddings[0], embiddings[1])

        return similarity


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
