import functools

def my_parametrized_decorator(parameter):
    def real_decorator(method):
        @functools.wraps(method) #Without the use the name of the 'example' function would have been 'wrapper'
        def wrapper(*args, **kwargs):
            print 'Calling decorated function'
            print parameter
            return method(*args, **kwargs)
        return wrapper
    return real_decorator

@my_parametrized_decorator('This is my decorator parameter')
def example():
    """Docstring"""
    print 'Called example function'

example()
print example.__name__
print example.__doc__