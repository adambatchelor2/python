#https://edabit.com/challenge/fRjfrCYXWJAaQqFXF
#A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.

#Create a function that returns the Primorial of a number.


#is it prime function


def primorial(n):

	def testPrime(val):
		y = 0
		for x in range(2,val):
			if val % x ==0:
				y = y + 1

		if y > 0:
			return("N")
		else:
			return("Y")



	c = 2 #test integer
	i = 1 #loop integer
	out = 1 #output integer

	while i <= n:
		if testPrime(c) == "Y":
			i = i + 1
			out = out * c
		c = c + 1

	return (out)


print (primorial(4))

