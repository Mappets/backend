from __future__ import absolute_import

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
if os.environ.get("DJANGO_DEBUG")=='True':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_solar.config.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mappets.settings")

app = Celery("mappets")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
