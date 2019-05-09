from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from.models import Encuesta

def encusta_lista(request):
    encuestas = Encuesta.objects.all()
    return render(request, 'encuestas/encuesta_list.html', {'encuestas': encuestas})


def encuesta_detail(request, pk): 
    # encuesta = Encuesta.objects.get(pk=pk)
    encuesta = get_object_or_404(Encuesta, pk=pk)
    return render(request, 'encuestas/detalle_encuesta.html', {'encuesta': encuesta})