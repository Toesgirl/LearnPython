# coding=utf-8
#将决策树存储到磁盘中，用第二个函数调用
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


a={'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

storeTree(a,'classifierStorage.txt')
print(grabTree('classifierStorage.txt'))


