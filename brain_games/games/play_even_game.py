import random


def generate_expression():
    number_1 = random.randint(1, 100)
    return number_1


def check_answer(number_1, player_input):
    if player_input == 'yes' and number_1 % 2 == 0:
        return True, None
    elif player_input == 'no' and number_1 % 2 == 1:
        return True, None
    elif player_input == 'yes' and number_1 % 2 == 1:
        correct_answer = 'no'
        return False, correct_answer
    else:
        correct_answer = 'yes'
        return False, correct_answer


if __name__ == '__main__':
    print('Run')
