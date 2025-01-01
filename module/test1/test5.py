import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from itertools import chain

from new_features_xtract import PhraseExtract
from app_feature import DifficultyAssessment, VocabularyChoice, ErrorsCheckResult
from LanguageToolChecker import ContextUnderStandingSuggestion


context = """Phones and driving"""
essay_text = """ Phones

Modern humans today are always on their phone. They are always on their phone more than 5 hours a day no stop .All they do is text back and forward and just have group Chats on social media. They even do it while driving. They are some really bad consequences when stuff happens when it comes to a phone. Some certain areas in the United States ban phones from class rooms just because of it.

When people have phones, they know about certain apps that they have .Apps like Facebook Twitter Instagram and Snapchat. So like if a friend moves away and you want to be in contact you can still be in contact by posting videos or text messages. People always have different ways how to communicate with a phone. Phones have changed due to our generation.

Driving is one of the way how to get around. People always be on their phones while doing it. Which can cause serious Problems. That's why there's a thing that's called no texting while driving. That's a really important thing to remember. Some people still do it because they think It's stupid. No matter what they do they still have to obey it because that's the only way how did he save.

Sometimes on the news there is either an accident or a suicide. It might involve someone not looking where they're going or tweet that someone sent. It either injury or death. If a mysterious number says I'm going to kill you and they know where you live but you don't know the person's contact ,It makes you puzzled and make you start to freak out. Which can end up really badly.

Phones are fine to use and it's also the best way to come over help. If you go through a problem and you can't find help you ,always have a phone there with you. Even though phones are used almost every day as long as you're safe it would come into use if you get into trouble. Make sure you do not be like this phone while you're in the middle of driving. The news always updated when people do something stupid around that involves their phones. The safest way is the best way to stay safe.    """


Phrase = PhraseExtract(question=context, text=essay_text)


Result = DifficultyAssessment(Phrase_instance=Phrase)

print('Result:')
print(Result)


# print('\n\n')
# print('Frequency Distribution of the words')

# Frequency_Distribution = VocabularyChoice.WordDificulty(Phrase)

# print(Frequency_Distribution.most_common(100))


print('sample output for the get_word_depth().')

depth = VocabularyChoice.get_word_depth('keyboard')

print(f"depth : {depth}")

print('average depth')

ave_depth = VocabularyChoice.AverageWordDepth(Phrase)

print(ave_depth)

print('depth group of the words')
WordDepthGroup = VocabularyChoice.depth_groups(Phrase)
print(f"common terms: {WordDepthGroup['common_term']} \n")
print(f"generalized term : {WordDepthGroup['generalized_term']} \n")
print(f"specific term : {WordDepthGroup['specific_term']} \n")
print(f"specialized term : {WordDepthGroup['specialized_term']} \n")



print('\n\n')

print('sample output of error_group\n')

Message_list = ContextUnderStandingSuggestion(Phrase)




original_errors = Message_list

UniList_errors = list()


error_id_found = {
        'GRAMMAR' : 0,
        'TYPOGRAPHY' : 0,
        'CASING' : 0,
        'PUNCTUATION' : 0,
        'SPELLING' : 0,
        'STYLE' : 0,
        'REDUNDANCY' : 0,
        'WHITESPACE' : 0,
        'MISC' : 0,
        'CONFUSED_WORDS' : 0,
        'CONTRADICTION' : 0,
        'WORDINESS' : 0,
        'DATE_TIME' : 0,
        'NAMES' : 0, 
        'NUMBERS' : 0,
        'INCONSISTENCY' : 0,
        'PASSIVE_VOICE' : 0,
        'MISSING_WORDS' : 0,
        'NONSTANDARD_PHRASE' : 0,
        'COMMA' : 0,
        'COLON_SEMICOLON' : 0
    }


for index, C_U in enumerate(original_errors):

    print(f"from sentence number : {index}")
    print(f"error_list : {C_U['messages']}")


    UniList_errors = list(chain(UniList_errors, C_U['messages']))

    print('Error Indentifiers: \n')
    print(C_U['error_indentifiers'])

    error_id_found['GRAMMAR'] += C_U['error_indentifiers']['GRAMMAR']
    error_id_found['TYPOGRAPHY'] += C_U['error_indentifiers']['TYPOGRAPHY']
    error_id_found['CASING'] += C_U['error_indentifiers']['CASING']
    error_id_found['PUNCTUATION'] += C_U['error_indentifiers']['PUNCTUATION']
    error_id_found['SPELLING'] += C_U['error_indentifiers']['SPELLING']
    error_id_found['STYLE'] += C_U['error_indentifiers']['STYLE']
    error_id_found['REDUNDANCY'] += C_U['error_indentifiers']['REDUNDANCY']
    error_id_found['WHITESPACE'] += C_U['error_indentifiers']['WHITESPACE']
    error_id_found['MISC'] += C_U['error_indentifiers']['MISC']
    error_id_found['CONFUSED_WORDS'] += C_U['error_indentifiers']['CONFUSED_WORDS']
    error_id_found['CONTRADICTION'] += C_U['error_indentifiers']['CONTRADICTION']
    error_id_found['WORDINESS'] += C_U['error_indentifiers']['WORDINESS']
    error_id_found['DATE_TIME'] += C_U['error_indentifiers']['DATE_TIME']
    error_id_found['NAMES'] += C_U['error_indentifiers']['NAMES']
    error_id_found['NUMBERS'] += C_U['error_indentifiers']['NUMBERS']
    error_id_found['INCONSISTENCY'] += C_U['error_indentifiers']['INCONSISTENCY']
    error_id_found['PASSIVE_VOICE'] += C_U['error_indentifiers']['PASSIVE_VOICE']
    error_id_found['MISSING_WORDS'] += C_U['error_indentifiers']['MISSING_WORDS']
    error_id_found['NONSTANDARD_PHRASE'] += C_U['error_indentifiers']['NONSTANDARD_PHRASE']
    error_id_found['COMMA'] += C_U['error_indentifiers']['COMMA']
    error_id_found['COLON_SEMICOLON'] += C_U['error_indentifiers']['COLON_SEMICOLON']

    print('\n')

print(f"Error Indentifiers summary : {error_id_found}")




print('\n UniList_errors : \n')
print(UniList_errors)



print('error_tacker sample output: \n')
# The UniList_error : list[str] will be an input the the ErrorCheckResult.errors_group()

error_tracker = ErrorsCheckResult.errors_group(UniList_errors)
print(error_tracker)


print('\nprinting the API mathces: \n')
print()


