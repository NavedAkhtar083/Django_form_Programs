from django.shortcuts import render

# Create your views here.
def home(request,my_id):
    if my_id=='1':
        student={'id':my_id ,'name':'rohan'}
    
    if my_id =='2':
        student={'id': my_id ,'name':'sonam'}
        
    if my_id =='3':
        student={'id':my_id,'name':'ali'}
        
    return render(request,'enroll/index.html', student)

def index(request):
    return render(request,'enroll/home.html')