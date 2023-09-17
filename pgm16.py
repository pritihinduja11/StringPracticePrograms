#PGM 16 ways to find a words which are greater than given length k

'''''
A string is given, and you have to find all the words (substrings separated by a space) which are greater than the given length k.
Examples:  
Input : str = "hello geeks for geeks 
          is computer science portal" 
        k = 4
Output : hello geeks geeks computer 
         science portal
Explanation : The output is list of all 
words that are of length more than k.
Input : str = "string is fun in python"
        k = 3
Output : string python 
'''''
str1=input("enter a string:  ")
n=int(input("Enter integer i.e length:  "))

#Method 1 = using for loop
'''''
Time Complexity: O(n), where n is the length of the given string.
Auxiliary Space: O(n)
'''''
def length(s1,n):
    s=s1.split()
    lst=[]
    for i in s:
        if len(i)>n:
            lst.append(i)
    return " ".join(lst)
ansM1=length(str1,n)
print("The string containing words having length greater than k in M1 is: ",end="---->  ")
print(ansM1)

#Method 2 = using list comprehension
'''''
Time Complexity: O(n), where n is the length of the given string.
Auxiliary Space: O(n)
'''''
def lengthM2(s2,n):
    lst=[char for char in s2.split() if len(char)>n]
    return " ".join(lst)
ansM2=lengthM2(str1,n)
print("The string containing words having length greater than k in M2 is: ",end="---->  ")
print(ansM2)

#Method 3 = using lambda function
'''''
Time Complexity: O(n), where n is the length of the given string.
Auxiliary Space: O(n)
'''''
def lengthM3(s3,n):
    s=s3.split()
    res=list(filter(lambda x:(len(x)>n),s))
    return " ".join(res)
ansM3=lengthM3(str1,n)
print("The string containing words having length greater than k in M3 is: ",end="---->  ")
print(ansM3)

#Method 4 = using enumerator
'''''
Time Complexity: O(n), where n is the length of the given string.
Auxiliary Space: O(n)
'''''
def lengthM4(s4,n):
    s=s4.split()
    lst=[j for i,j in enumerate(s) if len(j)>n]
    return " ".join(lst)
ansM4=lengthM4(str1,n)
print("The string containing words having length greater than k in M4 is: ",end="---->  ")
print(ansM4)