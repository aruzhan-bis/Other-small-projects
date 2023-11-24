# Assignment6BaselProblem
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# The program asks for the sum of the all of the numbers'(1-10000) reciprocals, squared and multiplies it by 6 and gives a sqrt

import math
result_1 = 0 # Setting the variable equal to zero
for i in range (1, 10001): # Ending the loop with 10001 because 10000 in the loop calculates reciprocal for 9999
    result_1 += 1/(i**2) # Adding a value to an existing variable and assigning the new value back to the same variable
result_2 = result_1 * 6 # Multiplying the result by 6
result_3 = math.sqrt(result_2) # Getting the square root
print(result_3) # getting the result
# The result is 3.1414971639472147 = it is Pi