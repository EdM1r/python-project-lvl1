#!/usr/bin/env python
# test project for hexlet lvl1
from brain_games.engine import engine
from brain_games.games.prime_game import generate_expression
from brain_games.games.prime_game import RULES


def main():
    engine(generate_expression, RULES)


if __name__ == '__main__':
    main()
