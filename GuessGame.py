from random import randrange


def generate_number(difficulty):
    secret_number = randrange(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    guess = input("guess number between 1 and " + str(difficulty) + ": ")
    return guess


def compare_results(secret_number, guess):
    if secret_number == guess:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, user_guess)
