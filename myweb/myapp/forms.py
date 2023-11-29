
from django import forms
from .models import Autor, Libro, Pelicula

class FormularioAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre']

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion']

class FormularioPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'fecha_estreno']

class FormularioBusqueda(forms.Form):
    consulta = forms.CharField(max_length=100)
