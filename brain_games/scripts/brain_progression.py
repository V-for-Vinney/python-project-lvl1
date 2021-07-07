#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.game_engine import start_game
from brain_games.games import progression


def main():
    user_name = welcome_user()
    print(progression.INTRO)
    start_game(user_name, progression.make_puzzle, progression.make_solution)


if __name__ == '__main__':
    main()
