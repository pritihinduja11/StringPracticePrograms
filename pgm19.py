#PGM 19 ways to check if a given string is binary string or not

'''''
Given string str. The task is to check whether it is a binary string or not. 
Examples:  
Input: str = "01010101010"
Output: Yes
Input: str = "geeks101"
Output: No
'''''
str1=input("Enter a String:  ")
#Method 1 = using set
'''''
1. Insert the given string in a set
2. Check if the set characters consist of 1 and/or 0 only.
Time Complexity: O(n), Here n is the length of the string.
Auxiliary Space: O(1), As constant extra space is used.
'''''
def checkM1(s1):
    s=set(s1)
    p={"0","1"}#set contaning 0 and 1 for comparision
    if s==p or s=={"0"} or s=={"1"}:#if s has both 1 and 0 or only 0 or only 1
        return "Yes"
    else:
        return "No"
ansM1=checkM1(str1)
print("Is given string a binary string in M1:  ",ansM1)

#Method 2 = using iteration
'''''
1. Iterate for every character and check if the character is 0 or 1.
2. If it is not then set a counter and break.
3. After iteration check whether the counter is set or not.
Time Complexity: O(n), Here n is the length of the string.
Auxiliary Space: O(1), As constant extra space is used.
'''''
def checkM2(s2):
    count=0
    # initialize the variable t with '01' string
    t = '01'
    # looping through each character of the string .
    for char in s2:
        # check the character is present in
        # string t or not.
        # if this condition is true
        # assign 1 to the count variable
        # and break out of the for loop
        # otherwise pass
        if char not in t:
            count=1
            break;
        else:
            pass
    # after coming out of the loop
    # check value of count is non-zero or not
    # if the value is non-zero the en condition is true
    # and string is not accepted
    # otherwise string is accepted
    if count:
        return "No"
        #ek bhi other than 0 1 so no
    else:
        return "Yes"
ansM2=checkM2(str1)
print("Is given string a binary string in M2:  ",ansM2)

#Method 3 = using regular expression
'''''
1. Compile a regular expression using compile() for “character is not 0 or 1”.
2. Use re.findall() to fetch the strings satisfying the above regular expression.
3. Print output based on the result.
Time complexity: O(n)
Auxiliary space: O(1)
'''''
import re
def checkM3(s3):
    # regular expression to find the strings
    # which have characters other than 0 and 1
    c=re.compile('[^01]')
    # use findall() to get the list of strings
    # that have characters other than 0 and 1.
    s=c.findall(s3)
    if len(s):
        return "No" # if length of list > 0 then it is not binary
    else:
        return "Yes"
ansM3=checkM3(str1)
print("Is given string a binary string in M3:  ",ansM3)

#Method 4 = Using exception handling and int
'''''
Python has a built in method to convert a string of a specific base to a decimal integer, using int(string, base). 
If the string passed as an argument is not of the specified base, then a ValueError is raised.
Time Complexity: O(1), 
Auxiliary Space: O(1)
'''''
def checkM4(s4):
    try:
        # this will raise value error if
        # string is not of base 2
        int(s4,2)
    except ValueError:
        return "No"
    return "Yes"
ansM4=checkM4(str1)
print("Is given string a binary string in M4:  ",ansM4)

#Method 5 = using count() function
'''''
Time Complexity: O(n), where n is number of characters in string.
Auxiliary Space: O(1)
'''''
def checkM5(s5):
    if (s5.count('0')+s5.count('1')==len(s5)):#0and 1 jitni honge voi string ka length matlab string binary
        return "Yes"
    else:
        return "No"
ansM5=checkM5(str1)
print("Is given string a binary string in M5:  ",ansM5)

#Method 6 = Using replace() and len() methods'
def checkM6(s6):
    binary="01"
    for i in binary:
        s6=s6.replace(i,"")#0 and 1 ko none se replace kiya hai
    if (len(s6)==0):#no other name then s6 because uska scope for ke under hi raheg so s6=s6. used
        return "Yes"#matlab all were binary
    else:
        return "No"
ansM6=checkM6(str1)
print("Is given string a binary string in M6:  ",ansM6)

#Method 7 = using all()
'''''
The all() method in Python3 can be used to evaluate if all the letters in the string are 0 or 1.
Time Complexity: O(n), Here n is the length of the string.
Auxiliary Space: O(1), As constant extra space is used.
'''''
def checkM7(s7):
    if all((letter in '01') for letter in s7):#if all values are 0 or 1
        return "Yes"
    else:
        return "No"
ansM7=checkM7(str1)
print("Is given string a binary string in M7:  ",ansM7)