

def engine(generate_expression, rules):
    print('Welcome to Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    iteration = 0
    while iteration < 3:
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
            break
    if iteration == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    print('Run')
