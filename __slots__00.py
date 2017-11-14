class student(object):
    pass
s=student()
s.name='xiao1'
print(s.name)
def set_age(self,age):# 定义一个函数作为实例方法
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25)
print(s.age)

#为了给所有实例都绑定方法，可以给class绑定方法
student.set_age=set_age
s2=student()
s2.set_age(33)
print(s2.age)