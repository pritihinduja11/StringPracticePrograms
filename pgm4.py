#PGM 4 -> ways to remove ith character from string in python

str1=input("enter a word or string without spaces : ")
n=int(input("index of chracter to be removed from string :  "))

#Method 1 = using for loop
'''''
In this method, one just has to run a Python loop and append the characters as they come and build a new string from 
the existing one except when the index is i. 
'''''
def removeM1(s1,n1):
    new_str=""
    for i in range(len(s1)):
        if i!=n1:
            new_str=new_str+s1[i]
    return new_str
stringM1=removeM1(str1,n)
print("The string after removal of ith character in M1: ",end="----------------->  ")
print(stringM1)

#Method 2 = using str.replace()
'''''
The str.replace() can possibly be used for performing the task of removal as we can replace the particular index with 
empty char, and hence solve the issue. 
Drawback: The major drawback of this approach is that it fails in case there as duplicates in a string that match the 
char at pos. i. replace() replaces all the occurrences of a particular character and hence would replace all the 
occurrences of all the characters at pos i. We can still sometimes use this function if the replacing character 
occurs for 1st time in the string. 
'''''
def removeM2(s2,n2):
    for i in range(len(s2)):
        char=s2[i]
        if i==n2:
            new_str=s2.replace(char,'',1)
            return new_str
            break
'''''
Example:
# Initializing String
test_str = "GeeksForGeeks"
# Removing char at pos 3
# using replace
new_str = test_str.replace('e', '')
# Printing string after removal
# removes all occurrences of 'e'
print ("The string after removal of i'th character( doesn't work) : " + new_str)
# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)
# Printing string after removal
# removes first occurrences of s
print ("The string after removal of i'th character(works) : " + new_str)
'''''
stringM2=removeM2(str1,n)
print("The string after removal of ith character in M2: ",end="----------------->  ")
print(stringM2)

#Method 3 = using slice + concatenation
'''''
One can use string slice and slice the string before the pos i, and slice after the pos i. Then using string 
concatenation of both, ith character can appear to be deleted from the string. 
'''''
def removeM3(s3,n3):
    #slicing and concetanation
    new_str=s3[:n3]+s3[n3+1:]
    return new_str
stringM3=removeM3(str1,n)
print("The string after removal of ith character in M3: ",end="----------------->  ")
print(stringM3)

#Method 4 = using str.join() and list comprehension
'''''
In this method, each element of a string is first converted as each element of the list, and then each of them is 
joined to form a string except the specified index.
'''''
def removeM4(s4,n4):
    lst=[]
    for i in range(len(s4)):
        if i!=n4:
            lst.append(s4[i])
    new_str="".join(lst)
    return new_str
stringM4=removeM4(str1,n)
print("The string after removal of ith character in M4: ",end="----------------->  ")
print(stringM4)

#Method 5 = Approach 2 of Method 4
def removeM5(s5,n5):
    new_str="".join(s5[i] for i in range(len(s5)) if i!=n5)
    return new_str
stringM5=removeM5(str1,n)
print("The string after removal of ith character in M5: ",end="----------------->  ")
print(stringM5)

#Method 6 = using translate()
def removeM6(s6,n6):
    new_str=s6.translate({ord(s6[i]): None for i in range(len(s6)) if i==n6})
    return new_str
stringM6=removeM6(str1,n)
print("The string after removal of ith character in M6: ",end="----------------->  ")
print(stringM6)

#Method 7 = using recursion
'''''
To use recursion to remove the ith character from a string, you can define a recursive function that takes in the 
string and the index to be removed as arguments. The function can check if the index is equal to 0, in which case it 
returns the string with the first character removed. If the index is not 0, the function can return the first character 
of the string concatenated with the result of calling the function again on the string with the index decremented by 1.
In terms of time complexity, this approach has a time complexity of O(n) where n is the length of the string, 
because the function makes a single recursive call for each character in the string.
In terms of space complexity, this approach has a space complexity of O(n) because the function makes a recursive call 
for each character in the string, and each call requires space on the call stack.
'''''
def removeM7(s7,n7):
    #remove first character or base character
    if n7==0:
        return s7[1:]
    #recursive: return first character concatenate with result of calling function on string with index decremented by 1
    return s7[0]+removeM7(s7[1:],n7-1)#only one recursive call not on loop
#this basically returns first character if index is > 0 and then recursive call
stringM7=removeM7(str1,n)
print("The string after removal of ith character in M7: ",end="----------------->  ")
print(stringM7)
'''''
#####OUTPUT#####
enter a word or string without spaces : GeeksForGeeks
index of chracter to be removed from string :  2
The string after removal of ith character in M1: ----------------->  GeksForGeeks
The string after removal of ith character in M2: ----------------->  GeksForGeeks
The string after removal of ith character in M3: ----------------->  GeksForGeeks
The string after removal of ith character in M4: ----------------->  GeksForGeeks
The string after removal of ith character in M5: ----------------->  GeksForGeeks
The string after removal of ith character in M6: ----------------->  GksForGks
The string after removal of ith character in M7: ----------------->  GeksForGeeks
'''''