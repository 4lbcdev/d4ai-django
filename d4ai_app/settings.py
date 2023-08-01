"""
Django settings for d4ai_app project.
"""
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = "d4ai.org"
SECRET_KEY = os.getenv('app_key')

if os.getenv('environment') == "dev":
    from d4ai_app.settings_dev import *
else:
    from d4ai_app.settings_prod import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    # Add-ons
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'd4ai_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'd4ai_app.wsgi.application'

# MySQL database settings
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.getenv('MYSQLname'),
        'USER': os.getenv('MYSQLuser'),
        'PASSWORD': os.getenv('MYSQLpwd'),
        'HOST': os.getenv('MYSQLhost'),
        'PORT': os.getenv('MYSQLport'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            "init_command": "SET default_storage_engine=INNODB",
            'charset': 'utf8mb4',
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]


MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = 'core.User'
LOGIN_URL = '/core/auth/'
LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# Specify the absolute path to the directory where static files will be collected.
STATIC_ROOT = '/home/daiorg/public_html/static/'
STATICFILES_DIRS = [
    # Add the path to app's static files
    os.path.join(BASE_DIR, 'static'),
]

# Media files (Images, Videos, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Temporary files (e.g. uploaded files)
TEMP = os.path.join(BASE_DIR, 'temp')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Third party plug-in settings for django-ckeditor
CKEDITOR_CONFIGS = {
    'full_editor': {
        'toolbar': 'full',
    },
    'custom_editor': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
}
