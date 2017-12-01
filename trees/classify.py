# coding=utf-8
#使用决策树分类函数，测试数据属于那个类别

def classify(inputTree, featLabels, testVec):#inputTree:已分类的决策树；featLabels：决策树的决策点，即分类标签;testVec:待分类的数据
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)#index查找当前列表中匹配firstStr变量元素的索引值；将标签字符串转为索引
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__=='dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:   classLabel = secondDict[key]
    return classLabel

a={'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
b=['no surfacing','flippers']
print(classify(a,b,[1,0]))
