from LanguageToolChecker import LangToolChecker
from features_xtrct import PhraseExtract
from rubrics import Ideas

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
sampleEssay = 'Technology has profoundly transformed education by enhancing accessibility, quality, and flexibility in learning. With the advent of digital tools, education has become more inclusive, allowing students from diverse locations and backgrounds to access the same learning opportunities through online platforms. No longer confined to physical classrooms, learners can now participate in virtual classrooms, access e-books, and engage with educational content at their own pace. This flexibility benefits both students and teachers by offering personalized learning experiences and broadening access to resources. Moreover, technological advancements such as interactive whiteboards and educational apps have enriched teaching methods, making learning more engaging and effective. Consequently, technology continues to break barriers and bridge educational inequalities, creating a more connected, informed, and adaptable global learning environment.'

"""
response_result = LangToolChecker(sampleEssay)

print(response_result)
"""




# EssayObject = PhraseExtract(question=question,text=sampleEssay)


# print(EssayObject.doc_sm)



phraseObject = PhraseExtract(question=question, text=sampleEssay)

sentence_list = phraseObject.ArrayOfSents()



print(sentence_list)


"""
result = Ideas.testingSimilarity(sentence_list)

print(result)

"""

print('\n\n\n')


print('this is the keywords found in the sentence using the rake_nltk')
keyword = Ideas.rake_KeyWord(phraseObject.text)

print(keyword)





