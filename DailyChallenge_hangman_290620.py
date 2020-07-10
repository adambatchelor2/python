# Guess a letter - if incorrect image is drawn
# Fuction that takes a letter or word and return true/false if letter is found
# Keep track of guesses made


class hangman:
    def __init__(self, hidden_string, guess_limit):
        self.hidden_string = hidden_string
        self.guess_count = 0
        self.guess_limit = guess_limit
        self.win = False
        self.current_string =  ['_' for x in range(len(self.hidden_string))]

    #Function to replace characters from current string with guessed character
    def char_replace(self, inStr):

        for x in range(0,len(self.hidden_string)):
            if self.hidden_string[x] == inStr:
                self.current_string[x] = inStr


    #If guess correct replace character else increase guess count
    def guess(self,inStr):
        if inStr in self.hidden_string:
            self.char_replace(inStr)
        else:
            self.guess_count += 1

    #Check to see if game complete
    def check_win(self):
        
        strTest = ''.join(self.current_string)

        if strTest == self.hidden_string:
            self.win = True
        else:
            self.win = False
        return self.win

    #Main guess checking function
    def guess_check(self,inStr):

        self.guess(inStr)

        if self.check_win():
            strfinal = ''.join(self.current_string)
            print (f"Well Done! It was '{strfinal}' and {self.guess_count} wrong guess(s)")
        else:
            strCurrent = ''.join(self.current_string)
            print (f"Try Again: {strCurrent}")


game1 = hangman(input("First person - enter string to guess.."), 5)
print(' '*10000)
print("Now time to guess the letters....")
while game1.guess_count < game1.guess_limit and game1.win == False:
     game1.guess_check(input("Guess letter:"))

