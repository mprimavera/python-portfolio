# import the random library
import random as rd

# create the lists for letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'
           , 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# prompt the user for the quantity of letters, numbers and symbols they desire
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# create the password variable as an empty list
password_list = []

# append the quantity of letters, symbols, and numbers desired to the password list
for letter in range(nr_letters):
    password_list.append(rd.choice(letters))
for symbol in range(nr_symbols):
    password_list.append(rd.choice(symbols))
for number in range(nr_numbers):
    password_list.append(rd.choice(numbers))

# shuffle the list
rd.shuffle(password_list)

# create a single string for the shuffled password list
password = "".join(password_list)

# print the password to the user
print(f"Your password is: {password}")
