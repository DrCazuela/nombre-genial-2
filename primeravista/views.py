from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Levantar(response):
    return HttpResponse("<h1>Inicializando</h1> <br> <h4>por favor espere</h4>")