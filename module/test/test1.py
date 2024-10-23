import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from features_xtrct import PhraseExtract
from token_tools import SpellingDetector
from LanguageToolChecker import LangTooChecker



question = 'What is your biggest fear?'
essay = 'The impact of technoloy on education has been tremendous in the past decade. Student are now able to access a wealth of informatin with just a few clicks, which has revolutionized the way they learn. However, this easy access to information can also lead to distractions, as many students find themselves scrolling through social media instead of focusing on their studies. Moreover, not all online resources are credible, and it’s crucial for learners to develop the skill to evaluate the reliability of the content they consume. Despite these challenges, the integration of technology in education continues to offer new opportunities for growth and learning, which can ultimately enhance student outcomes.'


phraseInstance = PhraseExtract(question=question, text=essay)



print(phraseInstance.ArrayOfSents())


for Sent in phraseInstance.ArrayOfSents():

    print(Sent)

    print('\n')

    matchFound = LangTooChecker(Sent)

    print(matchFound)


    print('\n\n\n')