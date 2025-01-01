import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from itertools import chain

from new_features_xtract import PhraseExtract
from app_feature import DifficultyAssessment, VocabularyChoice, ErrorsCheckResult
from LanguageToolChecker import ContextUnderStandingSuggestion


context = """What do you want to be when you grow up? How will you get there?"""
essay_text = """First, I want to be a flight attendant but i have fear of heights so i thought i can be that. The second one is nurse, but someone said being nurse is hard, so my best decision is architecture. I will get there by studying hard and studying math, I'll do my best to reach my dream and to be architecture, even though studying architecture is being hard, i'll make sure to be one of that, i also want to make my family proud and be the first daughter/grandaughter to reach my dream i've been inspired by other architectures, so why not fulfill my dream being an architecture? I also want to inspire other kids who want to be a architecture, to be an architecture i promise to myself to reach and fulfill my dream being an architect, life can be tough but all people can make it through hard life, trust yourself, be yourself, if you need to reach one dream you want, trust god, he is the only way that can make your life successful."""

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
        'TYPOS' : 0,
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


    UniList_errors = list(chain(UniList_errors, [C_U['error_indentifiers']]))

    print('Error Indentifiers: \n')
    print(C_U['error_indentifiers'])

    error_id_found['GRAMMAR'] += C_U['error_indentifiers']['GRAMMAR']
    error_id_found['TYPOS'] += C_U['error_indentifiers']['TYPOS']
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



