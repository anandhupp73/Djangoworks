from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sum(request,num1,num2):
    sum=num1+num2
    return HttpResponse(f"Sum = {sum}")

def index(request):
    return render(request,'index.html')


def index2(request):
    return render(request,'index2.html')