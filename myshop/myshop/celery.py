import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

# load any custom configuration from your project settings with namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery to auto-discover asynchronous tasks for your applications
# Celery will look for a tasks.py file in each application
app.autodiscover_tasks()
