'''
Exercise 90, file pp_90.py
Write a program that will check if a word/sentence is a palindrome or not.
Remove punctuations and spaces
Use iterative way (loop) to check if palindrome

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


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is palindrome or not

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    palindrome = False

    import string
    punct = string.punctuation
    text_nopunct = ''
    for character in text:
        if character not in punct:
            text_nopunct += character

    text_nopunct = text_nopunct.replace(" ", "").lower()

    mid = len(text_nopunct)//2

    for i in range(mid):
        palindrome = True
        if text_nopunct[i] != text_nopunct[-i - 1]:
            palindrome = False
            break

    return palindrome


text = input("Enter text to check whether it is a palindrome: ")

palindrome = is_palindrome(text)
print(palindrome)


# solution by teacher.
def is_palindrome(text):
    ''' 
    input: string 
    output: boolean 
    '''
    # your code below
    text = text.replace(' ', '').replace('.', '').replace(',', '').lower()
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    return False
