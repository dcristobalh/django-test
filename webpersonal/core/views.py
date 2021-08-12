from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>Mi web personal</h1><h2>Portada</2>")

# Create your views here.
