#In each input list, every number repeats at least once, except for two.
#Write a function that returns the two unique numbers.
#returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]


def return_unique(lst):
	out = []
	for x in list(dict.fromkeys(lst)):
		cnt = 0
		#print(x)
		for a in lst:
			if x==a:
				cnt = cnt + 1
		if cnt == 1:
			out.append(x)
	return out

print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))