"""Core app views."""
from core.models import Article, Subscribers, Volunteers
from core.forms import volunteerForm, subscribeForm, contactForm
from django.shortcuts import redirect, render, get_object_or_404
from core.models import Stat
from core.utils import get_client_ip
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
# from django.conf import settings

def home_view(request):
    """Home page view."""
    context = {}
    return render(request, 'core/index.html', context)

def about_view(request):
    """About page view."""
    context = {}
    return render(request, 'core/about.html', context)

def projects_view(request):
    """Project page view."""
    context = {}
    return render(request, 'core/projects.html', context)

def involved_view(request):
    """Involved page view."""
    context = {}
    return render(request, 'core/involved.html', context)

def blog_view(request):
    """Blog page view."""
    context = {}
    return render(request, 'core/blog.html', context)

def article_view(request):
    """Article page view."""
    context = {}
    return render(request, 'core/article.html', context)

def contact_view(request):
    """Contact page view."""
    context = {}
    return render(request, 'core/contact.html', context)
