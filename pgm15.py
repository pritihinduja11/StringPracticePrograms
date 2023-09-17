#PGM 15 Ways to check if a string contains any special character in python

'''''
Given a string, the task is to check if that string contains any special character (defined special character set). 
If any special character found, don’t accept that string.
Examples : 
Input : Geeks$For$Geeks
Output : String is not accepted.
Input : Geeks For Geeks
Output : String is accepted
'''''
str1=input("Enter a String:  ")
#Method 1 =using re
'''''
Approach: Make a regular expression(regex) object of all the special characters that we don’t want, then pass a string 
in search method. If any one character of string is matching with regex object then search method returns a match 
object otherwise return None.
'''''
import re
def specialCharacterM1(s1):
    # Make own character set and pass
    # this as argument in compile method
    regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(s1)==None:#it will search whole string if any special character not found == none so return no ele yes
        return "No"
    else:
        return "Yes"
ansM1=specialCharacterM1(str1)
print("If a string Contains Special character in M1:  ",ansM1)

#Method 2 = using set
def specialCharacterM2(s2):
    s2.split()
    s=set('[@_!#$%^&*()<>?/\|}{~:]')
    count=0
    for i in range(len(s2)):
        # checking if any special character is present in given string or not
        if s2[i] in s:
            count+=1
    if count>0:
        return "Yes"
    else:
        return "No"
ansM2=specialCharacterM2(str1)
print("If a string Contains Special character in M2:  ",ansM2)

#Method 3 = Using inbuilt methods
'''''
This approach uses the isalpha() and isdigit() methods to check if a character is an alphabetical character or a digit, 
respectively. If a character is neither an alphabetical character nor a digit, it is considered a special character.
The time complexity of this function is O(n), where n is the length of the input string, because it involves a single 
loop that iterates through all the characters in the string.
The space complexity of this function is O(1), because it does not use any additional data structures and the space 
it uses is independent of the input size.
'''''
def specialCharacterM3(s3):
    for c in s3:
        if not (c.isalpha()or c.isdigit() or c==" "):
            return "No"
        else:
            return "Yes"
ansM3=specialCharacterM3(str1)
print("If a string Contains Special character in M3:  ",ansM3)