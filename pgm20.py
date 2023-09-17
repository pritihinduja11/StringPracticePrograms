#PGM 20 ways in python program to find uncommon words from two strings

'''''
Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it 
appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a 
string of space-separated words. Each word consists only of lowercase letters. 
Examples:
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : [‘Learning’, ‘from’]
Input : A = “apple banana mango” , B = “banana fruits mango”
Output : [‘apple’, ‘fruits’]
Time Complexity: O(N)
Auxiliary Space : O(N)
'''''
str1=input("Enter First String:  ")
str2=input("Enter Second String: ")

#Method 1 = using for loop
def uncommonM1(string1,string2):
    #count will contain all word count
    count={}
    # insert words of string A to hash
    for word in string1.split():
        count[word]=count.get(word,0)+1#value of that word or u can say initialise count of that word to1
    # insert words of string B to hash
    for word in string2.split():
        count[word]=count.get(word,0)+1 #0 is defaault
    return [word for word in count if count[word]==1]
ansM1=uncommonM1(str1,str2)
print("The Uncommon words From Two strings in M1 are :   ",end="----->  ")
print(ansM1)

#Method 2 = Using split(),list(),set(),in and not in operators
def uncommonM2(string1,string2):
    s1=string1.split()
    s2=string2.split()
    x=[]
    for i in s1:
        if i not in s2:#joh string 2 mein element nhi ho but string 1 mein ho
            x.append(i)
    for j in s2:
        if j not in s1:
            x.append(j)
    #to remove duplicate elements
    s=set(x)
    #to convert to list and return
    return list(s)
ansM2=uncommonM2(str1,str2)
print("The Uncommon words From Two strings in M2 are :   ",end="----->  ")
print(ansM2)

#Method 3 = using counter() function
import collections
def uncommonM3(string1,string2):
    s1=string1.split()
    s2=string2.split()
    frequency_s1 = collections.Counter(s1)
    frequency_s2=collections.Counter(s2)
    result=[]
    for key in frequency_s1:
        if key not in frequency_s2:
            result.append(key)
    for key in frequency_s2:
        if key not in frequency_s1:
            result.append(key)
    return result
ansM3=uncommonM3(str1,str2)
print("The Uncommon words From Two strings in M3 are :   ",end="----->  ")
print(ansM3)

#Method 4 = using operator.countOf() method
import operator
def uncommonM4(string1,string2):
    s1=string1.split()
    s2=string2.split()
    x=[]
    for i in s1:
        if operator.countOf(s2,i)==0:
            x.append(i)
    for i in s2:
        if operator.countOf(s1,i)==0:
            x.append(i)
    return x
ansM4=uncommonM4(str1,str2)
print("The Uncommon words From Two strings in M4 are :   ",end="----->  ")
print(ansM4)