# coding=utf-8
import operator
#投票表决的方法决定该叶子节点的分类；此代码和classify0部分的投票表决代码非常类似

def majorityCnt(classList):
    classCount={}
    for  vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote] +=1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
