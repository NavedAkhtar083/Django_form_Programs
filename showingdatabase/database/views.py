from urllib import request
from django.shortcuts import render
from database.models import student
# Create your views here.

def studentinfo(request):
 stud =student.objects.all()
 return  render(request,'database/studentdetails.html',{'stu':stud})