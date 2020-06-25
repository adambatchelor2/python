
# Write a function that returns True if two lists, when combined, form a consecutive sequence.
# Examples
# consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
# consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

list1 = [44,46]
list2 = [45]

listNew = list1 + list2

#sort list

listNew.sort()

#check order
leng = len(listNew)
y = 0

for x in range (0,leng-1):
	if listNew[x] != listNew[x+1]-1:
		y = 1
		
if y == 1:
	print ("False")
else:
	print ("True")

#print (listNew)
