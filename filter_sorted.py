#filter
#delete the blank space
def f(s):
    return s and s.split()
print(list(filter(f,['a','b',None,' '])))

#delete the even
def odd(n):
    return n%2==1
print(list(filter(odd,[1,2,3,4,5,6,7,8,9])))

#for prime number
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
for n in primes():
    if n<1000:
        print(n)
    else:
        break


#number back
def is_palindrome(n):
    s=str(n)
    return s[:]==s[::-1]
output=filter(is_palindrome,range(1,1000))
print(list(output))


#sorted
print(sorted([36,5,-12,-21]))
print(sorted([36,5,-12,-21],key=abs))
print(sorted(['bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))


#sort by name and grade
L=[('bob',75),('adam',92),('xiao',10)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2=sorted(L,key=by_name)
L3=sorted(L,key=by_score)
print(L2)
print(L3)


##renfrence code
from operator import itemgetter
L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(1)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))