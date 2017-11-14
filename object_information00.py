class My(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=My()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
print(setattr(obj,'y',19))
print(hasattr(obj,'y'))
print(obj.y)
print(getattr(obj,'y'))
print(getattr(obj,'z',22))
print(hasattr(obj,'power'))
fn=getattr(obj,'power')
print(fn)
print(fn())


