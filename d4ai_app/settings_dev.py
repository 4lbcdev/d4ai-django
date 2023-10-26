"""
Django development settings for d4ai_app project.
"""
import os
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = [
    os.getenv('L_HOST'),
    '127.0.0.1',
    "localhost",
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False