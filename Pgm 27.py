#PGM  Ways to string slicing in python to rotate a string
'''''
Give a string of size n, write a function to perform following operations on string
1. Left(or Anticlockwise) rotate the given string by d elements (where d<=n).
2. Right(or Clockwise) rotate the given string by d elements (where d<=n).
Examples:
    INPUT: s="GeeksforGeeks"
           d=2
    OUTPUT:
            Left Rotation : "eksforGeeksGe"
            Right Rotation : "ksGeeksforGeeks"
'''''
str1=input("Enter a String: ")
d=int(input("Enter no. of rotations : "))

#Method 1 = navie method
'''''
A simple solution is to use a temporary string to do rotation. 
for left rotation first copy last n-d characters then copy the first d characters in order to the temperory string. 
for right rotation, first copy last d characters then copy n-d characters.
This idea is based on Reversal Algorithm For Rotation
Time Complexity : O(n)
Auxiliary Space : O(n)
'''''
def leftRotationM1(s1,d1):
    temp=s1[d1:]+s1[0:d1]
    return temp
#In place rotates s towards right by d
def rightRotationM1(s1,d1):
    temp1=s1[:len(s1)-d1:]
    temp2=s1[len(s1)-d1:]
    temp=temp2+temp1
    return temp

leftM1=leftRotationM1(str1,d)
rightM1=rightRotationM1(str1,d)
print("Left Rotation of Given String in M1 : ",end="---->   ")
print(leftM1)
print("Right Rotation of Given String in M1 : ",end="---->  ")
print(rightM1)

#Method 2 = same as above but using 1 function to call for other

def leftRotationM2(s2,d2):
    temp=s2[d2:]+s2[0:d2]
    return temp
def rightRotationM2(s2,d2):
    return leftRotationM2(s2,len(s2)-d2)
leftM2=leftRotationM2(str1,d)
rightM2=rightRotationM2(str1,d)
print("Left Rotation of Given String in M2 : ",end="---->   ")
print(leftM2)
print("Right Rotation of Given String in M2 : ",end="---->  ")
print(rightM2)

# #Method 3 = using extednded string
# '''''
# we can use extended string which is double in size of normal string to rotate string.
# For left rotation access the extended string from index n to the index len(string)+n
# For right rotation rotate the string ledt with size-d places
# Time complexity : O(n), where n is the size of the given string
# Auxiliary Space : O(n), where n is the size
# '''''
# def leftRotationM2()