from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sandesh.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('sandesh')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from django_celery_beat.models import PeriodicTask, CrontabSchedule

    # Clear the existing periodic tasks (optional)
    PeriodicTask.objects.all().delete()

    # Create a new periodic task to run every 20 minutes
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute='*/10'
    )

    PeriodicTask.objects.create(
        crontab=schedule,
        name='Scrape News every 10 minutes',
        task='news.tasks.scrape_news',  # Update the task path as per your project
    )

    # PeriodicTask.objects.create(
    #     crontab=schedule,
    #     name='Scrape Sports News every 20 minutes',
    #     task='news.tasks.scrape_sports_news',  # Update the task path as per your project
    # )

    # PeriodicTask.objects.create(
    #     crontab=schedule,
    #     name='Scrape Trade News every 20 minutes',
    #     task='news.tasks.scrape_trade_news',  # Update the task path as per your project
    # )


