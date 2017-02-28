# -*- coding:utf-8 -*- 

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import operator
def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

# 给定起始点inX  和其他所有点的左边，然后找出距离其最近的点
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    #print diffMat
    sqDiffMat = diffMat ** 2
    #print sqDiffMat

    sqDistances = sqDiffMat.sum(axis = 1)
    #print sqDistances

    distances = sqDistances ** 0.5
    #从小到大排序，给出下标的列表
    sortedDistIndicies = distances.argsort()
    classCount = {}
    #print sortedDistIndicies
    #print sqDistances
    #print distances

    for i in range(k):
        #print i
        voteIlabel = labels[sortedDistIndicies[i]]
        #print voteIlabel
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        print classCount
    print classCount.iteritems()
    print operator.itemgetter(1)
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    print sortedClassCount
    return sortedClassCount[0][0]

group, labels = createDataSet()
fig = plt.figure()
ax = fig.add_subplot(111)
#print group[0:, 0]
#print group[0:, 1]
#print 
#ax.scatter(group[0:, 0], group[0:, 1])
#plt.show()
print classify0([0,0], group, labels, 2)
