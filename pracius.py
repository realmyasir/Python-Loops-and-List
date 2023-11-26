# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:10:55 2023

@author: Web 123
"""
# fact=1
# user = int(input('Enter a Factorial Digit'))
# for user in range(1,user+1):
#     fact*=user
# print(f'You enter Digit {user} factorial is ',fact)    

# user = int(input('Enter a Factorial Digit: '))
# fact = 1

# for i in range(1, user + 1):
#     fact *= i

# print(f'The factorial of {user} is {fact}')



# user = input('Enter Your Name And Reverse Your name')

# rev= reversed(user)
# for char in rev:
#     print(char,end=' ')

# user = input('Enter Your Name: ')
# reversed_name = reversed(user)
# print('Reversed Name:', end=' ')
# for char in reversed_name:
#     print(char, end='')


# user = int(input('Enter a Verbaliy Number >>'))
# if user%2==0:
#     print('You Enter A even Number ')
# else:
#     print('You Enter a Odd Number')
    

# n=20
# for i in range(1,n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,'Fizz Buzz')
#     elif i % 3 == 0:
#         print(i ,'Fizz')
#     elif i % 5 == 0:
#         print(i ,'Buzz')
#     else:
#         print(i)        
        
# n=10
# for i in range(1,n+1):
#     if i % 5 == 0:
#        print(i ,'Buzz')
#     elif i % 3 == 0:
#         print(i ,'Fizz')
#     elif  i % 3 == 0 and i % 5 == 0:
#         print(i,'FizzBuzz')
#     else:
#         print(i)     

# print(list(range(11)))
# print(list(range(0,41,4)))

# print(type(range(20)))

# question No 1

n1,n2=0,0
while n1 < 0 or n2 < 0 or n1 > 100 or n2 > 100 or n1 == n1:
    print('Number Must be  Different between 1 - 100')
    n1=int(input('Enter the First Number 1 - 100>>'))
    n2=int(input('enter the Second Number 1 - 100>>'))

if n1 < n2:
    for i in range(n1,n2+1):
        print(i,end=' ')
else:
    for i in range(n2,n1+1):
        print(i,end=' ')
            




















































