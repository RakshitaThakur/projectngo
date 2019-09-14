from django.shortcuts import render,redirect
from .forms import MemberForm, MemberInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


'''
def test(request):
	return HttpResponse('testing urls for member application working properly for 127.0.0.1:8000/member/')
'''
def index(request):
    return render(request,'member/index.html')


@login_required
def userlogout(request):
    logout(request)
    return redirect('/member/')


def register(request):
    registered = False
    if request.method == 'POST':
        mform = MemberForm(data=request.POST)
        miform = MemberInfoForm(data=request.POST)
        if mform.is_valid() and miform.is_valid():
            user=mform.save()
            user.set_password(user.password)
            user.save()
            profile = miform.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print("found it")
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(mform.errors,miform.errors)
    else:
        mform = MemberForm()
        miform = MemberInfoForm()
    return render(request,'member/registration.html',{'user_form':mform,'profile_form':miform,'registered':registered})



def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("YOur account was inactive.")
        else:
            return HttpResponse("Invalid login detail given")
    else:
        return render(request,'member/login.html',{})

