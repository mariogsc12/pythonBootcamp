# FINAL PROJECT DAY 8 - CAESAR CIPHER 

"""
--- TODO-1 --- 
- Create a function called encrypt() that takes original_text and shift_amount as 2 inputs

--- TODO-2 ---
- Inside the encrypt function, shift each letter of the original_text forwards in the alphabet by the shift_amout and print the encrypted text

--- TODO-3 ---
- Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message


"""

import string 
import random

# Global variables
alphabet = list(string.ascii_lowercase) # ['a', 'b', 'c', ..., 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number\n"))


# Function definitions (TODO-1 and TODO-2)
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet) # Ensure that index is valid
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")


# TODO-3
encrypt(text,shift)

