from django.shortcuts import render
from django.http import HttpResponse



def test(request):
	return HttpResponse('testing urls for member application working properly for 127.0.0.1:8000/member/')
