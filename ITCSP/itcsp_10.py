'''
Let's imagine you live in a virtual country.
Write a program (here only the condition) that will manage airport fast check-in

Condition :
you will pass if you are from USA or EU, you have no more than 1000 dollars but no less than 100 dollars, your luggage weight is less equal than 20 kg
Test it for different inputs
eg., 
country="PL"
money = 500
luggage_weight = 20
# output = False
#
country="USA"
money = 500
luggage_weight = 20
# output = True
#
country="EU"
money = 2000
luggage_weight = 20
# output = False
#
country="EU"
money = 500
luggage_weight = 30
# output = False
#
'''
# INPUT
country = "EU"
money = 2000
luggage_weight = 20

##################################
# Here write the condition
condition = (country == "EU" or country ==
             "USA") and luggage_weight <= 20 and 100 <= money <= 1000

##################################
# OUTPUT
print(condition)
