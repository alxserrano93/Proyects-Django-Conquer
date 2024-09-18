from django.shortcuts import render

from .models import Courses
from django.contrib.auth.decorators import login_required

#Vistas generales de la aplicacion
@login_required
def course_list(request):
    all_courses = Courses.objects.all()

    context = {'courses': all_courses}

    return render(request, "courses/course_list.html", context)

@login_required
def course_detail(request, id):
    detail_course = Courses.objects.get(pk=id)

    context = {'course': detail_course}

    return render(request, "courses/course_detail.html", context)