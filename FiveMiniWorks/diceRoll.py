import random


def roll_dice(face_number):
    return random.randint(1, face_number)


print(roll_dice(10))
