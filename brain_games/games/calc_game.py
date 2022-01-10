import random

RULES = 'What is the result of the expression?'


def generate_expression():
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    return f'{number_1} {operation} {number_2}', correct_answer


if __name__ == '__main__':
    print('Run')
    print(generate_expression())
