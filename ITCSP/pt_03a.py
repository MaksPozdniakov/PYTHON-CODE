'''
Programming Task 03 (file: pt_03a.py)
Points: 15

https://www.w3schools.com/python/python_regex.asp

On the basis of Exercise 190,
Using RE, in 'shakespeare.txt' file, find and print all the 5-characters length words which starts with a vowel and ends with a vowel.
Additionally, print the amount of these words.
Implement the exception handling
Vowels: 'aeoiuy'
Think about the following Special Sequences
\b
\w
{}

Start your analysis from the line no 253.

`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.
Use input function to enter filepath

Exemplary start 
###############################################
Text analyzer - finds all 5 characters length words
which starts with a vowel and ends with a vowel

Enter the text filepath: PYTHON PROGRAMMING\shakespeare.txt
Enter the line number from which you want to start analysis: 253 

Results:
['use' ...]
The amount of words is 137

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
    with open(file_path, "r") as inFile:
        lines = inFile.readlines()[start_line:]
        return "".join(lines)


text = ""
try:
    args = sys.argv
    file = args[1]
    text = get_text(file)
    vowels = "aeoiuy"
    pattern = f"^{vowels}[\b\w{5}\b]{vowels}$"

    x = re.findall(pattern, text)

except FileNotFoundError:
    print("No such file or directory was found.")
except IndexError:
    print("You didn't enter valid filename.")
else:
    print(f"The amount of words is {x}.")
