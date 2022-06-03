from django import forms
from apps.libros.models import Libro

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'título',
            'número_pagina',
            'editorial',
            'isbn',
            'autor',
        ]

        labels = {
            'título':'Ingrese el título',
            'número_pagina':'Ingrese el número de páginas',
            'editorial':'Ingrese la editorial',
            'isbn':'Ingrese el ISBN del libro',
            'autor':'Seleccione el autor',
       }

        widgets ={
            'título': forms.TextInput(attrs={'class': 'form-control'}),
            'número_pagina': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }