from django.db import models
from user.models import CustomUser
# Create your models here.


class studentModel(CustomUser):

    class Meta:
        abstract = True

    def displayProperties(self):

        print(f"id: {self.id}")
        print(f"username : {self.username}")
        print(f"email : {self.email}")


