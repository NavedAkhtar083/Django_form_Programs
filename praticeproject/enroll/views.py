from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello good mo")

def about(request):
    return render(request,"templates/index.html")
         
