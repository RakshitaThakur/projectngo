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
     student_list = sdata.objects.order_by("id")
     rollno = []
     for i in student_list :
         rollno.append(i.id)
     data_dict = {'rollno': rollno}
     return render(request, 'student/reg.html',context=data_dict)



def storeattend(request):
    if request.method == 'POST':
        attend = request.POST.copy()

        a = Attendance()
        student_list=sdata.objects.order_by("id")
        for i in student_list:
            a.rollno = i
            st=atgetname(i.id)
            a.status = attend.get(st)
            a.save()

    return redirect('/')

def atgetname(r):
    q="attendance["+str(r)+"]"
    return q
