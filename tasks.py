"""Playing around with Celery and RabitMQ."""

import time

from celery import Celery

# Note: amqp = async messaging queue protocol
app = Celery(
    'tasks',  # name of current module
    broker='amqp://localhost//',
    backend='redis://localhost'  # not required
)


@app.task
def check_favorite_developer(name):
    """Verify if the given name belongs to everyone's favorite."""
    favorites = [
        'andrew',
        'ahlers',
        'andrew ahlers',
        'aahlers',
        'shitburg',
        'asa',
        'assa',
        'shatnerz'
    ]
    if name.lower() in favorites:
        return True
    return False


@app.task
def vaibhav(seconds):
    """Do nothing for a given number of seconds."""
    time.sleep(seconds)
    return 'Wigan is the greatest!!!'


@app.task(bind=True)
def long_task(self):
    """Arbitrary long task."""
    # Note: we can load tasks with
    # task = long_function.AsyncResult(task_id)
    num = 100000
    for i in range(num):
        progress = float(i)/num
        # I think calling update_state causes errors if we call the task
        # as a function.
        self.update_state(
            state='PROGRESS',
            meta={'current': i, 'total': num, 'progress': progress, 'status': 'TEST'}

        )
    return 'DONE'
