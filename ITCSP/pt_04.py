'''
Programming Task 04 (file: pt_04a.py, texta.py)
15 points, 35 min.

1. Create a file "texta.py", it is your new module now
3. Create a file "pt_04a.py"
4. Copy / paste the class definition "TextIO" from  your homework exercise "pp_230.py" to the file "texta.py"
5. Inside "texta.py", create a class "TextAnalyser"
TextAnalyser specyfication:
5.1 Data attributes:
_text # your text to analyze
_number_of_sentences
_list_of_sentences

5.2 Instance methods to implement
 def __init__(self, text: str):
 def set_list_of_sentences(self) -> None:
 def set_number_of_sentences(self) -> None:
 def get_list_of_sentences(self) -> list:
 def get_number_of_sentences(self) -> int:  
 def __str__(sef):
 
Implement complete classes (data attributes and methods) inside texta.py --> now it becomes your module you can import to pt_04 file
TextIO # you can copy from your homework
TextAnalyser # to implement from the beginning

Treat a sentence as a collection of characters ending with ".?!"
Use re.split() method

Using shakespeare.txt, print the results to the terminal

Exemplary result:
        -----------------------------------------
        TextAnalyser Module v.1.0
        -----------------------------------------


Enter the text filepath: PYTHON PROGRAMMING\shakespeare.txt
Enter the line number from which you want to start analysis: 252
Text File Analysis - PYTHON PROGRAMMING\shakespeare.txt
List of sentences:
1. 1
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee
2. 2
  When forty winters shall besiege thy brow,
  And dig deep trenches in thy beauty's field,
  Thy youth's proud livery so gazed on now,
  Will be a tattered weed of small worth held:
  Then being asked, where all thy beauty lies,
  Where all the treasure of thy lusty days;
  To say within thine own deep sunken eyes,
  Were an all-eating shame, and thriftless praise

'''
import texta

print(texta.start_banner)

file_path = input('Enter the text file path: ')
start_line = int(
    input('Enter the line number from which you want to start the analysis: '))

text_io = texta.TextIO(file_path, start_line)
text_io.read_from_file()

text_analyzer = texta.TextAnalyzer(text_io.get_text())
text_analyzer.set_sentences()

print(f'Text File Analysis - {file_path}')
print('List of Sentences:')
for i, sentence in enumerate(text_analyzer.get_sentences()[:10], 1):
    print(f'{i}. {sentence}')
