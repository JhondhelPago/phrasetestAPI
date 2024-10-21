from features_xtrct import PhraseExtract
from token_tools import SpellingDetector
from LanguageToolChecker import LangToolChecker


question = 'When you imagine yourself in 20 years, where do you want to be?'
essay = 'In 20 years I imagined myself as a successful software engineer and a businessman. I dreamed to work as programmer at global tech companies like Google, Microsoft, and Apple. After 20 years, I also think that I already have agricultural businesses. During my age of 20s it is the time when i have to get married and start my own family, but before all of it I need to make sure that i have enough resources to support family\'s needs. I also want to explore my career opportunity overseas. I know that there a lot to discover on myself during my age of 20\'s and continue to improve my life quality.'


phraseInstance = PhraseExtract(question=question, text=essay)


result =  phraseInstance.readability_score


print(f"result : {result}")pang