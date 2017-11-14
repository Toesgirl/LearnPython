import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)
print(isinstance([1,2,3],(list,tuple)))
print(dir(str))
print('abc'.__len__())