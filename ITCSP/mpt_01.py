'''
Midterm Programming Task, file mpt_01.py, 25 points
Double Six Dice Game
On the basis of: https://www.101computing.net/double-six-dice-game/

-- do not register in order to check the solution !!!!

In this challenge, your task is to create a 2-player dice game with the following rules:
- Each player has a pair of dice
- The first player rolls a pair of dice, and keeps rolling the dice again and again, until they roll a double six.
- It is then the turn of the the second player. They too will roll the dice and keep doing so until they roll a double six.
- The winner of the game is the user who rolled a double six in the smaller number of attempts.
- The game ends on a draw if both players used the same number of attempts to roll a double six.

In order to solve the task you have to implement 2 functions as below:

def get_roll_counter() -> int
def print_game_results(name1: str, counter1: int, name2: str, counter2: int) -> None

and use random number generator : random.randint(start,stop) function.

Details you can find on
https://www.w3schools.com/python/ref_random_randint.asp
https://www.geeksforgeeks.org/python-randint-function/

Exemplary result:

__________________________
|                          |
|   Double Six Dice Game   |
|__________________________|


Enter the name of player 1 ... John
Enter the name of player 2 ... Mark
==========
Player Mark won, with 25 double dice rolls!!!
Player John had, 175 attempts

'''


def get_roll_counter() -> int:
    '''
    Function rolls a pair of dice, and keeps rolling the dice again and again, until they roll a double six

    Returns:
        number of rolling attempts
    '''
    # pass

    import random

    roll = 0
    while True:
        roll += 1
        dice1: int = random.randint(1, 6)
        dice2: int = random.randint(1, 6)
        if dice1 == 6 and dice2 == 6:
            break
    return roll


def print_game_results(player1: str, counter1: int, player2: str, counter2: int) -> None:
    '''
    Function prints the results of 'Double Six Dice Game' for 2 players

    Parameters:
        name1: name of the first player
        counter1: number of attempts of the first player until get DoubleSix    
        name2: name of the first player
        counter2: number of attempts of the first player until get DoubleSix
    Returns:
        None
    '''
    # pass

    print("--------------")

    if counter1 < counter2:
        print(
            f"{player2} has won with {counter2} double dice rolls! Congratulations!!!")
        print(f"{player1} is second with {counter1} attempts.")
    elif counter1 > counter2:
        print(
            f"{player1} has won with {counter1} double dice rolls! Congratulations!!!")
        print(f"{player2} is second with {counter2} attempts.")
    elif counter1 == counter2:
        print(
            f"It's tie! Both players used {counter1} attempts. Congratulations!")


print("___________________________")
print("|                          |")
print("|   Double Six Dice Game   |")
print("|__________________________|")

player1 = str(input("Provide your name..."))
player2 = str(input("Provide your name..."))

counter1 = get_roll_counter()
counter2 = get_roll_counter()
print_game_results(player1, counter1, player2, counter2)
