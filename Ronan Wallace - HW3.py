## Author: Ronan Wallace
## Title: HW3
## Date: 03/13/19
##
## Solution:
## Mental -  123408
## Health -  920849
## Matters - 1044257
## M:1,E:2,N:3,T:4,A:0,L:8,H:9,R:5,S:7
##
## Time Complexity: BigTheta(n!) where n = length of letters


import itertools

# Creates a global vairable to be used for all of the unique letters found in all three user input words
letters = []


def main():
    # letters = [] resets for the entire program if main() is called a second time
    global letters
    letters = []

    # User Interface
    print("-"*34,"\nWelcome to the Alphametic Program!")
    print("-"*34,'\nSingular words without spaces should \nbe given, or else the program will \nnot work properly.\n\nFor the assignment, enter "mental", \n"health", and "matters" to get the \nsolution!\n')
    wordInput1 = input("First word: ")
    wordInput2 = input("Second word: ")
    wordOutput = input("Output word: ")
    print("-"*25)

    # Finds the solution for the given alphametic (if there is one) and prints the results
    getSolution(wordInput1.lower(),wordInput2.lower(),wordOutput.lower())



# Parameters: Three words given by the user (Strings)
# Objective:  Considers the three words as an alphametic puzzle and solves it
# Return:     Returns the solution(s) for the three-worded puzzle through print statements
def getSolution(wordIn1,wordIn2,wordOut):
    global letters
    # If x remains to be zero at the end of the function, alphametic puzzle cannot be solved
    x = 0
    # y used as a switch so "Processing..." prints only once when the looping begins
    y = 1
    # Arrays to store the final solution(s) to be printed at the end of the function
    finalNum1 = []
    finalNum2 = []
    finalNumOut = []

    # Creates a list of all the unique letters found in all three words
    letters = getLetters(wordIn1,letters)
    letters = getLetters(wordIn2,letters)
    letters = getLetters(wordOut,letters)

    # Alphametics cannot be longer than 10 unique letters
    if len(letters) > 10:
        print("Not an alphametic.")
        return None
    
    # Majority of computing is done here:
    # Creates a new permutation using python's itertools
    listOfNumbers = [0,1,2,3,4,5,6,7,8,9]
    for i in itertools.permutations(listOfNumbers,len(letters)):
        if y == 1:
            print("Processing...")
            y = 0
        permutation = i
        # Converts words (Strings) into numbers (Integers)
        wordIn1Num = wordToNumber(permutation,wordIn1)
        wordIn2Num = wordToNumber(permutation,wordIn2)
        wordOutNum = wordToNumber(permutation,wordOut)
        
                    
        # Checks if the alphametic can be solved (does not allow false solutions where a number starts with zero)
        if len(str(wordIn1Num)) == len(wordIn1):
            if len(str(wordIn2Num)) == len(wordIn2):
                if len(str(wordOutNum)) == len(wordOut):
                    if wordIn1Num + wordIn2Num == wordOutNum:
                        finalNum1.append(wordIn1Num)
                        finalNum2.append(wordIn2Num)
                        finalNumOut.append(wordOutNum)
                        x=1
        else:
            continue

    # Prints results
    if x == 0:
        print("\nThis alphametic could not be solved.")
    elif x == 1:
        print("-"*25)
        for i in range(len(finalNum1)):
            print("\nSolution "+str(i+1)+":","\n"+wordIn1+":",finalNum1[i],"\n"+wordIn2+":",finalNum2[i],"\n"+wordOut+":",finalNumOut[i])
    else:
        print("ERROR")
    # Time Complexity of getAnswer(): Big Theta(n!)



# Parameters: permutation (Array), word (String)
# Objective:  Replaces letters in each word with a number from the permutation
# Return:     Returns the word as a string of numbers (Integer)
def wordToNumber(permutation,word):
    for i in range(len(letters)):
        if letters[i] in word:
            word = word.replace(letters[i],str(permutation[i]))
        else:
            continue
        
    return int(word)



# Parameters: word (String), letters (Array)
# Objective:  Grabs all of the unique letters found in word and appends them to the letters array
# Return:     Array of unique letters (keeps the letters from previous word as well) (Array)
def getLetters(word,letters):
    count = 0
    for i in range(len(word)):
        if len(letters) == 0:
            letters.append(word[i])
        else:
            for j in range(len(letters)):
                if word[i] != letters[j]:
                    count += 1
                elif word[i] == letters[j]:
                    count = 0
                    break
                else:
                    print("ERROR")
            if count == len(letters):
                letters.append(word[i])
                count = 0
                
    return letters


main()
