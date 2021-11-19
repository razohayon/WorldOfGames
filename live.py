from classes.color import BColors
import GuessGame
import CurrencyRouletteGame
import MemoryGame


def welcome(name):
    welcome_greet = BColors.HEADER + "Hello " + name + " and welcome to the\
World of Games (WoG)." + "\n" + "Here you can find many cool games to\
play." + BColors.ENDC
    return welcome_greet


def validate_choose(value, min_val, max_val):
    if int(min_val) <= int(value) <= int(max_val):
        return True
    else:
        print(BColors.FAIL, value,  "is not valid choose", BColors.ENDC)
        return False


def load_game():
    game_valid = False
    diff_valid = False
    while not game_valid:
        print("""
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
""")
        game = input(BColors.BOLD + "Enter Yor Chose [1-3]:" + BColors.ENDC)
        game_valid = validate_choose(value=int(game), min_val=1, max_val=3)
    while not diff_valid:
        game_diff = input(BColors.BOLD + "Please choose game difficulty from 1 to 5:" + BColors.ENDC)
        diff_valid = validate_choose(value=int(game_diff), min_val=1, max_val=5)
    # print("Game is:", game, "Difficulty:", game_diff)
    if game == "1":
        MemoryGame.play(difficulty=int(game_diff))
    elif game == "2":
        GuessGame.play(difficulty=int(game_diff))
    else:
        CurrencyRouletteGame.play(difficulty=int(game_diff))


