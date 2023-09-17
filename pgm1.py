#PGM 1 -> ways to check if a string is palindrome or not

str1=input("Enter a string :  ")
print("original string: ",str1)

#Method 1 = Basic Method
'''''
1) Find reverse of the string
2) Check if reverse and original are same or not.
Time complexity: O(n)
Auxiliary Space: O(1)
'''''
def isPalindromeM1(s):
    if s == s[::-1]:
        return True
    else:
        return False
ansM1=isPalindromeM1(str1)
print("{} is palindrome in M1 : {}".format(str1,ansM1))

#Method 2 = Naive method using for loop
'''''
Run a loop from starting to length/2 and check the first character to the last character of the string and second 
to second last one and so on …. If any character mismatches, the string wouldn’t be a palindrome.
Time complexity: O(n)
Auxiliary Space: O(1)
'''''
def isPalindromeM2(s2):
    for i in range(0,int(len(s2)/2)):#as if no convert to int then it can be float also and range take only int so..
        if s2[i]!=s2[len(s2)-i-1]:
        #as last chaiye and range mid tak so i if 0 so last should be length-0-1 bcz index here starts
        # from 0 else it will give index range out of bound
            return False
        else:
            return True
ansM2=isPalindromeM2(str1)
print("{} is palindrome in M2 : {}".format(str1,ansM2))

#Method 3 = using the inbuilt function to reverse a string
'''''
In this method, the predefined function ‘ ‘.join(reversed(string)) is used to reverse string. 
Time complexity: O(n)
Auxiliary Space: O(n)
'''''
def isPalindromeM3(s3):
    s4="".join(reversed(s3))
    if s3 == s4:
        return True
    return False
ansM3=isPalindromeM3(str1)
print("{} is palindrome in M3 : {}".format(str1,ansM3))

#Method 4 = using one extra variable
'''''
In this method, the user takes a character of string one by one and store it in an empty variable. 
After storing all the characters user will compare both the string and check whether it is palindrome or not.
Time complexity: O(n)
Auxiliary Space: O(n)
'''''
def isPalindromeM4(s4):
    w=""
    for i in s4:
        w=i+w#as w mein ek ek s4 se element append as + and str so concat hote jayega and finally x ban jayega
        #yaha i+w use kiya hai not w+i so sab reverse hoga w=i yani ki joh abhi hai + prev w
    if(w==s4):
        return True
    return False
ansM4=isPalindromeM4(str1)
print("{} is palindrome in M4 : {}".format(str1,ansM4))

#Method 5 = using flag
'''''
In this method, the user compares each character from starting and ending in a for loop and if the character does 
not match then it will change the status of the flag. Then it will check the status of the flag and accordingly 
and print whether it is a palindrome or not.
Time complexity: O(n)
Auxiliary Space: O(1)  
'''''
#ismein it will have 2 for loop or 2 loop variables i andd j
#i will take element from string and j will start from -1 and take care of indexing of s5 for comparing
#where j doesnt match i falg is set to false and break the loop
def isPalindromeM5(s5):
    flag=False
    j=-1
    for i in s5:#no continue as continue means execute next line elif gets execute and then over for loop interrupts
        if i == s5[j]:
            flag = True
            #continue
        elif i != s5[j]:
            flag=False
            break
        j=j-1
    return flag
ansM5=isPalindromeM5(str1)
print("{} is palindrome in M5 : {}".format(str1,ansM5))

#Method 6 = using recursion
'''''
This method compares the first and the last element of the string and gives the rest of the substring 
to a recursive call to itself.
Time complexity: O(n)
Auxiliary Space: O(n)
here we have to convert all letters to upper or lowwer as it is cases ensitive  
'''''
def isPalindromeM6(s6):
    # to change it the string is similar case
    s=s6.lower()
    # length of s
    l=len(s)
    # if length is less than 2 as single character
    if (l<2):
        return True
    # If s[0] and s[l-1] are equal i.e first and last
    elif s[0]==s[l-1]:
        # Call is palindrome form substring(1,l-1)
        return isPalindromeM6(s[1:l-1])
    #as last is excluded so l-1 mot l-2 and this will again call fun with substring and uska first and last match
    #so again fun call uske bhi substring ke liye and this repeates till substring is >=2 as for 1  we have condition
    #and that works for single middle also and since length-1 so no out of bound  error and middle chsracter of
    #string with odd length is also handled. as ''' if yeh use inside function so it consider as string and gives error
    else:
        return False
ansM6=isPalindromeM6(str1)
print("{} is palindrome in M6 : {}".format(str1,ansM6))

#Method 7 = Using extend() and reverse() methods
'''''
Time complexity: O(n) where n is the length of a given string
Auxiliary space: O(n)
'''''
def isPalindromeM7(s7):
    x=list(s7)
    y=[]
    y.extend(x)
    y.reverse()
    if (x==y):
        return True
    return False
ansM7=isPalindromeM7(str1)
print("{} is palindrome in M7 : {}".format(str1,ansM7))