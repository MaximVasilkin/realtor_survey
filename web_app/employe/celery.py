import os
from celery import Celery
from .settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employe.settings')

app = Celery('django_celery',
             backend=CELERY_RESULT_BACKEND,
             broker=CELERY_BROKER_URL)

app.conf.broker_connection_retry_on_startup = True

app.conf.update(task_store_result=False)

app.autodiscover_tasks()

