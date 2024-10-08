"""
Django production settings for d4ai_app project.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = [
    'd4ai.org',
    'www.d4ai.org',
    '*.d4ai.org',
]

MEDIA_ROOT = '/home/daiorg/public_html/media/'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

CSRF_COOKIE_AGE = 15724800 #6months
CSRF_FAILURE_VIEW = 'core.errorviews.csrf_failure'

SESSION_EXPIRE_SECONDS = 7200 #2hrs
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_TIMEOUT_REDIRECT = "/"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
