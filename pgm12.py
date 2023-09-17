#PGM 12 ways to remove all duplicates from a given string in python

'''''
We are given a string and we need to remove all duplicates from it? What will be the output if the order of 
character matters? 
Examples:
Input : geeksforgeeks 
Output : geksfor
'''''

str1=input("Enter a String: ")

#Method 1  navie method basic
def removeM1(s1):
    lst1=[i for i in s1]
    lst2=[]
    for i in lst1:
        if i not in lst2:
            lst2.append(i)
        else:
            pass
    return "".join(lst2)
ansM1=removeM1(str1)
print("The string after removing all duplicates from original string in M1:  ",ansM1)

#Method 2 using joint
'''''
Time Complexity: O(n * n) 
Auxiliary Space: O(1), Keeps the order of elements the same as the input. 
'''''
def removeM2(s2):
    s=""
    for char in s2:
        if char not in s:
            s=s+char#string concatenation
    return s
ansM2=removeM2(str1)
print("The string after removing all duplicates from original string in M2:  ",ansM2)

#Method 3 using set
'''''
Time Complexity: O(n) 
Auxiliary Space: O(n)
'''''
def removeM3(s3):
    s=set(s3)#if aise set mein convert so random kahi bhi jayega index
    s1="".join(s)
    return s1
ansM3=removeM3(str1)
print("The string after removing all duplicates from original string in M3:  ",ansM3)

#Method 4 using sorting()
'''''
  1) Sort the elements.
  2) Now in a loop, remove duplicates by comparing the 
      current character with previous character.
  3)  Remove extra characters at the end of the resultant string.
'''''
def removeM4(s4):
    s=sorted(s4)
    i=1
    while(i<len(s)):
        if s[i]==s[i-1]:
           ans=s.pop(i-1)
        else:
            i+=1
    return "".join(s)
ansM4=removeM4(str1)
print("The string after removing all duplicates from original string in M4:  ",ansM4)

#Method 5 using dictionary
def removeM5(s5):
    dic=dict()
    lst=[]
    for i in s5:
        dic[i]=s5.count(i)
    for i,j in dic.items():
        if j>1 and j in lst:
            pass
        else:
            lst.append(i)
    return "".join(lst)
ansM5=removeM5(str1)
print("The string after removing all duplicates from original string in M5:  ",ansM5)

#Method 6 using operator.countof ()
import operator
def removeM6(s6):
    dic=dict()
    lst=[]
    for i in s6:
        dic[i]=operator.countOf(i,s6)
    for i,j in dic.items():
        if j>1 and j in lst:
            pass
        else:
            lst.append(i)
    return "".join(lst)
ansM6=removeM6(str1)
print("The string after removing all duplicates from original string in M6:  ",ansM6)

