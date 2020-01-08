#Create a function that returns the sum of missing numbers, given the input list is sorted in ascending order
#[1, 3, 5, 7, 10] ➞  (2 + 4 + 6 + 8 + 9) ➞ 29


def sum_missing_numbers(lst):
	
	lst.sort()
	y = len(lst)
	z = 0 
	for x in range(lst[0],lst[y-1]):
		if x not in lst:
			z = z + x
	return (z)


print (sum_missing_numbers([10, 7, 5, 3, 1]))

