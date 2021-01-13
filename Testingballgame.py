import random


class Rubbish(object):
    rubbish_position = [[100, 50], [600, 70], [1000, 10]]
    fix_position = 0
    number_of_rubbish = 0


class GG(Rubbish):
    while Rubbish.fix_position < 3:
        print(Rubbish.rubbish_position[Rubbish.fix_position][0])
        print(Rubbish.rubbish_position[Rubbish.fix_position][1])
        Rubbish.fix_position += 1
        Rubbish.number_of_rubbish += 1
