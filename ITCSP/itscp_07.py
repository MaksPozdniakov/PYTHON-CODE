'''
Exercise 07
Create a string made of the first, middle and last character and print it to the terminal

Expected results
text = 'abcdefg'  # expected result: adg
text = 'abcdef'  # expected result adf

Hints:
Use string indexing to get the character present at the given index
Get the index of the middle character by dividing string length by 2
Function that returns string length:
l= len(text)

'''

# INPUT
text = 'abcdefg'  # expected result: adg
text1 = 'abcdef'  # expected result adf
textcut1 = text1[0] + text1[3] + text1[5]
textcut = text[0:7:3]
print(textcut)
print(textcut1)
