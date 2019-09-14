from django.shortcuts import render,redirect
from django.http import HttpResponse
#from student.views import *
from student.models import *



'''
def test(request):
	return HttpResponse('this is testing function for dashboard at 127.0.0.1:8000/dashboard')
'''


def index(request):
    num = sdata.objects.count()
    return render(request,'dashboard/index.html',{'student_number':num})



def home(request):
	return redirect('/dashboard/')

def about(request):
    data_dict = {'insert_data': "Hello ", 'design': "its your desgin"}
    return render(request, 'dashboard/about.html', context=data_dict)


