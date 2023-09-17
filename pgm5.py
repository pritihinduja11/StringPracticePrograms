#PGM 5 --> ways to check if a substring is present in a given string

'''''
Example 1: Input : Substring = "geeks" 
           String="geeks for geeks"
Output : yes
Does Python have a string containing the substring method
Yes, Checking a substring is one of the most used tasks in python. Python uses many methods to check a string containing 
a substring like, find(), index(), count(), etc. The most efficient and fast method is by using an “in” operator which 
is used as a comparison operator. Here we will cover different approaches like:
1.Using the if… in 
2.Checking using the split() method
3.Using find() method
4.Using “count()” method
5.Using the index() method
6.Using  __contains__” magic class.
7.Using regular expressions 
8.using operator
Time Complexity : O(N)
Auxiliary Space : O(1)
'''''
str1=input("Enter a string :  ")
substr1=input("Enter substring :  ")

#Method 1 = using if in
'''''
Time Complexity : O(1)
Auxiliary Space : O(1)
this also works for string provided with spaces
'''''
def subStringM1(s1,subs1):
    s1=s1.lower()#handle as lower returns new string with all characters small it doesnt modify original string
    subs1=subs1.lower()#as it is case sensitive so if user used caps in string and small in substring so output wrong
    if subs1 in s1:
        return "Yes"
    return "No"
stringM1=subStringM1(str1,substr1)
print("The given substring is present in string in M1: {}".format(stringM1))

#Method 2 = using  split() method
'''''
Checking if a substring is present in the given string or not without using any inbuilt function. First split the given 
string into words and store them in a variable s then using the if condition, check if a substring is present in the 
given string or not.This also works for string with no spaces 
'''''
def subStringM2(s2,subs2):
    s2=s2.lower()
    subs2=subs2.lower()
    s2.split()
    if subs2 in s2:
        return "Yes"
    return "No"
stringM2=subStringM2(str1,substr1)
print("The given substring is present in string in M2: {}".format(stringM2))

#Method 3 = using the find() method
"""""
We can iteratively check for every word, but Python provides us an inbuilt function find() which checks if a substring 
is present in the string, which is done in one line. find() function returns -1 if it is not found, else it returns the 
first occurrence, so using this function this problem can be solved. 
"""
def subStringM3(s3,subs3):
    s3=s3.lower()
    subs3=subs3.lower()
    ans=s3.find(subs3)
    if (ans>-1):
        return "Yes"
    else:
        return "No"
stringM3=subStringM3(str1,substr1)
print("The given substring is present in string in M3: {}".format(stringM3))

#Method 4 =  using “count()” method
"""""
You can also count the number of occurrences of a specific substring in a string, then you can use the Python count() 
method. If the substring is not found then “yes ” will print otherwise “no will be printed”.
"""""
def substringM4(s4,subs4):
    s4=s4.lower()
    subs4=subs4.lower()
    if (s4.count(subs4)>0):
        return "Yes"
    return "No"
stringM4=substringM4(str1,substr1)
print("The given substring is present in string in M4: {}".format(stringM4))

#Method 5 = using the index() method
'''''
The .index() method returns the starting index of the substring passed as a parameter
'''''
def subStringM5(s5,subs5):
    s5=s5.lower()
    subs5=subs5.lower()
    if (s5.index(subs5)>=0):
        return "Yes"
    return "No"
stringM5=subStringM5(str1,substr1)
print("The given substring is present in string in M5: {}".format(stringM5))

#Method 6 = using the “__contains__” magic class.
'''''
Python String __contains__(). This method is used to check if the string is present in the other string or not. 
'''''
def subStringM6(s6,subs6):
    s6=s6.lower()
    subs6=subs6.lower()
    if s6.__contains__(subs6):
        return "Yes"
    return "No"
stringM6=subStringM6(str1,substr1)
print("The given substring is present in string in M6: {}".format(stringM6))

#Method 7 = using regular expressions
'''''
RegEx can be used to check if a string contains the specified search pattern. Python has a built-in package called re, 
which can be used to work with Regular Expressions. 
'''''
import re
def substringM7(s7,subs7):
    s7=s7.lower()
    subs7=subs7.lower()
    #re.search(pattern=,string=,flags=)
    if re.search(subs7,s7):
        return "Yes"
    return "No"
stringM7=substringM7(str1,substr1)
print("The given substring is present in string in M7: {}".format(stringM7))

#Method 8 = Using list comprehension
def substringM8(s8,subs8):
    s8=s8.lower()
    subs8=subs8.lower()
    lst=["yes" if subs8 in s8 else "No"]
    return lst[0]
stringM8=substringM8(str1,substr1)
print("The given substring is present in string in M8: {}".format(stringM8))

#Method 9 = Using lambda function and filter function
def subStringM9(s9,subs9):
    s9=s9.lower()
    subs9=subs9.lower()
    x=list(filter(lambda x : (subs9 in s9),s9.split()))
    return "Yes" if x else "No"
stringM9=subStringM9(str1,substr1)
print("The given substring is present in string in M9: {}".format(stringM9))

#Method 10 = Using countof function in opeartor module
'''''
    #def countOf(*args, **kwargs): # real signature unknown
    """ Return the number of items in a which are, or which equal, b. """
this doesnt work for no space seperated strings . a should be iterable so split if no split it wont work ans will be no
'''''
import operator
def substringM10(s10,subs10):
    s10=s10.lower()
    subs10=subs10.lower()
    if operator.countOf(s10.split(),subs10)>0:
        return "yes"
    return "No"
stringM10=substringM10(str1,substr1)
print("The given substring is present in string in M10: {}".format(stringM10))

#Method 11 = Using operator.contains() method
'''''
Approach 
1.Used operator.contains() method to check whether the substring is present in string
2.If the condition is True print yes otherwise print no
def contains(*args, **kwargs): # real signature unknown
    """ Same as b in a (note reversed operands). """
    this works for both space seperated string as well as no space seperated string
'''''
import operator
def substringM11(s11,subs11):
    s11=s11.lower()
    subs11=subs11.lower()
    if operator.contains(s11,subs11):
        return "Yes"
    return "No"
stringM11=substringM11(str1,substr1)
print("The given substring is present in string in M11: {}".format(stringM11))