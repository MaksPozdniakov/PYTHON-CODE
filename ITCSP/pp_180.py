'''
Exercise 180, pp_180.py

Modify the exercise 170 - you still print to the terminal the list of the 10  the longest words in the given text, you still  have to implement 
a function get_text(). 
But additionally, text analysis should start at specyfic line. 
Implement the possibility to decide if text should be analysed without or with punctuation and from which line number the analysis should start. Pass these arguments from command line.

On the beginning of the program a message should appear.

e.g. without punctuation removal
    ###############################################
    Text analyzer - finds 10 the longest words
    Do you want to analyse text as it is or you want to remove punctuation before?
    Press 1 if text as it is
    Press 2 if program should firstly remove punctuation
    ###############################################


-->  1
The longest word in the file 'shakespeare.txt' is 'swart-complexioned' with the length of 18 characters

The longest word in the file 'shakespeare.txt' is 'Lieutenant-General' with the length of 18 characters

The longest word in the file 'shakespeare.txt' is 'Lieutenant-General' with the length of 18 characters

use map function together with lambda, readline() method

Exception handling should be implemented.
Implement the possibility of entering "file_path" and "start_line"  from command line
'''


def get_text(file_path: str, start_line: int) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text fileS
        start_line: text analysis should start at this specyfic line
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
