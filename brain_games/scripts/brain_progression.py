#!/usr/bin/env python
from brain_games.game_engine import start_game
from brain_games.games import progression


def main():
    start_game(
        progression.INTRO,
        progression.make_puzzle,
        progression.make_solution,
    )


if __name__ == '__main__':
    main()
