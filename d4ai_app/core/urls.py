"""Core app URL Configuration."""
from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path("", home_view, name="index"),
    path("about/", about_view, name="about"),
    path("projects/", projects_view, name="projects"),
    path("involved/", involved_view, name="involved"),
    path("blog/", blog_view, name="blog"),
    path("article/", article_view, name="article"),
    path("contact/", contact_view, name="contact"),
]
