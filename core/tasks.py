from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.models import *
from asynco.celery import *
import time,random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asynco.settings')
app = Celery('asynco')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

 

@app.task(bind=True)
def test(self):
	for i in range(0,1):
		Data.objects.create(number=i)
		time.sleep(2) 
		print (i)


@app.task(bind=True)
def long_task(self):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}