from random import *


def new_game():
    print('')
    print('Would you like to play again? (yes/no)')
    answer = input()
    if answer == 'yes':
        # restart the hangman game
        return hangman()
    elif answer == 'no':
        print('')
        print('Ok, see you at the gallows next time!')
        return
    else:
        print('')
        print('Just give a yes or no')
        return new_game()


def hangman():
    ls = ['recursive', 'general', 'assembly', 'reticulated', 'python', 'constriction', 'anthropocentricities', 'inconsequentialities', 'electromagnetically', 'counterculturalisms',
          'crosslinguistically', 'exhibitionistically', 'interchangeableness', 'microelectronically', 'noninterventionists', 'phenomenalistically', 'uncommunicativeness']
    # make a list of words to be used at random in the game
    secret = ls[round((len(ls)-1)*random())]
    # choose a random word
    guess = []
    # empty guess list to add letters to
    display = ''
    for i in secret:
        display += '_ '
    # setting up a display for the secret word
    hangman = [
        ' _____',
        '|',
        '|',
        '|',
        '|',
        '[][][][]'
    ]
    # creating a hangman game display as a list
    count = 0

    # count variable to store wrong guesses

    def make_guesses(secret, guess, display, hangman, count, ls):
        # first, let's print our current hangman game state for each turn
        for i in hangman:
            print(i)
        # BASE CASE to determine if the game has been won or lost
        test = display.split(' ')
        # check for a win by checking to see if any _ are left in the answer
        # if there are not, the word has been guessed correctly
        if '_' not in test:
            answer = ''.join(test)
            print('')
            print(answer)
            print('You guessed right! No hanging today.')
            return new_game()
        elif count > 6:
            # if the number of wrong guesses is over 6, game over
            print('')
            print('Hangman. GG no re.')
            print(f'The correct answer was: {secret}')
            return new_game()

        # RECURSIVE CASE - repeat this until the game has met the conditions of the BASE CASE
        print('')
        print(display)
        if len(guess) > 0:
            print(f"Your guesses: {' '.join(guess)}")
        # Show the current display of user's guesses
        print('')
        print('Make a guess')
        letter = input().lower()
        # make all inputs lower case, to properly compare with the secret word
        if letter == secret:
            # If a user magically guesses the word, they win
            print('')
            print(letter)
            print('You guessed right! No hanging today.')
            return new_game()
        else:
            letter = letter[:1]
            # Otherwise, a guess is equal to the first character of any input size
            if letter in guess:
                print('')
                print('You already guessed that letter.')
                return make_guesses(secret, guess, display, hangman, count, ls)
            else:
                guess.append(letter)

        if letter in secret:
            # if the guess letter is found in the secret word
            for i in range(len(secret)):
                # check all indices of the secret word
                if secret[i] == letter:
                    # and if the value at an index in the secret word matches the letter
                    x = display.split(' ')
                    # split the display '_ _ _ ' list by spaces into a list ['_','_','_']
                    if x[i] == '_':
                        # then, if the value at an index in the new display list is unchanged
                        # i.e., still '_', replace it with the secret word's letter at each index
                        # that matches
                        x[i] = secret[i]
                    # after replacing the values, join the new list ['match','_','_']
                    # back into the original display string format 'match _ _ '
                    display = ' '.join(x)
        else:
            print('The crowd looks on with fervor')
            count += 1
            # Bad guess, add one to the wrong guesses count
            for i in range(0, len(hangman)):
                # replace values in the hangman game state at each count of wrong guesses
                # to reflect the current hangman game state
                if count == 1:
                    if hangman[4] == '|':
                        hangman[4] = '|  /'
                elif count == 2:
                    if hangman[4] == '|  /':
                        hangman[4] = '|  / \\'
                elif count == 3:
                    if hangman[3] == '|':
                        hangman[3] = '|   |'
                elif count == 4:
                    if hangman[3] == '|   |':
                        hangman[3] = '|  /|'
                elif count == 5:
                    if hangman[3] == '|  /|':
                        hangman[3] = '|  /|\\'
                elif count == 6:
                    if hangman[2] == '|':
                        hangman[2] = '|   0'
                elif count == 7:
                    if hangman[2] == '|   0':
                        hangman[1] = '|   |'
                        hangman[5] = '[]    []'
        # return the make_guesses function with updated values
        return make_guesses(secret, guess, display, hangman, count, ls)
    # start the guessing game loop
    make_guesses(secret, guess, display, hangman, count, ls)


# start hangman on running the file
hangman()
