from django.conf.urls.static import static
from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class HomePageView1(ListView):
    model = Intro
    template_name = 'home.html'
    context_object_name = 'info'

    def get_context_data(self, **kwargs):
        context = super(HomePageView1, self).get_context_data(**kwargs)
        context['description'] = Description.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super(HomePageView1, self).get_context_data(**kwargs)
        context['timetable'] = timetable.objects.all()
        return context

'''

class HomePageView2(ListView):
    model = timetable
    template_name = 'home.html'
    context_object_name = 'timetable_info'

class HomePageView3(ListView):
    model = guest
    template_name = 'home.html'
    context_object_name = 'guest_info'

'''