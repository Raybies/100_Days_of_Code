# Caeser Cipher - refactor

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
# Shift Alphabet by a set number, i.e. A-B-C-D shifted 3 = A = D, B = E, etc.
# Define list of alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = " "
    if cipher_direction == "decode":
        shift_amount *= -1 # makes decode negative
    for char in start_text: # runs through each letter in argument plain_text and does the steps indented below
        if char in alphabet: # for letters
            position = alphabet.index(char) # Find the position of the letter in the list alphabet
            new_position = position + shift_amount # Shift the index number by the value of shift_amount to get new alphabet position and thus new letter
            end_text += alphabet[new_position] # Set that new alphabet letter to variable new_letter and concatenate the values
        else: # if not a letter in list alphabet
            end_text += char
    print(f"The {direction}d text is \033[1m{end_text}\033[0m.")

print(logo)

should_continue = True
while should_continue:
    # User inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 # to correct for large numbers outside of the 26 letters range 0-25 [the index]
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input("Do you want to encode/decode another message? (Y/N)? \n").upper()
    if restart == "N":
        should_continue = False 
        print("Goodbye.")





