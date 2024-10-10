from LanguageToolChecker import LangToolChecker
from features_xtrct import PhraseExtract

# [
#     'message',
#     'shortMessage',
#     'replacements',
#     'offset', 
#     'length', 
#     'context', 
#     'sentence', 
#     'type', 
#     'rule', 
#     'ignoreForIncompleteSentence', 
#     'contextForSureMatch'
# ]



# make a class that will contain the error and the right

# for each error dict, find the span of the sentence to that corresponde to the error dict
    #the key "sentence" is a span of the sentence.
    #using the sentence key search for the highest possible sentence match in the instance of the PhraseExtract, and get the index of the sentence
    # return a list of tuple paired with sentence index, error_dict, sentence.text, and modified sentence. -> (1, errpor_dict, sentence_text, modif_setence_text)


# join the setence, to make it as in its original form
# return the list



question = 'Write your thought about the technology advancement.'
sampleEssay = 'The advancments in technolagy have revolutionized the way we comunicate and access information. With the rise of smartphons, tablets, and computers, people can now conect with others around the globe instanly. However, this rapid devlopment also comes with some challenges, such as the increase in cybercrime and the growing dependency on digital devices. As technolagy continues to evolve, it is crucial for societys to find a balance between embracing innovation and ensuring securty.'


response_result = LangToolChecker(sampleEssay)

print(response_result)




# EssayObject = PhraseExtract(question=question,text=sampleEssay)


# print(EssayObject.doc_sm)





