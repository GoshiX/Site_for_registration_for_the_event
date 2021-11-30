from django.contrib import admin
from django.db.models.fields import *

from .models import *
 
admin.site.register(Intro)
admin.site.register(About)
admin.site.register(timetable)
admin.site.register(guest)