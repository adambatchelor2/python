# In this challenge, you have to establish if a given number is undulating. A number n is undulating when the following conditions are all true:

# n has at least three digits.
# n has exactly two different digits.
# the two digits of n are alternating without repeating groups.
# If we think of the first digit of an undulating number as an "A", and the second digit as a "B", we notice a sequence of the form "ABA" that can repeat infinite times and ends either with an "A" or with a "B", but without clusters of "AA" or "BB" in it.

# Given a positive integer n, implement a function that returns True if n is an Undulating number, or False if it's not.

n = 121
list_str = []
n = str(n)

if len(n) >= 3:
	
	for x in range(0,len(n)):
		if n[x] not in list_str:
			list_str.append(n[x])

	print(list_str)
else:
	print('false')