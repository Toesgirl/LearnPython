def fn(self,name='world'):
    print('hello, %s.' % name)
hello=type('hello',(object,),dict(hello=fn))
h=hello()
h.hello()
print(type(h))
print(type(hello))