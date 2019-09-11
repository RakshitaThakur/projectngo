from django.urls import path
from dashboard import views

urlpatterns = [

#path('',views.test,name='dashboard'),
path('',views.index,name='dashboard'),

]