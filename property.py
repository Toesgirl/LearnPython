class student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def s(self,value):
        if not isinstance(value,int):
            raise ValueError('score...')
        if value < 0 or value > 100:
            raise ValueError('score.0-100..')
        self._score=value
s=student()
s.s=60
print(s.s)