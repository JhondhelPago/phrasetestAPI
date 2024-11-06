from django.db import models
import string
import random
from datetime import date, datetime



class essay_submitted(models.Model):

    student_id = models.IntegerField(unique=True)
    assignment_code = models.CharField(max_length=8, blank=True)
    date_submitted = models.DateField(default=datetime.now())
    

    
class question_composition(models.Model):

    essay_submitted = models.IntegerField(unique=True)
    question = models.CharField(max_length=500, blank=True)
    composition = models.CharField(max_length=5000, blank=True)


