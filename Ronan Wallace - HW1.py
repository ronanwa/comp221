## Author: Ronan Wallace
## Title: HW1
## Date: 02/21/19


def main():
    print("-"*50+"\nAnagram Checker!\n"+"-"*50+"\n")
    #Creates a loop to allow the user to use the anagram function multiple times
    x=1
    while(x==1):
        w1=input("First word: ")
        w2=input("Second word: ")
        anagram(w1,w2)
        #Asks the user if they would like to use the anagram function again. If an incorrect input is given, it will tell the user and ask them again
        y=1
        while (y==1):
            answer=input("\nWould you like to do two more words? (y/n) ")
            if answer=="y":
                print("-"*50)
                y=0
            elif answer=="n":
                x=0
                y=0
            else:
                print("\n**Incorrect input**\n")
            

# Purpose: Determines if two words are anagrams
# Parameters: Two words given by user. Does not check if it is a legitimate word and is inclusive to characters beyond the alphabet
# Return: 1 if anagram; -1 if not anagram; prints results for the user
def anagram(w1,w2):
    wLength=len(w1)
    w1=w1.lower().rstrip()
    w2=w2.lower().rstrip()
    
    #If word lengths are not equal, they are not an anagram
    if wLength!=len(w2):
        print("It is not an anagram.")
        return -1

    #Iterate through every character of both given words. Replacing matched letters with zero prevents letters in the second word to be counted twice
    for i in range(wLength):
        for j in range(wLength):
            if w1[i]==w2[j]:
                w1=w1.replace(w1[i],"0")
                w2=w2.replace(w2[j],"0")

    #Print statements were used for programmer to check both word strings if they were replaced with zeros or not (I left this here to show testing of the function)
    # print("First: ",w1)
    # print("Second: ",w2)

    #If both strings are only zeros and have an equal amount of zeros, then both given words are anagrams of each other. If not, they are not anagrams
    if w1==w2:
        print("It is an anagram.")
        return 1
    else:
        print("It is not an anagram.")
        return -1

        
#Calls main function
main()


