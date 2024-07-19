from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'global/home.html', context={
        'name': 'Douglas Ribeiro',
    })

def contato(request):
    return render(request, 'temp/temp.html')

def sobre(request):
    return HttpResponse('sobre')