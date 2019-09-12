import random

words = ['hangman', 'boss', 'massage', 'league', 'hatch', 'big ben', 'death star', 'programming', 'react', 'tea spoon']


def play_game():
    print('Let\'s play the Hangman game !')
    word = words[random.randint(1, len(words))]
    letter_number = len(word)
    for i in range(len(word)):
        if word[i] == ' ':
            print(' ', end=' ')
            letter_number -= 1
        else:
            print('_', end=' ')
    print('\n')
    guesses = 0
    wrong_letters = []
    right_letters = []
    right_guesses = 0
    check = True
    while right_guesses < letter_number and check:
        check = False
        entry = input('Enter a letter: ').lower()
        if entry.isalpha():
            guesses += 1
            if entry in word:
                right_guesses += 1
                right_letters.append(entry)
            else:
                wrong_letters.append(entry.upper())
        for i in range(len(word)):
            if word[i] in right_letters:
                print(word[i].upper(), end=' ')
            elif word[i] == ' ':
                print(' ', end=' ')
            else:
                check = True
                print('_', end=' ')
        print('\nLettres non présentes:', end='')
        print(*wrong_letters, sep=', ')
    print('Congratulations ! The word was : ' + word.upper() + '.\nYou did ' + str(guesses) + ' guesses.')


play_game()