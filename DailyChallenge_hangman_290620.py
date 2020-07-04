# Guess a letter - if incorrect image is drawn
# Fuction that takes a letter or word and return true/false if letter is found
# Keep track of guesses made


class hangman:
    def __init__(self, hidden_string, guess_limit):
        self.hidden_string = hidden_string
        self.guess_count = 0
        self.guess_limit = guess_limit
        self.win = False
        self.current_string = ['x' for x in range(len(self.hidden_string))]

    #Function to replace characters from current string with guessed character
    def char_replace(self, inStr):

        #"test".replace("t","x")

        char_loc = self.hidden_string.find(inStr)
        self.current_string[char_loc] = inStr

    #If guess correct replace character else increase guess count
    def guess(self,inStr):
        if inStr in self.hidden_string:
            self.char_replace(inStr)
        else:
            self.guess_count += 1

    #Check to see if game complete
    def check_win(self):
        if self.current_string == self.hidden_string:
            self.win = True
        else:
            self.win = False
        return self.win

    #Main guess checking function
    def guess_check(self,inStr):

        self.guess(inStr)

        if self.check_win():
            return "You win"
        else:
            return (f"Try Again - {self.current_string}")


game1 = hangman("ytsete", 3)
# game2 = hangman("loooong",3)


while game1.guess_count < game1.guess_limit and game1.win == False:
     game1.guess_check(input("Guess letter:"))

