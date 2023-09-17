#PGM 21  Ways to replace Multiple  words in a string with k (third word)

'''''
Sometimes, while working with Python strings, we can have problem in which we need to perform the replace of a word. 
This is quite common task and has been discussed many times. But sometimes, the requirement is to replace occurrence of 
only duplicate, i.e from second occurrence. This has applications in many domains. Let’s discuss certain ways in which 
this task can be performed. 
Example:
INPUT : Gfg is best . Gfg also has Classes now. Classes help understand better . 
OUTPUT : Gfg is best . It also has Classes now. They help understand better .
'''''

str1=input("Enter a Sentence:  ")
str2=input("enter word list you want to replace:  ")
word1=input("Enter word with which you want to replace using : ")

#Method 1 = Using join() + split() + list comprehension
'''''
The combination of above functions can be used to perform this task. In this, we split the string into words, check and 
replace the list words using join and list comprehension. 
Time complexity: O(n), where n is the number of words in the string “test_str”.
Auxiliary space: O(m), where m is the number of characters in the output string “res”. This is because the output string 
requires memory proportional to its length to store its characters.
'''''
def duplicateM1(s1,lst,word):
    lst=lst.split()
    s1=s1.split()
    m=[word if i in lst else i for i in s1 ]
    return " ".join(m)
ansM1=duplicateM1(str1,str2,word1)
print("The String after replacing multiple words with k in M1:  ",end="----->  ")
print(ansM1)

#Method 2 = using regex + join()
'''''
Using regex + join() The combination of above functions can be used to perform this task. In this, we find the words 
using regex and perform the replace using join() and list comprehension.
Time Complexity: O(n)
Auxiliary Space: O(n) 
'''''
import re
def duplicateM2(s2,lst2,word2):
    # Replace multiple words with K
    # Using regex + join()
    lst2=lst2.split()
    res=re.sub("|".join(sorted(lst2,key=len,reverse=True)),word2,s2)
    return str(res)
ansM2=duplicateM2(str1,str2,word1)
print("The String after replacing multiple words with k in M2:  ",end="----->  ")
print(ansM2)

#Method 3 = Using for loop+replace() methods
'''''
Time Complexity: O(n*m) where n is the length of the input string and m is the number of words in the word_list.
Auxiliary Space: O(n) as it only uses memory for storing the input string and the list of words.
'''''
def duplicateM3(s3,lst3,word3):
    lst3=lst3.split()
    for i in lst3:
        s3=s3.replace(i,word3)
    return s3
ansM3=duplicateM3(str1,str2,word1)
print("The String after replacing multiple words with k in M3:  ",end="----->  ")
print(ansM3)

#Method 4 = Using dictionary and re.sub()
'''''
Time Complexity: O(n), where n is the number of characters in the input string.
Auxiliary Space: O(n), as the pattern and result strings will require memory proportional to their length.
'''''
import re
def duplicateM4(s4,lst4,word4):
    lst4=lst4.split()
    dic=dict()
    for i in lst4:
        dic[i]=word4
    # create a regular expression pattern from the dictionary keys
    pattern=re.compile("|".join(map(re.escape,dic.keys())))
    # use re.sub to replace the keys with values in the text
    return pattern.sub(lambda x: dic[x.group(0)], s4)
ansM4=duplicateM4(str1,str2,word1)
print("The String after replacing multiple words with k in M4:  ",end="----->  ")
print(ansM4)