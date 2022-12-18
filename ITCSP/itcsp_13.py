'''
Exercise 13
Write a program, your task is to enter 3 positive integers x, y, z, calculate and print the least number among them
Use input() function and conditionals.
INPUT: int
OUTPUT: int
'''

x = int(input("Enter the first positive integer: "))
y = int(input("Enter the second positive integer: "))
z = int(input("Enter the third positive integer: "))

if x <= y and x <= z:
    print(x)

elif y <= x and y <= z:
    print(y)

elif z <= x and z <= y:
    print(z)
