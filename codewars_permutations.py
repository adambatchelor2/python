# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
# In this kata you have to create all permutations of an input string and remove duplicates
# ,if present. This means, you have to shuffle all letters from the input in all possible orders.
# permutations('a');  # ['a']
# permutations('ab');  # ['ab', 'ba']
# permutations('aabb');  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

# permutations using library function

# TOO SLOW
# def permutations(string):
#     from itertools import permutations
#
#     perm = permutations(list(string))
#
#     outList = []
#     y = ''
#
#     for i in list(perm):
#         for x in i:
#             y += str(x)
#         if y not in outList:
#              outList.append(y)
#         y = ''
#
#     return(outList)


def permutations(string):
    from itertools import permutations
    perm = permutations(list(string))

    inList = list(perm)
    outList = []
    outList = list(set([''.join(x) for x in inList]))

    return(outList)

print(permutations('aba'))