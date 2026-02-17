# Create flow of logic based on flow chart provided with the course
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
right_left = input("You're at a crossroad, where do you want to go?"
                   ' Type "left" or "right"\n').lower()
if right_left == 'left':
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake"
                         ' Type "wait" to wait for a boat.'
                         ' Type "swim" to swim across.\n').lower()
    if swim_or_wait != 'swim':
        which_door = input("You've arrived at the island where there is a house with 3 doors,"
                           " one red, one blue, and one yellow."
                           ' Which door do you choose, "red", "blue", or "yellow"\n').lower()
        if which_door == 'red':
            print('The door was red from fire within! Burned by fire.\nGame Over.')
        elif which_door == 'blue':
            print('Eaten by beasts.\nGame Over.')
        elif which_door == 'yellow':
            print("You found the treasure!")
        else:
            print("You've gone out of bounds! Game Over.")
    else:
        print("You were eaten by a shark! Game Over.")
else:
    print("You fell in a black hole! Game Over.")

