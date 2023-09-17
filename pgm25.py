#PGM 25 = Ways in python to Replace all occurence of substring with given string in main string

'''''
Sometimes, while working with Python strings, we can have a problem in which we need to replace all occurrences of a substring with other.

Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
Output : test_str = “geeksabcdgeeks”
'''''
string1=input("Enter a string : ")
sub_str1=input("Enter a sub string : ")
sub_str2=input("enter string with which you want to replace : ")
#Method 1 = using build in function replace
'''''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def replaceM1(s1,sub_s1,replace_s1):
    #while sub_s1 in s1:
    s1=s1.replace(sub_s1,replace_s1)#replace will replace all occurences of sub string in string
    return s1

ansM1=replaceM1(string1,sub_str1,sub_str2)
print("String after replacing all occurences of sub string in M1:  ",end="---->    ")
print(ansM1)

#Method 2 = using string.split()
'''''
Splitting the string by substring and then replacing with the new string.split() function is used.
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def replaceM2(s2,sub_s2,replace_s2):
    #spliting string by substring
    s=s2.split(sub_s2)#split return empty or blanck for givrn pattern if sub sn dreplace same so it will print 2 times
    #for split input=geeksforgeeks sub_str1=geeks replace_str=abcd
    #print(s)#output ['', 'for', ''],if sub aand replace same ['', '']
    new_str=""
    for i in s:
        #jaha match hua hoga wah split ne blank return kiya hoga so replace blank with replace string
        if i=="":
            new_str+=sub_str2
        else:
            new_str+=i
    return new_str
ansM2=replaceM2(string1,sub_str1,sub_str2)
print("String after replacing all occurences of sub string in M2:  ",end="---->    ")
print(ansM2)

#Method 3 = using re.sub()
'''''
def sub(pattern, repl, string, count=0, flags=0):
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""
    return _compile(pattern, flags).sub(repl, string, count)
    
Time Complexity: O(n), where n is the length of the input string. This is because the re.sub() function iterates through 
entire input string and performs a regular expression match on each character to find all occurrences of the substring. 
The number of iterations is directly proportional to the length of the input string.
'''''
import re
def replaceM3(s3,sub_s3,replace_s3):
   # while sub_s3 in s3:
    s3=re.sub(sub_s3,replace_s3,s3)#sub replaces all the occurences of substring in a main string
    return s3
ansM3=replaceM3(string1,sub_str1,sub_str2)
print("String after replacing all occurences of sub string in M3:  ",end="---->    ")
print(ansM3)

#Method 4 = iteration
'''''
The idea behind this approach is to iterate through the input string character by character and check if each substring 
of length m matches the substring we want to replace. If it does, we add the replacement substring to our result and 
move the pointer forward by m characters. If it doesn’t match, we add the current character to the result and move 
the pointer forward by 1 character.

Time complexity: O(nm), where n is the length of the input string and m is the length of the substring to be replaced. 
Auxiliary space: O(n), since we are creating a new string to store the result.
'''''
def replaceM4(s4,sub_s4,replace_s4):
    #initialise and empty string to store a result
    result=""
    #initialise variable to keep track of position in a string
    i=0
    while i <len(s4):
        #check if current sub string matches the substring we want to replace
        if s4[i:i+len(sub_s4)]==sub_s4:#i se len of sub string tak if all same matlab its substring
            # if it does add the replacement string to result and move the pointer forward
            result+=replace_s4
            #i ko increase karna hai match ke baad pe leke jana hai i.e substring ke baad wala index so curent + len of sub string
            i+=len(sub_s4)
        else:
            #if it doesnt add a current character to the result and move the pointer forward
            result+=s4[i]
            #now move to next character and check again if whole substring match
            i+=1
    return result
ansM4=replaceM4(string1,sub_str1,sub_str2)
print("String after replacing all occurences of sub string in M4:  ",end="---->    ")
print(ansM4)
