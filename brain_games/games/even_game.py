import random


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
