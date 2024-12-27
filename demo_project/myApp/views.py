from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1 style = 'background-color:grey'>Hellooo......</h1>")
    return render(request, 'index.html')