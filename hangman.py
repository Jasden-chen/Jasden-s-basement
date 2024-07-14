from random import choice

word_bank = ['red', 'orange', 'yellow', 'green', 'purple', 'blue', 'violet']  # enter custom words in word bank

# initializing the game
word = (choice(word_bank))  # chooses random word
main_game = '_' * len(word)  # creates '_' for the amount of letters
main_game = list(main_game)  # separates the '_' into list to find indexes later on
print(main_game)

phase = 0  # Global var, keeps track of phases using a counter

# different phases in a dictionary
hangman_phases = {
    1:              '_________'
                 '\n|'
                 '\n|'
                 '\n|'
                 '\n|'
                 '\n|'
                 '\n|'
                 '\n___________________',

    2:              '_________'
                 '\n|      ---'
                 '\n|     |   |'
                 '\n|      ---'
                 '\n|'
                 '\n|'
                 '\n|'
                 '\n___________________',

    3:              '_________'
                 '\n|      ---'
                 '\n|     |   |'
                 '\n|      ---'
                 '\n|       |'
                 '\n|       |'
                 '\n|'
                 '\n___________________',

    4:              '_________'
                 '\n|      ---'
                 '\n|     |   |'
                 '\n|      ---'
                 '\n|       |'
                 '\n|       |'
                 '\n|      / '
                 '\n___________________',
    5:              '_________'
                 '\n|      ---'
                 '\n|     |   |'
                 '\n|      ---'
                 '\n|       |'
                 '\n|       |'
                 '\n|      / |'
                 '\n___________________',

    6:              '_________'
                 '\n|      ---'
                 '\n|     |   |'
                 '\n|      ---'
                 '\n|       |'
                 '\n|      /|'
                 '\n|      / |'
                 '\n___________________',

    7:              '_________'
                 '\n|      ---'
                 '\n|     |   |'
                 '\n|      ---'
                 '\n|       |'
                 '\n|      /|/'
                 '\n|      / |'
                 '\n___________________',
    8: 'You lose!'
}

# main part of the program


def check(guess):  # guess is the user input
    if guess in word:  # checks if the letter inputted by the user is in the word
        indicies = [index for index, char in enumerate(word) if char == guess]
        for i in indicies:  # checks for multiple of the same letters in word and finds their index
            main_game[i] = guess   # swaps out the '_' with the corresponding index with the letter
        for x in main_game:
            print(x, end='')  # prints out what the user has so far
    else:
        global phase   # user guessed the wrong letter
        phase += 1  # 1 is added to the counter causing it to go to the next phase
        print('\nNope')
        print(hangman_phases[phase])  # displays the current phase to the user

# main game loop


while True:
    check(input('\n>>> '))  # takes the user's guess
    if '_' not in main_game:  # Checks to see if all '_' are gone. if all gone == win
        print('\nYou Win!')
        break
    if phase == 8:  # if user reaches 8 phases/counter == lose
        print(f'The word was {word}')
        break
