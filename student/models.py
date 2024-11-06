from django.db import models
import string
import random
from datetime import date, datetime



class essay_submitted(models.Model):

    student_id = models.IntegerField(unique=True)
    assignment_code = models.CharField(max_length=8, blank=True)
    date_submitted = models.DateField(default=datetime.now())
    

    
class question_composition(models.Model):

    essay_submitted = models.IntegerField()
    question = models.CharField(max_length=500, blank=True)
    composition = models.CharField(max_length=5000, blank=True)


class rubrics(models.Model):

    essay_submitted = models.IntegerField(blank=True, default=0)
    ideas = models.IntegerField(blank=True, default=0)
    gram_punc = models.IntegerField(blank=True, default=0)
    transition = models.IntegerField(blank=True, default=0)
    clarity = models.IntegerField(blank=True, default=0)
    word_choice = models.IntegerField(blank=True, default=0)
    structure = models.IntegerField(blank=True, default=0)
    lang_mechs = models.IntegerField(blank=True, default=0)
    label = models.CharField(max_length=30, blank=True, default='')

    def getBenchMarkScores(self):

        return {
            'ideas' : self.ideas,
            'gram_punc' : self.gram_punc,
            'transition' : self.transition,
            'clarity' : self.clarity,
            'word_choice' : self.word_choice,
            'structure' : self.structure,
            'lang_mechs' : self.lang_mechs,
            'label' : self.label
        }


class langtool_suggestion(models.Model):

    essay_submitted = models.IntegerField(blank=True, default=0)
    message = models.CharField(max_length=1500, blank=True, default='')
    shortmessage = models.CharField(max_length=1500, blank=True, default='')
    replacements = models.CharField(max_length=1500, blank=True, default='')
    context = models.CharField(max_length=1500, blank=True, default='')
    sentence = models.CharField(max_length=1500, blank=True, default='')
    final_sentence = models.CharField(max_length=1500, blank=True, default='')




