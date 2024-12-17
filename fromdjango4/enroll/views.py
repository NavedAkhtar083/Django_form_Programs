from django.shortcuts import render
from .form import studentRegistration

def showdata(request):
    if request.method=='POST':
        fm=studentRegistration(request.POST)
        if fm.is_valid():
         print('form validation')
         print('name:', fm.cleaned_data['name'])
         print('email:', fm.cleaned_data['email'])
         print('password',fm.cleaned_data['password'])
         print('repassword',fm.cleaned_data['repassword'])
    else:
        fm=studentRegistration()
    return render(request,'enroll/student.html',{'form':fm})

# Create your views here.
