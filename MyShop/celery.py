from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyShop.settings')

app = Celery('MyShop', broker='amqp://')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
