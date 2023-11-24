# Assignment 20 Copycat
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program creates a copy of itself
# And copies only the code without any comments

import os
# Open the file with the necessary program
this_file = open("Copycat.py", 'r')
# Open a new file to copy there the code
new_file = open('copyycat.py', 'w')
# Print the code without the comments into a new file
for line in this_file:
    if not line.startswith('#'):
        new_file.write(line)
# Close both files
this_file.close()
new_file.close()
os.system('python copycat.py')