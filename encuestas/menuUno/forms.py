from django import forms


from .models import Persona, Nota, Item
# from .models import Nota

NOTA_CHOICES = [
    ('servicio_cliente', 'Cliente particular'),
    ('servicio_empresa', 'Empresa'),
    ('venta', 'Venta'),
    ('garantia', 'Garantía'),
    ]

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    celular = forms.CharField(required=True)
    telefono = forms.CharField(required=False)
    email = forms.CharField(required=False)
    info = forms.CharField(required=False)

# class RawNotaForm(forms.Form):
#     tipo = forms.CharField(label='¿Qué tipo de nota es?', widget=forms.Select(choices=NOTA_CHOICES))
#     receptor = forms.CharField(required=True)


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = (
            'tipo',
            'person',
            'receptor'
        )
        widgets = {
            'tipo': forms.Select(choices=NOTA_CHOICES),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'nota',
            'descripción',
            'serie',
            'password',
            'cargador',
            'funda',
            'cables',
            'cartuchos',
            'falla',
        )

class RawNotaForm(forms.Form):
    tipo = forms.CharField(required=True)
    person = forms.CharField(required=True)
    receptor = forms.Select(choices=NOTA_CHOICES)

# class RawItemForm(forms.Form):
#     descripción = forms.CharField(required=True)
#     serie = forms.CharField(required=True)
#     password = forms.CharField(required=False)
#     cargador = forms.CharField(required=False)
#     funda = forms.CharField(required=False)
#     cables = forms.CharField(required=False)
#     cartuchos = forms.CharField(required=False)
#     falla = forms.CharField(required=True)
 

# class PersonaForm(forms.ModelForm):
#     class Meta:
#         model = Persona
#         fields = [
#             'name',
#             'lastName',
#             'ocupacion',
#             'redSocialUno',
#         ]

# class NaotForm(forms.ModelForm):
#     class Meta:
#         model = Encuesta
#         fields = [
#             'title',
#             'description',
#         ]

# class RawEncuestaForm(forms.Form):
#     title = forms.CharField(required=True)
#     description = forms.CharField(
#                         required=True,
#                         widget=forms.Textarea(
#                             attrs={
#                                 "rows" : 10,
#                                 "cols" : 70,
#                             }
#                         )
#                     )
