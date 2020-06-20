import random
from termcolor import colored


def generate_number(difficulty):
    secret_number = int(random.randint(1, difficulty))
    print("Please guess a number between 1 and " + str(difficulty) + ": ")
    return int(secret_number)


def get_guess_from_user():
    try:
        return int(input(""))
    except Exception as e:
        print(colored(str(e)))


def compare_results(x, y):
    if x == y:
        print(colored(True, 'green'))
        return True
    else:
        print(colored("False, The correct answer is " + str(x), 'red'))
        return False


def play(difficulty):
    won = compare_results(generate_number(difficulty), get_guess_from_user())
    return won
