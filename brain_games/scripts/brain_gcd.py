#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games import gcd


def main():
    start_game(gcd.INTRO, gcd.make_puzzle, gcd.make_solution)


if __name__ == '__main__':
    main()
