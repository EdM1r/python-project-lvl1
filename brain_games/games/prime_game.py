import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_expression():
    number_1 = random.randint(1, 100)
    correct_answer = ''
    if number_1 > 1:
        for i in range(2, int(number_1 / 2) + 1):
            if number_1 % i == 0:
                correct_answer = 'no'
                break
        if correct_answer != 'no':
            correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number_1, correct_answer


if __name__ == '__main__':
    print(generate_expression())
