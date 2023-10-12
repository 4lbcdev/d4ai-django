""" Core utilities.
This module contains common utilities for the core app.
"""
from django.core.mail import send_mail

def send_email(subject, message, from_email, recipient_list):
    """Send email."""
    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        pass