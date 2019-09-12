from django.contrib import admin
from django import forms
from .views import *
from .models import *


admin.site.register(sdata)
admin.site.register(Attendance)
