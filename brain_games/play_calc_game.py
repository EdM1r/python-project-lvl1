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


def play_calc_game(name):
    playing = True
    iteration = 0
    print('What is the result of the expression?')
    while playing is True and iteration < 3:
        expression = generate_expression()
        print(f'Questions: {expression}')
        player_input = int(input("Your answer: "))
        is_correct, correct_answer = check_answer(expression, player_input)
        if is_correct:
            print('Correct!')
            iteration += 1
        else:
            print(f"'{player_input}' is wrong answer ;( "
                  f"correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            playing = False
    if iteration == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    play_calc_game('Ed')
