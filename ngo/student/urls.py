from django.urls import path
from student import views



urlpatterns = [

path('',views.test,name='student'),
#path('registration/',views.registration,name="registration"),
]