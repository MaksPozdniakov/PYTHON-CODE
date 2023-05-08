import sys
import re
# inFile = open("testfile.txt", "r", encoding="utf-8")
# stuff = inFile.read()  # read from it
# inFile.close()  # we need to close it after we opened it
# print(stuff)

# inFile = open("testfile.txt", "r", encoding="utf-8")
# stuff = inFile.read()  # read from it
# inFile.close()  # we need to close it after we opened it
# lines = stuff.print("\n")  # split into lines #??
# # print lines and lenghts
# for line in lines:
#     print(f"{line}, : {len(line)} characters")  # list of all lines

# inFile = open("testfile.txt", "r", encoding="utf-8")
# stuff = inFile.readlies()  # read from it
# inFile.close()  # we need to close it after we opened it
# # print lines and lenghts
# for line in lines:
#     print(f"{line}, : {len(line)} characters")  # list of all lines

# this one we don't neeed to close, it closes auto with the end of block of code
# with open("testfile.txt", "r") as inFile:
#     lines = inFile.readlines()
#     # print lines and lenghts
#     for line in lines:
#         print(f"{line}, : {len(line)} characters")

# with open("testfile.txt", "r") as inFile:
#     stuff = inFile.read()
# lines = stuff.split("\n")
# # print lines and lenghts
# for line in lines:
#     print(f"{line}, : {len(line)} characters")

# with open("testfile.txt", "r", encoding="utf-8") as inFile:
#     stuff = inFile.read().splitlines()
# # print lines and lenghts
#     for line in lines:
#         print(f"{line}, : {len(line)} characters")

# with open("testfile.txt", "w", encoding="utf-8") as outFile:
#     # write to it
#     outFile.write("some text!\n")
#     outFile.write("edgar is the king!\n")

################################################################
# try:
#     a = int(input("Enter the integer number \"a\": ... "))
#     b = int(input("Enter the integer number \"b\": ... "))
#     num = a / b
#     print(f"The result of division {a} / {b} = {num}")
#     print("Writing the result to the file...")
#     file = open("testfile.txt", mode="a", encoding="utf-8")
#     file.write(f"\n The result of division {a} / {b} = {num}")
# except ValueError:
#     print("You didn't enter valid number!")
# except ZeroDivisionError:
#     print("You can't divide by 0!")
# except FileNotFoundError:
#     print("File doesn't exist!")
# except:
#     print("Something went wrong!")  # for all other errors
# else:
#     print("File is closed.")
# # useful for clean-upp code that should be run no mater what else hapened (e.g. close a file)
# finally:
#     file.close()

################################################################
# try:
#     a = int(input("Enter the integer number \"a\": ... "))
#     b = int(input("Enter the integer number \"b\": ... "))
#     num = a / b
#     print(f"The result of division {a} / {b} = {num}")
#     print("Writing the result to the file...")
#     with open("testfile.txt", "a", encoding="utf-8") as file:
#         file.write(f"\n The result of division {a} / {b} = {num}")
# except ValueError:
#     print("You didn't enter valid number!")
# except ZeroDivisionError:
#     print("You can't divide by 0!")
# except FileNotFoundError:
#     print("File doesn't exist!")
# except:
#     print("Something went wrong!")  # for all other errors

# REGULAR EXPRESSIONS
# RE METHODS
# if re.search("ab", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

# if re.search("a..b", sys.argv[1]):
#     print("a match")
# else:
#     print("no match")

if re.search("^abc", sys.argv[1]):  # start with abc
    print("a match")
else:
    print("no match")

if re.search("[a-d]", sys.argv[1]):
    print("a match")
else:
    print("no match")
