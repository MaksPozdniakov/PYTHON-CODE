'''
Exercise 60 (file "pp_60.py")

Write a program that will print to display a list of tuples that will consist of the most frequent character in the sentence / sentences and it's frequency, 
sorted in a descending order.
In order to complete the task
1. define a function
def most_freq_character(sentence):
    

    return sorted_characters_freq

2. As a data structure use a dictionary
3. In your analize, don't use spaces
4. Use loop in counting characters

For testing purposes you can  use 
sentence = "The robbed that smiles, steals something from the thief."
Expected result:
[('t', 7), ('e', 7), ('h', 5), ('s', 5), ('o', 3), ('m', 3), ('i', 3), ('r', 2), ('b', 2), ('a', 2), ('l', 2), ('f', 2), ('d', 1), (',', 1), ('n', 1), ('g', 1), ('.', 1)]
'''


def most_freq_character(sentence):
    '''
    Function returns list of characters together with its length

    Parameters:
        sentence: any text
    Returns:
        List of tuples
    '''
