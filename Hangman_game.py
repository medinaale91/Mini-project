import random

def choose_serie():
    netflix_series = ["MONEY HEIST", "DARK", "ELITE", "UNORTHODOX", "SEX EDUCATION", "NARCOS", "THE LAST KINGDOM", "MAKING A MURDERER", "STRANGER THINGS", "YOU", "PEAKY BLINDERS", "TIGER KING", "MODERN FAMILY", "BLACKLIST", "BABIES", "BREAKING BAD", "PRISON BREAK"]
    word = random.choice(netflix_series)
    return word

def greetings():
    print("Welcome to the Hangman game - Netflix Series version.")