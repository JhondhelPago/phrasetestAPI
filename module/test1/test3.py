import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from new_features_xtract import PhraseExtract
from app_feature import Vocabulary, synonyms, get_synonyms, underscoreTospace, sort_synonyms
from LanguageToolChecker import ResultCheker, LangToolChecker

context = 'What do you want to be when you grow up? How will you get there?'
essay_text = """First, I want to be a flight attendant but i have fear of heights so i thought i can be that. The second one is nurse, but someone said being nurse is hard, so my best decision is architecture. I will get there by studying hard and studying math, I'll do my best to reach my dream and to be architecture, even though studying architecture is being hard, i'll make sure to be one of that, i also want to make my family proud and be the first daughter/grandaughter to reach my dream i've been inspired by other architectures, so why not fulfill my dream being an architecture? I also want to inspire other kids who want to be a architecture, to be an architecture i promise to myself to reach and fulfill my dream being an architect, life can be tough but all people can make it through hard life, trust yourself, be yourself, if you need to reach one dream you want, trust god, he is the only way that can make your life successful."""

Phrase = PhraseExtract(question=context, text=essay_text)


# ['message', 'shortMessage', 'replacements', 'offset', 'length', 'context', 'sentence', 'type', 'rule', 'ignoreForIncompleteSentence', 'contextForSureMatch']


print(Phrase.gb_model_param_list())

Sentence_list = Phrase.ArrayOfSentNoEndSpace()


for index, sentence in  enumerate(Sentence_list):

    # print(f"index: {index}")
    print(sentence)
    print('\n')

    ErrorSuggestion = ResultCheker(index, sentence)

    # print(ErrorSuggestion.result_langtoolcheacker)
    # print(type(ErrorSuggestion.result_langtoolcheacker))
    # print(type(ErrorSuggestion.result_langtoolcheacker[0]))
    # print(list(ErrorSuggestion.result_langtoolcheacker[0].keys()))


    print(f"modify text: {ErrorSuggestion.modif_text}")
    print(ErrorSuggestion.MessageList)

    print('\n\n')

