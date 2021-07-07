import ast
import random

OPERATIONS = ('+', '-', '*')
MIN_NUMBER = 0
MAX_NUMBER = 10
INTRO = 'What is the result of the expression?'


def make_puzzle():
    number_one = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    number_two = str(random.randint(MIN_NUMBER, MAX_NUMBER))
    operation = random.choice(OPERATIONS)
    return ' '.join([number_one, operation, number_two])


def make_solution(puzzle) -> str:
    return str(ast.literal_eval(puzzle))
