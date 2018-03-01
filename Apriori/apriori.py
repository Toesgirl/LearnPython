# coding=utf-8-----
from numpy import *
def loadDataSet():
    return [[1,3,4], [2,3,5], [1,2,3,5], [2,5]]
def createC1(dataSet):
    C1 = []
    for transaction in  dataSet:
        for item in transaction:
            if  not [item] in C1:
                C1.append([item])
    C1.sort()
    return  map(frozenset,C1)#frozenset类型与set类似，但是不去重复值，里面的值是不可改变的
def scanD(D, CK, minSupport):
    ssCnt = {}
    for tid in D:
        for can in CK:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1#can是否在tid中
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems#计算所有项集的支持度
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData
dataSet = loadDataSet()
#print(dataSet)
#C1 = createC1(dataSet)
#print(C1)
#D = map(set,dataSet)
#print(D)
#L1, sup = scanD(D, C1, 0.5)
#print(L1)
#算法
def aprioriGen(Lk, k):#类似0,1,2生成（01）（02）（12）
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #将前k-2个项相同时，将两个集合合并
                retList.append(Lk[i] | Lk[j])
    return retList
def apriori(dataSet, minSupport = 0.5):#频繁项集
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D,C1,minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        CK = aprioriGen(L[k-2], k)
        LK, supK = scanD(D, CK,minSupport)
        supportData.update(supK)
        L.append(LK)
        k += 1
    return  L, supportData
l,su=apriori(dataSet)
#print(l)
#print(l[2])
#print(su)
#从频繁项集中挖掘关联规则
def generateRules(L, supportData, minConf=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf:
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
r=generateRules(l,su,minConf=0.7)
