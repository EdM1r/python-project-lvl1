#!/usr/bin/env python
# test project for hexlet lvl1
from brain_games.cli import welcome_user
from brain_games.games.engine import engine
from brain_games.games.play_calc_game import generate_expression
from brain_games.games.play_calc_game import check_answer


def main():
    print('Welcome to Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    engine(name, generate_expression, check_answer)


if __name__ == '__main__':
    main()
