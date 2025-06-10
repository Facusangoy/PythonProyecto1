from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola! Esta es la página de inicio del blog.")