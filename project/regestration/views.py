from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views.generic import *
from .models import *

class HomePageView(ListView):
    model = Intro
    template_name = 'home.html'
    context_object_name = 'intro_info'

class HomePageView1(ListView):
    model = About
    template_name = 'home.html'
    context_object_name = 'about_info'

class HomePageView2(ListView):
    model = timetable
    template_name = 'home.html'
    context_object_name = 'timetable_info'

class HomePageView3(ListView):
    model = guest
    template_name = 'home.html'
    context_object_name = 'guest_info'