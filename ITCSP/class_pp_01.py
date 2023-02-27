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

# Keyword arguments - to make things more logical? :)


def add_profile(index, ix, iy, area):
    print(
        f'Adding profile (index) with moments of inertia Ix={ix} cm4, Iy={iy} cm4 and area {area} cm2'
    )


add_profile("MC014", 166.9, 23.6, 14.99)
add_profile(index="MC014", ix=166.9, iy=23.6, area=14.99)

# default arguments

print("1_line", "Hello", sep="", end="")
print("1_line", "Hello", sep="")


def add_item(item_name, quantity=1):
    print(f'{quantity} units of {item_name} was added')


add_item("bread")
add_item("apples", 2)

# *ARGS - creates a tuple for a lot of arguments


def print_numbers(*numbers):
    for n in numbers:
        print(n)


def summarize(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print_numbers(1, 2, 3, 4, 5)

print(f'The sum of the numbers is {summarize(1,2,3,4,5)}')

# **KWARGS (xxargs) - creates a dictionary


def add_user(**user: dict) -> None:
    print(type(user))
    print(user)


add_user(id=1, Name="John", Surname="Kowalski", age=25)


def print_user(**user: dict) -> None:
    for key, value in user.items():
        print(f"{key} = {value}")


print_user(id=1, Name="John", Surname="Kowalski", age=25)


users = []


def add_user(**user: dict) -> None:
    users.append(user)


add_user(id=1, Name="John", Surname="Kowalski", age=25)
add_user(id=2, Name="John", Surname="Kowalski", age=26)
print(users)
