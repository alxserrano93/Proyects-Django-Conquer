from django.urls import path

from .views import blog_list, blog_detail, BlogListView

app_name = "blog"

urlpatterns = [
    path("", blog_list, name="blog_list"),

    path("<int:id>/", blog_detail, name="blog_detail"),
    path("ccbv/", BlogListView.as_view(), name="blog_list_ccbv"),

]