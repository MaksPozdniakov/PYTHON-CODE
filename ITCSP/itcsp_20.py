'''
Exercise 20
Modify Exercise 18 concerning prime numbers.
Implement solution based on list object.

'''

prime_numbers = []

prime_count = 10
num = 2
while prime_count > 0:
    for i in range(2, num-1):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
        prime_count -= 1
    num += 1

print(','.join((map(str, prime_numbers))))
