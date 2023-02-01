'''
ITCSP, Final Programming Task, 1LMT, group 01
(30 points)
Let's imagine you are a young entrepreneur. You decided to start a shop. Write a program to handle the assortment of your store. Implement the following functionalities:
adding product, changing the name of product, deleting product, showing all products on the terminal screen.

First, consider what data structure you will use to store your product names.

I see the program-user interaction as follows ( please printout on the terminal as below)

=========================================
Store management software, version 1.0.0
=========================================
Please select the operation you want to perform:
1. Add a product
2. Change the name of the product
3. Remove the product
4. Show all products
5. Exit the program
--> ... 
++++++++++++++

Selecting the operation number should result in the appearance of a message, e.g
--> Enter the name of the product you want to add ...
(Now the user should enter the name of the new product and the program should add this name to the data structure.)
--> Enter the product number you want to rename ...
(The user should now enter the product number and the program should give the option to enter a new name.)
--> Enter the product number you want to remove ...
(The user should now enter the product number, and after that, the program should remove the product.)

Printing to the terminal
Selecting option 4 should result in printing to the terminal the names of all products entered in the previous step along with their indexes (but starting from number 1, not 0).

Selecting number 4 should show all products you have enetered during runtime, e.g.,

My products:
1. Bananas
2. Oranges
3. Apples
4. Figs
5. Strawberries
=====  Finished


Finishing work with the program
Selecting option 5 should result in termination of work with the program

Data structure you use for storing product names should be a variable 'products'

Showing all products operation should be implemented as a function "show_products(products: list) -> None" and invoked if you choose required option

If you have enough time, implement error handling (for volunteers)

PASTE YOUR SOURCE CODE ON TEAMS !!! (ftp_itcsp_01.py)
'''


def show_products(products: list) -> None:
    '''
    Function prints all products

    Parameters : 
        products: enumerated list of products
        eg. 1. Orange
            2. Bananas
    '''
    # here your function code block
    print("My products: ")

    for index, product in enumerate(products, start=1):
        print(f"{index}.{product}")

    print("=====  Finished")

# HERE REST OF THE PROGRAM:


inventory = []

while True:
    print("=========================================")
    print("Store management software, version 1.0.0")
    print("=========================================")
    print("Please select the operation you want to perform:")
    print("1. Add a product")
    print("2. Change the name of the product")
    print("3. Remove the product")
    print("4. Show all products")
    print("5. Exit the program")

    text = input("--> ... ")

    if text == "exit" or text == "5":
        break
    elif text == "1":
        added = input("--> Enter the name of a product you want to add: ")
        inventory.append(added)
    elif text == "2":
        rename_index = int(
            input("--> Enter the number of the product you want to change: "))
        new_name = input("Enter a new name: ")
        inventory[rename_index - 1] = new_name
    elif text == "3":
        remove_index = int(
            input("--> Enter the number of the product you want to remove: "))
        inventory.pop(remove_index - 1)
    elif text == "4":
        show_products(inventory)
    else:
        print("Invalid entry. Please try again.")
