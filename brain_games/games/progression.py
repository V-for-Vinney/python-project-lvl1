import random

MIN_LENGTH = 5
MAX_LENGTH = 15
MIN_START = 0
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10

INTRO = 'What number is missing in the progression?'


def make_puzzle():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = list(range(start, start + length * step, step))
    puzzle_position = random.choice(list(range(length)))
    progression[puzzle_position] = '..'
    progression = list(map(str, progression))
    return ' '.join(progression)


def make_solution(puzzle: str):
    progr = sorted(map(int, (filter(lambda x: x != '..', puzzle.split()))))
    step = min([progr[i + 1] - progr[i] for i in range(len(progr) - 1)])
    sought_position = puzzle.split().index('..')
    start = progr[0]
    if sought_position == 0:
        return str(start - step)
    return str(start + step * sought_position)
