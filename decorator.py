import functools

def my_decorator(method):
    @functools.wraps(method) #Without the use the name of the 'example' function would have been 'wrapper'
    def wrapper(*args, **kwargs):
        print 'Calling decorated function'
        return method(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print 'Called example function'

example()
print example.__name__
print example.__doc__