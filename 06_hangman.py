# import libraries
import random as rd

# set number of available guesses
guesses = 2

# create a list of words to choose from for the game
word_list = ["aardvark", "baboon", "camel"]
# choose random word from word list
random_word = rd.choice(word_list)

# create blanks to print to user
blanks = ''
for letter in random_word:
    blanks += '_'

# create a chosen letter list
chosen_letters = []

# temporary variable for the current chosen letter
chosen_letter = ''

# todo remove after debugging
print(random_word)


# update user function for repeated code after choosing a letter
def update_to_user():
    print(f"You have {guesses} guesses remaining: {blanks}")


# welcome the user to the game
print("Welcome to hangman!")
# update the user of the guesses and current state of the game
update_to_user()

# loop to continue until guesses expire or word has zero blanks remaining
while guesses != 0 and '_' in blanks:
    # create temporary string for updating guesses and blanks
    updated_guesses = ''
    # prompt user for a letter and save it to a list of chosen letters and cast to lower
    chosen_letter = (input("Please choose a letter:\n")).lower()

    # error handling by a print to user
    if len(chosen_letter) != 1:
        print("You entered too many characters, please guess again.")
        update_to_user()

    # handle case when user chooses letter already chosen
    elif chosen_letter in chosen_letters:
        print("You have already chosen this letter, please guess again.")
        update_to_user()

    # Check if guess is in the word
    elif chosen_letter in random_word:
        # add chosen letter to chosen letters list
        chosen_letters.append(chosen_letter)

        # update the blanks with the correct chosen letter
        for letter_position in range(len(random_word)):
            if chosen_letters[-1] == random_word[letter_position]:
                updated_guesses += chosen_letters[-1]
            else:
                updated_guesses += blanks[letter_position]

        # swap the temporary updated guesses with the new blanks
        blanks = updated_guesses

        # determine if the player won
        if '_' not in blanks:
            print(f"You've Won The Game, the word is {blanks}!")

        else:
            print("You've chosen correctly!")
            update_to_user()

    else:
        # add chosen letter to chosen letters list
        chosen_letters.append(chosen_letter)

        # let the player know they were incorrect
        print("You have guessed incorrectly.")
        # update the remaining guesses
        guesses -= 1

        # check if there are guesses remaining
        if guesses == 0:
            # if zero guesses left, print that the user has lost the game
            print(f"You have lost the game, the word was {random_word}!")
        else:
            # if guesses remaining is not equal to zero, print updated guesses and reprint blanks
            update_to_user()
