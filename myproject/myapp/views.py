from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from the my app ! this is my first django app")

def dashbord(request):
    return HttpResponse ("this is my dashboard")

def htmc(request):
    return render(request,'index.html')