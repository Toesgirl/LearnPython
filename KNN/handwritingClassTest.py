# coding=utf-8
from numpy import *
from os import listdir
import classify0
import img2vector
#用ｋｎｎ算法识别手写数字
def handwritingClassTest():
    hwLabels=[]#用来存储数字类别０－９：即所有测试样本文件名字的第一个数字
    trainingFileList=listdir('trainingDigits')#listdir用来获取目录内容
    m=len(trainingFileList)#多少个训练样本文件
    trainingMat=zeros((m,1024))#用来存储所有训练样本
    for i in range(m):

        fileNameStr=trainingFileList[i]#第ｉ个文件名字　例：9_45.txt
        fileStr=fileNameStr.split('.')[0]#得到9_45,切片得到第一个字符串
        classNumStr=int(fileStr.split('_')[0])#得到９
#从文件名字解析分类数字
        hwLabels.append(classNumStr)#所有的类别标签

        trainingMat[i,:]=img2vector.img2vector('trainingDigits/%s' % fileNameStr)#图像转为向量存储到这个矩阵中

##########测试部分
    testFileList=listdir('testDigits')#获取测试样本的文件目录
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):

        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
#上三行代码得到测试样本的所有类别属性，用来核对算法的正确率
        vectorUnderTest=img2vector.img2vector('testDigits/%s' % fileNameStr)
        classifierResult=classify0.classify0(vectorUnderTest,trainingMat,hwLabels,3)
##                                      　　　每行测试样本　　　　所有训练样本　　所有训练样本标签
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult,classNumStr))
        if (classifierResult != classNumStr): errorCount +=1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))