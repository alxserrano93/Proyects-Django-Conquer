from django.shortcuts import render, redirect

from  courses.models import Courses
from blog.models import Post
from .models import Contact
from .forms import ContactForm, LoginForm, UserRegisterForm
from django.urls import reverse

from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# #Vistas generales de la aplicacion
# def home_view(request):
#     context = {
#         'courses': Courses.objects.filter(show_home = True),
#         'posts': Post.objects.filter(show_home = True),
#     }
#     return  render(request, "core/home.html", context)


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Courses.objects.filter(show_home = True)
        context['posts'] = Post.objects.filter(show_home = True)
        return context


def about_us_view(request):
    return  render(request, "core/about_us.html")



def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect(reverse('core:home'))               
        
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': 'Usuario no valido'
                }
                return render(request, "core/login.html", context)
            
        else:
            context = {
                'form':form,
                'error': True
            }
            return render(request, "core/login.html", context)

    else:
        form = LoginForm()
        context = {
            'form' : form
        }
    return  render(request, "core/login.html", context)



def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))



def register_view(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            user = User.objects.create_user(username, email, password2)
            if user:
                user.first_name = first_name
                user.last_name = first_name
                user.save()
            
            context = {
                'msj': 'Usuario creado correctamente'
            }

            return render(request, "core/register.html", context)
            
        else:
            context = {
                'form':form,
                'error': True
            }
            return render(request, "core/register.html", context)

    else:
        form = UserRegisterForm()
        context = {
            'form' : form
        }
        return  render(request, "core/register.html", context)



def contact_us_view(request):
    if request.POST:
        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email  = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            print(f'Se ha enviado un correo a {nombre} procedente del email {email} con el comentario {comentario}')

            message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

            success = send_mail(
                "Formulario de contacto de mi web",
                message_content,
                "alexserr.dev@gmail.com",
                ["alexserr.dev@gmail.com"],
                fail_silently=False,
            )

            context = {
                'form' : formulario,
                'success' : success
            }
            return render(request, "core/contact_us.html", context)
        else:

            context = {
                'form' : formulario
            }
            return render(request, "core/contact_us.html", context)
        
    formulario = ContactForm()
    context = {
        'form' : formulario
    }
    return  render(request, "core/contact_us.html", context)


