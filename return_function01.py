##
# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
#
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f4,f5,f6=count1()
print(f4())
print(f5())
print(f6())
