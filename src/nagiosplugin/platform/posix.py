# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

"""POSIX implementation of platform-specific services"""

from ..error import Timeout
import fcntl
import signal


def with_timeout(t, func, *args, **kwargs):
    """Call `func` but terminate after `t` seconds."""
    def timeout_handler(signum, frame):
        raise Timeout('{}s'.format(t))

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(t)
    try:
        func(*args, **kwargs)
    finally:
        signal.alarm(0)


def flock_exclusive(fileobj):
    """Acquire exclusive lock for open file `fileobj`."""
    fcntl.flock(fileobj, fcntl.LOCK_EX)
