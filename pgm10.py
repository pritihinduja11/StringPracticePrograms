#PGM 10  ways to accept the string which contains all vowels
'''''
Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present if it is 
present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ . 
Examples : 
Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present
Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
'''''

str1=input("enter a strring : ")

#Method 1 = using set and for loop
'''''
Firstly, create set of vowels using set() function. Check for each character of the string is vowel or not, if vowel 
then add into the set s. After coming out of the loop, check length of the set s, if length of set s is equal to the 
length of the vowels set then string is accepted otherwise not. 
Time complexity : O(n)
Auxiliary Space : O(n)
'''''
# Function for check if string  is accepted or not
def check(s1):
    if  s1.__contains__(" "):
        s1=s1.split()
    s1.lower()#because if vowel caps so alag se handling of that
    # set() function convert "aeiou"
    # string into set of characters
    # i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels = set("aeiou")
    # set() function convert empty
    # dictionary into empty set
    s = set({})
    # looping through each
    # character of the string
    for char in s1:
        # Check for the character is present inside
        # the vowels set or not. If present, then
        # add into the set s by using add method
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s)==len(vowels):#cant compare 2 obj with == as dono ka address diff so not work compare length
        return "Accepted"
    else:
        return "Not Accepted"
ansM1=check(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M1:  ",ansM1)

#Method 2 = using count
def checkM2(s2):
    s2.lower()
    vowels=[s2.count("a"),s2.count("e"),s2.count("i"),s2.count("o"),s2.count("u")]
    #print(vowels)===> output: [0, 1, 1, 1, 1]
    if vowels.count(0)>0:#if 0 is present in vowels or array of count of vowels
        return "Not Accepted"
    else:
        return "Accepted"
ansM2=checkM2(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M2:  ",ansM2)

#Method 3 = using set intersection
def checkM3(s3):
    if len(set(s3.lower()).intersection('aeiou'))>=5:#as intersection gives new set having common elements of both sets
        #it updates set s1 only s1.intersection(s2)
        # IF INTERSECTION Count is >5 means all vowels are present set 2 is subset of set1
        #intersection is all elements of set 2 should be present in set 1
        return "Accepted"
    else:
        return "Not Accepted"
ansM3=checkM3(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M3:  ",ansM3)

#Method 4 = using regular expression
import re
def checkM4(s4):
    # regular expression to find the strings
    # which have characters other than a,e,i,o and u
    #def compile(pattern, flags=0):
        #"Compile a regular expression pattern, returning a Pattern object."
        #return _compile(pattern, flags)
    c=re.compile('aeiouAEIOU')
    #print(c)==>Output re.compile('aeiou')it will have aeiou so if any aeiou in s4 it will find that so len >0
    if len(c.findall(s4)):#c.compile will have all consonants so if s4 match element with c so it doesnt have vowels
        #else it will have vowels
        #if len(string)>0 then it is not accepted
        print(c.findall(s4))#==>input:aeioussss output:['aeiou']
        #this fail in case where any vowel is missing it still ans accepted
        return "Not Accepted"
    else:
        return "Accepted"
ansM4=checkM4(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M4:  ",ansM4)

#Method 5 = using data structure
def checkM5(s5):
    new_list=[char for char in s5.lower() if char in "aeiou"]
    if new_list:
        dic,lst={},[]
        for char in new_list:
            dic["a"] = new_list.count("a")
            dic["e"] = new_list.count("e")
            dic["i"] = new_list.count("i")
            dic["o"] = new_list.count("o")
            dic["u"] = new_list.count("u")
        for i,j in dic.items():
            if j!=0:
                lst.append(i)
        if len(lst)>=5:
            return "Accepted"
        else:
            return "Not Accepted"
ansM5=checkM5(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M5:  ",ansM5)

#Method 6 = using set methods
#The issubset() attribute of a set in Python3 checks if all the elements of a given set are present in another set.
def checkM6(s6):
    # Checking if "aeiou" is a subset of the set of all letters in the string
    #set1 is subset of set2 i.e set1.issubset(set2)
    if set("aeiou").issubset(set(s6.lower())):
        return "Accepted"
    else:
        return "Not Accepted"
ansM6=checkM6(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M6:  ",ansM6)

#Method 7 = using collections
'''''
The time complexity of the above code is O(n), where n is the length of the input string. This is because the code 
iterates through each character in the input string and performs a constant number of operations on each character.
The auxiliary space complexity of the above code is also O(n), because the code creates two sets, one to store the 
vowels and one to store the vowels found in the input string, both of which have a size that is equal to the length of 
the input string. In addition to these sets, the code also creates a list to store the count of each vowel in the input 
string, which also has a size equal to the length of the input string. Overall, the auxiliary space complexity is O(n).
'''''
import collections
def checkM7(s7):
    # create a Counter object to count the occurrences of each character it is like dic key values
    counter=collections.Counter(s7.lower())
    # set of vowels
    vowels=set("aeiou")
    # counter for the number of vowels present
    vowels_count=0
    # check if each vowel is present in the string
    for vowel in vowels:
        if counter[vowel]>0:
            vowels_count+=1
    if vowels_count>=5:
        return "Accepted"
    else:
        return "Not Accepted"
ansM7=checkM7(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M7:  ",ansM7)

#Method 8 = using all() method
'''''
The Time Complexity of the function is O(n), and the Space Complexity is O (1) which makes this function efficient and 
suitable for most use cases.
'''''
def checkM8(s8):
    vowels="seiou"
    ''''
    def all(*args, **kwargs): # real signature unknown
    """
    Return True if bool(x) is True for all values x in the iterable.
    
    If the iterable is empty, return True.
    '''''
    if all(vowel in s8.lower() for vowel in vowels):#all checks if aeiou is there in s8 and returns true
        return "Accepted"
    else:
        return "Not Accepted"
ansM8=checkM8(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M8:  ",ansM8)

#Method 9 = using set.difference()
'''''
The difference between the two sets in Python is equal to the difference between the number of elements in two sets. 
The function difference() returns a set that is the difference between two sets. Let’s try to find out what will be the 
difference between two sets A and B. Then (set A – set B) will be the elements present in set A but not in B and 
(set B – set A) will be the elements present in set B but not in set A. 
Time complexity:O(n)
Auxiliary Space:O(n)
'''''
def checkM9(s9):
    a=set("aeiou")
    set1=a.difference(s9)
    #set 1 will have elements in a but not in b so a will be vowels that are not in b so if any vowel present
    # so A-B will not be 0 else 0
    if len(set1)==0:
        return "Accepted"
    else:
        return "Not Accepted"
ansM9=checkM9(str1)
print("The Acceptance status of given string whether it contains all vowels or not in M9:  ",ansM9)