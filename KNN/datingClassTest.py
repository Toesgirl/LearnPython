# coding=utf-8
from numpy import *
import operator
import autoNorm
import classify0
import file2matrix
##测试算法，错误率
def datingClassTest():
    horatio=0.10
    datingDataMat,datingLabels=file2matrix.file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals=autoNorm.autoNorm(datingDataMat)
##将数据集归一化，datingDataMat：所有的样本，datingLabels：样本标签
    m=normMat.shape[0]#总共多少行，例子１０００
    numTestVecs=int(m*horatio)#取出１０％，就是１００个样
    errorCount=0.0#错误
    for i in range(numTestVecs):#取出１０％测试
        classifierResult=classify0.classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        ##调用ｋｎｎ算法，　　　　　　　　　　　　　　每一行的测试数据　　　　　训练样本　　　　　　　　　　　　　　所有标签　　　　　　ｋ值是３　　
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult,datingLabels[i]))
        ##                                                                    输出测试的标签     正确的标签
        if (classifierResult != datingLabels[i]): errorCount +=1.0#若两者不等，错误加一
    print ("the total error rate is: %f " %(errorCount/float(numTestVecs)))
