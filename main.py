#Password Generator Project
import random
from random import randint
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = ""
for i in range(0, nr_letters):
  random_number = randint(0, 51)
  password_letters += letters[random_number]

password_numbers = ""
for i in range(0, nr_numbers):
    random_number = randint(0, 9)
    password_numbers += numbers[random_number]

password_symbols = ""
for i in range(0, nr_symbols):
    random_number = randint(0, 8)
    password_symbols += symbols[random_number]

password_total_1 = password_letters + password_numbers + password_symbols
password_total_2 = list(password_total_1)
shuffle(password_total_2)
password_total_3 = "".join(password_total_2)
print(f"Your Password is {password_total_3}")