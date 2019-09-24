## Author: Ronan Wallace
## Title: HW4/5
## Date: 04/11/19
##
## Question 1
##  > Return longest prefix from list of stringss where length of list is greater than 1
##
## Time Complexity: Big-Theta(nlogn)


def main():
    # Allows the user to create a list of words.
    words = []
    numOfWords = eval(input("How many words would you like to enter? "))
    for i in range(numOfWords):
        words.append(input("Enter word "+str(i+1)+": ").lower())
    print(words)
    print("-"*50)

    # Finds the longest prefix between all of the words in the given list.
    longestPrefix = findLongestPrefix(words)

    if longestPrefix == '':
        print("-"*50)
        print("\nNo shared prefix.")
    else:
        print("-"*50)
        print("\nLongest Prefix:",longestPrefix)
        

## Objective:  With the given list of strings, find the longest common prefix between all of the strings.
## Input:      List of strings; each string consists of lowercase letters (depending on the user's input).
## Output:     Return returns the longest common prefix at a string.
def findLongestPrefix(prefixList):
    count = 0
    x = 1
    # While list is greater than one, continue dividing and conquering.
    while x == 1:
        count+=1
        # Divide and conquer on the prefixList to find the longest common prefix.
        prefixList = divideAndConquer(prefixList)

        # If an empty string exists, there is no common prefix; if there is one string in the list, it is the longest common prefix.
        if '' in prefixList:
            return ''
        elif len(prefixList) == 1:
            return prefixList[0]
            
        if x == 1:
            print("\nMerged prefixes:",prefixList)
            print("-"*50)


## Objective:  Divide list of letter strings into pairs and find the longest common prefix between the two.
## Input:      List of strings; each string consists of lowercase letters (depending on the user's input).
## Output:     Returns list of common prefixes.
def divideAndConquer(prefixList):
    prefix = ""
    
    if len(prefixList)> 1:
        # Divides list into two halves.
        divide = len(prefixList)//2
        left = prefixList[:divide]
        right = prefixList[divide:]
        print("\n\nSplitting ",prefixList)
        print("Left:",left)
        print("Right:",right)
        
        # Finds the longest prefix between a pair of words and returns the prefix in a list.
        if len(prefixList) == 2:

            # Iterates through every letter in the first word of the pair.
            for i in range(len(left[0])):
                
                # Try the if statement; if an error is thrown, go to the except block.
                try:
                    if left[0][i] == right[0][i]:
                        prefix += left[0][i]
                    else:
                        prefixList[0] = prefix
                        prefixList.pop()
                        print("Common prefix:",prefix)
                        break

                    # If looped through if statement each time successfully.
                    if i == len(left[0])-1:
                        prefixList[0] = prefix
                        prefixList.pop()
                        print("Common prefix:",prefix)
                        break
                    
                # If previous block throws an error, default to this block of code.
                except:
                    if len(prefixList) != 1:
                        prefixList[0] = prefix
                        prefixList.pop()
                        print("Common prefix:",prefix)
                        
            return prefixList

        # Compiles all prefixes in prefixList to be returned.    
        else:
            prefixList = divideAndConquer(left)
            prefixList += divideAndConquer(right)
            return prefixList

    # If prefixList consists of one word, return said word.
    elif len(prefixList) == 1:
        print("\n\nDo not split",prefixList,", continue process.")
        print("Common prefix:",prefixList[0])
        return prefixList


main()
