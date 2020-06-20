import random
from time import sleep

from pip._vendor.distlib.compat import raw_input
from termcolor import colored


def generate_sequence(difficulty):
    try:
        lst = range(1, 101)
        rand = random.choices(lst, k=difficulty)
        print(rand)
        sleep(1)
        print('\n' * 1000)
        return str(rand)
    except Exception as e:
        print(colored(str(e)))


def get_list_from_user():
    try:
        user_list = raw_input("Enter the numbers that you you just saw: ")
        usr_input = str([int(i) for i in user_list.split()])
        return usr_input
    except Exception as e:
        print(colored(str(e)))


def is_list_equal(x, y):
    if x == y:
        print(colored(True, 'green'))
        return True
    else:

        print(colored("False, The correct answer is " + str(x), 'red'))
        return False


def play(difficulty):
    is_list_equal(generate_sequence(difficulty), get_list_from_user())
