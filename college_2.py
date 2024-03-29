# -*- coding: utf-8 -*-
"""college 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gPED6HdVznPCX1QzMt9UZlNEvLKRObQI
"""

"""
1. Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS 
"""
# inp = input()
inp = 'rhinoceros'
outp = ''.join(c.upper() if i%2 else c for i, c in enumerate(inp))
print(outp)

"""
2. Write a program that asks the user to enter their name in lowercase and then capitalizes the
first letter of each word of their name. 
"""
str = input("Enter your name:")
print("" , str.title())

"""3. Write a program to check whether the string is Symmetrical or Palindrome."""

# palin function to check whether string palindrome or not
def palin(string): 

  # declare and initialize with the starting and ending indexes
  st = 0
  end = len(string)-1
  f = 0

  # loop comparing letters moving from start to end and from end to start
  while(st<end): 

    if (string[st]== string[end]): 
      
      st += 1
      end -= 1
      
    else: 
      f = 1
      break; 
  # if loop with f as condition    
  if f == 0: 
    print("The entered string is palindrome") 
  else: 
    print("The entered string is not palindrome") 
    
# symm function to check string symmetrical or not
def symm(string): 
  
  l = len(string) 
  flag = 0
  
  # to check length of string even or odd 
  # to calculate middle value accordingly
  if l%2 == 0: 
    mid = l//2 # for even length
  else: 
    mid = l//2 + 1 # for odd length
    
  s1 = 0  # starting for first portion of string
  s2 = mid # starting for rest portion of string after middle value
  
  while(s1 < mid and s2 < l): 
    
    if (string[s1] == string[s2]): # comparing from start of both portions 
                                  # of given string
      s1 = s1 + 1
      s2 = s2 + 1
    else: 
      flag = 1
      break
  

  if flag == 0: 
    print("The entered string is symmetrical") 
  else: 
    print("The entered string is not symmetrical") 
    
# Main code 
string = input("Enter the string: ")
palin(string) 
symm(string)

'''4. Write a program to capitalize the first and last character of each word in a string.'''

s =input("enter the string:")
s =s.title()

a =""
for i in s.split():
   a +=i[:-1]+i[-1].upper()+ " "
   print(a[:-1])

'''5. Write a program to count the Number of matching characters in a pair of string'''

str1=input("enter 1st string: ")
str2=input("enter 2nd string: ")
c, j = 0, 0
for i in str1:
    if str2.find(i)>= 0 and j == str1.find(i):
      c += 1
      j += 1
print ('no. of matching characters are : ', c)

''' 6. Write a program which accepts full name of a user and print the output in the following format. 
Full name can have any number of components(FN, MN, LN etc)
Input: Akhil Kumar Das
Output : A.K. Das
'''


name = str(input("Enter Your Name : "))
list = []
list = name.split()
temp = ""
for i in range(len(list)-1):
  n=list[i]
  temp += n[0].upper() + "."
temp += " " + list[-1].title()
print("Your Short Name Is :",temp)