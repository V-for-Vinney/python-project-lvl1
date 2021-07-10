from typing import Callable

import prompt
from brain_games.cli import welcome_user

MAX_FRAGS = 3


def start_game(
    intro: str,
    make_puzzle: Callable,
    make_solution: Callable,
):
    user_name = welcome_user()
    print(intro)
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
