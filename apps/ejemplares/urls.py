from django.urls import path
from apps.ejemplares.views import *

app_name='ejemplares'
urlpatterns = [
    path('', listEjemplares, name='listEjemplares'), 
    path('nuevo/', ejemplaresCreate, name='ejemplaresCreate'), 
    path('actualizar/<int:id_ejemplar>/', ejemplaresEdit, name='ejemplaresEdit'), 
    path('eliminar/<int:id_ejemplar>/', ejemplaresEliminar, name='ejemplaresEliminar'), 
    
    path('usuario/', listUsuarios, name='listUsuarios'),
    path('nuevo_u/', usuariosCreate, name='usuariosCreate'), 
    path('actualizar_u/<int:id_usuario>/', usuariosEdit, name='usuariosEdit'), 
    path('eliminar_u/<int:id_usuario>/', usuariosEliminar, name='usuariosEliminar'), 
   
    path('prestamo/', listPrestamo, name='listPrestamo'),
    path('nuevo_p/', prestamoCreate, name='prestamoCreate'), 
    path('actualizar_p/<int:id_prestamo>/', prestamoEdit, name='prestamoEdit'), 
    path('eliminar_p/<int:id_prestamo>/', prestamoEliminar, name='prestamoEliminar'), 

    path('consulta1/', consulta1, name='consulta1'),
    path('consulta2/', consulta2, name='consulta2'),
    path('consulta3/', consulta3, name='consulta3'),
]

