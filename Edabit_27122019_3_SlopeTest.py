#Given two lines, determine whether or not they are parallel.

#Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

#def is_parallel(listNum)


l1 = [2,3,4]
l2 = [2,3,5]

slope1 = ((l1[0]*2) - (l1[0]*1)) / ((l1[1]*2) - (l1[1]*1))
slope2 = ((l2[0]*2) - (l2[0]*1)) / ((l2[1]*2) - (l2[1]*1))

print(slope1 == slope2)