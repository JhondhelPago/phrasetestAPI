from features_xtrct import PhraseExtract
from token_tools import SpellingDetector
from LanguageToolChecker import LangToolChecker



question = 'What is your biggest fear?'
essay = 'Reading is a rewarding habit. It opens doors to new worlds, ideas, and knowledge, and it helps people relax. Some prefer reading in the morning, while others enjoy it in the evening, but either way, it provides a much-needed escape from stress. For instance, reading a novel can help someone unwind after a long day, which might improve sleep. Although some people find reading difficult, with practice, anyone can get better at it. In the end, those who read regularly are likely to grow both personally and professionally.'


phraseInstance = PhraseExtract(question=question, text=essay)


result = phraseInstance.SentenceVariationAnalyzer(with_sent_index=True)

print('\n\nresuts')

print(result)
