import random

feet_in_mile = 5280
meters_in_kilometers = 1000
beatles = ["Jonh Lennon", "Ringo Star", "Paul McCartney", "George Harrison"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_a_dice(num):
    return random.randint(1, num)


