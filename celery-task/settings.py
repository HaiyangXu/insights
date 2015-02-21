from celery.schedules import crontab

## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost//'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('tasks', )

## Using the database to store task state and results.
#CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'

#CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}


CELERYBEAT_SCHEDULE = {
    # Executes every Day morning at 7:30 A.M
    'add-every-day-morning': {
        'task': 'tasks.testschedule',
        'schedule': crontab(hour=7, minute=30 ),
        'args': (16, 16),
    },
        'add-every-day-night': {
        'task': 'tasks.testschedule',
        'schedule': crontab(hour=19, minute=30 ),
        'args': (16, 16),
    },
}

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']