import spacy


class nlp_sm:

    def __init__(self, text : str):
        self.__nlp_sm = spacy.load('en_core_web_sm')
        self.text = text
        self.doc = self.__nlp_sm(self.text) 

        

    
    def getDocInstance(self):

        return self.doc
    

    def getWordCount(self):

        word_list = list(self.doc)

        return len(word_list)

    def generateToken(self):

        for token in self.doc:
            print(f"{token.text}, POS:{token.pos_}")