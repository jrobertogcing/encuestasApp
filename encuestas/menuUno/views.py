from django.shortcuts import render
from django.http import HttpResponse

from.models import Encuesta

def encusta_lista(request):
    encuestas = Encuesta.objects.all()
    return HttpResponse(encuestas)