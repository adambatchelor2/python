#Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.

def num_mult(num,length):
	
	out = []

	for x in range(1,length+1):
		out.append(x*num)
		print(x)

	return out

out_list = num_mult(7,3)	

print([x for x in out_list])