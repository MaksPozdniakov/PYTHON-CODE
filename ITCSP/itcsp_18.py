'''
Exercise 18
Write a program that prints first 10 primes, separated by a comma.
(Use a while loop and a break statement in your solution.)
INPUT: prime_count = 10
OUTPUT: str. e.g., 2,3,5,7,11,13,17,19,23,29
Hint: what is a prime numer
https://thirdspacelearning.com/blog/what-is-a-prime-number/

First think about how to implement if the number is prime
'''

prime_count = 10
num = 2
while prime_count > 0:
    for i in range(2, num-1):
        if num % i == 0:
            break
    else:
        print(num, end="")
        print(",", end="")
        prime_count -= 1
    num += 1
