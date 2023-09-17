#PGM 2 -> Ways to check whether the string is symmetrical or palindrome

'''''
Given a string. the task is to check if the string is symmetrical and palindrome or not. 
A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a 
palindrome string if one half of the string is the reverse of the other half or if a string appears same 
when read forward or backward.
Eg 1 :  Input: khokho
        Output: 
        The entered string is symmetrical
        The entered string is not palindrome
Eg 2 :  Input:amaama
        Output:
        The entered string is symmetrical
        The entered string is palindrome
'''''
str1=input("Enter a string : ")
print("Original String :  ",str1)

#Method 1 = Navie Method
'''''
The approach is very naive. In the case of palindrome, a loop is run to the mid of the string and the first and 
last characters are matched. If the characters are not similar then the loop breaks and the string is not palindrome 
otherwise the string is a palindrome. In the case of symmetry, if the string length is even then the string is broken 
into two halves and the loop is run, checking the characters of the strings of both the half. If the characters are 
not similar then the loops break and the string is not symmetrical otherwise the string is symmetrical. 
If the string length is odd then the string is broken into two halves in such a way that the middle element is 
left unchecked, and the above same step is repeated.
Time Complexity: O(n)
Auxiliary Space: O(n), where n is number of characters in string.
'''''
# Function to check whether the
# string is palindrome or not
def isPalindromeM1(s1):
    flag=False
    for i in range(0,int(len(s1)/2)):
        if s1[i] == s1[len(s1)-i-1]:
            flag = True
        else:
            flag = False
    if flag == False:
        return "Not Palindrome"
    else:
        return "Palindrome"
def symmetry(s1):
    n=len(s1)
    flag=0
    # Check if the string's length
    # is odd or even
    if n%2==0:
        mid=n//2+1 #as mid ek baad se traverse hoga n comparision so +1
    else:
        mid = n//2
    start1=0
    start2=mid
    while(start1<mid and  start2<n):#start1 mid se kaam hai and mid n se kaam toh hi voh mid hoga n
        #while loop start se till dono mein se koi ek condition fail nhi hoti as and
        #start ko incfrement kar ke while loop mein so if jab tak success aage jaha fail vaha break
        if (s1[start1] == s1[start2]):
            start1=start1+1
            start2=start2+1
        else:
            flag=1
            break
    if flag == 0:
        return "Not Symmetric"
    else:
        return "Symmetric"
pal1=isPalindromeM1(str1)
sym1=symmetry(str1)
print("The entered string is {} in M1.".format(pal1))
print("The entered string is {} in M1.".format(sym1))

#for further methods palindrome fuctions remain same as solve with different ways in previous example only symmetry function changes

#Method 2 -> We use slicing in this method.
'''''
The Time and Space Complexity for all the methods are the same:
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def isSymmetryM2(s1):
    flag=0
    n=len(s1)
    #if n%2==0:
    #    half=n//2+1
    #else:
    #    half = n//2
    half=int(n/2)
    #here no even odd as int so voh round off kar dega and slicing mein last exclude horta hai so half ke ek phele tak hi lega
    str1=s1[:half]
    str2=s1[half:n]
    if (str1 == str2):
        flag =1
    else:
        flag = 0
    if(flag == 0):
        return "Not Symmetric"
    else:
        return "Symmetric"
pal2=isPalindromeM1(str1)
sym2=isSymmetryM2(str1)
print("The entered string is {} in M2.".format(pal2))
print("The entered string is {} in M2.".format(sym2))