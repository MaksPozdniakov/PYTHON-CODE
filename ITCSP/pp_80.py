'''
Exercise 80, file "pp_80.py"
The text is given:
shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'
Write a program that will find and print to the terminal the longest word in the text.
In order to achieve it, implement the function that will delete all '.', ',', get the list of all words,  
use dictionary comprehension to get word:length pairs and use sorted() functio.

Expected result:
The longest word is 'trenches' with the length 8 characters.

'''
import string


def get_longest_word(text: str) -> tuple[str, int]:
    '''
    Function returns the longest word together with its length

    Parameters:
        text: any text
    Returns:

    Exemplary result:
    ('trenches',8)
    '''

#     shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautysfield, ....'
#     words = shakespeare.replace(',', '').replace('.', '').split()
#     word_length = {word: len(word) for word in words}
#     sorted_word_length = sorted(
#         word_length.items(), key=lambda item: item[1], reverse=True)
#     print(sorted_word_length)
#     print(dict(sorted_word_length))
#     return sorted_word_length


# print(
#     f"The longest word is '{word}' with the length {sorted_word_length} characters.")

    text = text.replace('.', '').replace(',', '')
    word_list = text.split()
    word_tups = [(word.lower(), len(word)) for word in word_list]
    return sorted(word_tups, key=lambda word: word[1], reverse=True)


shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'
print(get_longest_word(shakespeare))
