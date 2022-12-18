'''
Exercise 09
Write a program (modify the old one) that asks the user for their first name, year of birth and the current year, then calculates 
and lists the information about name and age in the terminal.
Sample workflow:
Enter your name: 
Ann 
Enter your birth Year:
2001 
Enter the current Year:
2021

Sample result
Ann, you are 30 years old.

Use "new line": \n
'''
name = input("Enter your name: ...")
birth_year = int(input("Enter your birth Year: ..."))
curr_year = int(input("Enter the current Year: ..."))

print(name, ",", "you are", curr_year - birth_year, "years old")
