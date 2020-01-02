#Create a function that returns the indices of all occurrences of an item in the list.

#Examples
#get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]



def get_indices(lst, el):
	out_list = []
	for i, x in enumerate(lst):
		if x == el:
			out_list.append(i)
	return out_list		


print(get_indices(["a", "a", "b", "a", "b", "a"],"a"))