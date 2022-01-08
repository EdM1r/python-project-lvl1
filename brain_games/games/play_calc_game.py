import random


def generate_expression():
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    return f'{number_1} {operation} {number_2}'


def check_answer(expression, player_input):
    number_1, operation, number_2 = expression.split()
    number_1 = int(number_1)
    number_2 = int(number_2)
    player_input = int(player_input)
    if operation == '+':
        correct_answer = number_1 + number_2
    elif operation == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2
    if player_input == correct_answer:
        return True, correct_answer
    else:
        return False, correct_answer


if __name__ == '__main__':
    print('Run')
