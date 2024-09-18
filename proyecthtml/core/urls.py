from django.urls import path
from .views import home_view, about_us_view, register_view, login_view, contact_us_view, logout_view, HomeView, HomeView2

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home2", HomeView2.as_view(), name="home2"),
    path("sobre-nosotros/", about_us_view, name="about_us"),
    path("contacta-con-nosotros/", contact_us_view, name="contact_us"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]