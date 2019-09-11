from django.urls import path
from member import views


urlpatterns = [

path('',views.test,name='member'),

]