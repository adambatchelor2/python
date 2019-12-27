#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import random

option = ['r','p','s']

p1_input = input("P1 choose (r)ock, (p)aper or (s)cissors?")

p2_input = option[random.randint(0, 2)]

print ("\nComputer chooses "+ p2_input +"\n")

if p1_input == 'r' and p2_input != 'r' and p2_input != 'p':
	print ("P1 wins!")
elif p1_input == 'p' and p2_input != 'p' and p2_input != 's':
	print ("P1 wins!")
elif p1_input == 's' and p2_input != 's' and p2_input != 'r':
	print ("P1 wins!")
elif p1_input == p2_input:
	print("Draw")
else: 
	print("Computer wins!")
