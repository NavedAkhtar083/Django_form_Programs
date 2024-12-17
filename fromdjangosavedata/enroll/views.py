from django.shortcuts import render
from .form import studentRegistration
from .models  import user  

def showdata(request):
    if request.method=='POST':
        fm=studentRegistration(request.POST)
        if fm.is_valid():
         nm='name:', fm.cleaned_data['name']
         em='email:', fm.cleaned_data['email']
         pw='email:', fm.cleaned_data['password']
        #  reg=user( id=1,name=nm,email=em,password=pw)
        #  reg.save()
         reg=user(id=1djan)
         reg.delete()
    else:
        fm=studentRegistration()
    return render(request,'enroll/student.html',{'form':fm})

# Create your views here.
