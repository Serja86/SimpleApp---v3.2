import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project', broker='redis://localhost:6379/0')

app.autodiscover_tasks()

