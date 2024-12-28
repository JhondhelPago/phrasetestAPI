import requests
import json

# from features_xtrct import PhraseExtract
from new_features_xtract import PhraseExtract

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

        #applying the replacement to the sentence
        self.modif_sentence = None
        self.FinalSentence = None
        self.applyReplacement()



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
            'SentenceId' : self.SentenceId,
            'SentenceModif' : self.modif_sentence,
            'FinalSentence' : self.FinalSentence
        }
    
    def getImportantBody(self):

        return{
            'message' : self.message,
            'shortMessage' : self.shortMessage,
            'replacements' : self.replacements[0]['value'],
            'context' : self.context['text'],
            'sentence' : self.sentence, 
            'final_sentence' : self.FinalSentence,
            'sentence_id' : self.SentenceId
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
        print(f"SentenceModif: {DictProperties['SentenceModif']}")
        print(f"FinalSetence: {DictProperties['FinalSentence']}")

        print('\n')

    def applyReplacement(self):

        replacement_value = self.replacements[0]['value']

        context_copy = self.context['text']

        offset = self.context['offset']

        pre_modif_sentence = removeBothEndsDots(SubStringInsertion(original_string=context_copy, start_index=offset, replacement_string=replacement_value, offset_length=self.context['length']))

        pre_modif_sentence_offset = FindSubStringPosition(SuperString=self.sentence, Substring=removeBothEndsDots(context_copy))

        self.modif_sentence = pre_modif_sentence

        #if pre_modif_sentence length is greater equal context copy -> use SubStringInsertion()

        #else -> use SentenceMerginigSolution()


        self.FinalSentence =  SubStringInsertion(original_string=self.sentence, start_index=pre_modif_sentence_offset, replacement_string=pre_modif_sentence, offset_length=len(removeBothEndsDots(context_copy)))
        #self.modif_sentence = pre_modif_sentence


#charcter replacement -> Done
#character removal -> Logical Error
#there is a bug here in this function
def SubStringInsertion(original_string, start_index, replacement_string, offset_length=0):

    #get here the left substrting using the start_index and the offset_length
    #get here the right substring using the start_index and the offset_length

    left_sub = original_string[:start_index]
    right_sub = original_string[start_index + offset_length:]

    

  
    #char_length = len(replacement_string)

    #end_index = start_index  + len(replacement_string)

    #modif_string = original_string[:start_index] + replacement_string + original_string[end_index:]

    modif_string = left_sub + replacement_string + right_sub

    return modif_string

def SentenceMerginSolution(orignal_string, start_index, process_substring):

    return

def removeBothEndsDots(String):
    end_index = len(String) - 3
    newString = String[3:end_index]

    return newString

def FindSubStringPosition(SuperString, Substring):

    index = SuperString.find(Substring)

    return index


#This function takes a list of MatchObject then merge the elements into single Matchobject then return.
def MatchMerger(MatchObjectList : list[Match]) -> Match:

    #OriginalSentenceRerence

    #SentencePlaceHolder

    #For each MatchObject.SentenceModif merge to the SentencePlaceHolder

    #Set MatchObject.FinalSentence = SentencePlaceHolder

    #Return the merged MatchObject


    return 




class ResultCheker:

    def __init__(self, sent_index, text):
        
        self.sent_index = sent_index,
        self.text = text
        self.modif_text = text


        self.result_langtoolcheacker = None
        self.MessageList = list()

        self.errorMessageList = None
        self.corrected_text = None


        self.initial_call_langtoolcheacker()

        self.ResolveSuggestion()
    
    def initial_call_langtoolcheacker(self):

        
        self.result_langtoolcheacker = LangToolChecker(self.text)


    def DisplayErrorList(self):

        for error_dict in self.result_langtoolcheacker:

            print(f"sentence number {self.sent_index} \n")

            print(f"message:  {error_dict['message']}")
            print(f"shortMessage: {error_dict['shortMessage']}")
            print(f"replacements: {error_dict['replacements']}")
            print(f"offset: {error_dict['offset']}")
            print(f"length: {error_dict['length']}")
            print(f"context: {error_dict['context']}")
            print(f"sentence: {error_dict['sentence']}")
            print(f"type: {error_dict['type']}")
            print(f"rule: {error_dict['rule']}")
            print(f"ignoreForIncompleteSentence: {error_dict['ignoreForIncompleteSentence']}")
            print(f"contextForSureMatch: {error_dict['contextForSureMatch']}")

            print('\n\n')

    def ReplacementInsertion(self, replacement_string, original_string, offset, length):

        left_string = original_string[:offset]
        right_string = original_string[offset+length:]


        # return (left_string, replacement, right_string) 
        return left_string + replacement_string + right_string

    def ResolveSuggestion(self):

        mathces = LangToolChecker(self.modif_text)

        if not mathces:

            return
        
        else:

            error_1 = mathces[0]


            self.MessageList.append(error_1['message'])
            offset = error_1['offset']
            length = error_1['length']
            replacement = error_1['replacements'][0]['value']


            self.modif_text = self.ReplacementInsertion(replacement, self.modif_text, offset, length)

            #Recursion
            self.ResolveSuggestion()





