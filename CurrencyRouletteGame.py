from currency_converter import CurrencyConverter
from random import randrange


def get_usd_to_ils():
    c = CurrencyConverter()
    currency = c.convert(1, "USD", "ILS")
    return round(currency, 2)


def get_money_interval(currency, difficulty):
    gen_num = randrange(1, 100)
    gen_currency = (gen_num * currency)
    upper_guess = gen_currency + (5 - difficulty)
    lower_guess = gen_currency - (5 - difficulty)
    # print(lower_guess)
    # print(gen_currency)
    # print(upper_guess)
    return gen_num, gen_currency, lower_guess, upper_guess


def get_guess_from_user(gen_num):
    user_guess = input("Enter your currency guess to " + str(gen_num) + " USD to ILS:\n")
    return user_guess


def play(difficulty):
    gen_num, gen_currency, lower_guess, upper_guess = get_money_interval(currency=get_usd_to_ils(), difficulty=difficulty)
    user_guess = get_guess_from_user(gen_num)
    if float(user_guess) > float(upper_guess) or float(user_guess) < float(lower_guess):
        return False
    else:
        return True
