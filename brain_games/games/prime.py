import random

MIN_NUMBER = 1
MAX_NUMBER = 100
INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int):
    if number in {2, 3}:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def make_puzzle():
    return str(random.randint(MIN_NUMBER, MAX_NUMBER))


def make_solution(puzzle):
    return 'yes' if is_prime(int(puzzle)) else 'no'
