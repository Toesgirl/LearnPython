class s(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def h(self):
        return self._width*self._height
q=s()
q.width=1
q.height=3
print(q.h)