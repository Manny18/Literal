#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1. Create a List (using list method and []) and print this list.
list_1=[1,2,3]
list_2=["a","b","c"]
list=[]
list.append(list_1)
list.append(list_2)
print(list)


# In[5]:


#2.Access all the list element using loop.
cities = ['Bergen','Kolkata', 'Seoul', 'Paris', 'Kyoto', 'Istanbul']

for city in cities:
    print(city)


# In[8]:


#3. Change a list element.
list = [ 10, 20, 30, 40, 50, 60]
list[0]=11
list[1]=21
list[2]=31
list[3]=41
list[4]=51
list[5]=61
print("New list")
print(list)


# In[14]:


#4. Sum all the numbers in a list.(without using any function).
list_1 = [1,2,3,4,5,6,7,8,9]
def listsum(numlist):
    total = 0
    i = 0
    while i < len(list_1):
        total = total + list_1[i]
        i = i + 1
    return total
totalsum = listsum(list_1);
print('Sum of List: ', totalsum)


# In[15]:


#5.Calculate min and maximum element in a list. (don’t use inbuild function).
lis = [2, 4,1, 5,3,8,9]   
min_1 = lis[0]    
max_1 = lis[0]   
for i in lis: 
    if i > max_1: 
        max_1 = i 
 
    if i < min_1: 
        min_1 = i 
print("min = ", min_1, " max = ", max_1) 
 


# In[18]:


#6. Python Program to Convert Decimal to Binary, Octal and Hexadecimal. 
decimal =143 
print(bin(decimal))
print(oct(decimal))
print(hex(decimal))


# In[19]:


#7.Write a Python program to reverses a string if it's length is a multiple of 4
def reverse_string(str1):
    if len(str1) % 4 == 0:
        return ''.join(reversed(str1))
    return str1

print(reverse_string('SUBHADIP'))


# In[24]:


#8.Write a Python program to count occurrences of a substring in a string
str1 = "we few, we happy few, we band of brothers." 
print(str1.count("we"))


# In[26]:


#9. Write a Python program to test whether a passed letter is a vowel or consonant.
l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
    print("the alphabet is vowel")
else:
    print("the alphabet is consonant") 


# In[1]:


#10. Find out the longest and smallest word in the input string
def smallest_largest_words(str1):
    word = "";
    all_words = [];
    str1 = str1 + " ";
    for i in range(0, len(str1)):
        if(str1[i] != ' '):
            word = word + str1[i];  
        else:
            all_words.append(word);  
            word = "";  
          
    small = large = all_words[0]; 


# In[5]:


#11. Find out the longest and smallest word in the input string
str_1=input("Enter the string ")
word=str_1.split()
largest=small=word[0]
for i in range(0, len(word)):
    if len(largest)<len(word[i]):
        largest=word[i]
    if len(small)>len(word[i]):
        small=word[i]
print("the smallest word in the string is",small)
print("the largest word in the string is",largest)


# In[9]:


#12.How to find the characters at an odd position in string input by Use
str_1= input('Enter a string: ')
odd_chars = []

for i in range(len(str_1)):
    if i % 2 == 0:
        even_chars.append(str_1[i])
    else:
        odd_chars.append(str_1[i])

print('Odd characters is',odd_chars)


# In[11]:


#13.How to replace all occurrence of sub-string in string
str_1 = "My name is Tom Cruise"
s1 = "Tom Cruise"
s2 = "Subhadip Das"
str_1 = str_1.replace(s1, s2)
print(str_1)


# In[18]:


#14.How to find the number of matching characters in two string
str_1=input("Enter first string:")
str_2=input("Enter second string:")
a=(set(str_1)&set(str_2))
print("The common letters are:",len(a))


# In[19]:


#15..How to convert a string in list.
str_1=input("Enter the string ")
word=str_1.split()
print(str_1)
print(word)


# In[20]:


#16. How to convert all string elements of list to int.
str_1=["1","2","3"]
str_1=list(map(int,str_1))
print(str_1)


# In[24]:


#17.Count Total numbers of upper case and lower case characters in input string
Str_1="My Name Is Subhadip Das"
lower=0
upper=0
for i in Str_1:
      if(i.islower()):
            lower+=1
else:
            upper+=1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)


# In[29]:


#18. Program to sort a string in Python.
str_1 =list(input("Enter the string : "))
sortedString=''.join(sorted(str_1)) 
print("Sorted String:", sortedString)


# In[30]:


#19. .How to print input string in upper case and lower case
str_input=input("Entering my favourite Sport")
print("Favourite Sport",str_input.upper())
print("Favourite Sport",str_input.lower())


# In[31]:


#20. Write a program to make a new string with all the consonents deleted from the string "Hello, have a good day"
a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = "Hello, have a good day"
for i in b:
    if i not in a:
    b = b[:b.index(i)]+b[b.index(i)+1:]
print(b)


# In[6]:


#21..Python Program to Convert Bytes to a String
data = b"Subhadip Das"
print('\nInput')
print(data)
print(type(data))
output = data.decode()
print('\nOutput:')
print(output)
print(type(output))


# In[17]:


#22. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500,2701):

    if i%7==0 and i%5==0:

        print(i,end=" ")


# In[18]:


#23.Write a Python program that accepts a word from the user and reverse it.
def reverse_string(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1     
str = "Racecar"       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) 


# In[20]:


#24. .Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (11, 22, 33, 44, 55, 66, 77, 88, 99)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[21]:


#25. Python program to interchange first and last elements in a list.
def swapList(sl):
    n = len(sl)
    temp = sl[0]
    sl[0] = sl[n - 1]
    sl[n - 1] = temp  
    return sl
      
l = [1,2,3,4,5,6,7,8]

print(l)
print("Swapped list: ",swapList(l))


# In[22]:


#26. Python program to swap two elements in a list
Cities = ['Bergen','Kolkata', 'Seoul', 'Paris', 'Kyoto', 'Istanbul']

print("List of cities before swap:")
print(Cities)
Cities[0], Cities[2] = Cities[2], Cities[0]

print("\nList of Cities after swap:")
print(Cities)


# In[23]:


#27.Python | Ways to find length of list
lst = ['Bergen','Kolkata', 'Seoul', 'Paris', 'Kyoto', 'Istanbul']
size = len(lst)
print(size)


# In[25]:


#28.Check if element exists in list in Python
list = ['Bergen','Kolkata', 'Seoul', 'Paris', 'Kyoto', 'Istanbul']

if 'Bergen' in list:
    print (" 'Bergen' is found in the list")
else:
    print (" 'Bergen' is not found in the list")
    


# In[27]:


#29. .Different ways to clear a list in Python
list_1=[1,2,3,4]
print("list before clear",list_1)
list_1.clear()
print("\nlist after clear",list_1)


# In[28]:


#30. Reversing a List in Python
list_1=[1,2,3,4]
print("list before reversing:",list_1)
list_1.reverse()
print("list after reversing:",list_1)


# In[29]:


#31. Python program to find sum of elements in list
num_list = [1,2,3,4,5,6,7,8,9]
numsum = sum(num_list)
print('Sum of List: ',numsum)


# In[31]:


#32.Python | Multiply all numbers in the list
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1, 2, 3]
print(multiplyList(list1))


# In[33]:


#33. Python program to find smallest number in a list
a=[3,545,575,4325,57524,354643]
res=min(a)
print("the smallest number in the list:",res)


# In[34]:


#34. .Python program to find largest number in a list
a=[3,545,575,4325,57524,354643]
res=max(a)
print("the largest number in the list:",res)


# In[41]:


#35. Python program to find second largest number in a list
a=[3,545,575,4325,57524,354643]
b=set(a)
b.remove(max(b))
res=max(b)
print("the second largest number in a list",res )


# In[43]:


# 36.Python program to find N largest elements from a list
list_1=[1,3,5,57,67,-24,-35,342,12,356]
n=3
list_1.sort()
print(list_1[-n:])


# In[46]:


#37..Python program to print even numbers in a list
def evens(nums_list):
   
   for num in nums_list:
        if num%2 == 0:
            print(num, end=' ')

evens([2,35,324,24,743,324,45,67])


# In[54]:


#38. Python program to print odd numbers in a List
def odds(nums_list):
   
   for num in nums_list:
        if num%2!= 0:
            print(num, end=' ')
odds([2,35,324,24,743,324,45,67])


# In[8]:


#39.Python program to print all even numbers in a range
first_number = int(input("Enter the first_number of range:"))
last_number = int(input("Enter the second_number of range:"))
for evens_num in range(first_number, last_number + 1):
    if evens_num % 2 == 0:
        print(evens_num,end=" ")


# In[7]:


#40. Python program to print all odd numbers in a range
first_number = int(input("Enter the first_number of range:"))
last_number = int(input("Enter the last_number of range:"))
for odds_num in range(first_number, last_number + 1):
    if odds_num % 2 != 0:
        print(odds_num,end=" ")


# In[10]:


#41. Python program to print positive numbers in a list
positive_number=[1,45,-78,-95,47,21,-78,65,23]
for i in positive_number:
    if i>=0:
        print(i,' ' ,end='')


# In[12]:


#42. Python program to print negative numbers in a list
negative_number=[1,45,-78,-95,47,21,-78,65,23]
for i in negative_number:
    if i<0:
        print(i,' ' ,end='')


# In[14]:


#43. Python program to print all positive numbers in a range
first_number = int(input("Enter the first_number of range:"))
last_number = int(input("Enter the last_number of range:"))
for positive_num in range(first_number, last_number + 1):
    if positive_num>= 0:
        print(positive_num,end=" ")


# In[16]:


#44. python program to print all negative numbers in a range
first_number = int(input("Enter the first_number of range:"))
last_number = int(input("Enter the last_number of range:"))
for Negative_num in range(first_number, last_number + 1):
    if Negative_num < 0:
        print(Negative_num,end=" ")


# In[21]:


#45.Remove multiple elements from a list in Python
list_1=[1,2,3,4,5,6,7,8,9]
for elements in list_1:
    if elements%2!=0:
        list_1.remove(elements)
print("New list",list_1)


# In[23]:


#46. Python – Remove empty List from List
list_1=[1,[],3,[],5,[],7,[],9,[]]
list_2=list(filter(None,list_1))
print(list_2)


# In[25]:


#47.Python | Cloning or Copying a list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
copy_list = my_list
print('Old List: ', my_list)
print('New List:', copy_list)


# In[27]:


#48. Python | Count occurrences of an element in a list
list_1 = ["a", "ab","a", "abc", "a", "abcd", "a", "abcde", "a", "abcdef"]
print(list_1.count("a"))


# In[28]:


#49. Python | Remove empty tuples from a list
list_1=[(1),(),(3),(),(5),(),(7),(),(9),()]
list_2=tuple(filter(None,list_1))
print(list_2)


# In[29]:


#50.Python | Program to print duplicates from a list of integers
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
uniqueList = []
duplicateList = []
 
for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
print(duplicateList)


# In[33]:


#51. Python | Program to print duplicates from a list of integers
list_1 = [1,2,3,4,5,6,7,8,9,1,5,6,7,8,9];     
print("Duplicate elements in given array: ");        
for i in range(0, len(list_1)):    
    for j in range(i+1, len(list_1)):    
        if(list_1[i] == list_1[j]):    
            print(list_1[j]);    


# In[36]:


#52.Python | Sum of number digits in List 
list_1 = [11,22,33,44,55,66,77,88,99]
print("The list is : ")
print(list_1)
result_1 = []
for elem in list_1:
   sum_1 = 0
   for digit in str(elem):
      sum_1+= int(digit)
   result_1.append(sum_1)
print ("The result after adding the digits is : " )
print(result_1)


# In[38]:


#53.Break a list into chunks of size N in Python
str_1=input("Enter the string ")
word=str_1.split()
print(word)


# In[41]:


#54.Python program to sort values of first list based on second list
def sort_list(list1, list2):
    zip_list = zip(list2, list1)
    x = [i for _, i in sorted(zip_list)]
    return x
   
list1 = ['v', 'i', 'b', 'g', 'y', 'o', 'r']
list2 = [0, 2, 1, 1, 2, 0, 1]
print("Sorted list", sort_list(list1, list2))


# In[42]:


#55. Remove empty List from List
list_1=[1,[],3,[],5,[],7,[],9,[]]
list_2=list(filter(None,list_1))
print(list_2)


# In[43]:


#56.Python – Convert List to List of dictionaries
l1=[1,2,3,4]
l2=['a','b','c','d']
d1=zip(l1,l2)
print (d1)
print (dict(d1))


# In[44]:


#57. Python – Convert Lists of List to Dictionary
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
print("The original list is : " + str(test_list))
res = dict()
for sub in test_list:
    res[tuple(sub[:2])] = tuple(sub[2:])
print("The dict: " + str(res)) 


# In[47]:


#58. Python | Uncommon elements in Lists of List
list1 = [ ["a, b"], ["c, d"], ["g, f"] ]
list2 = [ ["c, d"], ["e, f"], ["a, b"] ]
print ("The original list 1 : ",(list1))
print ("The original list 2 : ",(list2))
res_list = []
for i in list1:
    if i not in list2:
        res_list.append(i)
for i in list2:
    if i not in list1:
        res_list.append(i)
print ("The uncommon of two lists is : " + str(res_list))


# In[50]:


#59..Python Program to count unique values inside a list
list_1 = ['Bergen','Kolkata', 'Seoul', 'Paris', 'Kyoto', 'Istanbul','Bergen','Kolkatao', 'Seouly', 'Kyotoi' 'Istanbulk']
num_values = len(set(list_1))
print(num_values)


# In[53]:


#60.Python – List product excluding duplicates
a = [1,2,3,4,5,9,9,4,7,1,8,8,7,6,5,4,1,5,2]
print ("Original list : " + str(a))
b=list(set(a))
p=1
for i in b:
    p*=i
print ("Duplication removal list product : " + str(p))

