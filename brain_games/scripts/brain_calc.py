#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.game_engine import start_game
from brain_games.games import calc


def main():
    user_name = welcome_user()
    print(calc.INTRO)
    start_game(user_name, calc.make_puzzle, calc.make_solution)


if __name__ == '__main__':
    main()
