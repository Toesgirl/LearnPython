from functools import wraps
from time import time, sleep

start_time = time()
print("\n现在开始运行...\n\n**********************\n")

def log(text):
    def decorator(func):
        @wraps(func)
        def wrapers(*args, **kw):
            print("函数{0}()即将执行，此时系统已运行了 {1} 秒\n".format(func.__name__, time()-start_time))
            startTime =  time()
            return (func(*args, **kw),print("函数{0}()执行了 {1} 秒后，结束了自己\n".format(func.__name__, time()-startTime)))[0]
        return wrapers
    return (decorator,print("我是一个带参数的装饰器，我的参数是 '{}' ".format(text) ))[0] if text.__str__() == text else decorator(text)

@log
def abc():
    print("我是函数abc(),我正在执行中，不过我要睡 5 秒\n")
    sleep(5)

@log('嘿，伙计，是你吗？\n')
def efg():
    print("我是函数efg(),我正在执行中，我只想睡 3 秒\n")
    sleep(3)

abc()
efg()

print("运行结束，一共运行了",time()-start_time,"秒")

##实际上可以看出，在文件运行时，函数还未执行前，装饰器自己先运行了一阵。
 #给装饰器传递参数时，返回了 decorator 这个函数自动执行，然后又返回了warpers，所以在运行函数 efg() 之前，efg函数已变成了wrapers函数。
 #没有参数时，返回 wrapers函数，所以在运行函数 abc() 之前，abc函数已变成了wrapers函数
 #所以，你以为你执行了abc(),或者efg()这个函数，其实不然，你只是执行了wrapers()这个函数
 #总而言之，装饰器的功能就是一个 在保持此函数功能不变的基础上，给它额外增加了一些功能
