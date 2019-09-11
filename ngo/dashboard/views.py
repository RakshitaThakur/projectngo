from django.shortcuts import render,redirect
from django.http import HttpResponse



'''
def test(request):
	return HttpResponse('this is testing function for dashboard at 127.0.0.1:8000/dashboard')
'''


def index(request):
	return render(request,'dashboard/index.html')



def home(request):
	return redirect('/dashboard/')