# kthread
Killable threads in Python!

## Installation
To install this package, run the following command:

    $ pip install kthread

## Usage

    >>> import time
    >>> import kthread
    >>> def func():
    >>>     try:
    >>>         while True:
    >>>             time.sleep(0.2)
    >>>     finally:
    >>>         print "Greetings from Vice City!"
    >>>
    >>> t = kthread.KThread(target = func, name = "KillableThread1")
    >>> t.start()
    >>> t.isAlive()
    True
    >>> t.terminate()
    Greetings from Vice City!
    >>> t.isAlive()
    False
