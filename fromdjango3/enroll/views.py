from django.shortcuts import render
from .form import studentRegistration

def showdata(request):
    if request.method=='POST':
        fm=studentRegistration(request.POST)
        if fm.is_valid():
         print('form validation')
         name=fm.cleaned_data['name']
         email= fm.cleaned_data['email']
         rollno=fm.cleaned_data['rollno']
         age=fm.cleaned_data['age']
         print('name:', name )
         print('email', email)
         print('rollno',rollno)
         print('age',age)
         return render(request,'enroll/success.html',{'nm':name})

    else:
        fm=studentRegistration()
    return render(request,'enroll/student.html',{'form':fm})

# Create your views here.
