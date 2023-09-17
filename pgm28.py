#PGM 31 (Basic string program series) ways in python to upercase half string

'''''
Given a String, perform uppercase of later part of string. 

Input : test_str = ‘geeksforgeek’ 
Output : geeksfORGEEK 
Explanation : Latter half of string is uppercased. 

Input : test_str = ‘apples’ 
Output : appLES 
Explanation : Latter half of string is uppercased.
'''''
str1=input("Enter a string : ")

#Method 1 = using upper()+loop+len()
'''''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def uppercaseM1(s1):
    n=len(s1)//2
    res=""
    for  i in range(len(s1)):
        #uppercasing later half
        if i>=n:
            res+=s1[i].upper()
        #maintaining same first half
        else:
            res+=s1[i]
    return "".join(res)
ansM1=uppercaseM1(str1)
print("New string after uppercase half string in M1: ",end="---->    ")
print(ansM1)

#using list comprehension + join()+ upper()
'''''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def uppercaseM2(s2):
    n=len(s2)//2
    lst=[s2[x].upper() if x>=n else s2[x] for x in range(len(s2))]
    res="".join(lst)
    return res
ansM2=uppercaseM2(str1)
print("New string after uppercase half string in M2: ",end="---->    ")
print(ansM2)

#Method 3 = using string slicing and upper
'''''
Use string slicing to divide the string into two separate sub_string and convert the right sub_string to the upper 
case with upper() method.
Time Complexity: O(n) -> (slicing)
Auxiliary Space: O(n) 
'''''
def uppercaseM3(s3):
    n=len(s3)//2
    s=s3[:n]+s3[n:].upper()
    return s
ansM3=uppercaseM3(str1)
print("New string after uppercase half string in M3: ",end="---->    ")
print(ansM3)

#Method 4 = using slicing + index()+ loop without using upper
'''''
Time Complexity: O(n) where n is the length of the input string.
Auxiliary Space: O(n) as we are creating a new string ‘res’ with length equal to the length of the input string.
'''''
def uppercaseM4(s4):
    #computing half
    n=len(s4)//2
    a=s4[:n]
    b=s4[n:]
    cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small="abcdefghijklmnopqrstuvwxyz"
    res=""
    for i in b:
        res+=cap[small.index(i)]#small ka joh index corresponding caps ka bhi so voi kiya hai ider replace
    res=a+res
    return res
ansM4=uppercaseM4(str1)
print("New string after uppercase half string in M4: ",end="---->    ")
print(ansM4)

#Method 5 = using re module
'''''
step-by-step algorithm for implementing this approach:

1.Import the re module.
2.Define a string to be processed, test_str.
3.Print the original string.
4.Compute the half index of the string by dividing its length by 2.
5.Extract the second half of the string using the half index.
6.Use regular expressions to convert all word characters in the second half of the string to uppercase.
7.a. Use (?i) to set the regular expression to case-insensitive mode.
8.b. Use \w+ to match all word characters in the string.
9.c. Use a lambda function to convert each match to uppercase using the group() method of the match object.
10.d. Replace all matches in the second half of the string with their uppercase equivalents using re.sub().
11.Concatenate the first half of the string with the modified second half to create the result string.
12.Print the result string.

The time complexity of this algorithm is O(n), where n is the length of the input string. This is because the regular 
expression pattern is applied to the second half of the string, which has length n/2. The time complexity of re.sub() 
is proportional to the length of the input string, so the overall time complexity is O(n/2 + n/2) = O(n).

The auxiliary space of this algorithm is also O(n), where n is the length of the input string. This is because the 
re.sub() function creates a new string containing the modified second half of the input string, and the result string 
also has length n. The space used by the other variables (e.g., test_str, hlf_idx, res) is constant, 
regardless of the length of the input string.
'''''
import re
def uppercaseM5(s5):
    #computing half index
    n=len(s5)//2
    # Making new string with half upper case using regular expressions
    new_str=re.sub(r"(?i)(\w+)",lambda m:m.group().upper(),s5[n:])
    # concatenating the two parts of the string
    res=s5[:n]+new_str
    return res
ansM5=uppercaseM5(str1)
print("New string after uppercase half string in M5: ",end="---->    ")
print(ansM5)