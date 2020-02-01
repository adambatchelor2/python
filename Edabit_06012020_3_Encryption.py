#Make a function that encrypts a given input with these steps:
#Input: "apple"
#Step 1: Reverse the input: "elppa"
#Step 2: Replace all vowels using the following chart:

#a => 0
#e => 1
#o => 2
#u => 3

# "1lpp0"
#Step 3: Add "aca" to the end of the word: "1lpp0aca"
#Output: "1lpp0aca"

def encrypt(word):

	word = word[::-1]
	word = word.replace("a","0")
	word = word.replace("e","1")
	word = word.replace("o","2")
	word = word.replace("u","3")

	return(word+"aca")