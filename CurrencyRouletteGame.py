from forex_python.converter import CurrencyRates
import random
from urllib3.connectionpool import xrange
from termcolor import colored

get_rate = CurrencyRates()
exchange_rate = (get_rate.get_rate('USD', 'ILS'))


def get_money_interval(rand):
    correct_rate = int(get_rate.convert('USD', 'ILS', rand))
    return correct_rate


def get_guess_from_user(num):
    try:
        user_input = int(input("How much do you think " + str(num) + " USD is in ILS? "))
        return user_input
    except Exception as e:
        print(colored(str(e)))


def check_result(rate, user_guess, level):
    if rate == user_guess:
        print(colored("Correct, You won!", 'green'))
    elif user_guess in xrange(rate, rate + level) or user_guess == rate + level:
        print(colored("Close enough, You won!", 'green'))
    elif user_guess in xrange(rate - level, rate) or user_guess == rate - level:
        print(colored("Close enough, You won!", 'green'))
    else:
        print(colored("False, Correct answer is " + str(rate), 'red'))


def play(difficulty):
    rand = random.randint(1, 100)
    check_result(get_money_interval(rand), get_guess_from_user(rand), difficulty)

