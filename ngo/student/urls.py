from django.urls import path
from . import views


urlpatterns = [

path('',views.test,name='student'),
path('registration',views.registration,name="registration"),
path('attendance',views.attendance,name="attendance"),

]