#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games import calc


def main():
    start_game(calc.INTRO, calc.make_puzzle, calc.make_solution)


if __name__ == '__main__':
    main()
