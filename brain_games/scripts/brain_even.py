#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.even_game import run_even_game


def main():
    user_name = welcome_user()
    run_even_game(user_name)


if __name__ == '__main__':
    main()
