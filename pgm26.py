#PGM 26   Ways in python program to find all duplicate characters in string
'''''
INPUT: hello
Output:l
'''''

st1=input("Enter a String: ")

#Method 1 = Navie approach
'''''
The idea is to used dictionary to keep track of the count of each character in the input string .
The program iterates through the string and add each character to the dictionary, incrementing the count
if the character is already present in the dictionary. After iterating through the string, the program
the iterates through the dictionary to find characters with a count greater than , indicating that they are 
Duplicates. These duplicate characters are stored in a list and return as the output.
it is case sensitive caps and small are different for it.
Time complexity: O(n), where n is the length of the input string
Auxiliary space: O(k), where k is the number of distinct characters in the input string.
'''''
def duplicateCharacterM1(s1):
    #create an empty dictionary
    char=dict()
    #iterate through each character in a string
    for chars in s1:
        #if element not in dictionary add in dictionary with value 1
        if chars not in char:
            char[chars]=1
        else:
            #if element already in dictionary so increment its value by 1
            char[chars]+=1
    #create a list to store duplicates characters
    duplicate=[]
    #as items return key and value both
    for keys,count in char.items():
        if count>1:
            duplicate.append(keys)
    return " ".join(duplicate)

ansM1=duplicateCharacterM1(st1)
print("Duplicates characters in a given string in M1 : ",end="---->  ")
print(ansM1)

#Method 2 = using Python Counter() method
'''''
1. Create a dictionary using the counter method having string as key and their frquencies as value.
2. Declare a temp variable.
3. Print all the indexes from the keys which have value greater than 1.
Time complexity: O(n) where n is length of input string
Auxiliary Space:O(n) since we are creating a dictionary and at worst case all elements will be stored.
'''''
from collections import Counter
def duplicateCharactersM2(s2):
    #create empty list to store dic values based on indexes
    lst=[]
    #create dictionary using counter method which will hav estring as key and their frequencies as value
    dic=Counter(s2)
    #finding number of occurences of characater and get inex of it and store that element in a list
    for char,count in dic.items():
        if count>1:
            lst.append(char)
    return " ".join(lst)

ansM2=duplicateCharactersM2(st1)
print("Duplicates characters in a given string in M2 : ",end="---->  ")
print(ansM2)

#Method 3 = using filter method
'''''
Time complexity : O(n), where n is the length of the string
Auxiliary Space : O(n), since we are using a set to store all the values and in worst case 
                  all the elements will be stored inside it.
'''''
def duplicateCharactersM3(s3):
    lst=filter(lambda x:s3.count(x)>=2,s3)
    #print(lst)#this will return filter object
    #print(list(lst))#OUTPUT->['g', 'e', 'e', 'k', 's', 'g', 'e', 'e', 'k', 's']
    #convert filter object to list
    l=list(lst)
    #list will have duplicates as e first occured will check for that e ka next occurrence in whole list so use set
    s=set(l)
    return " ".join(s)#since set so order will be random of characters

ansM3=duplicateCharactersM3(st1)
print("Duplicates characters in a given string in M3 : ",end="---->  ")
print(ansM3)