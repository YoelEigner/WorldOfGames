import GuessGame
import MemoryGame
import CurrencyRouletteGame
from termcolor import colored
from Score import add_score


def welcome():
    players_name = input("Please Enter Your Name: ")
    return "Hello " + players_name + " and welcome to the World of Games (WoG). Here you can find many cool games to " \
                                     "play. "


def load_game():
    game = int(input("Please choose a game to play:\n"
                     "1. Memory Game - a sequence of numbers will appear for 1 second and you have to \n"
                     "guess it back \n"
                     "2. Guess Game - guess a number and see if you chose like the computer \n"
                     "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"))
    try:
        if 1 <= game <= 3:
            if game == 3:
                difficulty = int(input("Please choose game difficulty from 1 to 5 (5 is the easiest): "))
                check(game, difficulty)
            elif game <= 2:
                difficulty = int(input("Please choose game difficulty from 1 to 5 (5 is the hardest): "))
                check(game, difficulty)
        else:
            print(colored("Not a valid choice", 'red'))
            load_game()
    except Exception as e:
        print(colored("Error! Try again " + str(e), 'red'))
        print('\n' * 1)
        load_game()


def check(game, difficulty):
    try:
        if 1 <= difficulty <= 5:
            if game == 1:
                won = MemoryGame.play(difficulty)
                if won:
                    add_score(difficulty)
                load_game()
            if game == 2:
                won = GuessGame.play(difficulty)
                if won:
                    add_score(difficulty)
                load_game()
            if game == 3:
                won = CurrencyRouletteGame.play(difficulty)
                if won:
                    add_score(difficulty)
                load_game()
        else:
            print(colored("Not a valid choice", 'red'))
            load_game()
    except Exception as e:
        print(colored("Error! Try again " + str(e), 'red'))
        load_game()
