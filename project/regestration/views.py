from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views.generic import *
from .models import *

class HomePageView(ListView):
    model = Intro
    template_name = 'home.html'
    context_object_name = 'intro_info'