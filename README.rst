Celery - Asynchronous Tasks in Python
=====================================

- Distributed

- Relies on message broker

- Works well for distributed computing

- Released 2009

- Originally tied to Django


Getting started
---------------

    sudo apt-get install rabitmq-server

    pip install celery

    pip install -U "celery[redis]"

Write a celery app with tasks. Start with

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

http://zerosignal0.github.io/blog/2014/05/25/messaging-queue-showdown-amazon-sqs-vs-celery-rabbitmq/


Scheduling
----------
blah blah
Check the docs


Load a task
-----------

    task = task_function.AsyncResult(task_id)


Links
-----

http://talks.caktusgroup.com/pyohio/2014/celery/index.html#/slide-content

https://www.youtube.com/watch?v=3cyq5DHjymw

https://www.youtube.com/watch?v=fg-JfZBetpM

https://blog.miguelgrinberg.com/post/using-celery-with-flask

