from django.http import HttpResponse
from django.shortcuts import render

# def Home(request):
    #return HttpResponse ("hey  Fariya Baccha Golumolu pyara sa panda🥀🥀🥀🥀🥀😘😘")

# def login(request):
#     params={'name':'Naved ','looking':'its look like '}
#     return render(request,'index.html',params)

# def text(request):
#     return render(request,'text.html')

# def removepunc(request):
#     return HttpResponse("removepunc")

def analyze(request):
    djtext=request.GET.get('text','deafult')
    # removepunc=request.GET.get('removepunc','deafult')
    analyzed=djtext
    params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
    return render(request,'analyze.html',params)
    # return HttpResponse('remove punc')

def index(request):
    return render(request,'index.html')