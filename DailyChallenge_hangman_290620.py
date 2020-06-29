#Guess a letter - if incorrect image is drawn
#Fuction that takes a letter or word and return true/false if letter is found
#Keep track of guesses made

guess_count = 0
incorrect_guess_count = 0

def guess_entry():
    guess = input("What letter do you think is in in?")
    guess_count += 1

    return guess

