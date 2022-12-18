'''
Exercise 12
Write a program:
After you will enter an integer number, called x:
If a number is divisible by 2 and divisible by 3, print "Divisible by 2 and 3".
If a number is divisible by 2 and not by 3, print "Divisible by 2 and not by 3"
If a number is divisible by 3 and not by 2, print "Divisible by 3 and not by 2"
If a number is not divisible by 2 and not by 3, print "Not divisible by 2, not divisible by 3"
Use modulo division
Do the tests
'''
x = int(input("Enter the integer number:"))

if x % 2 == 0 and x % 3 == 0:
    print("Divisible by 2 and 3")

elif x % 2 == 0 and x % 3 != 0:
    print("Divisible by 2 and not by 3")

elif x % 3 == 0 and x % 2 != 0:
    print("Divisible by 3 and not by 2")

elif x % 3 != 0 and x % 2 != 0:
    print("Not divisible by 2, not divisible by 3")
