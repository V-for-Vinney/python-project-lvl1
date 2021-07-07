#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.game_engine import start_game
from brain_games.games import prime


def main():
    user_name = welcome_user()
    print(prime.INTRO)
    start_game(user_name, prime.make_puzzle, prime.make_solution)


if __name__ == '__main__':
    main()
