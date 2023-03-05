'''
Exercise 01, file pp_01.py
Write a function named fizz_buzz(num) that will return the string 'Fizz' if the num parameter  is divisible by 3,
will return the string 'Buzz' if the num is divisible by '5',
will return the string 'FizzBuzz' if the num is divisible by 3 and 5
will return num for any other number
Function should include docstring
Program should implement entering the number many times  during runtime. Typing "q"  should cause quitting the program.

'''


def fizz_buzz(num) -> str:
    '''
    Function will:
    return the string 'Buzz' if the num is divisible by '5',
    return the string 'FizzBuzz' if the num is divisible by 3 and 5,
    return num for any other number
    '''

    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"{num}")


flag = True

while True:
    num = input("Please enter a number or 'q' to exit: ")
    if num == "q":
        break
    else:
        try:
            int(num)
        except ValueError:
            flag = False
        if flag:
            num = int(num)
            fizz_buzz(num)
        else:
            print("The entered value is not a number, try again.")
            flag = True
