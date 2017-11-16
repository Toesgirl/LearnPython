class fooerror(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise fooerror('invalid value: %s' % s)
    return 10/n
foo('0')