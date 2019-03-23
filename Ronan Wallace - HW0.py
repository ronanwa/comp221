# Ronan Wallace
# HW0 - List Manipulation Time Analysis
# 02/14/2019

import time

def main():
    stepIncrease=1
    for i in range(9):
        print("\nAverage Execution Time of Each Function for",stepIncrease,"integers:")
        array=[]
        delFromFront(stepIncrease,addToFront(stepIncrease,array))
        array=[]
        delFromMid(stepIncrease,addToMid(stepIncrease,array))
        array=[]
        delFromEnd(stepIncrease,addToEnd(stepIncrease,array))
        stepIncrease*=10   


def addToFront(integ,array):
    avgTime=0
    for i in range(10):
        startTime=time.time()
        for j in range(integ):
            array=[j]+array
        endTime=time.time()
        avgTime+=(endTime-startTime)/integ
    print("addToFront: {0:.3g}".format(avgTime/10),"seconds")
    return array

def addToMid(integ,array):
    avgTime=0
    for i in range(10):
        startTime=time.time()
        for j in range (integ):
            array.insert(int(j/2),j)
        endTime=time.time()
        avgTime+=(endTime-startTime)/integ
    print("addToMid: {0:.3g}".format(avgTime/10),"seconds")
    return array

def addToEnd(integ,array):
    avgTime=0
    for i in range(10):
        startTime=time.time()
        for j in range(integ):
            array.append(j)
        endTime=time.time()
        avgTime+=(endTime-startTime)/integ
    print("addToEnd: {0:.3g}".format(avgTime/10),"seconds")
    return array

def delFromFront(integ,array):
    avgTime=0
    for i in range(10):
        startTime=time.time()
        for j in range(integ):
            array.pop(0)
        endTime=time.time()
        avgTime+=(endTime-startTime)/integ
    print("delFromFront: {0:.3g}".format(avgTime/10),"seconds")
    return array

def delFromMid(integ,array):
    avgTime=0
    for i in range(10):
        startTime=time.time()
        for j in range(integ):
            del array[int(len(array)/2)]
        endTime=time.time()
        avgTime+=(endTime-startTime)/integ
    print("delFromMid: {0:.3g}".format(avgTime/10),"seconds")
    return array

def delFromEnd(integ,array):
    avgTime=0
    for i in range(10):
        startTime=time.time()
        for j in range(integ):
            del array[len(array)-1]
        endTime=time.time()
        avgTime+=(endTime-startTime)/integ
    print("delFromEnd: {0:.3g}".format(avgTime/10),"seconds")
    return array


main()  
