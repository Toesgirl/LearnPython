# -*- coding: utf-8 -*-
import functools
def now():
    print("xiaoqi")
f=now
print(f.__name__)

# -*- coding: utf-8 -*-
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' %  func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print("xiaoqi")
print(now())
print(now.__name__)
# -*- coding: utf-8 -*-

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %  func.__name__)
        return func(*args,**kw)
    return wrapper
def now():
    print("xiaoqi")
n=log(now)
print(n())

# -*- coding: utf-8 -*-
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('DEBUG')
def now():
    print("xiaoqi")
print(now())
print(now.__name__)
