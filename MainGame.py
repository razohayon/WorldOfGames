from live import load_game, welcome
from Utils import clear_console

user_name = input("Please enter your name: ")
clear_console()
print(welcome(user_name))
print(load_game())
