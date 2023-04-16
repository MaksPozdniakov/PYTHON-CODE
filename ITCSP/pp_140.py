sum = 3000
counter = 0

try:
    result: sum / counter
except ZeroDivisionError:
    print("You can't divide by 0!")
