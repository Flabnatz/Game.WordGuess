from game.game_on import nlet, nlet_file

# Initiate User Interaction
print('Would you like to play the Word Guessing Game? [y/n]: ')
is_begin = input()

# Acceptable Inputs
y_inputs = ['y', 'Y', 'yes', 'Yes', 'yay', 'Yay']
n_inputs = ['n', 'N', 'no', 'No', 'nay', 'Nay']

# Game loops until the user is done playing
# ...or a fatal error occurs....
is_play = True
while is_play:
    if is_begin in y_inputs:
        print("Let's play!")

        # How many letters to play with?
        #   n = [n(int), is_play(bool), note(str)]
        n = nlet()
    elif is_begin in n_inputs:
        print("Maybe next time!")
        is_play = False
    else:
        print("Error: unacceptable input.  Press 'y' to play or 'n' to stop.")
        is_begin = input()