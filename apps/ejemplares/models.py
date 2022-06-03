from django.db import models
from apps.libros.models import Libro
# Create your models here.
class Usuario(models.Model):
    nombres=models.CharField(verbose_name="Nombres", max_length=80)
    apellidos=models.CharField(verbose_name="Apellidos", max_length=80)
    dirección=models.CharField(verbose_name="Dirección", max_length=80)
    teléfono=models.BigIntegerField(verbose_name="Teléfono")

    def __str__(self):
        return '%s %s' %(self.nombres, self.apellidos)
    
class Ejemplares(models.Model):
    libro= models.ForeignKey(Libro, verbose_name="Título del libro", on_delete=models.CASCADE)
    localización=models.CharField(verbose_name="Localización",max_length=60)
    usuario=models.ManyToManyField(Usuario, through="Prestamo")
 
    def __str__(self):
        return self.localización
    
class Prestamo(models.Model):
    usuario=models.ForeignKey(Usuario, verbose_name="Usuario", blank=True, null=True, on_delete=models.CASCADE)
    ejemplar=models.ForeignKey(Ejemplares, verbose_name="Ejemplar", blank=True, null=True, on_delete=models.CASCADE)
    fecha_dev=models.DateField(verbose_name="Fecha de Devolución")
    fecha_pres=models.DateField(verbose_name="Fecha de Préstamo")

    def __str__(self):
        return str(self.fecha_pres)
    
