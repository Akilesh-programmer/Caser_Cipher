# Importing logo from art.py file
from art import logo

# List with all the alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Creating the function named caesar
def caesar(start_text, shift_amount, cipher_direction):

    # Creating a variable to store the final output
    end_text = ""

    # Checking if the user want to decode
    if cipher_direction == "decode":
        # If he wants to decode then we just want to minus the shift amount from the position, for that we can do
        # the following
        shift_amount *= -1

    # Looping through all the characters in the start_text
    for char in start_text:

        # Checking if the character is a alphabet or any other thing, if any other thing, then just putting
        # it in end_text with else statement.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    # Printing the final output
    print(f"Here's the {cipher_direction}d result: {end_text}")


# Starting the program
# Printing the logo at the start of the program
print(logo)

# Creating a boolean variable for helping in the stopping and continuing of the game
should_end = False

# Creating a while loop for continuing or stopping the game
while not should_end:

    # Getting inputs from the user.
    # Asking the user whether to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Asking the user to type the text and then getting it into lower case
    text = input("Type your message:\n").lower()

    # Asking the shift number from the user
    shift = int(input("Type the shift number:\n"))

    # if the user puts a shift number more that 25, then we will get an error, so that we are getting the remainder
    # by dividing it by 26. Then we can use that remainder as the shift number.
    shift = shift % 26

    # Calling the caesar function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Asking the user if they want to restart the game
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    # Creating an if statement to stop or continue the game
    if restart == "no":
        should_end = True
        print("Goodbye")
