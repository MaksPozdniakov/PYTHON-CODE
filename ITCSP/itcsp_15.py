'''
Exercise 15
Write a program that counts vowels in a string
The program should implement the possibility for the user to enter any word.

INPUT: str
OUTPUT: str

Use input() function
vowels = 'aeiou'

The exemplary input:
Enter a word ... 

The exemplary output in  terminal should be:
You have 6 vowels in a word "Appalachicola"
Tests:
VOWELS -> 2 vowels
vowels -> 2 vowels
Appalachicola -> 6 vowels

'''

x = input(str("Enter a word: "))

vowels = 'aeiou'
VowelsCount = 0
for letter in x:
    if letter in vowels:
        VowelsCount += 1
print("You have", VowelsCount, "vowels in a word", x)
