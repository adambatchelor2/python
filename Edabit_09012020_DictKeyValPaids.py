# Create a function that takes:

# A list of keys.
# A list of values (same size).
# True, if key and value should be swapped, else False.
# The function returns the constructed dict. Empty lists return an empty dict.

# Examples
# swap_d([1, 2, 3], ["one", "two", "three"], False) ➞ { 1: "one", 2: "two", 3: "three" }

# swap_d([1, 2, 3], ["one", "two", "three"], True)) ➞ { "one": 1, "two": 2, "three": 3 }

def flipIf(k,v,swapped):
	if swapped:
		newDict = dict(zip(v,k))
	else:
		newDict = dict(zip(k,v))

	return newDict
# newList = list_1 + list_2
# newDict	 = {newList[i]:newList[i+3] for i in range(0,len(list_2))}

print(flipIf(["Paris",3,4.5],["France","is odd","is half of 9"],True))