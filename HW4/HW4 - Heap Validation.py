## Author: Ronan Wallace
## Title: HW4/5
## Date: 04/11/19
##
## Section 6.4 - Exercise 2
##  > check whether an array [1...n] is a heap
##
## Time-Efficiency: Big-Theta(n/2)
##
## Comments:
## I decided to design an analytics function that displays information on a validated heap.

import math

# Used for analytics()
dataCollect = []

def main():
    global dataCollect

    # Valid Test Heap
    # NOTE: This algorithm will only work with array that have only one Null/None element (which is located at the 0th index position)
    heap = [None,400,50,52,11,33,50,31,10,9,8,7,6,5,4,3,2,1,9]

    # Format of dataCollect: [Length of Array (not including initial Null), Height of Heap, Root of Heap, List of Comparisons]
    dataCollect = [len(heap)-1,math.ceil(math.log2(len(heap))),heap[1],[]]

    # Validates a heap
    ans = validateHeap(heap)

    # Displays heap validation results
    print("-"*49)
    print("Results")
    print("-"*49)
    if ans == True:
        print("True - The given array is a heap")
    elif ans == False:
        print("False - The given array is not a heap")
    else:
        print("Error")
    print("\n\n")


    # Interperets data and displays
    analytics(dataCollect,ans)


# Input:     An array where the number of elements in said array is greater than 1
# Return:    True - array is a valid heap; False - array is an invalid heap
# Objective: Check whether an array is a valid heap
def validateHeap(heap):
    global dataCollect
    # Only need to iterate over all of the parents of the heap (able to simplify as what's written in the range()) 
    if len(heap)%2 == 0:
        iterRange = int((len(heap)/2))
    else:
        iterRange = int((len(heap)/2)+1)

    # Iterates through all parent 
    for i in range(iterRange):
        if i == 0:
            continue
        
        # Makes comparisons between the parent node and its children. If the first 2 if statements are not met, it is not a heap (if it is a valid heap, the third nested if statement will be met and validateHeap() will return True). 
        # Comparison between parent and left child
        if heap[i] >= heap[2*i]:
            dataCollect[3].append(str(heap[i])+" >= "+str(heap[2*i]))
        else:
            return False
        # If at last parent node, try to evaluate right child if there is one
        if i == iterRange-1:
            try:
                if heap[i] >= heap[(2*i)+1]:
                    dataCollect[3].append(str(heap[i])+" >= "+str(heap[(2*i)+1]))
                    return True
            except:
                return True
        # Comparison between parent and right child
        elif heap[i] >= heap[(2*i)+1]:
            dataCollect[3].append(str(heap[i])+" >= "+str(heap[(2*i)+1]))
        else:
            return False


# Input:     An array with data collected from the heap and validateHeap() algorithm
# Output:    An analysis of the validated heap 
# Objective: Display information regarding the validated heap
def analytics(dataCollect,ans):
    # User interface
    print("-"*49)
    print("Heap Analytics")
    print("-"*49)
    # Will not perform analysis if data of a non-heap is given
    if ans == False:
        print("No analytics for a non-heap array.")
        return 0
    # Performs analysis on valid-heap data
    else:
        powerCount = 0
        lineCount = 0
        nextLevel = 0
        depth = 1
        math.pow(2,powerCount)
        # Time Efficiency Class of Algorithm
        print("Time Efficiency Class: Big-Theta(n/2)")
        # Total Number of Nodes
        print("Number of nodes in Heap:",dataCollect[0])
        # Height of Heap
        print("Height of Heap:",dataCollect[1])
        # Root of Node
        print("Root of Heap:",dataCollect[2],"\n")
        # Comparisons made at each depth level of the heap
        print("{0:<13}{1:<7}".format("Depth","Node Comparisons"))
        print("{0:<13}{1:<7}".format("-----","----------------"))
        for i in range(len(dataCollect[3])):
            if lineCount == nextLevel:
                print("{0:<13}{1:<7}".format(depth,dataCollect[3][i]))
                powerCount+=1
                depth+=1
                nextLevel+=math.pow(2,powerCount)
            else:
                print("{0:<13}{1:<7}".format("",dataCollect[3][i]))
            lineCount+=1
    

main()
