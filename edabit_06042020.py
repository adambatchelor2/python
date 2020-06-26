#Create a function that takes a variable number of groups of items, 
#and returns the number of ways the items can be arranged, with one 
#item from each group. Order does not matter.

#Examples
#combinations(2, 3) ➞ 6

def my_sum(*args):
    add = 0
    subtract = 0
    # Iterating over the Python args tuple
    out_set = []

    list1 = [x for x in args]

    for x in list1:
    	out_set.append(x)

    for x in range(0,len(list1)-1):
    	out_set.append(list1[x]+list1[x+1])
    	out_set.append(list1[x]-list1[x+1])
    	out_set.append(list1[x+1]-list1[x])
    	out_set.append(list1[x]*list1[x+1])

    return out_set

print(my_sum(2,3))

