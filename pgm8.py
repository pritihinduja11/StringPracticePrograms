#PGM 8 ways to find length of string in python

str1=input("Enter a string :  ")

#Method 1 = Using the built-in function len. The built-in function len returns the number of items in a container.
#space is also counted in length
def lengthM1(s1):
    ans=len(s1)
    return ans
ansM1=lengthM1(str1)
print("the length of string in M1: {}".format(ansM1))

#Method 2 = Using for loop and in operator
'''''
A string can be iterated over, directly in a for loop. Maintaining a count of the number of iterations will result in 
the length of the string.
'''''
def lengthM2(s2):
    count=0
    for i in s2:
        count+=1
    return count
ansM2=lengthM2(str1)
print("the length of string in M2: {}".format(ansM2))

#Method 3 = Using while loop and Slicing
'''''
We slice a string making it shorter by 1 at each iteration will eventually result in an empty string. This is when while 
loop stops. Maintaining a count of the number of iterations will result in the length of the string. 
'''''
def lengthM3(s3):
    count=0
    while s3[count:]:#yeh while loop empty tb hoga jab count last element ko bhi count kar lega
        count+=1
    return count
ansM3=lengthM3(str1)
print("the length of string in M3: {}".format(ansM3))

#Method 4 = Using string methods join and count
'''''
The join method of strings takes in an iterable and returns a string which is the concatenation of the strings in the 
iterable. The separator between the elements is the original string on which the method is called. Using join and 
counting the joined string in the original string will also result in the length of the string. 
'''''
def lengthM4(s4):
    new_str=" "
   # return (new_str.join(s4).count(new_str))#if this so 4 aayega ans priti ka as indexing of string start from 0 so index of last
    return (new_str.join(s4).count(new_str))+1
ansM4=lengthM4(str1)
print("the length of string in M4: {}".format(ansM4))

#Method 5 = Using reduce method. from funtools module
'''''
Reduce method is used to iterate over the string and return a result of collection element provided to the reduce 
function. We will iterate over the string character by character and count 1 to result each time. 
'''''
import functools
def lengthM5(s5):
    #reduce(function,sequence,initial)
    return functools.reduce(lambda x,y:x+1,s5,0)
ansM5=lengthM5(str1)
print("the length of string in M5: {}".format(ansM5))

#Method 6 = Using sum() and list comprehension function
'''''
 We use list comprehension for iterating over the string and sum function to sum total characters in string 
'''''
def lengthM6(s6):
    #sum(iterable) here for loop is iterable gives list list comprehension
    return sum(1 for i in s6)#1 as every iteration some hai so add
ansM6=lengthM6(str1)
print("the length of string in M6: {}".format(ansM6))

#Method 7 = Using enumerate function
def lengthM7(s7):
    count=0
    for i,a in enumerate(s7):
        count+=1
    return count
ansM7=lengthM7(str1)
print("the length of string in M7: {}".format(ansM7))