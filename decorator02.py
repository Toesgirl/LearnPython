import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text[0],func.name))
            f=func(*args,**kw)
            print(text[1])
            return f
        return wrapper
    return decorator
@log('Begin call','End call')
def f():
    print('a')
print(f())