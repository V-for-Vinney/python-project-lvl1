import prompt


def welcome_user():
    """Greetings."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
