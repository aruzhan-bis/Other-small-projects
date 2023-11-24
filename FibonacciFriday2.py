# Assignment 14 Fibonacci Friday Part 2
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program prints only the first term in the Fibonacci sequence which is greater than 10,000

last_term = 0
current_term = 1
next_term = 1
while next_term <= 10000: # loop until the next term is greater than 10,000
    next_term = last_term + current_term # calculate the next term
    last_term = current_term # last term is updated to current term
    current_term = next_term # current term is updated to next term
print(next_term)