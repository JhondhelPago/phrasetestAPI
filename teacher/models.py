from django.db import models
import string
import random

# Create your models here.


def generate_section_code():

    length = 8
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

class section(models.Model):

    section_code = models.CharField(max_length=8, unique=True, blank=True)
    teacher_id = models.IntegerField(null=True)

    def save(self, *args, **kwargs):

        if not self.section_code:

            self.section_code = generate_section_code()

            while section.objects.filter(section_code=self.section_code).exists():
                self.section_code = generate_section_code()

            super(section, self).save(*args, **kwargs)



