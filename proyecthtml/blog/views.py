from django.shortcuts import render

from django.views.generic.list import ListView

from .models import Post
#Vistas generales de la aplicacion
def blog_list(request):
    all_posts = Post.objects.all()

    context = {'posts': all_posts}

    return render(request, "blog/blog_list.html", context)

def blog_detail(request, id):
    detail_post = Post.objects.get(pk=id)

    context = {'post': detail_post}

    return render(request, "blog/blog_detail.html", context)


class BlogListView(ListView):
    model = Post
    template_name ="blog/blog_list_ccbv.html"
    context_object_name = "posts"