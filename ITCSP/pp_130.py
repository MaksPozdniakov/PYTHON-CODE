'''
Exercise 130, file: pp_130.py

Write a program that will summarize the digits of the given number

In this aim implement the function
get_sum(num:int)->int:

Use recursive implementation
Remind yourself: n%10, n//10
'''


def get_sum(n: int) -> int:
    '''
    The function takes an integer as input and returns the sum of its digits.

    Parameters:
        n: any positive int number
    Returns:
        the sum of the number digits
    '''

    sum = 0
    while (n != 0):
        print(f'sum =  {sum}, n = {n}')  # !!!! <33
        sum = sum + int(n % 10)
        n = n//10

    return sum


# # Driver code
# if __name__ == "__main__":
#     n = 687

#     # Function call
#     print(get_sum(n))


MyNumber = int(
    input("Enter a positive integer to calculate the sum of its digits: "))
print(get_sum(MyNumber))
