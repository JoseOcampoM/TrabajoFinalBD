from django.shortcuts import render,redirect
from apps.libros.models import *
from apps.libros.formAutor import AutorForm
from apps.libros.formLibro import LibrosForm

def listLibros(request):
    libros = Libro.objects.all().order_by('id')
    context = {'libros':libros} 
    return render(request, 'libros/listLibros.html', context)

def librosCreate(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libros:listLibros') 
    else:
        form = LibrosForm()
        return render(request,'libros/libros_form.html', {'form': form})

def librosEdit(request, id_libro):
    libro = Libro.objects.get(pk=id_libro)

    if request.method == 'GET':
        form = LibrosForm(instance=libro)
    else:
        form = LibrosForm(request.POST, instance=libro) 
        if form.is_valid():
            form.save()
        return redirect('libros:listLibros') 

    return render(request,'libros/libros_form.html', {'form': form})

def librosEliminar(request, id_libro):
    libros = Libro.objects.get(pk=id_libro)
    libros.delete()
    return redirect('libros:listLibros') 

def listAutor(request):
    autor = Autor.objects.all().order_by('id')
    context = {'libros':autor} 
    return render(request, 'autor/listAutor.html', context)

def autorCreate(request):
    if request.method == 'POST':
        form = AutorForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect('libros:listAutor') 
    else:
        form = AutorForm()
        return render(request,'autor/autor_form.html', {'form': form})

def autorEdit(request, id_autor):
    autor = Autor.objects.get(pk=id_autor)

    if request.method == 'GET':
        form =  AutorForm(instance= autor)
    else:
        form = AutorForm(request.POST, instance= autor) 
        if form.is_valid():
            form.save()
        return redirect('libros:listAutor') 

    return render(request,'autor/autor_form.html', {'form': form})
  
def autorEliminar(request, id_autor):
    autor = Autor.objects.get(pk=id_autor)
    autor.delete()
    return redirect('libros:listAutor') 