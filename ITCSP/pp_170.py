'''
Exercise 170, pp_170.py

Modify the exercise 160 - print to the terminal the list of the 10  the longest words in the given text,  you still have to implement 
a function get_text() to get text from file. 

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters
The longest word in the file 'shakespeare.txt' is '726002026compuservecom' with the length of 22 characters

use map function together with lambda

Exception handling should be implemented.

Implement the possibility of entering file_path from command line
'''


def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
    Returns:
        text
    '''


def remove_punctuation(word: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces.
    '''


def map_longest(text: str) -> list[tuple[str, int]]:
    '''
    Function returns the list of tuples containing the words and it's length

    Parameters:
        text: any text

    Returns:
        list of tuples containing the words and it's length

    '''


def print_word_length_list(word_l: list[tuple[str, int]], number: int) -> None:
    '''
    Function prints the list of tuples. Each tuple consists of word and its length

    Parameters:
        word_l: list of tuples (word, length)
        number: the amount of words to be printed
    '''
