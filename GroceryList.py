# Lab Assignment 24 Grocery List
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program creates an interactive program
# That allows the user to add, edit or print grocery lists

grocery_list = []

# Create a loop for continuous program
while True:
    # Print options to choose
    print("\nWelcome to the Generic Grocery List Application!\n")
    print("1) Add an item")
    print("2) Remove an item")
    print("3) Display all items")
    print("4) Clear the list")
    print("5) Exit")

    # Prompt the user to select an option
    choice = input("Select an option: ")

    if choice == '1':
        # Prompt the user to enter the item's name
        item = input("Enter the item's name: ")
        # Add the item to the list
        grocery_list.append(item)
        # Show that the item has been added to the list
        print(f"{item} has been added to the list.\n")

    # If the user chooses to remove an item
    elif choice == '2':
        # Prompt the user to enter the item's name
        item = input("Enter the item's name: ")
        if item in grocery_list:
            # Remove the item from the list
            grocery_list.remove(item)
            # Show that the item has been removed from the list
            print(f"{item} has been removed from the list.\n")
        else:
            # Inform the user that the item is not in the list
            print("Item not found!\n")

    # If the user wants to display all the items in the list
    elif choice == '3':
        # Print each item in the list on a new line
        print("Items in the list:")
        for item in grocery_list:
            print(item)
        print("\n")

    # If the user chooses to clear the list
    elif choice == '4':
        # Ask the user for confirmation before clearing the list
        confirm = input("Are you sure? (Y/N): ")
        if confirm == 'Y':
            grocery_list.clear()
            # Show that the list has been cleared
            print("The list has been cleared.\n")
        else:
            # Show the user that the list was not cleared
            print("The list was not cleared.\n")

    # If the exit option is chosen
    elif choice == '5':
        print("Have a great day!")
        break
    # Invalid input
    else:
        print("Unrecognized input!\n")