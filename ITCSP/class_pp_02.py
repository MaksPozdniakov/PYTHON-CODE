# # variable scope - local and global
# # local - inside a function, belongs to it. global - outside, can be accessible from anywhere

# # def my_func():
# #     message = "a"

# # print(message)

# # global

# message = "a"


# def my_func():
#     print(message)


# my_func()

# # ----------------

# message = "a"


# def my_func():
#     message = "b"
#     print(message)


# my_func()
# print(message)

# # ----------------

# # list unpacking
# colors = ["red", "green", "blue"]
# var1 = colors[0]
# var2 = colors[1]
# var3 = colors[2]
# print(var1)

# colors = ["red", "green", "blue"]
# var1, var2, var3 = colors
# print(var1)
# print(var2)
# print(var3)

# # error
# # numbers = [1, 2, 3, 4, 5, 3, 24, 2, 4, 55]
# # first_num, sec_num = numbers
# # print(first_num)
# # print(sec_num)
# print("--------------------")

# numbers = [1, 2, 3, 4, 5, 3, 24, 2, 4, 55]
# # asterisk(*) only in definition, not in printing
# first_num, sec_num, *others = numbers
# print(first_num)
# print(others)

# numbers = [1, 2, 3, 4, 5, 3, 24, 2, 4, 55]
# # asterisk(*) only in definition, not in printing
# first_num, *others, last_num = numbers  # mozna tez pr_last_num - przedostatni
# print(others)
# print(last_num)
# print(numbers[-1])  # same result

# print("-------------------")

# # list sorting
# L1 = [5, 3, 5, 2, 7, 8]  # sort ascending, mutates list
# L1.sort()
# print(L1)
# print("-------------------")
# # 2 sort ascending
# L1 = [5, 3, 5, 2, 7, 8]
# L2 = sorted(L1)
# print(L1)  # mutated
# print(L2)  # return value of sorted
# print("-------------------")
# # 3, sort descending + mutate
# L1 = [5, 3, 5, 2, 7, 8]
# L1.sort(reverse=True)
# print(L1)
# print("-------------------")
# # 4 sort descending
# L1 = [5, 3, 5, 2, 7, 8]
# L2 = sorted(L1, reverse=True)
# print(L1)
# print(L2)
# print("--------------------")
# # NEW SORTING
# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("ChocolateWhite", 17),
#     ("Cakes", 19)
# ]

# print(L1)
# L1.sort(reverse=True)
# print(L1)
# print("--------------------")

# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate dark", 15),
#     ("ChocolateWhite", 17),
#     ("Cakes", 19)
# ]


# def sort_product(item):
#     return item[1]


# L1.sort(key=sort_product)
# print(L1)
# print("--------------------")


# def sort_product(item):
#     return item[1]


# L1.sort(key=sort_product, reverse=True)
# print(L1)
# print("--------------------")

# # lambda function
# # anonymous function -> no name one line function

# L1 = [
#     ("Bread", 10),
#     ("Butter", 20),
#     ("Chocolate Dark", 15),
#     ("Chocolate White", 17),
#     ("Cakes", 19)
# ]


# def sort_product(item):
#     return item[1]


# L1.sort(key=lambda item: item[1])
# print(L1)
# print("--------------------")

# # map function

# # map(func, *iterables) -> returns map object
# # func -> lambda expression or pointer to a function which will be executed on each element of the *iterables

# # help(map)

L1 = [
    ("Bread", 10),
    ("Butter", 20),
    ("Chocolate dark", 15),
    ("ChocolateWhite", 17),
    ("Cakes", 19)
]

# # 1
# prices = []
# for l in L1:
#     prices.append(l[1])
# print(prices)  # standard way

# # transorming the list (returns map object) -> only prices

# # 2


# def get_item_1(item):
#     return item[1]


# L2 = list(map(get_item_1, L1))
# print(L2)

# # 3
# L2 = list(map(lambda item: item[1], L1))
# print(L2)
# print("--------------------")

# # increase prices for 20%
L2 = list(map(lambda item: (item[0], item[1]*1.2), L1))
print(L2)
print("--------------------")
# map sprawia, ze funkcja dziala na wszystkie argumenty, a lambda sprawia, ze parametry i argumenty sa wszystkie razem, bezpieczne, rodzinka
