#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is
# a string that reads the same forwards and backwards.)

testStr = 'asdsa'

if testStr == testStr[::-1]:
	print("This is a palindrome")
else:
	print("This ia not a palindrome")