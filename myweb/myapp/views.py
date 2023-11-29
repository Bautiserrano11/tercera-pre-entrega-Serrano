from django.shortcuts import render, redirect
from .models import Autor, Libro, Pelicula
from .forms import FormularioAutor, FormularioLibro, FormularioPelicula, FormularioBusqueda

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'myapp/lista_libros.html', {'libros': libros})

def agregar_datos(request):
    if request.method == 'POST':
        formulario_libro = FormularioLibro(request.POST)
        formulario_pelicula = FormularioPelicula(request.POST)
        formulario_autor = FormularioAutor(request.POST)

        if formulario_libro.is_valid() and formulario_pelicula.is_valid() and formulario_autor.is_valid():
            formulario_libro.save()
            formulario_pelicula.save()
            formulario_autor.save()
            return redirect('lista_libros')

    else:
        formulario_libro = FormularioLibro()
        formulario_pelicula = FormularioPelicula()
        formulario_autor = FormularioAutor()

    return render(request, 'myapp/agregar_datos.html', {'formulario_libro': formulario_libro, 'formulario_pelicula': formulario_pelicula, 'formulario_autor': formulario_autor})

def busqueda(request):
    if request.method == 'GET':
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            consulta = formulario.cleaned_data['consulta']
            resultados = Libro.objects.filter(titulo__icontains=consulta) | \
                          Pelicula.objects.filter(titulo__icontains=consulta) | \
                          Autor.objects.filter(nombre__icontains=consulta)
            return render(request, 'myapp/resultados_busqueda.html', {'resultados': resultados, 'consulta': consulta})
    else:
        formulario = FormularioBusqueda()

    return render(request, 'myapp/busqueda.html', {'formulario': formulario})
