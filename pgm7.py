#PGM 7  ways to convert snake case to pascal case

'''''
Sometimes, while working with Python Strings, we have problem in which we need to perform a case conversion of String. 
This a very common problem. This can have application in many domains such as web development. Lets discuss certain ways 
in which this task can be performed.
Example:
    Input : geeks_for_geeks
    Output : GeeksforGeeks
    Input : left_index
    Output : leftIndex
The Time and Space Complexity for all the methods are the same:
Time Complexity: O(n)
Space Complexity: O(n)
'''''
str1=input("enter string seperated by _ underscore : ")

#Method 1 = : Using title() + replace()
'''''
 In this, we first convert the underscore to empty string and then title case each word. 
 pascal case is whole string as one word no spaces
'''''
def snackeCaseIntoPascalCaseM1(s1):
    new_str=s1.replace("_"," ").replace(" ","")
    return new_str
ansM1=snackeCaseIntoPascalCaseM1(str1)
print("The string after conversion from snack case to pascal case in M1: ",end="----->  ")
print(ansM1)

#Method 2 = Using capwords() in string module->The task of performing title case is performed using capwords() in this method.
'''''
# Capitalize the words in a string, e.g. " aBc  dEf " -> "Abc Def".
def capwords(s, sep=None):
    """capwords(s [,sep]) -> string

    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join.  If the optional second argument sep is absent or None,
    runs of whitespace characters are replaced by a single space
    and leading and trailing whitespace are removed, otherwise
    sep is used to split and join the words.

    """
    return (sep or ' ').join(x.capitalize() for x in s.split(sep))
'''''
import string
def snackeCaseIntoPascalCaseM2(s2):
    res=string.capwords(s2.replace("_"," ")).replace(" ","")#if direct replace "_" to "" not work first convert to space then blank
    return res
ansM2=snackeCaseIntoPascalCaseM2(str1)
print("The string after conversion from snack case to pascal case in M2: ",end="----->  ")
print(ansM2)

#Method 3 =   Using split(),title() and join() methods
def snackeCaseIntoPascalCaseM3(s3):
    x=s3.split("_")
    l=[]
    for i in x:
        i=i.title()#title() converts first letter to caps of all words in string
        print(i)
        l.append(i)
    new_str="".join(l)
    return new_str
ansM3=snackeCaseIntoPascalCaseM3(str1)
print("The string after conversion from snack case to pascal case in M3: ",end="----->  ")
print(ansM3)