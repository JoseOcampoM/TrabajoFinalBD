from django import forms
from apps.ejemplares.models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            'usuario',
            'ejemplar',
            'fecha_dev',
            'fecha_pres',
        ]

        labels = {
            'usuario':'Elija el usuario',
            'ejemplar':'Elija el ejemplar',
            'fecha_dev': 'Ingrese la fecha de devolución',
            'fecha_pres':'Ingrese la fecha del préstamo',
        }

        widgets ={
            'fecha_dev': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_pres': forms.DateInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'ejemplar': forms.Select(attrs={'class': 'form-control'}),
        }