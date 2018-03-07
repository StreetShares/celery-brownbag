=====================================
Celery - Asynchronous Tasks in Python
=====================================

These are just quick notes we tried to cover while discussing Celery
over a brownbag discussion at lunch. They only complement the points
we were trying to get across. Reading through the links at the bottom will
likely cover everythin.

What is Celery
--------------

- Distributed

- Relies on message broker

- Works well for distributed computing

- Released 2009

- Originally tied to Django


Getting started
---------------
::

    sudo apt-get install rabitmq-server

    pip install celery

    pip install -U "celery[redis]"

Write a celery app with tasks. Start with::

    celery -A tasks worker --loglevel=info


What is a Message Broker
------------------------

Stores tasks on queues. Allows workers on different processes/machines to produce and consume tasks.
The broker stores data that answers the question "What work remains to be done?"


How it works
------------

Producers --task-> queue -> comsumer --success/fail--> backend for storage


Do we need a backend?
---------------------

No, not necessary.
Redis is ideal if needed


Concurrency Solutions
---------------------

- prefork pool (multiprocessing)
- eventlet (green threads)
- gevent (green threads)


Parallel Safety
---------------
- write tasks to be parallel safe
- use db transactions
- don't pass objects as task parameters
    - pickle: security
    - pickle: stale data


Task Granularity
-----------------
too big - lose concurrency
too small - not enough workers


Notes
-----

amqp - async messaging queue protocol


SQS vs RabbitMQ as brokers
--------------------------

See: `Messaging Queue Showdown`_

.. _Messaging Queue Showdown: http://zerosignal0.github.io/blog/2014/05/25/messaging-queue-showdown-amazon-sqs-vs-celery-rabbitmq/


Scheduling
----------
blah blah

Check the docs, they are pretty thorough.


Load a task
-----------
::

    task = task_function.AsyncResult(task_id)


Links
-----

`Introduction to Celery`_

`Introduction to Celery Video`_

`Asynchronous Tasks in Python`_

`Using Celery With Flask`_

.. _Introduction to Celery: http://talks.caktusgroup.com/pyohio/2014/celery/index.html#/slide-content

.. _Introduction to Celery Video: https://www.youtube.com/watch?v=3cyq5DHjymw

.. _Asynchronous Tasks in Python: https://www.youtube.com/watch?v=fg-JfZBetpM

.. _Using Celery With Flask: https://blog.miguelgrinberg.com/post/using-celery-with-flask

