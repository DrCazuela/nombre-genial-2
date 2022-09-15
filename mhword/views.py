from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pepinillo(response):
    return HttpResponse("<h1> Devil Jho </h1>")


def minibueno(response):
    return HttpResponse("<h1>Magnamalo</h1>")