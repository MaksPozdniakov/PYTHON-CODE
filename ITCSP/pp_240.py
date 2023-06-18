'''
Exercise 240, file pp_240.py

Using your konowledge from previous exercises

Your task is, using python:
0. Entering text_file_path, db_file_path, start_line 
1. Create a MyDB01.db (everything using python) Create a table Alice_tb with columns Id integer primary key, Line text, Length integer
2. Read text data from alice.txt (use your TextIO class from your module)
3. Analize your text:
- lines_length data structure variable
- save your data in lines_length variable
- write your data to DB
3. Read first 10 data rows from your database and print to the terminal

In order to do the exercise, implement the following functions:
def get_lines_length(text: str) -> list[tuple[str, int]]:
def write_alice_tb(db_file_path: str, data: list[tuple[str, int]]) -> None:
def read_alice_tb(db_file_path: str) -> list[tuple[int, str, int]]:
def print_alice_tb(data: list[tuple[int, str, int]], number: int) -> None:

'''

import sqlite3


class TextIO():
    def __init__(self, filepath, startline=0):
        self.filepath = filepath

        try:
            self.startline = int(startline)
        except:
            print("Wrong line number.")

        self.text = None

    def get_text(self):
        if self.text:
            return self.text
        else:
            print("No text was read, try reading text first.")

    def read_from_file(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as in_file:
                self.text = "\n".join(
                    in_file.read().splitlines()[self.startline:])
        except:
            print("Wrong path provided, file was not read.")

    def write_to_file(self, text: str, f_path: str, mode: str = "w"):
        try:
            with open(f_path, mode=mode, encoding="utf-8") as in_file:
                in_file.write(text)
            print("Your text was written to the file.")
        except:
            print("Failed to write to the file.")


def get_lines_length(text: str) -> list[tuple[str, int]]:
    lines_list = text.splitlines()
    lines_length_list = list(map(lambda line: (line, len(line)), lines_list))
    return lines_length_list


def write_alice_tb(db_file_path: str, data: list[tuple[str, int]]) -> None:
    with sqlite3.connect(db_file_path) as conn:
        command = "INSERT INTO Alice_tb (Line, Length) VALUES (?, ?)"
        for l in data:
            conn.execute(command, l)


def read_alice_tb(db_file_path: str) -> list[tuple[int, str, int]]:
    with sqlite3.connect(db_file_path) as conn:
        command = "SELECT * FROM Alice_tb"
        cursor = conn.execute(command)
        return cursor.fetchall()


def print_alice_tb(data: list[tuple[int, str, int]], number: int) -> None:
    print(data[: number])


# 0.
text_file_path = input("Enter the text file path: ")
db_file_path = input("Enter the db file path: ")
start_line = input(
    "From which line in the text do you want to start the analysis: ")

# 1.
with sqlite3.connect(db_file_path) as conn:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS Alice_tb ('Id' INTEGER PRIMARY KEY, 'Line' TEXT, 'Length' TEXT)"
    )

# 2.
text = TextIO(text_file_path, start_line)
text.read_from_file()

# 3.
lines_data = get_lines_length(text.get_text())
write_alice_tb(db_file_path, lines_data)
lines_data_from_db = read_alice_tb(db_file_path)
print_alice_tb(lines_data_from_db, 10)
