from ml_model import rf_model_predict
from features_xtrct import PhraseExtract1


Question1 = 'What do you want to be when you grow up? How will you get there?'
Question2  = 'What is the most valuable lesson you have learned in life?'

text = 'The economy is growing rapidly, and many new businesses are emerging. However, not all industries are benefiting equally. Some sectors, such as technology, are experiencing rapid growth, while others lag behind. This imbalance can cause challenges in workforce distribution and wage levels.'
text1 = 'In 20 years I imagined myself as a successful software engineer and a businessman. I dreamed to work as programmer at global tech companies like Google, Microsoft, and Apple. After 20 years, I also think that I already have agricultural businesses. During my age of 20s it is the time when i have to get married and start my own family, but before all of it I need to make sure that i have enough resources to support family\'s needs. I also want to explore my career opportunity overseas. I know that there a lot to discover on myself during my age of 20\'s and continue to improve my life quality.'
text2 = 'When i grow up iwanna be a doctor to help people who have sick or who is pregnant, i know that i can go to my dream and i will gonna do my best for my parents and to be doctor'
text3 ="""First, I want to be a flight attendant but i have fear of heights so i thought i can be that. The second one is nurse, but someone said being nurse is hard, so my best decision is architecture. I will get there by studying hard and studying math, I'll do my best to reach my dream and to be architecture, even though studying architecture is being hard, i'll make sure to be one of that, i also want to make my family proud and be the first daughter/grandaughter to reach my dream i've been inspired by other architectures, so why not fulfill my dream being an architecture? I also want to inspire other kids who want to be a architecture, to be an architecture i promise to myself to reach and fulfill my dream being an architect, life can be tough but all people can make it through hard life, trust yourself, be yourself, if you need to reach one dream you want, trust god, he is the only way that can make your life successful."""
text4 = """What do you want to be when you grow up? a lot of people asked me that question and i always say that i want to be a lawyer or a nurse, but i often say that i want to be a lawyer and my parents want me to be a nurse, because my promise to them is that i win fulfill their promise. And i promised to my parents that I will make them proud always and no matter what happens. Another thing that i always ask to myself. How will you get there? Well i want to study at De La Salle University and and promised to stuju marter study and also I am or Harvard Law myself that i will for my parents to University always study study hard be proud at me going to take care of my parents because they take cared of me while growing up and they experienced hard time for me and also they have sacrifieses that they did to me."""
text5 = """When I grow up I wanna Be a Police Officer so I can help everybody and i wont let criminals escape and rob or kidnap anyone to get there i'll study more. help other people and i will study the police officer rules.""" 
text6 = """I want to be an IT professional. I can achieve this pursuing a relevant education (a degree in computer science or a related field), gaining practical experience through internships or entry-level positions, and continuing to study of new technologies and skills throughout my career. By combining education, skills, and experience, you can build a successful career in the dynamic world of IT. """


Phrase = PhraseExtract1(question=Question1, text=text6)


print(Phrase.FeatureList1())

print(rf_model_predict(Phrase.FeatureList1()))
