import random

RULES = 'Type "yes" if number is even, and "no" if it is not'


def generate_expression():
    number_1 = random.randint(1, 100)
    if number_1 % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number_1, correct_answer


if __name__ == '__main__':
    print('Run')
    print(generate_expression())
