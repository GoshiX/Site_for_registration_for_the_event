from django.db import models
from django.db.models import *
from django.db.models.fields import *
import datetime

class About(models.Model):
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
       return self.title

class timetable(models.Model):
    day = models.DateField()
    time = models.TimeField()
    action = models.TextField()

    def __str__(self):
       return self.action

class guest(models.Model):
    name = models.TextField()
    surname = models.TextField()
    phone = models.TextField()
    email = models.EmailField()

    def __str__(self):
       return self.name + " " + self.surname

class Description(models.Model):
        text = models.TextField()
        def __str__(self):
            return self.text[:50]

class Intro(models.Model):
    bc_img = models.ImageField(upload_to = "templates/image")
    title = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    text = models.TextField()
    text_color = models.TextField(default = "#000000")
    block_color = models.TextField(default = "#000000")
    subtitle = models.TextField(default = "Описание")

    def __str__(self):
       return self.title

    def get_img(self):
        return str(self.bc_img)

    def days_left(self):
        return datetime.datetime.now()