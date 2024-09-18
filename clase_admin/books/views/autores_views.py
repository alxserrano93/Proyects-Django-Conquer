from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Autor
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class AutorListView(ListView):
    model = Autor
    template_name = "autores/AutorList.html"
    context_object_name = 'autores'


class AutorDetailView(DetailView):
    model=Autor
    template_name = "autores/AutorDetail.html"
    context_object_name = 'autor'


class AutorCreateView(CreateView):
    model = Autor
    template_name = "autores/AutorCreate.html"
    fields = [
        'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia', 'email', 'telefono', 'sitio_web', 'premios'
    ]
    success_url = reverse_lazy('autor:list')


class AutorUpdateView(UpdateView):
    model = Autor
    fields = [
        'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'biografia', 'email', 'telefono', 'sitio_web', 'premios'
    ]
    template_name = "autores/AutorUpdate.html"
    success_url = reverse_lazy('autor:list')


class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor:list')
    template_name = "autores/AutorDelete.html"

    

# def autor_detail(request, id):

#     autores = [
#         {"id": 1, "nombre": "Antonio", "f_nac": date(1980, 8, 1)},
#         {"id": 2, "nombre": "Felipe", "f_nac": date(1985, 10, 1)},
#         {"id": 3, "nombre": "Matilde", "f_nac": date(1990, 11, 5)},
#     ]

#     context = {
#         "autor": None,
#     }
#     for autor in autores:
#         if autor["id"] == id:
#             context["autor"] = autor
#             break

#     return render(request, "autores/autor_detail.html", context)