from functools import wraps

# Without parameters
'''''
def introduce(f):
    @wraps(f)
    def outer(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs) 
    return outer
'''''

# Without parameters with separation def decorator
'''''
def decorator(real_dec):
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            return real_dec(f, *args, **kwargs)
        return inner
    return outer

@decorator
def introduce(f, *args, **kwargs):
    print(f.__name__)
    return f(*args, **kwargs)
'''''

# With parameters
'''''
#With parametrs
def introduce(*decargs, **deckwargs):
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            print(f.__name__ * decargs[0])
            return f(*args, **kwargs)
        return inner
    return outer
'''''


# With parameters and separation def decorator
def parametrize(new_dec):
    a = 1

    def param_deco(*args, **kwargs):
        def res_deco(f):
            return new_dec(f, *args, **kwargs)

        return res_deco

    return param_deco


@parametrize
def introduce(f, *decargs, **deckwargs):
    a = 1

    @wraps(f)
    def inner(*args, **kwargs):
        print(f.__name__ * decargs[0])
        return f(*args, **kwargs)

    return inner


@introduce(3)
def identity(x):
    a = 1
    return x


'''''
from functools import wraps, partial

def bucket(func=None, *decargs, **deckwargs):
    if func is None:
        return partial(bucket, **deckwargs)

    @wraps(func)
    def inner(*args, **kwargs):
        print(deckwargs)
        return func(*args, **kwargs)
    return inner

@bucket
def identity(x):
  return x

print(identity(42))
'''''
