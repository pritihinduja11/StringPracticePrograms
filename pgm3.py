#PGM 3 -> ways to reverse words in a string in python
'''''
Example:
Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks  
time complexity: O(n)  
auxiliary space: O(n)
'''''

str1=input("Enter a sentence : ")

#Method 1 -> Basic method
def reverseM1(s1):
    l1=s1.split(" ")
    l2=l1[::-1]
    return l2
lst1=reverseM1(str1)
strM1=" ".join(lst1)#if " " no space so list ke sab wods ek sath as single if space so seperated by space if , so comma
print("The reversed string in M1 is : ")
print(strM1)

#Method 2 -> using for loop and list comprehension
def reversedM2(s2):
    s=s2.split()[::-1]
    l=[]
    for i in s:
        l.append(i)
    return l
lst2=reversedM2(str1)
strM2=" ".join(lst2)
print("The reversed string in M2 is : ")
print(strM2)

#Method 3 using revrersed ()
def reversedM3(s3):
    words=s3.split()
    strans=" ".join(reversed(words))
    return strans
strM3=reversedM3(str1)
print("The reversed string in M3 is : ")
print(strM3)

#Method 4 -> using re.findall() function
'''''
This solution use the same procedure but have different methods to reverse the words in string with the help backward 
iteration and regular expression module. Following are the steps of our approach:
1)Find all the words in string with the help of re.findall() function. 
2)Iterate over the list in backward manner. 
3)Join the words in a string with the help of join() function.
'''''
import re
def reversedM4(s4):
    # find all the words in sentence
    words=re.findall('\w+',s4)
    # Backward iterate over list of words and join using space
    strans=" ".join(words[i] for i in range(len(words)-1,-1,-1))
    #for reverse len = len-1 start = len-1 end -1 reverse so -1
    return strans
strM4=reversedM4(str1)
print("The reversed string in M4 is : ")
print(strM4)

#Method 5 -> using stack
'''''
Another approach to reverse the words in a given string is to use a stack. A stack is a data structure that supports 
push and pop operations. You can use a stack to reverse the words in a string by pushing the words onto the stack 
one by one and then popping them off the stack to form the reversed string.
'''''
def reversedM5(s5):
    # creating an empty stack
    stack=[]
    # pushing words onto the stack
    for words in s5.split():
        stack.append(words)
    # creating an empty list to store the reversed words
    reversed_words=[]
    # popping words off the stack and appending them to the list
    while stack:
        reversed_words.append(stack.pop())#as pop pops last element of list
    reversed_string=" ".join(reversed_words)
    return reversed_string
strM5=reversedM5(str1)
print("The reversed string in M5 is : ")
print(strM5)

#Method 6 -> using strip() and string concatenation
'''''
1. The input string is split into a list of words using the split() method. By default, split() splits the string on 
whitespace characters (spaces, tabs, and newlines), so each word is separated into its own element of the list.
2. An empty string variable called reversed_string is initialized.
3. A for loop is used to iterate over the indices of the words list in reverse order. The loop starts from the index 
of the last word in the list (i.e., len(words)-1) and goes backwards to the first word (i.e., index 0). For each index, 
the corresponding word is appended to reversed_string, followed by a space character.
4. Finally, the extra space character at the end of reversed_string is removed using the strip() method, 
and the resulting string is returned.
'''''
def reversedM6(s6):
    words=s6.split()
    reversed_string=" "
    # loop through the words in reverse order and append them to the reversed string
    for i in range(len(words)-1,-1,-1):
        reversed_string+=words[i]+" "#extra space after concation so prev word will hv space in end
    # remove the extra space at the end of the reversed string and return it
    return reversed_string.strip()
strM6=reversedM6(str1)
print("The reversed string in M6 is : ")
print(strM6)