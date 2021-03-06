import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from Analytics.models import busarrivalv2
from datetime import datetime
from datetime import timedelta
import time
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery import task

@shared_task
def delete_record_older_than_three_days():
    print('From scheduler task ----->>',"For Delete ")
    response = busarrivalv2.objects.filter(last_updated_time__lte=datetime.now()-timedelta(days=1)).delete()
    return response

@task(name="delete_record_older_than_one_days_beat")
def delete_record_older_than_one_days_beat():
    print('From scheduler task ----->>',"For Delete ")
    response = busarrivalv2.objects.filter(last_updated_time__lte=datetime.now()-timedelta(days=1)).delete()
    return response