#PGM 17 ways for removing i-th character from a string in python

'''''
Given the string, we have to remove the ith indexed character from the string. In any string, indexing always start 
from 0. Suppose we have a string geeks then its indexing will be as –
g e e k s
0 1 2 3 4
Examples :
Input : Geek
        i = 1
Output : Gek
Input : Peter 
        i = 4
Output : Pete
'''''
str1=input("enter a String:  ")
n=int(input("enter a Index:  "))

#Method 1 = diving string into 2 havles and then concatening
'''''
From the given string, i-th indexed element has to be removed. So, Split the string into two halves, before indexed 
character and after indexed character. Return the merged string. Below is the implementation of above approach : 
Time Complexity: O(n) where n is the length of the string.
Auxiliary Space: O(n) where n is the length of the string.
'''''
def removeM1(s1,i):
    a=s1[:i]
    b=s1[i+1:]
    s=a+b
    return s
ansM1=removeM1(str1,n)
print("The string after removing i th character in M1: ",end="----->  ")
print(ansM1)

#Method 2 = using string.replace()
'''''
Time Complexity: O(n) where n is the length of the string. This is because the function performs a single loop through 
the string and calls the replace function once.
Auxiliary Space: O(1) because the function uses only a few variables and no additional data structures are created.
'''''
def removeM2(s2,i):
    for j in range(len(s2)):
        if j==i:
            s2=s2.replace(s2[i],"",1)#one to replace only first occurrence
    return s2
ansM2=removeM2(str1,n)
print("The string after removing i th character in M2: ",end="----->  ")
print(ansM2)

#Method 3 =  Using list(),pop() and join() methods
'''''
Time Complexity: O(n) where n is the length of the string
Auxiliary Space: O(n) where n is the length of the string 
'''''
def removeM3(s3,i):
    lst=[]
    for j in s3:
        lst.append(j)
    ans=lst.pop(i)
    return "".join(lst)
ansM3=removeM3(str1,n)
print("The string after removing i th character in M3: ",end="----->  ")
print(ansM3)

#Method 4 =  using enumerate and join
'''''
The above approach uses a list comprehension to create a new list of characters from the original string, but excluding 
the i-th character. It iterates over the original string and for each character, it checks if the index of the 
character (j) is not equal to the specified index (i). If it is not equal, the character is included in the new list. 
Then, the join method is used to combine the characters of the new list into a single string. This approach is more 
concise than the previous ones, as it combines the steps of creating a new list and joining it into a single line of code.
Time complexity: O(n), where n is the length of the input string. This is because the function involves iterating through 
all the characters in the string and creating a new string by concatenating the characters that are not being removed.
Auxiliary Space: O(n) because it involves creating a new string with the same length as the input string.
'''''
def removeM4(s4,j):
    lst=[a for i,a in enumerate(s4) if i!=j]
    return "".join(lst)
ansM4=removeM4(str1,n)
print("The string after removing i th character in M4: ",end="----->  ")
print(ansM4)

#Method 5 = using re module and f-string
'''''
Import the re module
pattern = f”(^.{{{i}}})(.)” Create a regular expression pattern that matches the character along with the substring 
before it. ^ matches the start of the string, {i} specifies the index of the character to be removed,
re.sub(pattern, r”\1″, string) is used to substitute the matched pattern with the captured substring before the given index.
Time Complexity: O(N)  where n is the length of the input string as it iterates over all characters in the string to 
find the matching pattern.
Space Complexity: O(N) where n is the length of the input string as we creates a new string with the same length

def sub(pattern, repl, string, count=0, flags=0):
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""
    return _compile(pattern, flags).sub(repl, string, count)
'''''
import re
def removeM5(s5,i):
    pattern=f"(^.{{{i}}})(.)"
    return re.sub(pattern,r"\1",s5)
ansM5=removeM5(str1,n)
print("The string after removing i th character in M5: ",end="----->  ")
print(ansM5)