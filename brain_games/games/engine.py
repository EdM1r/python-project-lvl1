

def engine(name, generate_expression, check_answer):
    playing = True
    iteration = 0
    while playing is True and iteration < 3:
        expression = generate_expression()
        print(f'Questions: {expression}')
        player_input = input("Your answer: ")
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
    print('Run')
