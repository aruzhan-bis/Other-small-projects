# Assignment8LatteFactor
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program prints out the weekly, monthly, and yearly spending on coffee

import sys # Importing sys for sys exit
Coffee_Price = float(input("How much money do you usually spend on coffee per visit of a coffee shop: "))
if Coffee_Price <= 0: # Adding a condition to be greater than 0
    print("Invalid number. Try again")
    sys.exit() # Program stops running
Coffee_Freq = float(input("How often per week do you visit a coffee shop: "))
if Coffee_Freq <= 0:
    print("Invalid number. Try again")
    sys.exit()
weekly_spending = Coffee_Price * Coffee_Freq # Counting weekly spending
montly_spending = weekly_spending * 4 # Monthly spending
yearly_spending = weekly_spending * 52 # Yearly spending
print("\n") # A new line
print("Your expenses are:")
print ("Weekly", "Monthly", "Yearly")
# The answer is printed with 2 digits after a decimal and with a dollar sign
print ("$%.2f" % weekly_spending, "$%1.2f" % montly_spending, "$%.2f" % yearly_spending)



