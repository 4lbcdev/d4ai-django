"""Core app views."""
from core.forms import contactForm, subscriberForm, volunteerForm
from core.models import Article
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse


# Common function to handle form submissions for subscribing to the newsletter
def handle_subscribe_form(request, redirect_url):
    if 'submit_subscribe' in request.POST:
        subscribe_form = subscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(request, 'You have successfully subscribed to our newsletter.')
            return redirect(reverse(redirect_url))
    return None

def home_view(request):
    """Home page view."""
    context = {}
    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/index.html', context)

def about_view(request):
    """About page view."""
    context = {}
    # Handle subscribe form
    handle_subscribe_form(request, 'core:about')
    return render(request, 'core/about.html', context)

def projects_view(request):
    """Project page view."""
    context = {}
    # Handle subscribe form
    handle_subscribe_form(request, 'core:projects')
    return render(request, 'core/projects.html', context)

def involved_view(request):
    """Involved page view."""
    context = {}
    # Handle volunteer form
    if 'submit_volunteer' in request.POST:
        volunteer_form = volunteerForm(request.POST)
        if volunteer_form.is_valid():
            volunteer_form.save()
            messages.success(request, 'Your application has been sent successfully.')
            return redirect(reverse('core:involved'))

    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/involved.html', context)

def blog_view(request):
    """Blog page view."""
    context = {}
    context['articles'] = Article.objects.filter(status='P')
    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/blog.html', context)

def article_view(request, pk, slug):
    """Article page view."""
    context = {}
    context['article'] = get_object_or_404(Article, id=pk, slug=slug)
    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/article.html', context)

def contact_view(request):
    """Contact page view."""
    context = {}
    # Handle contact form
    if 'submit_contact' in request.POST:
        contact_form = contactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect(reverse('core:contact'))

    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/contact.html', context)
