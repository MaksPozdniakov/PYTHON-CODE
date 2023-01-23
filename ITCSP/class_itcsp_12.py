# FORMATTING STRING
name = "Jess"
print(f'My name is {name} :)')
#
var1 = 2
var2 = 5
print(f'var1 multiplied by var2 equals: {var1*var2}')

print('f-string')
name = "Jess"
print('My name is', name, ":)")
print(f'My name is {name} :)')

print('var1 multiplied by var2 equals:', var1*var2)
print(f'var1 multiplied by var2 equals: {var1*var2}')

# FUNCTIONS
# functions are not run until they are "called" or "invoked" in a program


def is_even(i):
    '''
    Functions checks if the number is even or odd.

    Parameters:
    i(int): positive int tunmber to be checked

    returns:
    (bool): True if i is even, otherwise False
    '''

    return i % 2 == 0


print(is_even(3))  # invoking function with parameter 3
print(is_even.__doc__)  # print doc string
print(str.strip.__doc__)


def greet():
    "Function sends out greetings"
    print("Hello")
    print("How are you?")


number = 2
is_even(number)
greet()


def send_greetings(name):
    '''
    Function prints the greeting

    Parameters:
        name:name of the person
    '''
    print(f'Hello {name}')


send_greetings("Jess")
print(send_greetings.__doc__)


def send_greetings(name: str) -> None:
    '''
    Function prints the greeting

    Parameters:
        name:name of the person
    '''
    print(f'Hello {name}')


send_greetings("Jess")
print(send_greetings.__doc__)


def send_greetings(name):
    '''
    Function prints the greeting

    Parameters:
        name:name of the person
    '''
    return f'Hello {name}'


def send_self_presentation(name, surname, birth_year, current_year):

'''
Function returns specific presentation of the person...

Parameters:
    name (str): name of the person
    surname (str): surname of the person
    birth_year (int): person's year of the birth
    current_year (int): current year
Returns:
    (str): presentation
    e.g. Hello, my name is Jessica Jones and I am 25 years old
'''
age = current_year - birth_year
return f'Hello, my name is {name}, {surname} and I am {age} years old'

print(send_self_presentation("Jessica", "Jones", 1998, 2023))
print(send_self_presentation.__doc__)
