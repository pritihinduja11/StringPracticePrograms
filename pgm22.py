#PGM 22 Ways in python program to replace duplicate occurence in a string

'''''
Sometimes, while working with Python strings, we can have problem in which we need to perform the replace of a word. 
This is quite common task and has been discussed many times. But sometimes, the requirement is to replace occurrence of 
only duplicate, i.e from second occurrence. This has applications in many domains. Let’s discuss certain ways in which 
this task can be performed. 
Example:
INPUT : Gfg is best . Gfg also has Classes now. Classes help understand better . 
OUTPUT: Gfg is best . It also has Classes now. They help understand better .
'''''
str1=input("enter a string:  ")
#Method 1 = Using split() + enumerate() + loop
'''''
The combination of above functions can be used to perform this task. In this, we separate the words using split. In this, 
we memoize the first occurrence in set and check if the value is saved before and then is replaced is already occurred. 
'''''
def duplicateM1(s1):
    # initializing replace mapping
    repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }
    # Replace duplicate Occurrence in String
    # Using split() + enumerate() + loop
    s11=s1.split(' ')
    res=set()
    for idx,ele in enumerate(s11):
        if ele in repl_dict:
            if ele in res:#if already once occured we have to replace secon occurence
                s11[idx]=repl_dict[ele]
            else:
                res.add(ele)
    res=' '.join(s1)
    return res
ansM1=duplicateM1(str1)
print("The string after replacing duplicates inM1: ",end="---->  ")
print(ansM1)