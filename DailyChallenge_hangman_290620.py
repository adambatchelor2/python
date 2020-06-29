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

    def test(self):
        print(self.current_string)

    def char_replace(self, inStr):
        char_loc = self.hidden_string.find(inStr)
        self.current_string[char_loc] = inStr
        return self.current_string

    def guess(self,inStr):
        if inStr in self.hidden_string:
            print (''.join(self.char_replace(inStr)))
        else:
            self.guess_count += 1
            print ("False")


game1 = hangman("ytest", 3)
game2 = hangman("loooong",3)

#print(game1.current_string)
# print(new_game.test())
# print(second_game.test())
#
while game1.guess_count < game1.guess_limit and game1.win == False:
     game1.guess(input("Guess letter:"))

