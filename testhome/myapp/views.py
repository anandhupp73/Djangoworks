from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def textmessage(request):
    return HttpResponse('Welcome  to django project ')

def sumcalc(request,num1,num2):
    sum = num1 + num2
    return HttpResponse(f'Sum = {sum}')

def index(request):
    return render(request,'index.html')

def secondpage(request):
    return render(request,'secondpage.html')

