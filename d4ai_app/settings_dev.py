"""
Django development settings for d4ai_app project.
"""
import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

ALLOWED_HOSTS = [
    os.getenv('L_HOST'),
    '127.0.0.1',
    "localhost",
]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False