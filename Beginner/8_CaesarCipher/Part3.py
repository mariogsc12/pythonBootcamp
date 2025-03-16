# FINAL PROJECT DAY 8 - CAESAR CIPHER 

"""
--- TODO-1 --- 
- Import and print the logo (optional)

--- TODO-2 ---
- What happens if the user enters a number/symbol/space that is not in the alphabet list?
- Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

--- TODO-3 ---
- Can you figure out a way to restart the cipher program?

"""

import string 
import random

# Global variables
alphabet = list(string.ascii_lowercase) # ['a', 'b', 'c', ..., 'z']


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
        if letter not in alphabet:
            output_text += letter # Keep the space/symbol/number
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabet) # Ensure that index is valid
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_decode} result: {output_text}")

end_condition = "yes"

while end_condition != "no":
    # User inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Type the shift number\n"))
    except ValueError:
        print("ERROR: Please enter a valid integer.")
    
    # Caesar logic
    caesar(text,shift,direction)

    # Repeat or finish the loop
    end_condition=input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if end_condition != 'yes' and end_condition !='no':
        print("ERROR-Invalid format")

print("""
\n\n=====================================
THANK YOU FOR USING THE CAESAR CIPHER!
=====================================\n\n
""")

