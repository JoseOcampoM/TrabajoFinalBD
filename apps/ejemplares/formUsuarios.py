from django import forms
from apps.ejemplares.models import Usuario

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombres',
            'apellidos',
            'dirección',
            'teléfono',
        ]

        labels = {
            'nombres':'Ingrese los nombres',
            'apellidos':'Ingrese los apellidos',
            'dirección':'Ingrese la dirección',
            'teléfono':'Ingrese el teléfono',
       }

        widgets ={
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dirección': forms.TextInput(attrs={'class': 'form-control'}),
            'teléfono': forms.TextInput(attrs={'class': 'form-control'}),
        }