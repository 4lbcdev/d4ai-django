"""
Django production settings for d4ai_app project.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = [
    'd4ai.org',
    'www.d4ai.org',
    'dev2412.d4ai.org',
]

# STATIC_ROOT = '/home/daiorg/public_html/static/'
STATIC_ROOT = '/home/daiorg/dev2412.d4ai.org/static/'

# MEDIA_ROOT = '/home/daiorg/public_html/media/'
MEDIA_ROOT = '/home/daiorg/dev2412.d4ai.org/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# SECURITY RELATED HEADERS
SECURE_CONTENT_TYPE_NOSNIFF = True # Protects against MIME type sniffing attacks
SECURE_BROWSER_XSS = True # Enables the browser’s XSS filter
SECURE_HSTS_SECONDS = 0 # Ensures the site is only accessible via HTTPS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True # Requests over HTTP are redirected to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY RELATED COOKIES
SESSION_COOKIE_SECURE = True # Send the session cookie over secure (HTTPS) connections only
CSRF_COOKIE_SECURE = True # Ensure that the CSRF cookie is sent over secure connections only

# CROSS SITE REQUEST FORGERY SETTINGS
CSRF_COOKIE_AGE = 15724800 #6months
CSRF_FAILURE_VIEW = 'core.errorviews.csrf_failure'

# SESSION SETTINGS
SESSION_EXPIRE_SECONDS = 7200 #2hrs
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_TIMEOUT_REDIRECT = "/"
