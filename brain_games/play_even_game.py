import random


def generate_number():
    number_1 = random.randint(1, 100)
    return number_1


def check_player_answer(number_1, player_input):
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


def play_even_game(name):
    playing = True
    iteration = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while playing is True and iteration < 3:
        number_1 = generate_number()
        print(f'Questions: {number_1}')
        player_input = input("Your answer: ")
        is_correct, correct_answer = check_player_answer(number_1, player_input)
        if is_correct:
            print('Correct!')
            iteration += 1
        else:
            print(f"'{player_input}'is wrong answer ;( "
                  f"correct answer was '{correct_answer}'")
            print(f"Let's try again {name}")
            playing = False
    if iteration == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    play_even_game('Ed')
