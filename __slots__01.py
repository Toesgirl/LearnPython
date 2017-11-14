class student(object):
    __slots__=('name','age')
class G(student):
    pass

s=student()
s.name='xiao1'
s.age=23
g=G()
g.score=23

