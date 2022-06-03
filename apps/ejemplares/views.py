from django.shortcuts import render, redirect
from apps.ejemplares.models import *
from apps.ejemplares.formEjemplares import EjemplaresForm
from apps.ejemplares.formUsuarios import UsuariosForm
from apps.ejemplares.formPrestamo import PrestamoForm
from django.db.models import Count

def listEjemplares(request):
    ejemplares = Ejemplares.objects.all().order_by('id')
    context = {'ejemplares':ejemplares} 
    return render(request, 'ejemplares/listEjemplares.html', context)

def home (request):
    return render(request, 'base/base.html')

def ejemplaresCreate(request):
    if request.method == 'POST':
        form = EjemplaresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listEjemplares')
    else:
        form = EjemplaresForm()
        return render(request,'ejemplares/ejemplar_form.html', {'form': form})

def ejemplaresEdit(request, id_ejemplar):
    ejemplar = Ejemplares.objects.get(pk=id_ejemplar)

    if request.method == 'GET':
        form = EjemplaresForm(instance=ejemplar)
    else:
        form =EjemplaresForm(request.POST, instance=ejemplar) 
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listEjemplares') 

    return render(request,'ejemplares/ejemplar_form.html', {'form': form})
 
def ejemplaresEliminar(request, id_ejemplar):
    ejemplar = Ejemplares.objects.get(pk=id_ejemplar)
    ejemplar.delete()
    return redirect('ejemplares:listEjemplares') 

def listUsuarios(request):
    usuario = Usuario.objects.all().order_by('id')
    context = {'ejemplares':usuario} 
    return render(request, 'usuarios/listUsuarios.html', context)

def usuariosCreate(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listUsuarios') 
    else:
        form = UsuariosForm()
        return render(request,'usuarios/usuarios_form.html', {'form': form})

def usuariosEdit(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'GET':
        form =  UsuariosForm(instance= usuario)
    else:
        form = UsuariosForm(request.POST, instance= usuario) 
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listUsuarios') 

    return render(request,'usuarios/usuarios_form.html', {'form': form})

def usuariosEliminar(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)
    usuario.delete()
    return redirect('ejemplares:listUsuarios') 

def listPrestamo(request):
    prestamo = Prestamo.objects.all().order_by('id')
    context = {'ejemplares':prestamo} 
    return render(request, 'prestamo/listPrestamo.html', context)

def prestamoCreate(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listPrestamo')
    else:
        form = PrestamoForm()
        return render(request,'prestamo/prestamo_form.html', {'form': form})

def prestamoEdit(request, id_prestamo):
    prestamo = Prestamo.objects.get(pk=id_prestamo)

    if request.method == 'GET':
        form =  PrestamoForm(instance= prestamo)
    else:
        form = PrestamoForm(request.POST, instance= prestamo) 
        if form.is_valid():
            form.save()
        return redirect('ejemplares:listPrestamo') 

    return render(request,'prestamo/prestamo_form.html', {'form': form})

def prestamoEliminar(request, id_prestamo):
    prestamo = Prestamo.objects.get(pk=id_prestamo)
    prestamo.delete()
    return redirect('ejemplares:listPrestamo') 

def consulta1(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta1=Prestamo.objects.values('ejemplar__localización','ejemplar__libro__título','ejemplar__libro__autor__nombres','fecha_dev','fecha_pres').filter(fecha_pres__range=[fecha1,fecha2])
    
    return render(request,'consultas/consulta1.html',{'consulta1':consulta1})

def consulta2(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')

    consulta2=Prestamo.objects.filter(fecha_pres__range=[fecha1,fecha2]).aggregate(Count('ejemplar'))
    
    context = {
        'fecha1': fecha1,
        'fecha2': fecha2,
        'consulta2': consulta2,
    }
    print(consulta1)
    return render(request,'consultas/consulta2.html',{'context':context})

def consulta3(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')

    consulta3=Prestamo.objects.values('usuario__nombres','usuario__apellidos').filter(fecha_pres__range=[fecha1,fecha2]).annotate(cantidad=Count('ejemplar'))
    
    return render(request,'consultas/consulta3.html',{'consulta3':consulta3})