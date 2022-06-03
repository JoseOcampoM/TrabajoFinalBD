from django.urls import path
from apps.libros.views import *

app_name='libros'
urlpatterns = [
    path('', listLibros, name='listLibros'), 
    path('nuevo/', librosCreate, name='librosCreate'), 
    path('actualizar/<int:id_libro>/', librosEdit, name='librosEdit'),
    path('eliminar/<int:id_libro>/', librosEliminar, name='librosEliminar'), 
    
    #Autor
    path('autor/', listAutor, name='listAutor'),
    path('nuevo_a/', autorCreate, name='autorCreate'), 
    path('actualizar_a/<int:id_autor>/', autorEdit, name='autorEdit'), 
    path('eliminar_a/<int:id_autor>/', autorEliminar, name='autorEliminar'), 
      
    ]
