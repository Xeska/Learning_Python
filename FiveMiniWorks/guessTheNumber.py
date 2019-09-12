import random


def play_guess():
    try:
        max = int(input('Enter a maximum number: '))
        print('The game will be between ' + str(max) + ' included.')
        target = random.randint(0, max)
        while True:
            entry = int(input('Enter a positive number: '))
            if entry > target:
                print('Less')
            elif entry < target:
                print('More')
            else:
                print('Correct !')
                return 0
    except ValueError:
        print('Enter a proper value. Please use an integer greater than zero or equal.')

play_guess()
