class student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'student object(name: %s)' % self.name
    __repr__=__str__
s=student('xiao')
print(s)