import sys
import os

# Add the project directory to the PYTHONPATH
sys.path.append('/home/daiorg/repositories/d4ai-django')

# Set the Django settings module environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'd4ai_app.settings'

from d4ai_app.wsgi import application
