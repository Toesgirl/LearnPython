#理解装饰器的例子
def sum(a, b):
    return a+b
result = sum(1,2)
print(result)
#最终输出：3
#现在做一个装饰器
#这个装饰器的功能是：在执行函数的时候，会告诉我是哪两个数在求和，不带return的：
def sum_log(func):
    def wrapers(a, b):
        print("{}+{}的值为：".format(a, b), end = '')
        func(a, b)
    return wrapers
@sum_log
def sum(a, b):
    return a+b
result = sum(1,2)
print(result)
#最终输出： 1+2的值为：None
#我再把装饰器改为带return的：
def sum_log(func):
    def wrapers(a, b):
        print("{}+{}的值为：".format(a, b), end = '')
        return func(a, b)
    return wrapers
@sum_log
def sum(a, b):
    return a+b
result = sum(1,2)
print(result)
#最终输出： 1+2的值为：3
#所以说一定不要忽略装饰器的原意