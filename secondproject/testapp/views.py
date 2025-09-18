from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def sample(request):
    return HttpResponse('Welcome to our django project.....')

def sample2(request,num):
    return HttpResponse(num)

def sample3(request):
    return HttpResponse('Welcome to page 3 ... ')

def index(request):
    return render(request,'index.html')  #render user for rendering html pages

def second(request):
    return render(request,'second.html')