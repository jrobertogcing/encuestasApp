from django import forms


from .models import Persona, Nota
# from .models import Nota

NOTA_CHOICES= [
    ('servicio_cliente', 'Cliente particular'),
    ('servicio_empresa', 'Empresa'),
    ('venta', 'Venta'),
    ('garantia', 'Garantía'),
    ]

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    celular = forms.CharField(required=True)
    telefono = forms.CharField(required=True)
    email = forms.CharField(required=True)
    info = forms.CharField(required=True)

class RawNotaForm(forms.Form):
    tipo = forms.CharField(label='¿Qué tipo de nota es?', widget=forms.Select(choices=NOTA_CHOICES))


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
