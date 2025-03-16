# DAY 10 FINAL PROJECT - CALCULATOR

import art
art.tprint("CALC")


def add(num1, num2):
    return num1+num2

def substract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def calculator(num1,num2,operation):
    if operation=='+':
        return add(num1,num2)
    elif operation=='-':
        return substract(num1,num2)
    elif operation=='*':
        return multiply(num1,num2)
    elif operation=='/':
        return divide(num1,num2)
    else:
        print("ERROR - Invalid operation")
    
user_action = 'n'
first_number = 0
next_number = 0
result = 0
while user_action != 'e':
    if user_action == 'n':
        first_number = int(input("What is the first number?: "))
    else:
        first_number = result
    
    operation = ""
    while operation !='+' and operation !='-' and operation !='*' and operation !='/':
        operation = input("Pick an operation (+,-,*,/): ")
        if operation !='+' and operation !='-' and operation !='*' and operation !='/':
            print("ERROR - Please introduce a valid operation")

    next_number = int(input("What is the next number?: "))
    result = calculator(first_number,next_number,operation)
    print(f"{first_number} + {next_number} = {result}")
    user_action = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'e' to exit: ")
