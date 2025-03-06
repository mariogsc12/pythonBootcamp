# Simple examples with conditionals

height = int(input("What is your height (in cm)?"))

# Very careful with the indentation
if height>120:
    print("You can ride.\n")
    age = int(input("What is your age?"))
    if age<=12:
        price = 5
    elif age>12 and age<=18 :
        price = 7
    else:
        price=12
    print(f"The price is {price}$")
else: 
    print("Sorry, you can't ride")
