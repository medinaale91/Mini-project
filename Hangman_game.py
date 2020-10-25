import random

def choose_serie():
    netflix_series = ["MONEY HEIST", "DARK", "ELITE", "UNORTHODOX", "SEX EDUCATION", "NARCOS", "THE LAST KINGDOM", "MAKING A MURDERER", "STRANGER THINGS", "YOU", "PEAKY BLINDERS", "TIGER KING", "MODERN FAMILY", "BLACKLIST", "BABIES", "BREAKING BAD", "PRISON BREAK"]
    word = random.choice(netflix_series)
    return word

def greetings():
    print("Welcome to the Hangman game - Netflix Series version.")

def ask_character():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character = input("Which character do you want to type?: ")
    while character.upper() not in alphabet:
        character = input("Only letters allowed: ")
    return character.upper()

def print_gaps(serie, hits):
    gaps = ""
    for i in range(len(serie)):
        if serie[i] != " " and hits[i] == False:
            gaps += "_ "
        elif serie[i] == " ":
            gaps += "   "
        else:
            gaps += serie[i]
    print(gaps)

def generate_word_hits(str):
    hits = []
    for i in str:
        if i == " ":
            hits.append(True)
        else:
            hits.append(False)
    return hits

def update_gaps(serie, hits, character):
    for i in range(len(serie)):
        if serie[i] == character:
            hits[i] = True
    print_gaps(serie, hits)
    
def game():
    greetings()
    serie = choose_serie()
    word_hits = generate_word_hits(serie)
    print_gaps(serie, word_hits)
    while False in word_hits:
        character = ask_character()
        update_gaps(serie, word_hits, character)

game()