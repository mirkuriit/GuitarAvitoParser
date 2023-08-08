import time


def fet(func):
    "fet - function execution time"
    from functools import wraps
    @wraps(func)
    def inner(self):
        now_time = time.time()
        func(self)
        new_time = time.time() - now_time
        return new_time
    return inner
