# kthread
Killable threads in Python! 

## Purpose
The built-in `threading.Thread` class offers no simple solution to terminate a running thread.  `kthread.KThread` inherits `threading.Thread` and supplies methods named `exit()`, `kill()`, and `terminate()` that serve the same purpose: attempt to stop a thread if it's running.

## How it works
KThread leverages the CPython API to raise a `SystemExit` exception on a given thread.  Assuming that the thread is not blocked by an operating system call (such as `sleep`, `accept`, or `recv`), the thread will forcefully quit.

## DISCLAIMER
**TERMINATING THREADS MAY INTRODUCE INSTABILITY OR OTHER UNDESIRABLE EFFECTS IN YOUR PROGRAMS.  THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY.  THE MUNSHI GROUP CANNOT BE HELD LIABLE FOR ANY DAMAGES, LOSSES, OR EXPENSES INCURRED BY YOU OR YOUR ORGANIZATION WHILE USING THIS SOFTWARE.**

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
    
## License
MIT
