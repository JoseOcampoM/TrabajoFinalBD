from django import forms
from apps.ejemplares.models import Ejemplares

class EjemplaresForm(forms.ModelForm):
    class Meta:
        model = Ejemplares
        fields = [
            'libro',
            'localización',
        ]

        labels = {
            'libro':'Seleccione un libro',
            'localización':'Ingrese la localización',
        }

        widgets ={
            'localización': forms.TextInput(attrs={'class': 'form-control'}),
            'libro': forms.Select(attrs={'class': 'form-control'}),
        }