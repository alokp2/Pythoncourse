# # Module -2 Fundamentals of python

'''1. Write a Python program to check if a number is positive, negative or
zero?'''

n = int(input("Enter a number:"))

if (n < 0):
    print(n, "is negative")
elif (n == 0):
    print("n is zero")
else:
    print(n, "is positive")

"""
2.Write a Python program to get the Factorial number of given number.
 """
factors = 1

if (n == 0):
    print("The factorial O is 1")
elif (n < 1):
    print("The factorial does not exist")
else:
    for i in range(1, n + 1):
        factors = factors * i
print("The Factorial of", n, "=", factors)

# 5. What is the purpose continue statement in python?

"""
The purpose of continue statement in python is to skip the current condition or loop and move to next one."""

'''6.Write python program that swap two number with temp variable and without temp variable.'''

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

temp= a
a = b
b =temp
print("a=",a,"b=",b)

#Without the temp
A = int(input("Enter value of A: "))
B = int(input("Enter value of B: "))
A,B=B,A
print("A=",A,"B=",B)

'''7.Write a Python program to find whether a given number is even or odd,
print out an appropriate message to the user.'''

num=int(input("Enter a num:"))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")

'''8.Write a Python program to test whether a passed letter is a vowel or
not.'''
letter=input("Enter a letter:")
if(letter=='A'or letter== 'a' or letter =='E'or letter== 'e' or letter=='I'or letter== 'i'
        or letter =='O' or letter== 'o'
        or letter=="U" or letter== 'u' ):
    print(letter,"is a vowel")
else:
    print(letter,"is not a vowel")



'''9. Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero'''

num1=int(input("Enter value of num1:"))

num2=int(input("Enter value of num2:"))

num3=int(input("Enter value of num3:"))


if(num1==num2):
    sum=0
    print(sum)

elif(num2==num3):
   sum=0
   print(sum)
elif(num1 == num3):
   sum = 0
   print(sum)
else:
    sum=num1+num2+num3
    print("The sum of three numbers are: ",sum)

'''10.Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5. '''

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

if(a==b or(a+b==5)or(a-b==5)):
 print("True")

else:
    print("The numbers do not equal or their sum or difference are not 5.")

'''
11.Write a python program to sum of the first n positive integers. 
'''
nums =int(input("Enter a value of nums:"))
sum=nums*(nums+1)/2
print(int(sum))

'''
12.Write a Python program to calculate the length of a string.
'''
str=input("Enter a string:")
print(len(str))

'''13.Write a Python program to count the number of characters (character
frequency) in a string '''
s=input("Enter a characters:")
count=0
for c in s:
     print(c,end="")
     count=count+1
print("\nTotal count of characters:",count)

'''14.What are negative indexes and why are they used?
Negative indexes  is used to begin the slicing from the end of the string. They are used in reversing the order
of the string.'''

'''15.Write a Python program to count occurrences of a substring in a string.'''
str1 = "THis is  python"
print("Total count of substring=",str1.count("h"))


'''16.Write a Python program to count the occurrences of each word in a
given sentence '''
'''I do not know how to do this one '''

'''17.Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. '''

x = 'abc'
b = 'efg'

a=(x[:2]+b[:2]) # abef
b= (b[:2]+x[:2]) #efab
#After swap
z =a
a=b
b=z
print("a:",a,"b:",b)

'''Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''

str4 = input("Enter a string:")
totallength=len(str4)
if totallength>=3:
    if(str4[-3:])=='ing':
        str4=str4+'ly'
    else:
        str4 = str4+'ing'

