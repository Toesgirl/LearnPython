def print_scores(**kw):
    print('      Name  Score')
    print('---------------')
    for name, score in kw.items():
        print('%10s  %d'  % (name, score))

print_scores(adam=99,lisa=88,bart=77)
data={
     'adam lee':99,
     'lisa s':88,
     'f.bare':77
 }
print_scores(**data)
def print_info(name,*,gender,city='beijing',age):
     print('   personal info')
     print('     name:%s' % name)
     print('   gender:%s' % gender)
     print('     city:%s' % city)
     print('      agr:%s' % age)
     print()

print_info('bob',gender='male',age=20)
print_info('lisa',gender='female',city='shanghai',age=20)