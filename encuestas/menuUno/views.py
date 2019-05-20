from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect


from .forms import  RawPersonaForm, RawNotaForm
from.models import Persona, Nota

# def encuesta_create_view(request):
#     my_form = RawEncuestaForm()
#     if request.method == "POST":
#         my_form = RawEncuestaForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Encuesta.objects.create(**my_form.cleaned_data)
#             return redirect('/encuestas')
#         else:
#             print(my_form.errors)
#     context= {
#         "form": my_form
#     }
#     return render(request, 'encuestas/encuesta_create.html', context)

def persona_create_view(request):
    my_form = RawPersonaForm()
    if request.method == "POST":
        my_form = RawPersonaForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Persona.objects.create(**my_form.cleaned_data)
            return redirect('menuUno:persona_list')
        else:
            print(my_form.errors)
    context= {
        "form": my_form
    }
    return render(request, 'encuestas/persona_create.html', context)

def nota_create_view(request):
    my_form = RawNotaForm()
    if request.method == "POST":
        my_form = RawNotaForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Nota.objects.create(**my_form.cleaned_data)
            # return redirect('menuUno:nota_list')
        else:
            print(my_form.errors)
    context= {
        "form": my_form
    }
    return render(request, 'encuestas/nota_create.html', context)

# def persona_create_view(request):
#     form = PersonaForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context= {
#         'form': form,
#     }
#     return render(request, 'encuestas/persona_create.html', context)

# def encuesta_create_view(request):
#     form = EncuestaForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = EncuestaForm()

#     context= {
#         'form': form,
#     }
#     return render(request, 'encuestas/encuesta_create.html', context)

# def encusta_lista(request):
#     encuestas = Encuesta.objects.all()
#     return render(request, 'encuestas/encuesta_list.html', {'encuestas': encuestas})


# def encuesta_detail(request, pk): 
#     # encuesta = Encuesta.objects.get(pk=pk)
#     encuesta = get_object_or_404(Encuesta, pk=pk)
#     return render(request, 'encuestas/detalle_encuesta.html', {'encuesta': encuesta})

def persona_detail(request, encuesta_pk, persona_pk):
    persona = get_object_or_404(Persona, encuesta_id=encuesta_pk, pk=persona_pk)
    return render(request, 'encuestas/persona_detail.html',{'persona': persona})

def persona_lista(request):
    personas = Persona.objects.all()
    return render(request, 'encuestas/persona_list.html', {'personas': personas})
