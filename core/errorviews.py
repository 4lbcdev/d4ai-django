"""Error views."""
from django.shortcuts import render


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
    # context = {'message': 'some custom messages'}
    return render(request, 'core/40x.html', context)
