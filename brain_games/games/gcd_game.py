import random
import math


def generate_expression():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    correct_answer = math.gcd(number_1, number_2)
    return f'{number_1} {number_2}', correct_answer


if __name__ == '__main__':
    print('Run')
    print(generate_expression())
