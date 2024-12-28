from django.shortcuts import render,redirect


# Create your views here.
from django.http import HttpResponse,JsonResponse

def home(request):
    # return HttpResponse("<h1 style = 'background-color:grey'>Hellooo......</h1>")
    # return render(request, 'index.html')
    
    # data = {"name":"amit", "age":"22", "active":"true", "active1":"null"}   #JSON Data
    # return JsonResponse(data)
    
    return redirect('https://www.djangoproject.com/start/')