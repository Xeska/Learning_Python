story = ['This is the story of a ', '. It happened to be very ', ' but it also tells you how ', ' was made for the very first time !']


def fill_story():
    copy_story = story.copy()
    copy_story.insert(1, input('Enter a noun of your choice: '))
    copy_story.insert(3, input('Enter an adjective of your choice: '))
    copy_story.insert(5, input('Enter the recipe name of your choice: '))
    for sentence in copy_story:
        print(sentence, end='')

fill_story()
