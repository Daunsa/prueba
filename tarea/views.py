from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def clientes(request):
    html = "<html><body><h1>Esta es la pagina clientes</h1></body></html>"
    return HttpResponse(html)

def productos(request):
    html = "<html><body><h1>Esta es la pagina productos</h1></body></html>"
    return HttpResponse(html)