#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games import even


def main():
    start_game(even.INTRO, even.make_puzzle, even.make_solution)


if __name__ == '__main__':
    main()
