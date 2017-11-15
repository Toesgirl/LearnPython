class fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            l=[]
            for x in range(stop):
                if x>=start:
                    l.append(a)
                a,b=b,a+b
            return l
f=fib()
print(f[5])
print(f[5:10])
