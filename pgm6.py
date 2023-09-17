#PGM 6 Ways to find Words Frequency in String Shorthands

'''''
Sometimes while working with Python strings, we can have problem in which we need to extract frequency of all the words 
in string. This problem has been solved earlier. This discusses the shorthands to solve this problem as this has 
application in many domains ranging from web development and competitive programming. Let’s discuss certain ways in 
which this problem can be solved.
Example:
    Input : test_str = ‘Gfg is best’ 
     Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
     Input : test_str = ‘Gfg Gfg Gfg’ 
     Output : {‘Gfg’: 3}
Time Complexity: O(N)
Auxiliary Space : O(N)
'''''
str1=input("Enter a string : ")

#Method 1 = Using dictionary comprehension + count() + split()
def frequencyM1(s1):
    dic={key: s1.count(key) for key in s1.split()}
    return dic
ansM1=frequencyM1(str1)
print("The frequency of words in M1:  ",end="------->  ")
print(ansM1)

#Method 2 =  Using Counter() from collection + split()=====
# >>> c = Counter({'a': 4, 'b': 2})
# a new counter from a mapping
from collections import Counter
def frequencyM2(s2):
    dic=Counter(s2.split())
    return dic
#if return dic -> output=The frequency of words in M2:  ------->  Counter({'geeks': 2, 'for': 1}) convert to dic or str
ansM2=frequencyM2(str1)
print("The frequency of words in M2:  ",end="------->  ")
print(dict(ansM2))

#Method 3 = Using dictionary comprehension + operator.countOf() + split() :
import operator as op
def frequwncyM3(s3):
    lst=s3.split()
    dic={key: op.countOf(lst,key) for key in lst}#here give lst split wali not string
    return dic
ansM3=frequwncyM3(str1)
print("The frequency of words in M3:  ",end="------->  ")
print(dict(ansM3))