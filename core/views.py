from asyncio import events
from django.shortcuts import render
from .models import Producto


def index (request):
    return render(request, 'index.html')

def registro (request):
    return render(request, 'registro.html')

def identificadores (request):
    return render(request, 'identificadores.html')

def correas (request):
    return render(request, 'correas.html')

def bandanas (request):
    return render(request, 'bandanas.html')

def api (request):
    return render(request, 'api.html')

def api2 (request):
    return render(request, 'api2.html')  

def categoria (request):
    cosa_lista= Producto.objects.all()
    return render(request, 'categoria.html', {'cosa_lista':cosa_lista})  
    
