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

def user_succeed(serie, hits, character):
    succeed = False
    for i in range(len(serie)):
        if serie[i] == character:
            hits[i] = True
            succeed = True
    return succeed
    
def print_hangman(fails_count, fails_allowed):
    if fails_count == 1:
        print(
            '''
            ______
            |	  |
            |     O
            |    
            |     
            |     
            |
            |
            '''
        )
    if fails_count == 2:
        print(
            '''
            ______
            |	  |
            |     O
            |    /
            |     
            |     
            |
            |
            '''
        )
    if fails_count == 3:
        print(
            '''
            ______
            |	  |
            |     O
            |    /|
            |     
            |     
            |
            |
            '''
        )
    if fails_count == 4:
        print(
            '''
            ______
            |	  |
            |     O
            |    /|\\
            |     
            |     
            |
            |
            '''
        )
    if fails_count == 5:
        print(
            '''
            ______
            |	  |
            |     O
            |    /|\\
            |     |
            |     
            |
            |
            '''
        )
    if fails_count == 6:
        print(
            '''
            ______
            |	  |
            |     O
            |    /|\\
            |     |
            |     /
            |
            |
            '''
        )
    if fails_count == 7:
        print(
            '''
            ______
            |	  |
            |     O
            |    /|\\
            |     |
            |     /\\
            |
            |
            '''
        )
    print("You have made ", fails_count, " fails of an overall of ", fails_allowed)


def game():
    greetings()
    serie = choose_serie()
    max_fails_allowed = 7
    fails_count = 0
    word_hits = generate_word_hits(serie)
    while fails_count < max_fails_allowed and False in word_hits:
        print_gaps(serie, word_hits)
        character = ask_character()
        if user_succeed(serie, word_hits, character) == False:
            fails_count += 1
            print_hangman(fails_count, max_fails_allowed)
    print("The serie was ", serie)

game()
