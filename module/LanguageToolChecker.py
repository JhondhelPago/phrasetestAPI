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

    
    def findMatchingSent(MatchObject : Match):

        nonlocal sentence_list_copy

        #get the MatchObject.sentence
        #find the associated sentence then assign the index using the MatchObject.BelongsToSetenceId(index)
        
        # index  = sentence_list_copy.index(MatchObject.sentence)

        # MatchObject.BelongsToSentenceId(index)


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



    for sent in sentence_list_original:
        print(sent)



    print('\n\n')

    print('sentence_list_copy')
    for sentence in sentence_list_copy:

        print(sentence)



    print('\n\n')


    

    #inverted login in the for loop
    # should first lopp to the sentence, then access eache element in the match_result and get the sentence property.
    #then match if the MatchObject is == to the current sentece state
    for MatchObject in match_result:


        for index, sent in enumerate(sentence_list_copy):

            print(f"index : {index}")
            print('\n')

            print(f"sent:{sent}")
            print(f"MatchObject.sentence:{MatchObject.sentence}")
            print(f"match resut:{sent == MatchObject.sentence}")

            print('\n')

            if sent == MatchObject.sentence:

                MatchObject.BelongsToSentenceId(index)



        print(f"MatchObject BelongsToSentenceID: {MatchObject.SentenceId}, MatchObject sentence: {MatchObject.sentence}")



    #loop to the match_result using foreach
    #access the Match().sentence
    #find the matching sent from the PhraseExtract.ArrayOfSent()
        #if found pop the sent from the PhraseExract.ArrayOfSent(), and store it to another list

    



    return True


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

        self.belongsToSentenceId = id

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
            'contextForSureMatch' : self.contextForSureMatch
        }

#This function takes a list of MatchObject then merge the elements into single Matchobject then return.
def MatchMerger(MatchObjectList : list[Match]) -> Match:


    return 






    



