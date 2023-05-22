'''
Exercise 190

https://www.w3schools.com/python/python_regex.asp

Using RE find all the 5-characters length

Think about the following Special Sequences
\b
\w
{}


`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.

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
    s_line = int(args[2])
    text = get_text(file, s_line)
    pattern = r"\b\w{5}\b"

    x = re.findall(pattern, text)

except FileNotFoundError:
    print("No such file or directory was found.")
except IndexError:
    print("You didn't enter valid filename.")
else:
    print(x)

    # L1 = re.findall("/\b\w{1,5}\b/", text)
    # # /\b\w{1,5}\b/
