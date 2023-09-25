from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
end = False


def caesar(user_text, user_shift, user_direction):
    result = ''

    for letter in user_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if user_direction == 'encode':
                new_position = alphabet[(position + user_shift) % len(alphabet)]
            else:
                new_position = alphabet[(position - user_shift) % len(alphabet)]
            result += new_position
        else:
            result += letter

    print(f'The {user_direction}d text is {result}.')


print(logo)

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    restart = input("Do you want to restart the cipher program? Type 'yes' or 'no'.\n").lower()
    if restart == 'no':
        end = True
