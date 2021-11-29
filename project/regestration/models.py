from django.db import models
from django.db.models import *
from django.db.models.fields import *

class User(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name + " " + self.surname

class Intro(models.Model):
    bc_img = models.ImageField()
    title = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField()

    def __str__(self):
       return self.title