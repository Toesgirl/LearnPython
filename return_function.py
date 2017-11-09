#for example
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f1=lazy_sum(1,2,3,4,5)
f2=lazy_sum(1,2,3,4,5)
print(f1==f2)

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum()
print(lazy_sum(1,2,3,4,5))


