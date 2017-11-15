class student(object):
    def __init__(self):
        self.name='xaio'
    def __getattr__(self,attr):
        if attr=='score':
            return 99
s=student()
print(s.sc)




class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        #%s%s将字符串相互联系在一起
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)