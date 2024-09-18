from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Libro
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class LibroListView(ListView):
    model = Libro
    template_name = "libros/LibroList.html"
    context_object_name = 'libros'


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/LibroDetail.html"
    context_object_name = 'libro'

class LibroCreateView(CreateView):
    model = Libro
    fields = [
        'titulo', 'isbn', 'fecha_publicacion', 'numero_paginas', 'idioma',
        'descripcion', 'editorial', 'autores', 'genero', 'precio'
    ]
    template_name = "libros/LibroCreate.html"
    success_url = reverse_lazy('libro:list')


class LibroUpdateView(UpdateView):
    model = Libro
    fields = [
        'titulo', 'isbn', 'fecha_publicacion', 'numero_paginas', 'idioma',
        'descripcion', 'editorial', 'autores', 'genero', 'precio'
    ]
    template_name = "libros/LibroUpdate.html"
    success_url = reverse_lazy('libro:list')


class LibroDeleteView(DeleteView):
    model = Libro
    success_url = reverse_lazy('libro:list')
    template_name = "libros/LibroDelete.html"
