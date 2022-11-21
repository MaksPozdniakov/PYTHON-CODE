i = 5
j = 7
k = i > j
print(k)

# truth table
print('and operator')
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print('negation operator')
print(not True)
print(not False)

expression_01 = 2 > 1
expression_02 = 5 > 6

print("The results")
print(expression_01)
print(expression_02)

'''
Exercise 06
Write a program that calculates a „Delta” for the quadratic equation  as below. 
y = 3x2 - 4x + 1

The formula for Delta is as following:
y = ax2  + bx + c 
Delta = b2 – 4ac

hint: first you have to declare 3 variables: a, b, c

Expected result, print to terminal: 
"Delta equals: 4"
'''
a = 3
b = 4
c = 1
Delta = (b*2) - (4*a*c)
print("Delta equals:", abs(Delta))
