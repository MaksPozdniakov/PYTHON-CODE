# s = "Hi there"
# s.upper()
# s.lower()

# counter = 0
# while counter < 6:
#     print(counter)
#     counter += 1

# # print("Infinite Loop")
# # counter = 0
# # while counter < 6:
#     # print(counter)

# type(range(5))
# print(type)

# for i in range(5):  # dont need to initialize i separately
#     print(i)

# for i in range(3, 7):
#     print(i)

# for i in range(3, 20, 2):
#     print(i)

# for i in "Appalachicola":
#     print(i)

# mysum = 0
# for i in range(0, 210):
#     mysum += 1
# print("The sum of numbers 0-20 is", mysum)

vowels = "aeiou"
vowelCount = 0  # variable to accumulate count
word = "Appalachicola"
for letter in word:  # go letter by letter
    if letter in vowels:  # vowel?
        vowelCount += 1  # add 1
print("Number of vowels is", vowelCount)

# # while True:
# #     # infinite looop
# #     text = input("Enter any text...")
# #     if text == "exit":
# #         break  # the way to stop

# mylist = [1, 2, 3, 7, 5]
# mylist = [[1, 2, 3], ["Warsaw"]]
# l1 = []

# first_list = [2, "cat", 5.0, True]
# first_list[0]
# print(first_list)

# text = "hello"
# print(id(text))
# print(hex(id(text)))

# # text[0] = "M"  #strings are immutable, lists are mutable

# L = [1, 2, 9, 5]
# for i in L:
#     print(i)

# L = [1, 2, 9, 5]
# sum = 0
# for i in L:
#     sum += 1
# print(sum)

# L = [1, 2, 5, 7]
# L.append(10)  # ADDING ITEMS TO THE LIST
# print(L)

# L1 = [2, 6, 3]
# L2 = [8, 7, 3]
# L3 = L1 + L2
# print(L3)
# L1.extend(L2)

# L = ["apple", "banana", "banana"]
# L.remove("banana")
# print(L)
# L.pop()
# print(L)

# # L.clear - empties the list
