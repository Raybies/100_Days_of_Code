# Caeser Cipher - refactor

# Shift Alphabet by a set number, i.e. A-B-C-D shifted 3 = A = D, B = E, etc.
# Define list of alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # double the alphabet index to allow for shifting around 

# User inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1 # makes decode negative
    for letter in start_text: # runs through each letter in argument plain_text and does the steps indented below
        position = alphabet.index(letter) # Find the position of the letter in the list alphabet
        new_position = position + shift_amount # Shift the index number by the value of shift_amount to get new alphabet position and thus new letter
        end_text += alphabet[new_position] # Set that new alphabet letter to variable new_letter and concatenate the values
    print(f"The {direction}d text is \033[1m{end_text}.")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)