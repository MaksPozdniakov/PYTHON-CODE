'''
Exercise 21
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), use lists

'''
x = input(str("Please enter your string: "))


while x:
    print(x[::-1])
    break

while x == "exit":
    print("exit")
    break
