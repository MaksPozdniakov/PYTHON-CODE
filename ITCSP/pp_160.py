'''
Exercise 160, pp_160.py

Task is the same as in exercise 40 - finding the longest word in the given text, but additionally you have to implement a function get_text(). 
The new function should return the text from a file, 
Write a program with a function called map_longest() that takes a text as a parameter and returns the longest word contained in that text and its length - tuple.

Result of a program should be a message 
e.g. after punctuation removal
The longest word in the file 'shakespeare.txt' is 'internethartvmdcsouiucedu' with the length of 25 characters

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters

use map function together with lambda

Exception handling should be implemented.
Implement the possibility of entering file_path from command line
'''


import sys


def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
    Returns:
        text
    '''
    with open(file_path, "r") as inFile:
        return inFile.read()


def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    import string
    punct = string.punctuation
    WordCleared = ""
    for character in word:
        if character not in punct:
            WordCleared += character
    return WordCleared


def map_longest(text: str) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the logest word and it's length

    '''
    L1 = text.split()
    L2 = list(map(lambda item: (item, len(item)), L1))
    L2.sort(key=lambda item: item[1], reverse=True)
    return L2[0]


text = ""
try:
    args = sys.argv
    file = args[1]
    text = get_text(file)
    text_wp = remove_punctuation(text)
    t = map_longest(text_wp)

except FileNotFoundError:
    print("No such file or directory was found.")
except IndexError:
    print("You didn't enter valid filename.")
else:
    print(
        f"The longest word in the file {file} is {t[0]} with the length of characters of {t[1]} characters.")
