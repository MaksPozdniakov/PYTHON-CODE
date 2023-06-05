'''
Exercise 230 (file pp_230.py)
Create a class that will be responsible for reading text from file and writing text to file

Class data attributes:
filepath: str, file path of the file
start_line: int, the line number from which you start reading the file
_text:str, text that was read from file

Implement class procedural attributes:
def __init__(self, filepath, startline=0):
def get_text(self) -> str:
def read_from_file(self) -> None:
def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:

Exception handling should be implemented

Enter filepath to read from file and startline using input() function
'''


class FileStuff:
    def __init__(self, filepath, startline=0):
        self.filepath = filepath
        self.startline = startline
        self.text = None

    def get_text(self) -> str:
        return self.text

    def read_from_file(self) -> None:
        with open(self.filepath, 'r') as inFile:
            self.text = ''.join(inFile.readlines()[self.startline:])

    def write_to_file(self, text: str, f_path: str, mode: str = 'w') -> None:
        with open(f_path, mode='w', encoding='utf-8') as file:
            file.write(''.join(text))


try:
    file = input('Enter the text filepath: ')
    # #'PYTHON PROGRAMMING\shakespeare.txt'
    number = int(
        input('Enter the line number from which you want to start analysis: '))
    # #253

    shakes = FileStuff(file, number)
    shakes.read_from_file()
    shakes.write_to_file(shakes.get_text(), 'results_230.txt')

except FileNotFoundError:
    print('File not found')
except IndexError:
    print('Invalid filename')
except ValueError:
    print('Invalid line number, did you type a number?')
else:
    print('Results written to results_230.txt')
