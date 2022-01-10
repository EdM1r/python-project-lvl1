import random

RULES = 'What number is missing in the progression?'


def generate_expression():
    first_number = random.randint(1, 100)
    progression_number = random.randint(1, 10)
    expression = []
    for index in range(random.randint(5, 11)):
        expression.append(first_number + progression_number * index)
    correct_answer = str(random.choice(expression))
    expression = ' '.join(str(number) for number in expression)
    expression = expression.replace(correct_answer, '..')
    return expression, correct_answer


if __name__ == '__main__':
    print('Run')
    print(generate_expression())
