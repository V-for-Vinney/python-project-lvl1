import random
from operator import add, mul, sub

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
}
MIN_NUMBER = 0
MAX_NUMBER = 10
INTRO = 'What is the result of the expression?'


def make_puzzle():
    number_one = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    number_two = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    operation = random.choice(list(OPERATIONS.keys()))
    return ' '.join([number_one, operation, number_two])


def make_solution(puzzle: str) -> str:
    number_one, operation, number_two = puzzle.split(' ')
    solution = OPERATIONS[operation](int(number_one), int(number_two))
    return str(solution)
