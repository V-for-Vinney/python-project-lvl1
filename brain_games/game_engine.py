from typing import Callable

import prompt

MAX_FRAGS = 3


def start_game(
    user_name: str,
    make_puzzle: Callable,
    make_solution: Callable,
):
    for _ in range(MAX_FRAGS):
        puzzle = make_puzzle()
        print(f'Question: {str(puzzle)}')
        answer = prompt.string('Your answer: ')
        solution = make_solution(puzzle)
        if answer.strip().lower() == solution:
            print('Correct!')
            continue
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{solution}"')
        print(f"Let's try again, {user_name}!")
        break
    else:
        print(f'Congratulations, {user_name}!')
