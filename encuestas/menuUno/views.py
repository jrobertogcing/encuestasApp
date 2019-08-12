from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RawPersonaForm, RawNotaForm, NotaForm, ItemForm
from.models import Persona, Nota, Item

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
           # print(my_form.cleaned_data)
            Persona.objects.create(**my_form.cleaned_data)
            return redirect('menuUno:persona_list')
        else:
            print(my_form.errors)
    context = {
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
    context = {
        "form": my_form
    }
    return render(request, 'encuestas/nota_create.html', context)


class NotaCreateView(CreateView):

    model = Nota
    form_class = NotaForm
    template_name = "encuestas/nota_create.html"
    success_url = reverse_lazy("menuUno:nota_create")

class ItemCreateView(CreateView):

    model = Item
    form_class = ItemForm
    template_name = "encuestas/item_create.html"
    success_url = reverse_lazy("menuUno:item_create")


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

def persona_detail(request, pk):
    notas = Nota.objects.all()
    persona = get_object_or_404(Persona, pk=pk)
    item = Item.objects.all()
    return render(request, 'encuestas/persona_detail.html',{'persona': persona, 'notas' : notas, 'item' : item})

def persona_lista(request):
    notas = Nota.objects.all()
    personas = Persona.objects.all()
    return render(request, 'encuestas/persona_list.html', {'personas': personas, 'notas' : notas})

def nota_detail(request, persona_pk, nota_pk,):
    nota = get_object_or_404(Nota, person_id = persona_pk, pk = nota_pk)
    persona = get_object_or_404(Persona, pk=persona_pk)
    items = Item.objects.all()
    return render(request, 'encuestas/nota_detail.html', {'persona': persona, 'nota': nota, 'items': items})

def nota_lista(request):
    notas = Nota.objects.all()
    return render(request, 'encuestas/nota_list.html', {'notas': notas})
