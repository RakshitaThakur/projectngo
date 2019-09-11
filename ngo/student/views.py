from django.shortcuts import render,redirect
from django.http import HttpResponse
from student.forms import *
from student.models import *
 


def test(request):
 	return HttpResponse('testing student application successful at 127.0.0.1:8000/student/')


'''
def registration(request):
	form = NewRegistration()
	if request.method == 'POST':
		form = NewRegistration(request.POST)
        if form.is_valid():
        	form.save()
            return redirect('/')
    else:
        form = NewRegistration()
    return render(request,'student/registration.html',{'forms':form})
'''