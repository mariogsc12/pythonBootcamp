# DAY 5 FINAL PROJECT - PASSWORD GENERATOR

import random

# Inputs
letters = ['a','b','c','d','e','f']
numbers = ['0','1','2','3','4','5']
symbols = ['!','#','?','%','&','(']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""
status = False
for i in range(0,(nr_letters+nr_symbols+nr_numbers)):
    while status != True:
        type = random.randint(1,3)            # Refering to the character type
        if type==1 and nr_letters!=0:         # Insert letter
            password += random.choice(letters)
            nr_letters -= 1
            status = True
        elif type == 2 and nr_numbers!=0:     # Insert number
            password += random.choice(numbers)
            nr_numbers -= 1
            status = True
        elif type == 3 and nr_symbols!=0:     # Insert symbol
            password += random.choice(symbols)
            nr_symbols -= 1
            status = True
    
    status = False

print("Your password is: " + password)
        
