import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from features_xtrct import PhraseExtract
from LanguageToolChecker import LangToolChecker, EssayExamineErrorSuggest, OffsetFinder, FindSubStringPosition


print(len(' to discover on myself during my age of 20\'s and continue to improve my life quality'))
print(len('to discover on myself during my age of 20s and continue to improve my life quality'))



string = 'y'
new_string = string[1:]

print(f'new_string:{new_string}')


offset_position = FindSubStringPosition('I know that there a lot to discover on myself during my age of 20\'s and continue to improve my life quality.',  'to discover on myself during my age of 20\'s and continue to improve my life quality')
print(offset_position)
print(len('to discover on myself during my age of 20\'s and continue to improve my life quality'))

print(len('to discover on myself during my age of 20\'s and continue to improve my life quality.'))