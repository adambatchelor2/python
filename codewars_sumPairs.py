
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

# def sum_pairs(ints, s): # option 4 timeout
#
#     from itertools import permutations
#
#     perm = permutations(ints,2)
#     permList = list(perm)
#
#     z = [x for x in permList if x[0]+x[1] == s]
#
#     if len(z)==0:
#         return None
#     else:
#         z = [a for i,a in enumerate(z) if i < len(z)/2]
#
#         a = 1000
#         outstr = []
#
#         for x in z:
#
#             if ints.index(x[0]) < a: # check first value less than max
#                 ints[ints.index(x[0])] = 'a'  # hide first value
#
#             if ints.index(x[1]) < a:
#                     a = ints.index(x[1])
#                     outstr = []
#                     outstr.append(x[0])
#                     outstr.append(x[1])
#         return outstr


# 1 list traverse


# def sum_pairs(ints, s): # option 5 still timed out
#     z = 1000000000
#     out = []
#
#     for position, value in enumerate(ints):
#         if position > z:
#             return out
#         elif s - value in ints[position + 1:]:
#             # print('pos: {} val:{} ind:{}'.format(position,value,ints[position + 1:].index(s-value)))
#             if ints[position + 1:].index(s-value) < z: # check to see if before previous value
#                 z = ints[position + 1:].index(s-value)
#                 out = [value, s-value] # overwrite if earlier
#
#     if len(out)==0:
#         return None
#     else:
#         return out
#
#
# print(sum_pairs([1, 2, 3, 4, 1, 0], 2))

#
# def sum_pairs(ints, s): # option 6 still timed out
#     out = []
#
#     for position, value in enumerate(ints):
#        if s - value in ints[position + 1:]:
#             ints = ints[position:(position + 1 + ints[position + 1:].index(s-value))] # cut down list
#
#             out.append([value, s-value]) # overwrite if another found in cut back list
#
#     if len(out)==0:
#         return None
#     else:
#         return out
#
#
# print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

def sum_pairs(nums, sum_value):
    seen = []
    for x in nums:
        diff = sum_value - x
        if diff in seen:
            return [diff, x]
        seen.append(x)

print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

# def sum_pairs(ints, s): # paul code
#     out = dict()
#     for i, value in enumerate(ints):
#         num = s - value
#         if num in out:
#             return [ints[out[num]],ints[i]]
#         else:
#             out[value] = i

