from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
   pass

from django.db import models
from django.templatetags.static import static



class Teacher(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.EmailField(blank=True)
    Email_Address = models.EmailField(blank=True)
    Phone_Number = models.BigIntegerField(max_length=100, blank=True)
    Room_Number = models.CharField(max_length=10)
    Subjects_taught = models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name + " " + self.Last_Name


"""

    @property
    def img_url(self):
        return static("media/{}".format(self.Email_Address))
"""

