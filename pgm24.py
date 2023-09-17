#PGM 24 ways to string slicing in python program to check if a string can become empty by recursive deletion

'''''
Given a string “str” and another string “sub_str”. We are allowed to delete “sub_str” from “str” any number of times. 
It is also given that the “sub_str” appears only once at a time. The task is to find if “str” can become empty by 
removing “sub_str” again and again. 
Examples:
    Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
    Output : Yes
    Explanation :   In the string GEEGEEKSKS, we can first 
                    delete the substring GEEKS from position 4.
                    The new string now becomes GEEKS. We can 
                    again delete sub-string GEEKS from position 1. 
                     Now the string becomes empty.

    Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
    Output : No
    Explanation :   In the string it is not possible to make the
                    string empty in any possible manner.
'''''

string1=input("Enter a string : ")
sub_string=input("Enter a sub string : ")

#Method 1 = using string slicing
'''''
1. use find() method of string to search a given substring .
2. if substring lies in main string then find function will return its index at its first occurence.
3. now slice string in two parts 
    1. from start of string till index  -1 of founded substring 
    2. start from first index of founded substring + length of substring  till end.
4. concate these two sliced part and repeat from step 1 until original string becomes empty or we dont find substring 
    anymore. 
    
Time Complexity: O(n/m), where n is the length of string, and m is the length of substring
Auxiliary Space: O(1)
    
one should use while instead of if so your code doesnt work properly 
'''''
'''''
def deleteM1(s1,sub_s1):
    print(s1)
    n=len(sub_s1)
    str1=0
    ans=s1.find(sub_s1)
    print("index: ",ans,"string ",s1)
    if ans>=0:
        print("inside if ")
        s=s1[:ans]
        m=s1[ans+n:]
        str1=s+m
        print(str1)
        print(len(str1))
        if len(str1) > 0:
            deleteM1(str1, sub_s1)
        return len(str1)

    else:
        print("inside else")
        return "Sub string not present in a given main string"
'''''
def deleteM1(s1,sub_s1):
    #if both the strings are empty
    if len(s1) == 0 and len(sub_s1) == 0:
        return "Yes"
    #if only sub string is empty
    if len(sub_s1) == 0:
        return "No"
    while(len(s1)!=0):
        index=s1.find(sub_s1)
        #check if substring found or not
        if index == -1:
            return "No" #"Sub string not present in main string"
        #slice input string in 2 parts
        #here we are doing using third variable one can also used list comprehension as shown below
        #s1=s1[:index]+s1[index+len(sub_s1):]
        s=s1[:index]
        m=s1[index+len(sub_s1):]
        temp=s+m
        s1=temp
    return "Yes"

ansM1=deleteM1(string1,sub_string)
print("is main string became empty by recursive deletion of substring in M1 : ",end="------>    ")
print(ansM1)

#Method 2 = using regular expression

'''''
One possible solution would be to use the regular expression. Regular expressions modules are very helpful with string. 
The regular expression module has a search function that is used to find the patterns in the string. 
And replace function is used for replacing the characters of string. 
Follow are the steps for our approach:
1. use re.search() function on a string to find sub string in a string.
2. use re.replace() function to replace substring from a string,
3. Repeat step 1 and 2 until there is substring in a string after replacing it.
4. At last if a string is empty after all replacing then it can become empty else it cannot become empty

def search(pattern, string, flags=0):
    """Scan through string looking for a match to the pattern, returning
    a Match object, or None if no match was found."""
    
    def sub(pattern, repl, string, count=0, flags=0):
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""
    return _compile(pattern, flags).sub(repl, string, count)
'''''
import re
def deleteM2(s2,sub_s2):
    #re.search(sub_string,string1)#<re.Match object; span=(3, 8), match='GEEKS'>
    while sub_s2 in s2:
        #replacing substring from string
        s2=re.sub(sub_s2,"",s2)#s2 ko assign s while loop lagaya hai
    return "Yes" if s2=="" else "No"
ansM2=deleteM2(string1,sub_string)
print("is main string became empty by recursive deletion of substring in M1 : ",end="------>    ")
print(ansM2)