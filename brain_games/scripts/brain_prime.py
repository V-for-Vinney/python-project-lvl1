#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games import prime


def main():
    start_game(prime.INTRO, prime.make_puzzle, prime.make_solution)


if __name__ == '__main__':
    main()
