#PGM 13 ways to find least frequency character from a string in python

'''''
This article gives us the methods to find the frequency of minimum occurring character in a python string. This is quite 
important utility nowadays and knowledge of it is always useful. Let’s discuss certain ways in which this task can be 
performed. 
Example:
INPUT:The original string is : GeeksforGeeks
OUTPUT:The minimum of all characters in GeeksforGeeks is : f
'''''

str1=input("Enter a string: ")

#Method 1 = Naive method + min()
'''''
In this method, we simply iterate through the string and form a key in a dictionary of newly occurred element or if 
element is already occurred, we increase its value by 1. We find minimum occurring character by using min() on values.
Time Complexity: O(n)
Auxiliary Space: O(n), where n is number of characters in string. 
'''''
def minimumM1(s1):
    dic=dict()
    for i in s1:
        #if element already exist its value is incremented by 1
        if i in dic:
            dic[i]+=1
        #if element doesnt exist in dictionary it is added with value 1
        else:
            dic[i]=1
    res=min(dic,key=dic.get)
    return res
ansM1=minimumM1(str1)
print("The Minimum of all characters in {} is in M1:  {}".format(str1,ansM1))

#Method 2 = Using collections.Counter() + min()
'''''
The most suggested method that could be used to find all occurrences is this method, this actually gets all element 
frequency and could also be used to print single element frequency if required. We find minimum occurring character by 
using min() on values.
Time complexity: O(n)
Auxiliary space: O(n)
'''''
import collections
def minimumM2(s2):
    res=collections.Counter(s2)
    res=min(res,key=res.get)
    return res
ansM2=minimumM2(str1)
print("The Minimum of all characters in {} is in M2:  {}".format(str1,ansM2))