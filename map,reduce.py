#reduce
from functools import reduce
def f(x,y):
    return x+y
print(reduce(f,[1,3,5,7,9]))


#reduce
from functools import reduce
def add(x,y):
    return x*10+y
print(reduce(add,[1,2,3,4,5]))


#reduce
def prof(s):
    return reduce(lambda x,y:x*y,s)
print(prof([3,5,7,9]))


#map reduce str-->int
from functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(fn,map(char2num,'13579')))
#simple
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(t):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[t]
    return reduce(fn,map(char2num,s))
print(str2int('12345678'))
#lambda simple
def char2num(s):
    return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(lambda x,y:x*10+y,map(char2num,'123')))


#map reduce str-->float
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(t):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[t]
    return reduce(fn,map(char2num,s))
def str2float(s):
    str=s.split('.')
    before=str2int(str[0])
    after=str2int(str[1])/10**len(str[1])
    return before+after
print(str2float('123.456'))


#map reduce str-->float
#reference code...
def str2int(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(lambda x, y: x *10 + y, map(char2num, s))
def str2float(s):
    s_list = s.split('.')
    float_i = str2int(s_list[0])
    float_f = str2int(s_list[1]) / (10**len(s_list[1]))
    return float_i + float_f
print(str2float('123.456'))


#Name of standardized
def f(name):
    return name[0].upper()+name[1:].lower()
L1=['xiao','Qi','apple']
print(list(map(f,L1)))
# simple
L1=['ADma','leMon','apple']
print(list(map(lambda name:name.title(),L1)))
# simple
L1=['ADma','leMon','apple']
print(list(map(lambda name:name.capitalize(),L1)))


# -*- coding: utf-8 -*-
##
###temporary storage
###reference code...
from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))