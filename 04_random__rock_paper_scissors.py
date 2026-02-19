# import the random library
import random as rd
import ascii_art as aa

rock = aa.rps_rock
paper = aa.rps_paper
scissors = aa.rps_scissors

# set options to a list
options = [rock, paper, scissors]
# select a random choice for the computer
computers_choice = rd.choice(options)

# create a users choice variable for printing ascii art
users_choice = ''
# prompt user for their chioce and save as variable
users_choice_str = input('Which do You choose, "rock", "paper", or "scissors"?\n')

if users_choice_str not in ['rock', 'paper', 'scissors']:
    print("You entered an invalid choice. You lose!")
else:
    # set variable for winner
    winner = ''

    # logic to determine winner
    if users_choice_str == 'rock':
        users_choice = rock
        if computers_choice == rock:
            winner = 'tie'
        elif computers_choice == paper:
            winner = 'computer'
        else:
            winner = 'You'
    elif users_choice_str == 'paper':
        users_choice = paper
        if computers_choice == rock:
            winner = 'You'
        elif computers_choice == paper:
            winner = 'tie'
        else:
            winner = 'computer'
    else:
        users_choice = scissors
        if computers_choice == rock:
            winner = 'computer'
        elif computers_choice == paper:
            winner = 'You'
        else:
            winner = 'tie'

    # print the choices
    print(f"The computer chose\n{computers_choice}")
    print(f"You chose\n {users_choice}")

    # print the winner
    if winner != 'tie':
        if winner == 'You':
            print(f"{winner} are the winner!")
        else:
            print(f"The {winner} is the winner!")
    else:
        print(f"The game was a {winner}!")
