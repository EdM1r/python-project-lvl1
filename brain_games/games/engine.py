

def engine(name, generate_expression):
    playing = True
    iteration = 0
    while playing is True and iteration < 3:
        expression, correct_answer = generate_expression()
        correct_answer = str(correct_answer)
        print(f'Questions: {expression}')
        player_input = input("Your answer: ")
        if correct_answer == player_input:
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
