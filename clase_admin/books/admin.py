from django.contrib import admin

from books.models import Autor, Editorial, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ("nombre", "apellido", "fecha_nacimiento")
        export_order = ("nombre", "apellido", "fecha_nacimiento")


class LibroInline(admin.StackedInline):
    model = Libro


@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    resource_class = AutorResource
    list_display = ["pk", "nombre", "apellido", "fecha_nacimiento", "email", "telefono"]
    ordering = [
        "apellido",
        "nombre",
    ]


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "ciudad",
        "telefono",
        "email",
        "sitio_web",
        "fecha_fundacion",
    ]
    list_filter = ["fecha_fundacion"]
    inlines = [
        LibroInline,
    ]

#Definir la accion personalaizada
def set_out_stock(modeladmin, request, queryset):
    #Actualizar los objetos seleccionados a publicados
    queryset.update(out_of_stock = True)
    #Mostrar un mensaje informativo en la interfaz del admin
    modeladmin.message_user(request, "Los libros selccionados han sido marcados como fuera de stock")

#Personalizamos el nombre de la accion 
set_out_stock.short_description = "Marcar como fuera de Stock"


#Definir accion personalizada para exportar a CSV
def export_posts_to_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type = "text/csv")
    response['content-Disposition'] = 'attachment; filename="books.csv'
    #creamos un writer para escribir archivos csv
    writer = csv.writer(response)

    writer.writerow(['Titulo', 'ISBN', 'Fecha de Publicacion', 'Numero de Paginas', 'Idioma'])
    for book in queryset:
        writer.writerow([book.titulo, book.isbn, book.fecha_publicacion, book.numero_paginas, book.idioma])

    return response
#Personalizar nombre del acction
export_posts_to_csv.short_description = "Exportar a CSV"

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "editorial",
        "isbn",
        "out_of_stock",
        "fecha_publicacion",
        "numero_paginas",
        "idioma",
    ]
    list_filter = ["editorial", "idioma", "out_of_stock"]
    search_fields = ["titulo", "autores_nombre"]
    filter_horizontal = ["autores"]
    actions = [set_out_stock, export_posts_to_csv]