import random

# Character sets for the pw
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Asking for user input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# List for the pw
password_list = []

# Take the nr_letters as range, in that range "choose" a random letter and append to the List for the password
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Repeat the same step for symbols
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# Repeat the same step for numbers
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Shuffle up the randomly generated letters, symbols, numbers to be truly random
random.shuffle(password_list)

# Using a for loop, append the items from the List to the string -> converting the List to a string
password = ""
for char in password_list:
    password += char

# Print out the password to the console
print(f"Your password is: {password}")
