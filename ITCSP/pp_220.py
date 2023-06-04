'''Exercise 220
Instrukcje:
On the basis of Programming Task 03, 
additionally implement the functionality of writting the results to the file.
'''

import re
import sys


def get_text(file_path: str, start_line: int) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text fileS
        start_line: text analysis should start at this specyfic line
    Returns:
        text
    '''
    with open(file_path, 'r') as inFile:
        return ''.join(inFile.readlines()[start_line:])


begin = '''
###############################################
Text analyzer - finds all 5 characters length words
which starts with a vowel and ends with a vowel

'''
print(begin)

try:
    file = input('Enter the text filepath: ')
    # #'PYTHON PROGRAMMING\shakespeare.txt'
    number = int(
        input('Enter the line number from which you want to start analysis: '))
    # #253

    text = get_text(file, number)

    #x = re.findall(r"^[aeiou].*[aeiou]$", text)
    x = re.findall(r"\b[AEIOUYaeiouy]\w{3}[AEIOUYaeiouy]\b", text)

    with open('results_220.txt', mode='w', encoding='utf-8') as file:
        file.write(f'The amount of words is: {len(x)}\n')
        file.write('\n'.join(x))
except FileNotFoundError:
    print('File not found')
except IndexError:
    print('Invalid filename')
except ValueError:
    print('Invalid line number, did you type a number?')
else:
    # print(x)
    # print(f'The amount of words is: {len(x)}')
    print('Results written to results_220.txt')
