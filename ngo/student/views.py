from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def test(request):
    return HttpResponse('testing student application successful at 127.0.0.1:8000/student/')



def registration(request):
    form=sdata_form()
    if request.method == 'POST':
        form = sdata_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=sdata_form()
    return render(request,'student/registration.html',{'forms':form})

def attendance(request):
     student_list = Attendance.objects.order_by('rollno')
     data_dict = {'students': student_list}
     return render(request, 'student/attendance.html', context=data_dict)

