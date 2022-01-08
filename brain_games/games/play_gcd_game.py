import random
import math


def generate_expression():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    return f'{number_1} {number_2}'


def check_answer(expression, player_input):
    number_1, number_2 = expression.split()
    number_1 = int(number_1)
    number_2 = int(number_2)
    player_input = int(player_input)
    correct_answer = math.gcd(number_1, number_2)
    if player_input == correct_answer:
        return True, correct_answer
    else:
        return False, correct_answer


if __name__ == '__main__':
    print('Run')
