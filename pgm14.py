#PGM 14 ways to find maximum frequency character in a string

'''''
This article gives us the methods to find the frequency of maximum occurring character in a python string. This is quite 
important utility nowadays and knowledge of it is always useful. Let’s discuss certain ways in which this task can be 
performed. 
'''''
str1=input("Enter a String:  ")

#Method 1 =  Naive method + max()
'''''
In this method, we simply iterate through the string and form a key in a dictionary of newly occurred element or if 
element is already occurred, we increase its value by 1. We find maximum occurring character by using max() on values. 
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def maximumM1(s1):
    dic=dict()
    for i in s1:
        #if element already in dictionary increment its value by 1
        if i in dic:
            dic[i]+=1
        #if element not in dictionary add in dictinary with value as 1
        else:
            dic[i]=1
    res=max(dic,key=dic.get)#get give values so based on values maximum returns key
    return res
ansM1=maximumM1(str1)
print("The maximum frequency character in {} is in M1: {}".format(str1,ansM1))

#Method 2 = using collections.Counter() + max()
'''''
The most suggested method that could be used to find all occurrences is this method, this actually gets all element 
frequency and could also be used to print single element frequency if required. We find maximum occurring character by 
using max() on values. 
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
import collections
def maximumM2(s2):
    res=collections.Counter(s2)#this gives dictionary with element as key and value as there count of occurences
    res=max(res,key=res.get)
    return res
ansM2=maximumM2(str1)
print("The maximum frequency character in {} is in M2: {}".format(str1,ansM2))

#Method 3 = using dictionary
'''''
1.First, the string “GeeksforGeeks” is initialized and stored in the variable test_str.
2.An empty dictionary called freq is created. This dictionary will be used to store the frequency of each character in 
the string.
3.The for loop iterates over each character in the test_str string. For each character, it checks if the character 
already exists in the freq dictionary. If it does, the frequency count is incremented by 1. If not, a new key is added 
to the dictionary with a frequency count of 1.
4.After the for loop completes, the max() function is used to find the key with the maximum value in the freq dictionary. 
The key parameter is passed to the max() function to specify that the key with the maximum value (i.e., the character 
with the highest frequency) should be returned.
5.Finally, the result is printed to the console as a string.
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def maximumM3(s3):
    dic=dict()
    for i in s3:
        if i not in dic:
            dic[i]=s3.count(i)
    res=max(dic,key=dic.get)
    return res
ansM3=maximumM3(str1)
print("The maximum frequency character in {} is in M3: {}".format(str1,ansM3))

#Method 4 =  Using a generator expression:
'''''
This approach uses a generator expression with the max function to find the character with the maximum frequency. 
The lambda function returns the frequency count for each character in the string, and the max function returns the 
character with the maximum frequency. This approach may be less efficient for longer strings because it has to count 
the frequency of each character multiple times.
Time Complexity: O(n)
Auxiliary Space: O(1)
'''''
def maxmimumM4(s4):
    res=max(s4,key=lambda x:s4.count(x))
    return res
ansM4=maxmimumM4(str1)
print("The maximum frequency character in {} is in M4: {}".format(str1,ansM4))