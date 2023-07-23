"""Core app views."""
# from core.models import Article, Subscribers, Volunteers
# from core.forms import volunteerForm, subscribeForm, contactForm
from django.shortcuts import redirect, render, get_object_or_404
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

def page404(request, exception):
    """Page not found view."""
    context = {
        'exception': exception,
        'code': '404',
        'error_msg': "The page you're looking for doesn't exist."
    }
    return render(request, 'core/40x.html', context)

def page403(request, exception):
    """Permission denied view."""
    context = {
        'exception': exception,
        'code': '403',
        'error_msg': "You don't have permission to access this page."
    }
    return render(request, 'core/40x.html', context)

def page500(request):
    """Server error view."""
    context = {
        'code': '500',
        'error_msg': "Something went wrong."
    }
    return render(request, 'core/50x.html', context)

def csrf_failure(request, reason=""):
    """CSRF failure view."""
    context = {}
    return render(request, 'core/40x.html', context)
