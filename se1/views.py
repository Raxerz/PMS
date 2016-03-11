from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'se1/dashboard/index.html',{})

def index1(request):
	return render(request,'se1/dashboard/dashboard.html',{})

def index2(request):
	return render(request,'se1/dashboard/notifications.html',{})

def index3(request):
	return render(request,'se1/dashboard/table.html',{})

def index4(request):
	return render(request,'se1/dashboard/template.html',{})

def index5(request):
	return render(request,'se1/dashboard/user.html',{})

