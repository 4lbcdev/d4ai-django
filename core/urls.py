"""Core app URL Configuration."""
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name = "core"

sitemaps = {
    'static_sitemap': StaticViewSitemap,
}

urlpatterns = [
    path("", home_view, name="index"),
    path("about/", about_view, name="about"),
    path("projects/", projects_view, name="projects"),
    path("get-involved/", involved_view, name="involved"),
    path("blog/", blog_view, name="blog"),
    path("article/<slug:slug>-<int:pk>", article_view, name="article"),
    path("contact/", contact_view, name="contact"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
