import re


class TextIO:
    def __init__(self, file_path, start_line=0):
        self.file_path = file_path
        self.start_line = start_line
        self._text = ''

    def get_text(self) -> str:
        if self._text:
            return self._text
        else:
            self.read_from_file()
            return self._text

    def read_from_file(self) -> None:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self._text = ''.join(file.readlines()[self.start_line:])
        except Exception:
            print('There was an error when reading the file.')

    def write_to_file(self, text: str, output_file_path: str, mode: str = 'w') -> None:
        with open(output_file_path, mode) as file:
            try:
                file.write(text)
            except Exception:
                print('There was an error when reading the file.')


start_banner = '''
-----------------------------------------
TextAnalyzer Module v.1.0
-----------------------------------------
'''


class TextAnalyzer:
    def __init__(self, text: str):
        self._text = text
        self._num_sentences = 0
        self._sentences = []

    def set_sentences(self) -> None:
        self._sentences = re.split(r'(?<=[.?!]$)\s+', self._text)

    def set_num_sentences(self) -> None:
        self._num_sentences = len(self._sentences)

    def get_sentences(self) -> list:
        return self._sentences

    def get_num_sentences(self) -> int:
        return self._num_sentences

    def __str__(self):
        return f'TextAnalyzer Module v.1.0\nNumber of Sentences: {self._num_sentences}\nList of Sentences:\n{self._sentences}'
