import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    print('test')
    welcome_user()


if __name__ == '__main__':
    main()
