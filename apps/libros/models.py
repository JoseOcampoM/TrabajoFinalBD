from email import charset
from django.db import models

class Autor(models.Model):
    nombres= models.CharField(verbose_name="Nombres", max_length=80)

    def __str__(self):
        return self.nombres
    
class Libro(models.Model):
    título = models.CharField(verbose_name="Título", max_length=120)
    número_pagina=models.SmallIntegerField(verbose_name="Número de Página")
    editorial=models.CharField(verbose_name="Editorial",max_length=50)
    isbn=models.CharField(verbose_name="ISBN", max_length=50) 
    autor=models.ForeignKey(Autor, verbose_name="Autor", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.título
    