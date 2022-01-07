#!/usr/bin/env python
# test project for hexlet lvl1
from brain_games.cli import welcome_user
from brain_games.play_even_game import play_even_game


def main():
    print('Welcome to Brain Games!')
    name = welcome_user()
    play_even_game(name)


if __name__ == '__main__':
    main()
