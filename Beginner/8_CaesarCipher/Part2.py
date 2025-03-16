# FINAL PROJECT DAY 8 - CAESAR CIPHER 

"""
--- TODO-1 --- 
- Create a function called decrypt() that takes original_text and shift_amount as 2 inputs

--- TODO-2 ---
- Inside the 'decrypt()' function, shift each letter of the original_text backwards in the alphabet by the shift_amout and print the decoded text

--- TODO-3 ---
- Combine the 'encrypt()' and 'decrypt()' functions into a single function called 'caesar()'
- Use the value of the user chosen direction variable to determinate which functionallity to use
- Call the caesar function and pass the three user variables


"""

import string 
import random

# Global variables
alphabet = list(string.ascii_lowercase) # ['a', 'b', 'c', ..., 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
try:
    shift = int(input("Type the shift number\n"))
except ValueError:
    print("ERROR: Please enter a valid integer.")


# Function definitions 
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet) # Ensure that index is valid
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

def decrypt(cipher_text, shift_amount):
    decoded_text = ""

    for letter in cipher_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position = shifted_position % len(alphabet) # Ensure that index is valid
        decoded_text += alphabet[shifted_position]

    print(f"Here is the decoded result: {decoded_text}")

def caesar(original_text, shift_amount, encode_decode):
    output_text = ""
    
    if encode_decode=='encode':
        shift_amount *= 1       # Don't change (addition)
    elif encode_decode == 'decode':
        shift_amount *= -1      # Convert into a subtraction  
    else:
        print("ERROR-Invalid direction format")
        return # Exit the function


    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet) # Ensure that index is valid
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_decode} result: {output_text}")

caesar(text,shift,direction)

