'''
Exercise 31 (modify exercise 15)
Write a program that counts vowels in a string
The program should implement the possibility for the user to enter any word.

INPUT: str
OUTPUT: str

DEFINE YOUR OWN FUNCTION:
    count_vowels(text:str)->int
    remember about docstring

Finally
use input() function to enter text
invoke count_vowels function
use f-string formatting together with print function

vowels = 'aeiou'

The exemplary input:
Enter a word ... 

The exemplary output in  terminal should be:
You have 6 vowels in the word "Appalachicola"
Tests:
VOWELS -> 2 vowels
vowels -> 2 vowels
Appalachicola -> 6 vowels

'''


def count_vowels(word: str):
    '''
    Function counts vowels in a string.

    Parameters:

    Returns:

    '''
    vowels = 'aeiou'
    VowelCount = 0

    for letter in word:
        if letter in vowels:
            VowelCount += 1

    return VowelCount


x = input("Enter a word: ")

print(f"You have {count_vowels(x)} vowels in the word {x}")
