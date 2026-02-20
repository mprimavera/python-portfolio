from ascii_art import caesar_cipher_logo

# data--letters in alphabet
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# print welcome logo
print("Welcome to:")
print(caesar_cipher_logo)


def cypher():
    # prompt the user to encrypt or decrypt
    choice = input("Type 'encode' to encrypt, and 'decode' to decrypt:\n")
    # attain message and shift from user
    message_raw = input("Type your message:\n").lower()
    shift = int(input("Type the shift number\n"))
    message_encrypted = ''

    # change shift direction if decode is selected
    if choice == 'decode':
        shift = 26 - shift

    # account for negative values
    if shift < 0:
        while shift < -26:
            shift += 26
        shift = shift + 26

    # perform the shift and output the letters
    # get shift for each letter in the message
    for letter_m in message_raw:
        # create temporary variables for individual letter shift
        count = 0
        shifted_letter = 0
        if letter_m not in letters:
            message_encrypted += letter_m
        else:
            # count the letters until the match to get the current position of the letter in the alphabet
            while letter_m != letters[count]:
                count += 1
            # add the shift to the current position to get the position of the shifted letter
            shifted_letter = count + shift

            # modulo 26 the value so if it's greater than the length of the alphabet it will cycle back to
            # the beginning of the alphabet
            shifted_letter %= len(letters)

            # add the shifted letter to the encrypted message
            message_encrypted += letters[shifted_letter]

    # print the encrypted message to the user
    print(f"Here's the encoded result {message_encrypted}")
    play_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if play_again == 'yes':
        cypher()
    else:
        print('Goodbye')

cypher()
