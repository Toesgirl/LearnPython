class student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
       self._birth=value
    @property
    def age(self):
        return 2033-self._birth
s=student()
s.birth=23
print(s.birth)