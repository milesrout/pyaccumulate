import functools

def accumulate(accum_type):
    def outer_wrapper(f):
        @functools.wraps(f)
        def inner_wrapper(*args, **kwds):
            return accum_type(iter(f(*args, **kwds)))
        return inner_wrapper
    return outer_wrapper