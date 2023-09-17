#PGM 11 ways to count number of matching characters in a pair of string

'''''
Given a pair of non-empty strings. Count the number of matching characters in those strings (consider the single count 
for the character which have duplicates in the strings).
Examples:
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
(i.e. matching characters :- a, d, e, f)
Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5 
(i.e. matching characters :- b, 1, 2, @, k) 
'''''

str1=input("Enter first String:  ")
str2=input("Enter second string:  ")

#Method 1 = using for loop
'''''
1. Initialize a counter variable with 0. 
2. Iterate over the first string from the starting character to ending character.
3. If the character extracted from first string is found in the second string and also first occurrence index of that 
    extracted character in first string is same as that of index of current extracted character then increment 
    the value of counter by 1.
4. Output the value of counter.
'''''
def occurenceM1(s1,s2):
    i=0
    count=0
    if len(s1)<len(s2) or len(s1)==len(s2):
        while (i<len(s1) ):
            for j in s2:
                if s1[i]==j and count<len(s1):
                    count+=1
            i+=1
        return count
    elif len(s1)>len(s2):
        while i<len(s2):
            for j in s1:
                if s2[i]==j and count<len(s2):
                    count+=1
        return count
    else:
        return
ansM1=occurenceM1(str1,str2)
print("The number od matching character in a pair of string in M1:  ",ansM1)