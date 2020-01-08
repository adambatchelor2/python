#Given a number, return the difference between the maximum and minimum
#numbers that can be formed when the digits are rearranged.

#rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833  

def rearranged_difference(num):

	num = str(num)
	num = list(num)
	maxInt = ""
	minInt = ""

	num.sort(reverse=True)

	for x in num:
		maxInt = maxInt + str(x)

	num.sort()

	for x in num:
		minInt = minInt + str(x)

	return (int(maxInt)-int(minInt))

print(rearranged_difference(972882))