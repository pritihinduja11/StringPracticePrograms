#PGM 29 ways in python to capitalise first and last charcater of each word in a string

'''''
Given the string, the task is to capitalize the first and last character of each word in a string. 

Examples:

Input: hello world 
Output: HellO WorlD

Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS
'''''

str1=input("Enter a string : ")

#Method 1 = using indexing and title
'''''
1.Access the last element using indexing.
2.Capitalize the first word using title() method.
3.Then join the each word using join() method.
4.Perform all the operations inside lambda for writing the code in one-line.
->There used a built-in function map( ) in place of that also we can use filter( ).Basically these are the functions 
which take a list or any other function and give result on it.
Time Complexity: O(n)
Auxiliary Space: O(n), where n is number of characters in string.
'''''
def capitaliseM1(s1):
    return " ".join(map(lambda s1 : s1[:-1]+s1[-1].upper(),s1.title().split()))
    #split is used to split words of string at spaces
    #title is used to capitalise first character of each word in a string
    #lambda is used to access last element and capitalise it in lambda string is concatenated with last element as upper.
ansM1=capitaliseM1(str1)
print("new string after capitalising first and last character of each wors n a string in M1 : ",end="---->   ")
print(ansM1)

#Method 2 = using slicing and upper() and split()
'''''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''''
def capitaaliseM2(s2):
    s=s2.split()
    res=[]
    for i in s:
        x=i[0].upper()+i[1:-1]+i[-1].upper()#-1 iss used to acces last element
        res.append(x)
    return " ".join(res)
ansM2=capitaaliseM2(str1)
print("new string after capitalising first and last character of each wors n a string in M2 : ",end="---->   ")
print(ansM2)