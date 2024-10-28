import requests
import json

from features_xtrct import PhraseExtract

LanguageToolAPI = 'https://api.languagetool.org/v2/check'

def LangToolChecker(text):

    response = requests.post(LanguageToolAPI, 
        data={
            'text' : text,
            'language' : 'en-US',
        }
    )


    if response.status_code == 200:

        result = response.json()
        matches = result.get('matches', [])

        return matches
    
    else:
        print('Error post request to the langiage tool api')
        return "request did not satisfy. no feedback response."
    


def EssayExamineErrorSuggest(PhraseInstance : PhraseExtract):

    

    match_result =  LangToolChecker(PhraseInstance.text)
    sentence_list_original = PhraseInstance.ArrayOfSentNoEndSpace()

    sentence_list_copy = sentence_list_original

    #Dict for storing the sentence list
    SentenceCollection = dict()

    
    def findMatchingSent(MatchObject : Match):

        nonlocal sentence_list_copy
        nonlocal SentenceCollection

        #get the MatchObject.sentence
        #find the associated sentence then assign the index using the MatchObject.BelongsToSetenceId(index)
        
        # index  = sentence_list_copy.index(MatchObject.sentence)

        # MatchObject.BelongsToSentenceId(index)


        index = sentence_list_copy.index(MatchObject.sentence)

        MatchObject.BelongsToSentenceId(index)

        #check here if the key exist, if exist append the sentence to the list using the key
        #else, instantiate the dictionary with key and assign an empty list

        if index in SentenceCollection:

            SentenceCollection[index].append(MatchObject)

        else:

            SentenceCollection[index] = list()
            SentenceCollection[index].append(MatchObject)


        return MatchObject
    

    match_result = [
        findMatchingSent(
            Match(
                message=result['message'],
                shortMessage=result['shortMessage'],
                replacements=result['replacements'],
                offset=result['offset'],
                length=result['length'],
                context=result['context'],
                sentence=result['sentence'],
                type=result['type'],
                rule=result['rule'],
                ignoreForIncompleteSentence=result['ignoreForIncompleteSentence'],
                contextForSureMatch=result['contextForSureMatch']
            )
        )

        for result in match_result
    ]


    print('SentenceCollection dictionary')


    print(SentenceCollection)

    SentenceCollection_keys = sorted(list(SentenceCollection.keys()))
    print(f"keys: {SentenceCollection_keys}")



    SentenceListContainer = list()

    for index_key in SentenceCollection_keys:

        if len(SentenceCollection[index_key]) > 1:

            #Merging Process


            pass

        else:

            #Append to a list
            SentenceListContainer.append(SentenceCollection[index_key][0])







    return match_result

    

def OffsetFinder(text, offset_value):

    return text[offset_value]


class Match:

    def __init__(self, message, shortMessage, replacements, offset, length, context, sentence, type, rule, ignoreForIncompleteSentence, contextForSureMatch):
    
        self.message = message
        self.shortMessage =  shortMessage
        self.replacements = replacements
        self.offset = offset
        self.length = length
        self.context = context
        self.sentence = sentence
        self.type = type
        self.rule = rule
        self.ignoreForIncompleteSentence = ignoreForIncompleteSentence
        self.contextForSureMatch = contextForSureMatch


        self.SentenceId = None

    def BelongsToSentenceId(self, id: int):

        self.SentenceId = id

    def getDictPropeties(self):

        return {
            'message' : self.message,
            'shortMessage' : self.shortMessage,
            'replacements' : self.replacements,
            'offset' : self.offset,
            'length' : self.length,
            'context' : self.context,
            'sentence' : self.sentence,
            'type' : self.type,
            'rule' : self.rule,
            'ignoreForIncompleteSentence' : self.ignoreForIncompleteSentence,
            'contextForSureMatch' : self.contextForSureMatch,
            'SentenceId' : self.SentenceId
        }
    
    def Print_getDictProperites(self):

        DictProperties = self.getDictPropeties()
        

        print(f"message: {DictProperties['message']}")
        print(f"shortMessage: {DictProperties['shortMessage']}")
        print(f"replacements: {DictProperties['replacements']}")
        print(f"offset: {DictProperties['offset']}")
        print(f"length: {DictProperties['length']}")
        print(f"context: {DictProperties['context']}")
        print(f"sentence: {DictProperties['sentence']}")
        print(f"type: {DictProperties['type']}")
        print(f"rule: {DictProperties['rule']}")
        print(f"ignoreForIncompleteSentence: {DictProperties['ignoreForIncompleteSentence']}")
        print(f"contextForSureMatch: {DictProperties['contextForSureMatch']}")
        print(f"SentenceId: {DictProperties['SentenceId']}")

        print('\n')



#This function takes a list of MatchObject then merge the elements into single Matchobject then return.
def MatchMerger(MatchObjectList : list[Match]) -> Match:


    #SentencePlaceHolder

    #For each MatchObject.sentence merge the replacement to the SentencePlaceHolder

    #Return the merged MatchObject


    return 






    



