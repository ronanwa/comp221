## Author: Ronan Wallace
## Title: HW6 - Path Finder
##
## Time Complexities:
##    > Best:    O(n^2)
##    > Worst:   O(n^2)
##    > Average: O(n^2)

import time, itertools

def main():
    source = input("Source word: ")
    target = input("Destination word: ")
    wordList = []
    # Puts words into array
    file = open("three_letter_words.txt","r")
    for i in file:
        wordList.append(i.rstrip().lower())
    allBridges = generateAllBridges(wordList)
    # Removes duplicate bridges
    for i in allBridges:
        for j in range(len(allBridges[i])):
            if allBridges[i][j] == i:
                allBridges[i].pop(j)
                break
    visitedWords = [source]
    path = [source]
    deadendWords = []
    print("Beginning Path Finding Process...\n")
    for i in allBridges[source]:
        if i not in visitedWords:
            if i == target:
                path.append(i)
                return "Path:",path
            else:
                visitedWords = findPath(i,allBridges,visitedWords,path,target,source,deadendWords)
                break
    print("Process Complete.\n")

    
# THIS WORKS DO NOT TOUCH #
# Function to find path from source word to target word
# There are so many inputs to describe, all I'm going to say is that this bad boy returns a path between said words. :)
def findPath(iAmSoTired,allBridges,visitedWords,path,target,source,deadendWords):
    visitedWords.append(iAmSoTired)
    for i in allBridges[iAmSoTired]:
        if i not in visitedWords and i not in deadendWords:
            if i == str(target):
                visitedWords.append(i)
                print("Path Found:",visitedWords,"\n")
                print("Continuing process...")
                return visitedWords
            else:
                findPath(i,allBridges,visitedWords,path,target,source,deadendWords)
                if visitedWords[-1] != target:
                    deadendWords = visitedWords.pop()
    return visitedWords


# THIS WORKS DO NOT TOUCH #
# Input:   List of words generated from .txt file
# Output:  A dictionary of all possible connecting words that bridge one word to another; is now traversable
def generateAllBridges(wordList):
    pathPieces = {}
    for i in wordList:
        pathPieces[i] = findBridges(i,wordList)
    return pathPieces


# THIS WORKS DO NOT TOUCH #
# Input:   A word and an array of available words to connect with
# Output:  An array of words that differ from the original word by only one letter
def findBridges(word,wordList):
    bridges = []
    for i in wordList:
        if word[0:2] in i[0:2]:
            bridges.append(i)        
        elif word[1:3] in i[1:3]:
            bridges.append(i)
        elif word[0]+word[2] in i[0]+i[2]:
            bridges.append(i)
        else:
            continue
    return bridges

main()
