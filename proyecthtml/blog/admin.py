from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PorstResource(admin.ModelAdmin):
    model = Post
    list_display = "pk", "title", "author", "show_home", "created_at"