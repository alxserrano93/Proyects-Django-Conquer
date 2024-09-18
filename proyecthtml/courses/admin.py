from django.contrib import admin

# Register your models here.
from .models import Courses

@admin.register(Courses)
class CourseResource(admin.ModelAdmin):
    model = Courses
    list_display = "pk", "title", "show_home", "created_at"