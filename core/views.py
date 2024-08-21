"""Core app views."""
import threading
from core.forms import contactForm, subscriberForm, volunteerForm
from core.models import Article, Stat
from core.utils import send_email, get_client_ip
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt


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
    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="homepage",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    # Check if the user has accepted cookies and set context accordingly
    # cookie_accepted = request.COOKIES.get('cookie_accepted', 'no') == 'yes'
    context = {
        # 'cookie_accepted': cookie_accepted,
        'articles': Article.objects.filter(status='P')[0:4]
    }
    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/index.html', context)

def about_view(request):
    """About page view."""
    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="about_page",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    context = {}
    # Handle subscribe form
    handle_subscribe_form(request, 'core:about')
    return render(request, 'core/about.html', context)

def projects_view(request):
    """Project page view."""
    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="projects_page",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    context = {}
    # Handle subscribe form
    handle_subscribe_form(request, 'core:projects')
    return render(request, 'core/projects.html', context)

def involved_view(request):
    """Involved page view."""
    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="involved_page",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
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
    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="blog_page",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    context = {}
    context['articles'] = Article.objects.filter(status='P')
    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/blog.html', context)

def article_view(request, pk, slug):
    """Article page view."""
    article=get_object_or_404(Article, id=pk, slug=slug)
    article_url = article.get_absolute_url()

    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page=article_url,
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    context = {article: article}
    # context['article'] = get_object_or_404(Article, id=pk, slug=slug)
    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/article.html', context)

def contact_view(request):
    """Contact page view."""
    ip = get_client_ip(request)
    Stat.objects.get_or_create(
        page="contact_page",
        IPAddres=ip,
        device = request.META.get('HTTP_USER_AGENT')
    )
    context = {}
    # Handle contact form
    if 'submit_contact' in request.POST:
        contact_form = contactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent successfully.')
            subject = f'New message from {contact_form.cleaned_data["full_name"]}'
            message = f'Name: {contact_form.cleaned_data["full_name"]}\nEmail: {contact_form.cleaned_data["email"]}\nMessage: {contact_form.cleaned_data["message"]}\n\n---------------------------------------------------------------------\nThis is a copy of a message sent to you on the site D4AI.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.EMAIL_HOST_USER]
            # try:
            #     send_mail(subject, message, from_email, recipient_list)
            #     print(f"Email sending succeeded")
            # except Exception as e:
            #     print(f"Email sending failed: {e}")
            # Create a thread to send the email asynchronously
            email_thread = threading.Thread(target=send_email, args=(subject, message, from_email, recipient_list))
            email_thread.start()
            return redirect(reverse('core:contact'))

    # Handle subscribe form
    handle_subscribe_form(request, 'core:index')
    return render(request, 'core/contact.html', context)

# @csrf_exempt
# def set_cookie(request):
#     """Set the cookie to remember the user's choice."""
#     if request.method == 'POST':
#         response = JsonResponse({'status': 'Cookie accepted'})
#         response.set_cookie('cookie_accepted', 'yes')
#         return response
#     return JsonResponse({'status': 'Failed'}, status=400)
