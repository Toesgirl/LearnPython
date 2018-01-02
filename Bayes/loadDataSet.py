# coding=utf-8
from numpy import *
#创建一些实验样本;词集模型
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec= [0,1,0,1,0,1]
    return postingList,classVec

#创建一个不重复词的列表,以下提供了两方法
def createVocabList(dataSet):#词集模型
    vocabSet = set([])#创建一个空集
    for document in dataSet:
        vocabSet = vocabSet | set(document)#｜：并操作；每篇文档返回的新词集合添加到该集合中
    return list(vocabSet)
def bagOfWords2VecMN(vocabList, inputSet):#词集模型
    returnVec = [0]*len(vocabList)#创建一个和词汇表等长的０向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1#index() 函数用于从列表中找出某个值第一个匹配项的索引位置
    return returnVec#文档向量

#输入为词汇表和某个文档；此函数用来表示词汇表中的单词再输入文档中是否出现
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)#创建一个和词汇表等长的０向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1#index() 函数用于从列表中找出某个值第一个匹配项的索引位置
        else: print( "the word: %s is not in my Vocabulary!" % word)
    return returnVec#文档向量,例如０，１，０，１

#以上代码是初始化数据
#训练样本，找出那个单词最能表征类别，例如侮辱性文档类的单词
def trainNB0(trainMatrix, trainCategory):#输入经过处理的文档矩阵，每篇文档类别标签向量
    numTrainDocs = len(trainMatrix)#文档数目
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    #初始化概率
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == i:
            p1Num += trainMatrix[i]#向量相加
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive#输出两个向量，一个概率


#朴素贝叶斯分类函数；第一个输入函数是待分类函数，后三个输入上面代码已求函数
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


# coding=utf-8..................................................................................................
#这里是用开头的数据做了第一次测试，过滤网站的｀恶意留言
def testing1():
    a, b = loadDataSet()
    c = createVocabList(a)
    trainMat = []
    for postinDoc in a:
        trainMat.append(setOfWords2Vec(c, postinDoc))
    p0, p1, pA = trainNB0(array(trainMat), array(b))
    test1 = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(c, test1))
    print(test1, 'classified as: ', classifyNB(thisDoc, p0, p1, pA))
    test2 = ['stupid', 'garbage']
    this = array(setOfWords2Vec(c, test2))
    print(test2, 'classified as: ', classifyNB(this, p0, p1, pA))

# coding=utf-8..................................................................................................
#垃圾邮件的测试函数，用到了交叉验证方法和用正则表达式来切分句子
#解析字符串列表
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)#用正则表达式来切分句子，其中分隔符是除去单词和数字外的任意字符串
    return [tok.lower() for tok in listOfTokens if len(tok)>2]#除去少于两个字符的字符串，并小写
#抽取１０个作为测试，剩余用来训练，输出的是错误率
def spamTest():
    docList = []; classList = []; fullText = []
    #导入并解析文本文件
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)#垃圾邮件
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = range(50); testSet = []
    #随机构建训练集
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))#随机抽取
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    #对测试集分类
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print( "classification error", docList[docIndex])
    print('the error rate is: ',float(errorCount)/len(testSet))#每次输出结果是有差异的，取平均值

# coding=utf-8..................................................................................................
#使用贝叶斯分类器从个人广告中获取低于倾向
#RSS源分类器和高频词去除函数
def callcMostFreq(vocabList, fullText):
    import operator
    freqDict={}
    for token in vocabList:#计算出现频率
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[ :30]
def localWords(feed0, feed1):
    import feedparser
    docList = []; classList = []; fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    #导入并解析文本文件
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])#每次访问一条ＲＳＳ源
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = callcMostFreq(vocabList, fullText)
    for pairW in top30Words:#去电掉出现频率最高的那些词
        if pairW[0] in vocabList:vocabList.remove(pairW[0])
    trainingSet = range(50); testSet = []
    #随机构建训练集
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))#随机抽取
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    #对测试集分类
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print( "classification error", docList[docIndex])
    print('the error rate is: ',float(errorCount)/len(testSet))
    return vocabList, p0V, p1V
#显示地域相关的用词
#最具有特征性的｀词汇显示函数；两个ＲＳＳ作为输入，经过分类器，返回使用的概率值。创建元祖列表，返回某个阈值的所有词排序
def getTopWords(ny, sf):
    import operator
    vocabList, p0V, p1V=localWords(ny, sf)
    topNY=[]; topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i], p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse= True)
    print("SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**")
    for item in sortedSF:
        print(item[0])
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print("SF**SF**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**")
    for item in sortedNY:
        print(item[0])


import feedparser
ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
a, b, c = localWords(ny, sf)
getTopWords(ny, sf)
