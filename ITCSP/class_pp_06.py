# ternary operator
# exceptions
# error that terminates the exectuion of a program

# exception vs syntax error

# print(0/0)
# types of exceptions

# index error
# numbers = [1, 2, 3]
# print(numbers[3])
# print("Here I am")

# TypeError
# l = [1, 7, 4]
# print(int(l))

# TypeError
# print("a"/4)

# NameError
# print(a)  # never declared

# ValueError
# num = int(input("Enter the integer number: "))  # input a
# print(f"Our number is {num}")

# IOError -> file not found error
# file = open("ztest.py")
# print("File is open")
# file.close()

# handling exceptions

# handling indexerror
try:
    numbers = [1, 2, 3]
    print(numbers[3])
    print("Here I am not")
except IndexError:
    print("Wrong index!!!")
print("Program continues")

# handling ValueError

try:
    num = int(input("Enter integer number: "))
    print(f'Our number is {num}')
except ValueError:
    print("You didn't enter a valid number!")

# Value error (a, 1, 0)

try:
    a = int(input("Enter integer number 'a': "))
    b = int(input("Enter integer number 'b': "))
    num = a/b
    print(f'the result of division {a} / {b} = {num}')
except ValueError:
    print("You didn't enter a valid number!")

# ZeroDivisionError

try:
    a = int(input("Enter integer number 'a': "))
    b = int(input("Enter integer number 'b': "))
    num = a/b
    print(f'the result of division {a} / {b} = {num}')
except ValueError:
    print("You didn't enter a valid number!")
except ZeroDivisionError:
    print("You cant't divide by 0")

# raising exceptions


def divide(a: int, b: int) -> float:
    '''
    input: a,b: positive int
    output: float
    '''
    if a < 0 or b < 0:
        # instead of "input("Enter positive int")"
        raise ValueError("You didn't enter a valid number!")
    return a/b


try:
    a = int(input("Enter integer number 'a': "))
    b = int(input("Enter integer number 'b': "))
    num = a/b
    print(f'the result of division {a} / {b} = {divide(a,b)}')
except ValueError as error:
    print(error)
except ZeroDivisionError:
    print("You cant't divide by 0")


##########

try:
    a = int(input("Enter integer number 'a': "))
    b = int(input("Enter integer number 'b': "))
    assert a >= 0 and b >= 0  # program only works for these values
    print(f'Division a / b = {a/b}')
except AssertionError:
    print("Numbers are not positive integers")
except ZeroDivisionError:
    print("You cant't divide by 0")
except:
    print("Enter the correct integer")
else:
    print("Code without exceptions.", end=" ")
    print(f"Multiplying a x b = {a*b}.", end=" ")
    print("It is OK")
finally:
    print("The try...except block is finished. Always. Useful for clearing up resources that are used in the try block")
