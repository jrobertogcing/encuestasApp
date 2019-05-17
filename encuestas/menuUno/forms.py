from django import forms


from .models import Persona
from .models import Encuesta

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'name',
            'lastName',
            'ocupacion',
            'redSocialUno',
        ]

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = [
            'title',
            'description',
        ]

class RawEncuestaForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(
                        required=True,
                        widget=forms.Textarea(
                            attrs={
                                "rows" : 10,
                                "cols" : 70,
                            }
                        )
                    )
