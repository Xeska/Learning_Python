rooms = [['A1', 'A2'],
         ['B1', 'B2', 'B3'],
         ['C1', 'C2']]

description = {
    'A1': 'red',
    'A2': 'blue',
    'B1': 'violet',
    'B2': 'orange',
    'B3': 'pink',
    'C1': 'grey',
    'C2': 'white'
}

start_x = 1
start_y = 0


def play_game():
    actual_x = start_x
    actual_y = start_y
    stop = False
    print('You can move in 4 directions: Top, Bottom, Left, Right. Enter \'Quit\' to stop.')
    while not stop:
        move = input('Choose a direction to move :')
        if move.lower() == 'quit':
            stop = True
        elif move.lower() == 'top':
            if actual_x - 1 < 0:
                print('You can\'t move further in that direction')
            else:
                actual_x -= 1
        elif move.lower() == 'bottom':
            if actual_x + 1 >= len(rooms):
                print('You can\'t move further in that direction')
            else:
                actual_x += 1
        elif move.lower() == 'left':
            if actual_y - 1 < 0:
                print('You can\'t move further in that direction')
            else:
                actual_y -= 1
        elif move.lower() == 'right':
            if actual_y + 1 >= len(rooms[actual_x]):
                print('You can\'t move further in that direction')
            else:
                actual_y += 1
        else:
            print('Try again :)')
        print('The room you\'re actually in is ' + description[rooms[actual_x][actual_y]] + ' (' + rooms[actual_x][actual_y] + ')')


play_game()
