import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rubrics import grade_corpus, IdeaCriterion
from features_xtrct import PhraseExtract, PhraseExtract1

Question1 = 'What do you want to be when you grow up? How will you get there?'
Question2  = 'What is the most valuable lesson you have learned in life?'

text = 'The economy is growing rapidly, and many new businesses are emerging. However, not all industries are benefiting equally. Some sectors, such as technology, are experiencing rapid growth, while others lag behind. This imbalance can cause challenges in workforce distribution and wage levels.'
text1 = 'In 20 years I imagined myself as a successful software engineer and a businessman. I dreamed to work as programmer at global tech companies like Google, Microsoft, and Apple. After 20 years, I also think that I already have agricultural businesses. During my age of 20s it is the time when i have to get married and start my own family, but before all of it I need to make sure that i have enough resources to support family\'s needs. I also want to explore my career opportunity overseas. I know that there a lot to discover on myself during my age of 20\'s and continue to improve my life quality.'


Phrase = PhraseExtract1(question=Question1, text=text1)

Phrase.displayFeatures()
print('Feature List')
print(Phrase.FeatureList())


IdeaCriterion_result = IdeaCriterion(Phrase)

print('\n\n' + f"IdeaCriterion_result : {IdeaCriterion_result}")




