import random

MIN_NUMBER = 1
MAX_NUMBER = 10
INTRO = 'Find the greatest common divisor of given numbers.'


def gcd(x: int, y: int):
    while y:
        x, y = y, x % y
    return x


def make_puzzle():
    number_one = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    number_two = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    return ' '.join([number_one, number_two])


def make_solution(puzzle):
    number_one, number_two = map(int, puzzle.split())
    return str(gcd(number_one, number_two))
