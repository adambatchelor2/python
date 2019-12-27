
#Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

#If the number is a multiple of 3 the output should be "Fizz".
#If the number given is a multiple of 5, the output should be "Buzz".
#If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
#If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.

def pass_me_number(y):

	if y % 3 == 0 and y % 5 == 0:
		return "FizzBuzz"
	elif y  % 3 ==0:
		return "Fizz"
	elif y % 5 == 0:
		return "Buzz"
	else:
		return y

print (pass_me_number(15))
