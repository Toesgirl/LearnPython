# -*- coding: utf-8 -*-
def int2(x,base=2):
    return int(x,base)
print(int2('1000'))


# -*- coding: utf-8 -*-
import functools
int=functools.partial(int,base=2)
print(int('1000'))
print(int('1000',base=10))

# -*- coding: utf-8 -*-
max2=functools.partial(max,10)
print(max2(2,5,7))