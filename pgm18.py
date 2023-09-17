#PGM 18 ways in python program to split and join a string

'''''
Python program to Split a string based on a delimiter and join the string using another delimiter. Splitting a string 
can be quite useful sometimes, especially when you need only certain parts of strings. A simple yet effective example is 
splitting the First-name and Last-name of a person. Another application is CSV(Comma Separated Files). We use split to 
get data from CSV and join to write data to CSV. In Python, we can use the function split() to split a string and join() 
to join a string. For a detailed articles on split() and join() functions, refer these : split() in Python and join() 
in Python. 
Examples :
Split the string into list of strings
Input : Geeks for Geeks
Output : ['Geeks', 'for', 'Geeks']
Join the list of strings into a string based on delimiter ('-')
Input :  ['Geeks', 'for', 'Geeks']
Output : Geeks-for-Geeks
'''''
str1=input("Enter a String: ")

#Method 1 = based on delimiter
def concatM1(s1):
    # Split the string based on space delimiter
    s=s1.split(" ")
    # Join the string based on '-' delimiter
    return "_".join(s)
ansM1=concatM1(str1)
print("new string in M1: ",end="----->  ")
print(ansM1)

#Method 2 = using split() and join()
'''''
Time complexity: O(n), where n is the length of given string
Auxiliary space: O(n)
'''''
def concatM2(s2):
    return "_".join(s2.split(" "))
ansM2=concatM2(str1)
print("new string in M2: ",end="----->  ")
print(ansM2)

#Method 3 = using re module
'''''
In the below code, we first imported the re (regular expression) module in order to use the split() function from it. 
We then defined a string s which we want to split and join using different delimiters.
To split the string, we used the split() function from the re module and passed it the delimiter that we want to use to 
split the string. In this case, we used a space character as the delimiter. This function returns a list of substrings, 
where each substring is a part of the original string that was separated by the delimiter.
To join the list of substrings back into a single string, we used a for loop to iterate through the list. For each 
substring in the list, we concatenated it to a new string called new_string using the + operator. We also added a hyphen 
between each substring, to demonstrate how to use a different delimiter for the join operation.
Finally, we printed both the split and joined versions of the string to the console. The output shows that the string 
was successfully split and joined using the specified delimiters.
'''''
import re
def concatM3(s3):
    s=re.split('[^a-zA-z]',s3)#if not alphabet waha pe split
    joined_string=''
    for i,s in enumerate(s):
        if i>0:
            joined_string+='_'
        joined_string+=s
    return s,joined_string
join,ansM3=concatM3(str1)
print("new string in M3: ",end="----->  ")
print(ansM3)

#Method 4 =  Using regex.findall() method
'''''
Time complexity: O(n), where n is the length of given string
Auxiliary space: O(n)
'''''
import re
def concatM4(s4):
    # print the string after split method
    st=re.findall(r'[a-zA-Z]+',s4)#pattern is r wala
    return "_".join(st)
ansM4=concatM4(str1)
print("new string in M4: ",end="----->  ")
print(ansM4)