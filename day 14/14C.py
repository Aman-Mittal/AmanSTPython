import math
import random
import operator

def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    length=4
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distaances[x][0])
    return neighbors
