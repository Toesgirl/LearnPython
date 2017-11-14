class student(object):

    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score...')
        if value < 0 or value > 100:
            raise ValueError('score.0-100..')
        self._score=value
s=student()
s.set_score(60)
print(s.get_score())