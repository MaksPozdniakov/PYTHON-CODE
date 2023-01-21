'''
Exercise 16

Enter any file name together with it's extension.
Check if the entered file name is of type pdf or others.
INPUT: str
Exemplary input
Enter the filname together with it's estension: ...
OUTPUT: str
Exemplary output
Your file has an extension "2s"
Program should implement error handling. In a case that a filename without an extension was entered, the following message should appear:
You entered a filename without an extension, try once more


use:
input()
string slicing
for volunteers/advanced use ternary operator

tests:
file01.docx, myBook.pdf, file02.2s
'''
# enter a filename

# find the index of "." which separates filename and it's extension

# specify the index of the first character of your extension

# write the conditional (if statement), using string slicing, substring your extension and print messages

# for advanced -> use ternary operator

x = input(str("Enter the filename together with its extension: "))

i = x.find(".")


if x:
    print("Your file has an extension:", x[-3:])
else:
    print("You entered a filename without an extension, try once more.")
