# -*- coding: utf-8 -*-
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

# -*- coding: utf-8 -*-
f=lambda x:x*x
print(f)
print(f(5))

# -*- coding: utf-8 -*-
def bulid(x,y):
    return lambda x,y:x*x+y*y
t=bulid(1,2)
print(t(2,3))
#
def bulid():
    return lambda x,y:x*x+y*y
t=bulid()
print(t(2,3))
print(bulid()(1,2))


# -*- coding: utf-8 -*-
sq=[]
for x in range(5):
    def f(n=x):
        return n**2
    sq.append(f())
print(sq)

# -*- coding: utf-8 -*-
squares = []
squares.append(lambda n: n**2)
print(squares[0](2))

