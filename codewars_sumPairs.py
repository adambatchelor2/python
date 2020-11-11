
# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

# Given a list of integers and a single sum value, return the first two values
# (parse from the left please) in order of appearance that add up to form the sum.

# sum_pairs([11, 3, 7, 5],10) - answer is 7 and 3 [7,3]

# def sum_pairs(ints,s):  # Option 1 too slow
#     myDict = {}
#
#     for i,z in enumerate(ints):
#         for j,y in enumerate(ints):
#             if z + y == s and i!=j:
#                 if i > j:
#                     myDict[i] = [y,z]
#                 else:
#                     myDict[j] = [y,z]
#     if len(myDict) > 0:
#         temp = min(myDict.items())
#         return temp[1]
#     else:
#         return None


# def sum_pairs(ints, s):  # Option 2 also too slow
#
#     outstr = []
#     k = 1000 # artificial high number
#
#     for i, z in enumerate(ints):
#
#         for j, y in enumerate(ints):
#             if z + y == s and i != j:
#                 if i < k and j < k:
#                     if i > j:
#                         k = i
#                     else:
#                         k = j
#                     outstr = []
#                     outstr.append(z)
#                     outstr.append(y)
#     if len(outstr) ==0:
#         return None
#     else:
#         return outstr


# print(sum_pairs([10, 5, 2, 3, 7, 5],10))


from itertools import permutations

inList = [10, 5, 2, 3, 7, 5]
target = 10
perm = permutations(inList,2)

permList = list(perm)

z = [x for x in permList if x[0]+x[1] == target]
z = list(set(z)) # remove duplicates

for x in z:
    print('{} and {}'.format(x[0],x[1]))
    print(inList.index(x[0])+inList.index(x[0]))

# print(z)