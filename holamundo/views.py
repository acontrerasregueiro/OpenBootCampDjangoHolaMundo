from curses.ascii import HT
from django.http import HttpResponse


def saludo(request):
    return HttpResponse('Hola Mundo')

def despedida(request):
    return HttpResponse('Hasta luego')

def adulto(request,edad):
     if(edad >= 18):
         return(HttpResponse('Es mayor de edad'))
     else:
         return (HttpResponse('No eres mayor de edad'))