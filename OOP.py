# -*- coding: utf-8 -*-
class student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print(self):
        print('%s: %s' % (self.name,self.score))
    def get_grade(self):
        if self.score>=90:
            return 'a'
        elif self.score>=60:
            return 'b'
        else:
            return 'c'

bart=student('bart Simpson',89)
lisa=student('lisa Simpson',23)
bart.print()
lisa.print()
print(bart.get_grade())
bart.score=0
print(bart.score)

# -*- coding: utf-8 -*-
class student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print(self):
        print('%s: %s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        self.__score=score

bart=student('bart Simpson',89)
lisa=student('lisa Simpson',23)
print(bart._student__name)
print(bart.get_name())
bart.set_score(2)
print(bart.get_score())
bart.__name='new'
print(bart.__name)
print(bart.get_name())

# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 10159)
print('bart.get_name() =', bart.get_name())
bart.set_score(103)
print('bart.get_score() =', bart.get_score())
print('DO NOT use bart._Student__name:', bart._Student__name)
