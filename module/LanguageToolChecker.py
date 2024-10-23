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

    match_result = [
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
        for result in match_result
    ]


    sentence_list = PhraseInstance.ArrayOfSents()


    print(match_result)
    print(isinstance(match_result[0], Match))



    print('\n\n')

    print(sentence_list)

    return True


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


        self.belongsToSentenceId = None

    def setBelongsToSentenceId(self, id: int):

        self.belongsToSentenceId = id







    



