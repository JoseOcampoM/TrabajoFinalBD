from django import forms
from apps.libros.models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombres',
        ]

        labels = {
            'nombres':'Ingrese el nombre',
        }

        widgets ={
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
        }