from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def arriba(response):
    return HttpResponse("<p> Jet stream sam </p>")

def gnomed(response):
    return HttpResponse("<h1>Hullo me old chum! I'm g'not a gn'elf, I'm g'not a g'n'oblin, · I'm a gn'ome! And you've been, GNOOOOMED!</h1>")