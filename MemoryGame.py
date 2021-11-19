from random import sample
from time import sleep
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def generate_sequence(difficulty):
    seq_list = sample(range(1, 101), difficulty)
    print(seq_list)
    sleep(0.7)
    clearConsole()
    return seq_list


def get_list_from_user(difficulty):
    user_list = []
    print("Please enter " + str(difficulty) + " numbers between 1 to 101")
    for i in range(0, difficulty):
        user_guess = input("Please enter your " + str(i + 1) + " guess: ")
        user_list.append(user_guess)
    return user_list


def is_list_equal(gen_list, user_list):
    is_equal = True
    for num in user_list:
        if int(num) not in gen_list:
            is_equal = False
            break
    return is_equal


def play(difficulty):
    gen_seq = generate_sequence(difficulty)
    user_seq = get_list_from_user(difficulty)
    return is_list_equal(gen_seq, user_seq)
