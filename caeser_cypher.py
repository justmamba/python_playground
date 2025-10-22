# TODO-1: Import and print the logo from art.py when the program starts.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

restart = "yes"

def caesar(direction, original_text, shift_amount):
    if direction == "decode":
        shift_amount *= -1
    cipher = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            position2 = (position + shift_amount) % 26
            new_letter = alphabet[position2]
            cipher = cipher + new_letter
        else:
            cipher += letter
    print(f"Here is the {direction}d result: {cipher}")



# This is here for testing purposes
# print(position)
# print(position2)
# print(old_letter)
# print(new_letter)
# old_letter = alphabet[position]


# TODO-3: Can you figure out a way to restart the cipher program?

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, direction =direction)
    restart = input("Would you like to go again? Yes or No. ").lower()



