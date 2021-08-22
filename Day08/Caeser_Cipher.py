# Caeser Cipher

# Shift Alphabet by a set number, i.e. A-B-C-D shifted 3 = A = D, B = E, etc.
# Define list of alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # double the alphabet index to allow for shifting around 

# User inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text: # runs through each letter in argument plain_text and does the steps indented below
        position = alphabet.index(letter) # Find the position of the letter in the list alphabet
        new_position = position + shift_amount # Shift the index number by the value of shift_amount to get new alphabet position and thus new letter
        new_letter = alphabet[new_position] # Set that new alphabet letter to variable new_letter
        cipher_text += new_letter # Run through each letter in plain_text and concatenate the new_letter values to each other to make new variable cipher_text
    print(f"The encoded message is \033[1m{cipher_text}.") # Tab out and print the output message including the final cipher_text value
        

def decrypt(cipher_text, shift_amount):
    original_text = ""
    for letter in cipher_text: # runs through each letter in argument plain_text and does the steps indented below
        position = alphabet.index(letter) # Find the position of the letter in the list alphabet
        new_position = position + (0 - shift_amount) # Shift the index number by the inverse value of shift_amount to get new alphabet position and thus the original letter
        original_letter = alphabet[new_position] # Set that new alphabet letter to variable new_letter
        original_text += original_letter # Run through each letter in plain_text and concatenate the original_letter values to each other to make new variable cipher_text
    print(f"The decoded message is \033[1m{original_text}.") # Tab out and print the output message including the final cipher_text value

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift) # call the function 
else:
    decrypt(cipher_text=text, shift_amount=shift) # call the function 

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 