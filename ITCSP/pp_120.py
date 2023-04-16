'''
Exercise 120, file pp_120.py
Write a function that will check if a word/sentence is a palindrome or not.
Use recursive implementation
These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a
'''

"https://www.dictionary.com/e/palindromic-word/"


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    import string
    punct = string.punctuation
    text = text.translate(str.maketrans('', '', punct))
    if remove_space:
        text = text.replace(' ', '')
    return text


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is a palindrome

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    # def ispalindrome(word):
    # return word == word[::-1]

    if len(text) <= 1:
        return False
    if len(text) <= 3 and text[0] == text[-1]:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:len(text)-1])
    else:
        return False


def print_palindrome_check(text: str) -> None:
    '''
    Function prints the message if text is palindrome or not

    Parameters:
        text: any text
    '''
    text = remove_punctuation(text, True)
    text = text.lower()
    print(is_palindrome(text))


print_palindrome_check('Dad')
print_palindrome_check('Evil olive.')
print_palindrome_check('Never odd or even.')
print_palindrome_check('Amore, Roma.')
print_palindrome_check('test')
print_palindrome_check('ad')
print_palindrome_check('a')
