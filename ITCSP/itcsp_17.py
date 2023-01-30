'''
Exercise 17
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH'
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), don't use lists (only strings) 

'''

# x = input(str("Please enter your string: "))

# while x == "exit":
#     break

# print(x.reverse(x))


def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1


input_str = input("Please write your string: ")

while input_str == "exit":
    break

if __name__ == "__main__":
    print(reverse_while_loop(input_str))
