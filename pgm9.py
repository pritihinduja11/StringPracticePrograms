#PGM 9 ways to print even length words in a string

str1=input("Enteer a String:  ")

#Method 1 = using for loop and if statement without def function
'''''
Finding even length words using for loop and if statement and without using the def function. First split the given 
string using the split() function and then iterate the words of a string using for loop. Calculate the length of each 
word using the len() function. If the length is even, then print the word.
Time Complexity: O(n), where n is the length of the given string
Auxiliary Space: O(n)
'''''
s1=str1.split(" ")
lst1=[]
for i in s1:
    if len(i)%2==0:
        lst1.append(i)
print("The even length words in a string in M1: ",end="------>  ")
print(lst1)

#Method 2 = using the lambada function
s2=str1.split(" ")
lst2=list(filter(lambda x:len(x)%2==0,s2))
print("The even length words in a string in M2: ",end="------>  ")
print(lst2)

#Method 3 = using list comprehension
s3=str1.split(" ")
lst3=[i for i in s3 if len(i)%2==0]
print("The even length words in a string in M3: ",end="------>  ")
print(lst3)

#Method 4 = using enumerate
s4=str1.split(" ")
lst4=[x for i,x in enumerate(s4) if len(x)%2==0]
print("The even length words in a string in M4: ",end="------>  ")
print(lst4)

#Method 5 = using recursion
def evenWordsM5(itr,s5):
    lst=[]
    if itr==len(s5):#for 0th and first elementor when all elements are traversed
        return
    if (len(s5[itr])%2==0):
        lst.append(s5[itr])
        print(s5[itr])
    evenWordsM5(itr+1,s5)
lst5=evenWordsM5(0,str1.split(" "))#as function requires list
print("The even length words in a string in M5: ",end="------>  ")
print(lst5)

#Method 6 = Using the itertools.filterfalse() function
import itertools
s6=str1.split(" ")
lst6=list(itertools.filterfalse(lambda x:len(x)%2!=0,s6))
print("The even length words in a string in M6: ",end="------>  ")
print(lst6)


