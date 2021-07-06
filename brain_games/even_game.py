import random

import prompt


def run_even_game(user_name: str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    frags = 0
    while frags < 3:
        number = random.randint(1, 1000)
        print(f'Question: {str(number)}')
        answer = prompt.string('Your answer: ')
        solution = 'yes' if number % 2 == 0 else 'no'
        if answer.strip().lower() == solution:
            print('Correct!')
            frags += 1
            continue
        msg = f'"{answer}" is wrong answer ;(. Correct answer was "{solution}"'
        print(msg)
        print(f"Let's try again, {user_name}!")
        break
    else:
        print(f'Congratulations, {user_name}!')
