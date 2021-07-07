import random

MIN_NUMBER = 1
MAX_NUMBER = 100
INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_puzzle():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def make_solution(puzzle):
    return 'yes' if puzzle % 2 == 0 else 'no'
