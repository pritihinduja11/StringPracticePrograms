#PGM 23 ways to check for URL in a string

'''''
we will need to accept a string and we need to check if the string contains any URL in it. If the URL is present in the 
string, we will say URL’s been found or not and print the respective URL present in the string. We will use the concept 
of Regular Expression of Python to solve the problem.

Examples:

Input : string = 'My Profile: 
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
in the portal of https://www.geeksforgeeks.org/'

Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
'https://www.geeksforgeeks.org/']

Input : string = 'I am a blogger at https://geeksforgeeks.org'
Output : URL :  ['https://geeksforgeeks.org']
'''''

str1=input("Enter a string : ")

#Method 1 = using findall() from reular expression module
'''''
Time complexity: O(n) where n is the length of the input string, as the findall function of the re library iterates 
through the entire string once to find the URLs.
Auxiliary space: O(n), where n is the length of the input string, as the function Find stores all the URLs found in the 
input string into a list which is returned at the end.
'''''
import re
def urlM1(s1):
    #findall () have been used with valid conditions
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url=re.findall(regex,s1)
    return [x[0] for x in url]
ansM1=urlM1(str1)
print("The URLs in the given string in M1 are : ",end="---->  ")
print(ansM1)

#Method 2 = using startwith()
'''''
Time Complexity: O(n), where n is the number of words in the input string.
Auxiliary Space: O(n), where n is the number of URLs found in the input string. The auxiliary space is used to store the found URLs in the res list.
'''''
def urlM2(s2):
    x=s2.split()
    res=[]
    for i in x:
        if i.startswith("https:") or i.startswith("http:") or i.startswith("www."):
            res.append(i)
    return res
ansM2=urlM2(str1)
print("The URLs in the given string in M2 are : ",end="---->  ")
print(ansM2)

#Method 3 = using find() method
'''''
Time Complexity : O(N)
Auxiliary Space : O(N)
'''''
def urlM3(s3):
    x=s3.split()
    res=[]
    for i in x:
        if i.find("https:")==0 or i.find("http:")==0:#find returns the index of particular substrig in string and both will be at 0
            res.append(i)
    return res
ansM3=urlM3(str1)
print("The URLs in the given string in M3 are : ",end="---->  ")
print(ansM3)