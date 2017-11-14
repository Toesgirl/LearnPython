class Student(object):
    name='stu'
s=Student()
print(s.name)
print(Student.name)
s.name='xiao'
print(s.name)
print(Student.name)