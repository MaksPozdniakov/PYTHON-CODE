'''
Exercise 14

Enter any file name together with it's extension e.g., file01.docx, myBook.pdf
Check if the entered file name is of type pdf or others.
INPUT: str
"Enter the filname"
OUTPUT:
"Your file is of type pdf"
"Your file is not of type pdf"

use:
input()
string slicing
ternary operator

'''

x = input("Enter the filename: ")

i = x.find(".")

if x[i+1:] == "pdf":
    print("Your file is of type pdf")
else:
    print("Your file is not of type pdf")
