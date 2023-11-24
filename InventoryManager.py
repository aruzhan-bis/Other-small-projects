# Lab Assignment 26 Inventory Manager
# Aruzhan Bissenbay (aruzhanbissenbay@mail.adelphi.edu)
# This program creates an inventory where a store manager can store product information
# That includes its quantity in stock and price

print("Welcome to the Inventory Program!")
# Create an empty dictionary to store the inventory
inventory = {}

# Function to add or edit a product in the inventory
def add_product():
    # Prompt the user for the product name, quantity, and price
    name = input("Enter product name: ")
    quantity = input("Enter quantity in stock: ")
    price = input("Enter price per unit in $: ")
    # Check that the quantity is a positive integer or zero
    if not quantity.isdigit() or int(quantity) < 0:
        print("Invalid quantity, product not added.")
    else:
        # Add the product to the inventory with the quantity and price as values
        inventory[name] = [int(quantity), float(price)]
        print(f"{name} added to inventory.")

# Function to find a product in the inventory
def find_product():
    # Prompt the user for the product name
    name = input("Enter product name: ")
    if name in inventory:
        # Print the product name, quantity, and price
        print(f"{name}: {inventory[name][0]} in stock at ${inventory[name][1]} each.")
    else:
        print("Product not found.")

# Function to remove a product from the inventory
def remove_product():
    # Prompt the user for the product name
    name = input("Enter product name: ")
    if name in inventory:
        # Delete the product from the inventory
        del inventory[name]
        print(f"{name} removed from inventory.")
    else:
        print("Product not found.")

# Function to display all products in the inventory
def display_inventory():
    # Print a table with the product name, quantity, and price
    print("{:<20}{:<10}{:<10}".format("Product", "Quantity", "Price in $"))
    print("-"*40)
    for name, item in inventory.items():
        print("{:<20}{:<10}{:<10.2f}".format(name, item[0], item[1]))

# Create a loop
while True:
    # Print a menu of options and prompt the user for a choice
    print("\n1. Add/Edit a product")
    print("2. Find a product")
    print("3. Remove a product")
    print("4. Display the inventory")
    print("5. Quit")
    choice = input("Enter choice: ")
    # Call the appropriate function based on the user's choice
    if choice == "1":
        add_product()
    elif choice == "2":
        find_product()
    elif choice == "3":
        remove_product()
    elif choice == "4":
        display_inventory()
    elif choice == "5":
        # Exit the program if the user chooses to quit
        break
    else:
        print("Invalid choice. Try again.")